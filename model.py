#=======================================================================
# Description:
# Model class to handle media-related operations and data management
#=======================================================================
import pandas as pd
import utils.dbqueries as dbqueries
import utils.metahelper as metahelper

from datetime          import datetime
from utils.dbhelper    import execute_read, execute_query
from utils.common      import isNumeric
from utils.constants   import (
    MEDIA_TYPE, 
    MEDIA_DETAILS,
    MEDIA_COLUMNS,
    SERIES_COLUMNS,
    FILTER_COLUMNS,
    META_COLUMNS,
    APP_CONFIG,
    MEDIA_BOOLEAN_COLUMNS,
    MEDIA_FILTER_COLUMNS
)

#=======================================================================
def convert_bool_cols(media : pd.DataFrame) -> pd.DataFrame:
    """
    Converts specified columns in a DataFrame to boolean type.

    Parameters:
    media (DataFrame): A pandas DataFrame containing the data to be processed. 
                       It is expected to have columns that match the names in MEDIA_BOOLEAN_COLUMNS.

    Returns:
    DataFrame: The modified DataFrame with specified columns converted to boolean type.
    """
    for col in MEDIA_BOOLEAN_COLUMNS:
        if col in media.columns:
            media[col] = media[col].astype(bool)
    return media


def get_media_count(media_type : MEDIA_TYPE) -> int:
    '''
    Returns the total count of media items for the specified media type.

    Parameters:
    media_type (MEDIA_TYPE): The type of media (MOVIE or SERIES) to count.

    Returns:
    int: The total count of media items for the specified type.
    '''
    return execute_read(dbqueries.QUERY_GET_TOTAL_MOVIE_COUNT)['COUNT'][0] if media_type == MEDIA_TYPE.MOVIE \
      else execute_read(dbqueries.QUERY_GET_TOTAL_SERIES_COUNT)['COUNT'][0]


def get_media(media_type : MEDIA_TYPE, filters : dict) -> tuple:
    """
    Retrieves media information based on the specified media type and filters.

    Parameters:
    media_type (MEDIA_TYPE): The type of media to retrieve, either MOVIE or SERIES.
    filters (dict): A dictionary containing filter criteria. Keys are filter types (e.g., GENRE, TITLE), 
                    and values are the corresponding filter values.

    Returns:
    tuple: A tuple containing:
        - A list of media records that match the specified filters, with boolean columns converted appropriately.
        - An integer representing the count of media items that match the specified filters.
    """
    meta_query_mapping ={
        FILTER_COLUMNS.GENRE : {
            MEDIA_TYPE.MOVIE  : dbqueries.QUERY_FILTER_MOVIE_GENRES,
            MEDIA_TYPE.SERIES : dbqueries.QUERY_FILTER_SERIES_GENRES
        },
        FILTER_COLUMNS.LANGUAGE : {
            MEDIA_TYPE.MOVIE  : dbqueries.QUERY_FILTER_MOVIE_LANGUAGE,
            MEDIA_TYPE.SERIES : dbqueries.QUERY_FILTER_SERIES_LANGUAGE
        }
    }
    where_clause = ''

    for filter in filters:
        where_clause += ' WHERE ' if where_clause == '' else ' AND '   

        if filter in meta_query_mapping:
            where_clause += '{0} IN ({1})'.format(filters[filter], meta_query_mapping[filter][media_type])

        elif filter in [FILTER_COLUMNS.TITLE, FILTER_COLUMNS.DIRECTOR]:
            where_clause += '{0} LIKE "%{1}%"'.format(MEDIA_FILTER_COLUMNS[media_type][filter], filters[filter])

        elif filter == FILTER_COLUMNS.ACTOR:
            actor_query = dbqueries.QUERY_FILTER_MOVIE_CAST if media_type == MEDIA_TYPE.MOVIE \
                     else dbqueries.QUERY_FILTER_SERIES_CAST
            where_clause += f'EXISTS({actor_query.format(actor=filters[filter])})'

        elif filter == FILTER_COLUMNS.TO_BURN:
            where_clause += '{} = {}'.format(MEDIA_FILTER_COLUMNS[media_type][filter], filters[filter])

        else:
            where_clause += '{} = "{}"'.format(MEDIA_FILTER_COLUMNS[media_type][filter], filters[filter])

    query = dbqueries.QUERY_GET_MOVIES.format(where=where_clause) if media_type == MEDIA_TYPE.MOVIE \
       else dbqueries.QUERY_GET_SERIES.format(where=where_clause)
    
    return convert_bool_cols(execute_read(query)), get_media_count(media_type)


