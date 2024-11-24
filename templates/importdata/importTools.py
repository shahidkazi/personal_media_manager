#=======================================================================
# Description:
# Common utility methods used by the importer scripts to save the info
# to the application database
#=======================================================================
import model
import pandas as pd
import utils.metahelper as metahelper

from datetime     import datetime
from utils.common import isNumeric

from utils.constants import (
    MEDIA_DETAILS,
    MEDIA_COLUMNS, 
    MOVIE_COLUMNS, 
    META_COLUMNS
)

#=======================================================================
def get_meta_id(colname : str, value: str) -> int:
    """
    Retrieves the metadata ID for a given column name and value.

    Args:
        colname (str): The metadata column name (SOURCE, EDITION, or QUALITY).
        value (str): The value to match in the metadata.

    Returns:
        int or None: The corresponding ID if found, otherwise None.
    """
    meta_mapping = {
        META_COLUMNS.SOURCE  : metahelper.get_media_sources,
        META_COLUMNS.EDITION : metahelper.get_media_editions,
        META_COLUMNS.QUALITY : metahelper.get_media_qualities
    }

    # Retrieve the appropriate metadata function based on the column name
    metadata_func = meta_mapping.get(colname)
    if metadata_func:
        metadata = metadata_func()
        if not metadata.empty:
            id_value = metadata.loc[metadata[colname] == value, MEDIA_COLUMNS.ID]
            if not id_value.empty:
                return id_value.values[0]
    
    return None