def get_movie_details(movie_id : int) -> dict:
    """
    Retrieves detailed information about a movie from the database.

    Parameters:
    movie_id (int): The unique identifier for the movie whose details are to be retrieved.

    Returns:
    dict: A dictionary containing various details about the movie, including:
        - MEDIA_DETAILS.CONTENT: The main content details of the movie.
        - MEDIA_DETAILS.GENRES: The genres associated with the movie.
        - MEDIA_DETAILS.LANGUAGES: The languages available for the movie.
        - MEDIA_DETAILS.CAST: The cast members of the movie.
        - MEDIA_DETAILS.OTHERS: Other miscellaneous details about the movie.
    """
    return { MEDIA_DETAILS.CONTENT   : execute_read(dbqueries.QUERY_GET_MOVIE.format(id=movie_id)),
             MEDIA_DETAILS.GENRES    : execute_read(dbqueries.QUERY_GET_MOVIE_GENRES.format(id=movie_id)),
             MEDIA_DETAILS.LANGUAGES : execute_read(dbqueries.QUERY_GET_MOVIE_LANGUAGES.format(id=movie_id)),
             MEDIA_DETAILS.CAST      : execute_read(dbqueries.QUERY_GET_MOVIE_CAST.format(id=movie_id)), 
             MEDIA_DETAILS.OTHERS    : execute_read(dbqueries.QUERY_GET_MOVIE_OTHERS.format(id=movie_id))}


def get_series_details(series_id : int) -> dict:
    """
    Retrieves detailed information about a TV series, including its content, episodes, genres, languages, and cast.

    Parameters:
    series_id (int): The unique identifier for the TV series.

    Returns:
    dict: A dictionary containing the following keys:
        - MEDIA_DETAILS.CONTENT: The main content details of the series.
        - MEDIA_DETAILS.EPISODES: A list of episodes for the series.
        - MEDIA_DETAILS.GENRES: The genres associated with the series.
        - MEDIA_DETAILS.LANGUAGES: The languages available for the series.
        - MEDIA_DETAILS.CAST: The cast members of the series.
    """
    return { MEDIA_DETAILS.CONTENT   : execute_read(dbqueries.QUERY_GET_SERIES_DETAIL.format(id=series_id)),
             MEDIA_DETAILS.EPISODES  : get_series_episodes(series_id),
             MEDIA_DETAILS.GENRES    : execute_read(dbqueries.QUERY_GET_SERIES_GENRES.format(id=series_id)),
             MEDIA_DETAILS.LANGUAGES : execute_read(dbqueries.QUERY_GET_SERIES_LANGUAGES.format(id=series_id)),
             MEDIA_DETAILS.CAST      : execute_read(dbqueries.QUERY_GET_SERIES_CAST.format(id=series_id)) }


def get_series_episodes(series_id : int, season=None) -> pd.DataFrame:
    """
    Retrieves episodes for a given series, optionally filtered by season.

    Parameters:
    series_id (int): The unique identifier for the series.
    season (int, optional): The specific season to filter episodes by. If 'All Seasons' or None, 
                            episodes from all seasons are retrieved.

    Returns:
    DataFrame: A list of episodes for the specified series and season, with boolean columns converted 
          appropriately.
    """
    if season and season != 'All Seasons':
        where_clause = ' AND t.SEASON = {}'.format(season)
    else:
        where_clause = ''

    query = dbqueries.QUERY_GET_SERIES_EPISODES.format(id=series_id, where_clause=where_clause)

    df_episodes = convert_bool_cols(execute_read(query))
    df_episodes['EPISODE'] = df_episodes['EPISODE'].astype(str)
    df_episodes['EPISODE'] = df_episodes['EPISODE'].apply(lambda x: f'0{x}' if len(x) == 1 else x)

    return df_episodes


def get_episode_details(episode_id : int) -> pd.DataFrame:
    """
    Retrieves episodes details for a given episode id.

    Parameters:
    episode_id (int): The unique identifier for the episode.

    Returns:
    DataFrame: Details of the episode for the specified episode ID.
    """
    return execute_read(dbqueries.QUERY_GET_EPISODE_DETAILS.format(id=episode_id))


def get_discs(media_type : MEDIA_TYPE) -> pd.DataFrame:
    """
    Retrieves a list of discs based on the specified media type.

    Parameters:
    media_type (MEDIA_TYPE): The type of media for which discs are to be retrieved. 
                             It can be either MEDIA_TYPE.MOVIE or MEDIA_TYPE.SERIES.

    Returns:
    DataFrame: A list of discs corresponding to the specified media type.
    """
    query = dbqueries.QUERY_GET_MOVIE_DISCS if media_type == MEDIA_TYPE.MOVIE \
       else dbqueries.QUERY_GET_SERIES_DISCS
    
    return execute_read(query)


def create_new_media(**kwargs) -> int:
    """
    Creates a new media entry in the database using the provided keyword arguments.

    Parameters:
    - kwargs (dict): A dictionary of keyword arguments that includes:
        - 'query' (str): The SQL query template for inserting a new media entry.
        - 'season' (str/int): The season number of the media, if applicable.
        - 'episode' (str/int): The episode number of the media, if applicable.
        - 'title' (str): The title of the media.
        - 'parent_id' (str/int, optional): The ID of the parent media, if applicable.
        - 'plot' (str): The plot description of the media.
        - 'release' (str): The release date of the media.
        - 'max_query' (str): The SQL query to retrieve the maximum ID of the media entries.

    Returns:
    - int: The ID of the newly created media entry if successful, otherwise -1.

    The function formats the SQL query with the provided arguments and executes it.
    If the query execution is successful, it retrieves and returns the new media ID.
    If the query execution fails, it returns -1.
    """
    timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    query     = kwargs['query'].format( kwargs['season'],
                                        kwargs['episode'],
                                        kwargs['title'], 
                                        kwargs['parent_id'],
                                        kwargs['plot'], 
                                        kwargs['release'],
                                        timestamp, 
                                        timestamp ) \
           if 'parent_id' in kwargs \
           else kwargs['query'].format( kwargs['title'], 
                                        timestamp, 
                                        timestamp )
    
    response  = execute_query(query)
    if response:
        new_media_id = execute_read(kwargs['max_query'])
        return new_media_id[MEDIA_COLUMNS.ID][0]
    
    return -1


def add_new_movie(title : str) -> int:
    """
    Adds a new movie in the database.

    Parameters:
    - title (str): The title of the episode.

    Returns:
    - ID from the database for the new movie
    """
    return create_new_media(title     = title, 
                            query     = dbqueries.QUERY_ADD_NEW_MOVIE, 
                            max_query = dbqueries.QUERY_GET_MAX_MOVIE_ID)


def add_new_series(title : str) -> int:
    """
    Adds a new series in the database.

    Parameters:
    - title (str): The title of the episode.

    Returns:
    - ID from the database for the new series
    """
    return create_new_media(title     = title, 
                            query     = dbqueries.QUERY_ADD_NEW_SERIES, 
                            max_query = dbqueries.QUERY_GET_MAX_SERIES_ID)


def add_new_episode(season : int, episode : int, title : str, plot : str, release_date : str, series_id : int) -> int:
    """
    Adds a new episode to a series in the database.

    Parameters:
    - season (int): The season number to which the episode belongs.
    - episode (int): The episode number within the season.
    - title (str): The title of the episode.
    - plot (str): A brief description or plot summary of the episode.
    - release_date (str): The release date of the episode in 'YYYY-MM-DD' format.
    - series_id (int): The unique identifier of the series to which the episode belongs.

    Returns:
    - ID from the database for the new movie / series / episode
    """
    return create_new_media(season    = season,
                            episode   = episode,
                            title     = title, 
                            plot      = plot,
                            release   = release_date,
                            query     = dbqueries.QUERY_ADD_NEW_EPISODE, 
                            max_query = dbqueries.QUERY_GET_MAX_EPISODE_ID, 
                            parent_id = series_id)