def save_movies(data : pd.DataFrame, column_map : dict) -> bool: 
    """
    Saves movie data to the database, including details, source, genres, and languages.

    Args:
        data (pd.DataFrame): DataFrame containing movie data.
        column_map (dict): Mapping of column names to DataFrame columns.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:   
        for _, row in data.iterrows():
            movie_id       = model.add_new_movie(row[column_map[MEDIA_COLUMNS.TITLE]])
            movie_details  = {}
            source_details = {}

            for col in column_map:
                if col in [MEDIA_COLUMNS.LOOKUP_SOURCE, MEDIA_COLUMNS.SOURCE_URL] and col in column_map:
                    source_details[col] = row[column_map[col]] if pd.notnull(row[column_map[col]]) else None
                else:
                    if col == MEDIA_COLUMNS.QUALITY and row[col] is not None and MEDIA_COLUMNS.QUALITY_ID not in column_map:
                        movie_details[MEDIA_COLUMNS.QUALITY_ID] = get_meta_id(col, row[col])
                    elif col == MOVIE_COLUMNS.EDITION and row[col] is not None and MOVIE_COLUMNS.EDITION_ID not in column_map:
                        movie_details[MOVIE_COLUMNS.EDITION_ID] = get_meta_id(col, row[col])
                    elif col == MOVIE_COLUMNS.SOURCE and row[col] is not None and MOVIE_COLUMNS.SOURCE_ID not in column_map:
                        movie_details[MOVIE_COLUMNS.SOURCE_ID] = get_meta_id(col, row[col])
                    elif col not in [MEDIA_DETAILS.GENRES, MEDIA_DETAILS.LANGUAGES]:
                        movie_details[col] = row[column_map[col]] if pd.notnull(row[column_map[col]]) else None

            if MEDIA_COLUMNS.TO_BURN in movie_details:
                movie_details[MEDIA_COLUMNS.TO_BURN] = 1 if movie_details[MEDIA_COLUMNS.TO_BURN] == True else 0
            
            if MEDIA_COLUMNS.WATCHED in movie_details:
                movie_details[MEDIA_COLUMNS.WATCHED] = 1 if movie_details[MEDIA_COLUMNS.WATCHED] == True else 0

            movie_details[MEDIA_COLUMNS.ID]           = movie_id
            movie_details[MEDIA_COLUMNS.UPDATED_DATE] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

            genres    = row[column_map[MEDIA_DETAILS.GENRES]].split(',') \
                            if MEDIA_DETAILS.GENRES in column_map and not isNumeric(row[column_map[MEDIA_DETAILS.GENRES]]) \
                            else None
            languages = row[column_map[MEDIA_DETAILS.LANGUAGES]].split(',') \
                            if MEDIA_DETAILS.LANGUAGES in column_map and not isNumeric(row[column_map[MEDIA_DETAILS.LANGUAGES]]) \
                            else None

            model.update_movie( movie_details,
                                source_details if len(source_details) > 0 else None,
                                genres,
                                languages )
    except Exception as e:
        print(f"Error saving movies: {e}")
        return False

    return True


def save_series(data : pd.DataFrame, column_map : dict) -> bool: 
    """
    Saves series and episode data to the database, including details, source, genres, and languages.

    Args:
        data (pd.DataFrame): DataFrame containing series data.
        column_map (dict): Mapping of column names to DataFrame columns.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        prev_title = None
        data.dropna(axis=0, how='all', inplace=True)

        for _, row in data.iterrows():
            series_title   = row[column_map[MEDIA_COLUMNS.TITLE]]
            
            if series_title != prev_title:
                series_id = model.add_new_series(series_title)

            series_details  = {}
            source_details  = {}
            episode_details = {}

            for col in column_map:
                if col in [MEDIA_COLUMNS.LOOKUP_SOURCE, MEDIA_COLUMNS.SOURCE_URL] and col in column_map:
                    source_details[col] = row[column_map[col]] if pd.notnull(row[column_map[col]]) else None
                if col == MEDIA_COLUMNS.QUALITY and row[col] is not None and MEDIA_COLUMNS.QUALITY_ID not in column_map:
                    episode_details[MEDIA_COLUMNS.QUALITY_ID] = get_meta_id(col, row[col])
                elif col.startswith('EPISODE'):
                    episode_details[col.replace('EPISODE_', '')] = row[column_map[col]] if pd.notnull(row[column_map[col]]) else None
                elif series_title != prev_title and col not in [MEDIA_DETAILS.GENRES, MEDIA_DETAILS.LANGUAGES]:
                    series_details[col] = row[column_map[col]] if pd.notnull(row[column_map[col]]) else None
                
            if series_title != prev_title:
                series_details[MEDIA_COLUMNS.ID]           = series_id
                series_details[MEDIA_COLUMNS.UPDATED_DATE] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

                genres    = row[column_map[MEDIA_DETAILS.GENRES]].split(',') \
                                if MEDIA_DETAILS.GENRES in column_map and not isNumeric(row[column_map[MEDIA_DETAILS.GENRES]]) \
                                else None
                languages = row[column_map[MEDIA_DETAILS.LANGUAGES]].split(',') \
                                if MEDIA_DETAILS.LANGUAGES in column_map and not isNumeric(row[column_map[MEDIA_DETAILS.LANGUAGES]]) \
                                else None

                model.update_series(series_details,
                                    source_details if len(source_details) > 0 else None,
                                    None,
                                    genres,
                                    languages)

            episode_id = model.add_new_episode(episode_details[MEDIA_COLUMNS.TITLE], series_id) 
            episode_details[MEDIA_COLUMNS.ID]           = episode_id
            episode_details[MEDIA_COLUMNS.UPDATED_DATE] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

            if MEDIA_COLUMNS.TO_BURN in episode_details:
                episode_details[MEDIA_COLUMNS.TO_BURN] = 1 if episode_details[MEDIA_COLUMNS.TO_BURN] == True else 0
            
            if MEDIA_COLUMNS.WATCHED in episode_details:
                episode_details[MEDIA_COLUMNS.WATCHED] = 1 if episode_details[MEDIA_COLUMNS.WATCHED] == True else 0
            
            model.update_episode(episode_details)
            prev_title = series_title
    except Exception as e:
        print(f"Error saving movies: {e}")
        return False

    return True

#=======================================================================