def delete_media(media_type : MEDIA_TYPE, media_id : int) -> bool:
    """
    Deletes media records from the database based on the media type and media ID.

    Parameters:
    media_type (MEDIA_TYPE): The type of media to delete, either a movie or a series.
    media_id (int): The unique identifier of the media to be deleted.

    Returns:
    bool: Returns True if the media was successfully deleted, False if an error occurred.
    """
    if media_type == MEDIA_TYPE.MOVIE:
        execute_query(dbqueries.QUERY_DELETE_MOVIE_CAST.format(id=media_id))
        execute_query(dbqueries.QUERY_DELETE_MOVIE_GENRES.format(id=media_id))
        execute_query(dbqueries.QUERY_DELETE_MOVIE_LANGUAGES.format(id=media_id))
        execute_query(dbqueries.QUERY_DELETE_MOVIE.format(id=media_id))
    else:
        execute_query(dbqueries.QUERY_DELETE_SERIES_CAST.format(id=media_id))
        execute_query(dbqueries.QUERY_DELETE_SERIES_GENRES.format(id=media_id))
        execute_query(dbqueries.QUERY_DELETE_SERIES_LANGUAGES.format(id=media_id))
        execute_query(dbqueries.QUERY_DELETE_SERIES_EPISODES.format(id=media_id))
        execute_query(dbqueries.QUERY_DELETE_SERIES.format(id=media_id))

    poster_path  = f'{metahelper.get_app_config(APP_CONFIG.POSTER_PATH)}/{media_type.lower()}/{str(media_id)}.jpg'
    import os
    if os.path.exists(poster_path):
        os.remove(poster_path)

    return True


def delete_series_episodes(episode_ids : list) -> bool:
    """
    Deletes a series of episodes from the database using their IDs.

    Parameters:
    episode_ids (list of str): A list of episode IDs to be deleted.

    Returns:
    bool: Returns True if the deletion is successful, otherwise returns False.
    """
    media_ids = ', '.join(episode_ids)
    execute_query(dbqueries.QUERY_DELETE_SERIES_EPISODE.format(id=media_ids))

    return True


def update_content(content_details : dict, update_query : str) -> None:
    """
    Updates the content in a database or data structure based on the provided details and query.

    Parameters:
    content_details (dict): A dictionary containing the details of the content to be updated. 
                            The keys represent column names, and the values represent the new values 
                            for those columns. The key MEDIA_COLUMNS.ID is used to identify the specific 
                            record to update.
    update_query (str): A string representing the SQL update query template. It should contain placeholders 
                        for the update clause and the ID, which will be filled in by this function.

    """
    update_clause = ''
    for detail in content_details:
        if detail != MEDIA_COLUMNS.ID:
            update_clause += '{} = NULL, '.format(detail) if content_details[detail] is None \
                        else '{} = {}, '.format(detail, content_details[detail]) if isNumeric(content_details[detail]) \
                        else '{} = "{}", '.format(detail, content_details[detail])
    update_clause = update_clause[:-2]
    update_clause = update_clause.replace('""', 'NULL').replace('"None"', 'NULL').replace('None', 'NULL')

    update_query  = update_query.format(updates=update_clause, id=content_details[MEDIA_COLUMNS.ID])

    execute_query(update_query)


def update_meta(**kwargs) -> None:
    """
    Updates metadata for a given media item by removing outdated metadata and adding new metadata.

    Parameters:
    - get_query (str): A query string to retrieve existing metadata for the media item.
    - media_id (int): The identifier for the media item whose metadata is being updated.
    - meta_column_name (str): The name of the column containing metadata.
    - meta_data (list): A list of new metadata values to be associated with the media item.
    - remove_query (str): A query string to remove outdated metadata from the media item.
    - add_new_query (str): A query string to add new metadata to the media item.

    The function performs the following steps:
    1. Retrieves existing metadata for the specified media item.
    2. Identifies metadata to be removed and metadata to be added.
    3. Removes outdated metadata using the provided remove_query.
    4. Retrieves all possible metadata values if there are new metadata to add.
    5. Adds new metadata using the provided add_new_query, creating new metadata entries if necessary.
    """
    existing_meta  = execute_read(kwargs['get_query'].format(id=kwargs['media_id']))
    meta_to_remove = [x for x in existing_meta[kwargs['meta_column_name']].tolist() if x not in kwargs['meta_data']]
    meta_to_add    = [x for x in kwargs['meta_data'] if x not in existing_meta[kwargs['meta_column_name']].tolist()]

    for meta in meta_to_remove:
        execute_query(kwargs['remove_query'].format(meta, kwargs['media_id']))
    
    all_meta = metahelper.get_meta_values(kwargs['meta_column_name']) if len(meta_to_add) > 0 else None
    for meta in meta_to_add:
        meta_id = all_meta.loc[all_meta[kwargs['meta_column_name']] == meta, MEDIA_COLUMNS.ID]
        meta_id = metahelper.add_meta(kwargs['meta_column_name'], meta) if len(meta_id) == 0 else int(meta_id.values[0])
        
        execute_query(kwargs['add_new_query'].format(
                        kwargs['media_id'], 
                        meta_id, 
                        datetime.now().strftime('%d-%m-%Y %H:%M:%S')))


def update_movie(movie_details : dict, lookup_details : dict, genres : list, languages : list) -> bool:
    """
    Updates movie information in the database, including its details, source, genres, and languages.

    Parameters:
    - movie_details (dict): A dictionary containing the movie's details, including its ID.
    - lookup_details (dict): A dictionary containing lookup information such as source and source URL.
    - genres (list): A list of genres associated with the movie.
    - languages (list): A list of languages associated with the movie.

    Returns:
    - bool: Returns True if the update process is successful.
    """
    update_content(movie_details, dbqueries.QUERY_UPDATE_MOVIE)

    if lookup_details:
        execute_query(dbqueries.QUERY_UPDATE_MOVIE_SOURCE.format(
                        id         = movie_details[MEDIA_COLUMNS.ID],
                        source     = lookup_details[MEDIA_COLUMNS.LOOKUP_SOURCE],
                        source_url = lookup_details[MEDIA_COLUMNS.SOURCE_URL]))
        
    if genres:
        update_meta(get_query        = dbqueries.QUERY_GET_MOVIE_GENRES, 
                    media_id         = movie_details[MEDIA_COLUMNS.ID], 
                    meta_data        = genres, 
                    meta_column_name = META_COLUMNS.GENRE, 
                    remove_query     = dbqueries.QUERY_REMOVE_MOVIE_GENRE, 
                    add_new_query    = dbqueries.QUERY_ADD_MOVIE_GENRE)

    if languages:
        update_meta(get_query        = dbqueries.QUERY_GET_MOVIE_LANGUAGES, 
                    media_id         = movie_details[MEDIA_COLUMNS.ID], 
                    meta_data        = languages, 
                    meta_column_name = META_COLUMNS.LANGUAGE, 
                    remove_query     = dbqueries.QUERY_REMOVE_MOVIE_LANGUAGE, 
                    add_new_query    = dbqueries.QUERY_ADD_MOVIE_LANGUAGE)
        
    return True


def bulk_update_movies(updates : dict) -> None:
    """
    Updates multiple movie records in the database with the provided information.

    Parameters:
    updates (dict): A dictionary containing the update information. The keys are column names, and the values are the new values for those columns.
    """
    if len(updates[MEDIA_COLUMNS.ID]) > 0:
        query = ''

        for key in updates:
            if key not in [MEDIA_COLUMNS.ID, META_COLUMNS.GENRE]:
                query += '{} = {}, '.format(key, updates[key]) if isNumeric(updates[key]) \
                    else '{} = "{}", '.format(key, updates[key])

        query = query[:-2]

        execute_query(dbqueries.QUERY_UPDATE_MOVIE_BULK.format(
                        updates=query, 
                        id=updates[MEDIA_COLUMNS.ID]))

        if META_COLUMNS.GENRE in updates:
            for movie_id in updates[MEDIA_COLUMNS.ID].split(','):
                execute_query(dbqueries.QUERY_ADD_MOVIE_GENRE.format(
                                movie_id, 
                                updates[META_COLUMNS.GENRE], 
                                datetime.now().strftime('%d-%m-%Y %H:%M:%S')))


def update_episode(episode_details : dict) -> None:
    """
    Updates the details of a series episode in the database.

    Parameters:
    - episode_details (dict): A dictionary containing details of episodes to be updated. If None, no episode update is performed.
    """
    update_content(episode_details, dbqueries.QUERY_UPDATE_SERIES_EPISODE)


def update_series(series_details : dict, lookup_details : dict, episode_details : dict, genres : list, languages : list) -> bool:
    """
    Updates the details of a series in the database, including its metadata such as genres and languages.

    Parameters:
    - series_details (dict): A dictionary containing the details of the series to be updated. It should include keys defined in MEDIA_COLUMNS.
    - lookup_details (dict or None): A dictionary containing lookup information for the series, including source and source URL. If None, no lookup update is performed.
    - episode_details (dict or None): A dictionary containing details of episodes to be updated. If None, no episode update is performed.
    - genres (list): A list of genres associated with the series.
    - languages (list): A list of languages associated with the series.

    Returns:
    - bool: Returns True if the update process completes successfully.
    """
    update_content(series_details, dbqueries.QUERY_UPDATE_SERIES)

    if lookup_details:
        execute_query(dbqueries.QUERY_UPDATE_SERIES_SOURCE.format(
                        id         = lookup_details[MEDIA_COLUMNS.ID],
                        source     = lookup_details[MEDIA_COLUMNS.LOOKUP_SOURCE],
                        source_url = lookup_details[MEDIA_COLUMNS.SOURCE_URL]))
        
    if episode_details:
        update_episode(episode_details)

    if genres:
        update_meta(get_query        = dbqueries.QUERY_GET_SERIES_GENRES, 
                    media_id         = series_details[MEDIA_COLUMNS.ID], 
                    meta_data        = genres, 
                    meta_column_name = META_COLUMNS.GENRE, 
                    remove_query     = dbqueries.QUERY_REMOVE_SERIES_GENRE, 
                    add_new_query    = dbqueries.QUERY_ADD_SERIES_GENRE)

    if languages:
        update_meta(get_query        = dbqueries.QUERY_GET_SERIES_LANGUAGES, 
                    media_id         = series_details[MEDIA_COLUMNS.ID], 
                    meta_data        = languages, 
                    meta_column_name = META_COLUMNS.LANGUAGE, 
                    remove_query     = dbqueries.QUERY_REMOVE_SERIES_LANGUAGE, 
                    add_new_query    = dbqueries.QUERY_ADD_SERIES_LANGUAGE)
        
    return True


def update_media_actors(media_type : MEDIA_TYPE, media_id : int, cast : dict, source : str, url='') -> bool:
    """
    Updates the cast information for a given media item (movie or series) in the database.

    Parameters:
    - media_type (MEDIA_TYPE): The type of media, either a movie or a series.
    - media_id (int): The unique identifier for the media item.
    - cast (dict): A dictionary containing actor information, where keys are actor IDs and values are dictionaries with actor details.
    - source (str): The source from which the actor information is retrieved.
    - url (str, optional): The URL of the source. Defaults to an empty string.

    Returns:
    - bool: Returns True if the update process is completed successfully.
    """
    delete_query = dbqueries.QUERY_DELETE_MOVIE_CAST.format(id=media_id) if media_type == MEDIA_TYPE.MOVIE \
              else dbqueries.QUERY_DELETE_SERIES_CAST.format(id=media_id)
    execute_query(delete_query)

    for actor_id in cast:
        df = execute_read(dbqueries.QUERY_GET_ACTOR.format(
                            name=cast[actor_id][MEDIA_COLUMNS.NAME], 
                            online_id=actor_id))
        
        if df.empty or len(df) == 0:
            execute_query(dbqueries.QUERY_ADD_ACTOR.format(
                            name          = cast[actor_id][MEDIA_COLUMNS.NAME],
                            online_id     = actor_id,
                            lookup_source = source,
                            source_url    = url,
                            created_date  = datetime.now().strftime('%d-%m-%Y %H:%M:%S')))
            
            df = execute_read(dbqueries.QUERY_GET_ACTOR.format(
                                name=cast[actor_id][MEDIA_COLUMNS.NAME], 
                                online_id=actor_id))

        if media_type == MEDIA_TYPE.MOVIE:
            execute_query(dbqueries.QUERY_ADD_MOVIE_CAST.format(
                            media_id, 
                            int(df.values[0]), 
                            cast[actor_id][MEDIA_COLUMNS.CHARACTER],
                            datetime.now().strftime('%d-%m-%Y %H:%M:%S')))
        else:
            execute_query(dbqueries.QUERY_ADD_SERIES_CAST.format(
                            media_id, 
                            int(df.values[0]),
                            cast[actor_id][MEDIA_COLUMNS.CHARACTER],
                            cast[actor_id][SERIES_COLUMNS.EPISODES],
                            datetime.now().strftime('%d-%m-%Y %H:%M:%S')))
        
    return True

#=======================================================================