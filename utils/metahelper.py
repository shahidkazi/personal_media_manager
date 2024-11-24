#=======================================================================
# Description: 
# Helper class to perform CRUD operations on meta data used for the
# different media types (Movies / TV Series)
#=======================================================================
import pandas as pd
import utils.dbqueries as dbqueries

from datetime import datetime

from utils.dbhelper  import execute_read, execute_query
from utils.constants import META_COLUMNS

#=======================================================================
def get_actors() -> pd.DataFrame:
    """
    Retrieves a list of actors from the database.

    Returns:
        DataFrame: A DataFrame containing actors retrieved from the database.
    """
    return execute_read(dbqueries.QUERY_GET_ACTORS)


def get_app_config(key=None):
    """
    Retrieve application configuration data from the database.

    Parameters:
    key (str, optional): The key for which the configuration value is required.
                         If None, the entire configuration data is returned.

    Returns:
    pandas.DataFrame or any: If a key is provided, returns the configuration value
                             associated with the key. If no key is provided, returns
                             the entire configuration data as a pandas DataFrame.
    """
    df_app_config = execute_read(dbqueries.QUERY_GET_APP_CONFIG)

    if key:
        return df_app_config[key][0]
    
    return df_app_config


def update_app_config(**kwargs) -> None:
    """
    Updates the application configuration in the database using the provided keyword arguments.

    Parameters:
    - export_template (str): The template used for exporting data.
    - import_template (str): The template used for importing data.
    - lookup_template (str): The template used for lookup operations.
    - publish_template (str): The template used for publishing data.
    - default_lookup (str): The default template for lookup operations.
    - default_publish (str): The default template for publishing operations.
    """
    execute_query(dbqueries.QUERY_UPDATE_APP_CONFIG.format(
        export_template  = kwargs['export_template'],
        import_template  = kwargs['import_template'],
        lookup_template  = kwargs['lookup_template'],
        publish_template = kwargs['publish_template'],
        default_lookup   = kwargs['default_lookup'],
        default_publish  = kwargs['default_publish'],
    ))


def get_genres() -> pd.DataFrame:
    """
    Retrieves a list of genres from the database.

    Returns:
        DataFrame: A DataFrame continaing genres retrieved from the database.
    """
    return execute_read(dbqueries.QUERY_GET_GENRES)


def add_new_genre(genre : str) -> int:
    """
    Adds a new genre to the database and retrieves the maximum genre ID.

    Parameters:
    genre (str): The name of the genre to be added.

    Returns:
    int: The maximum genre ID after the new genre is added.
    """
    retry_count = 3

    while retry_count > 0:
        retry_count -= 1

        df_genres = get_genres()
        if genre not in df_genres[META_COLUMNS.GENRE].to_list():
            execute_query(dbqueries.QUERY_ADD_GENRE.format(
                            genre, 
                            datetime.now().strftime('%d-%m-%Y %H:%M:%S')))
    
        df_genres = get_genres()
        if genre in df_genres[META_COLUMNS.GENRE].to_list():
            return int(df_genres.loc[df_genres[META_COLUMNS.GENRE] == genre, 'ID'].values[0])
        
    return 0


def get_media_editions() -> pd.DataFrame:
    """
    Retrieves a list of media editions from the database.

    Returns:
        DataFrame: A DataFrame containing media editions retrieved from the database.
    """
    return execute_read(dbqueries.QUERY_GET_MEDIA_EDITION)


def add_new_media_edition(edition : str) -> int:
    """
    Adds a new media edition to the database 

    Parameters:
    edition (str): The name of the editionm to be added.

    Returns:
    int: Defaulted to 0 to not break reusable method
    """
    execute_query(dbqueries.QUERY_ADD_MEDIA_EDITION.format(
                  edition, 
                  datetime.now().strftime('%d-%m-%Y %H:%M:%S')))
    return 0


def get_media_sources() -> pd.DataFrame:
    """
    Retrieves a list of media sources from the database.

    Returns:
        DataFrame: A DataFrame containing media sources retrieved from the database.
    """
    return execute_read(dbqueries.QUERY_GET_MEDIA_SOURCE)


def add_new_media_source(source : str) -> int:
    """
    Adds a new media source to the database 

    Parameters:
    source (str): The name of the source to be added.

    Returns:
    int: Defaulted to 0 to not break reusable method
    """
    execute_query(dbqueries.QUERY_ADD_MEDIA_SOURCE.format(
                    source, 
                    datetime.now().strftime('%d-%m-%Y %H:%M:%S')))
    return 0


def get_media_qualities() -> pd.DataFrame:
    """
    Retrieves a list of media qualities from the database.

    Returns:
        DataFrame: A DataFrame containing media qualities retrieved from the database.
    """
    return execute_read(dbqueries.QUERY_GET_MEDIA_QUALITY)


def add_new_media_quality(quality : str) -> int:
    """
    Adds a new media quality to the database 

    Parameters:
    quality (str): The name of the quality to be added.

    Returns:
    int: Defaulted to 0 to not break reusable method
    """
    execute_query(dbqueries.QUERY_ADD_MEDIA_QUALITY.format(
                    quality, 
                    datetime.now().strftime('%d-%m-%Y %H:%M:%S')))
    return 0

def get_languages() -> pd.DataFrame:
    """
    Retrieves a list of languages from the database.

    Returns:
        DataFrame: A DataFrame containing lnaguages retrieved from the database.
    """
    return execute_read(dbqueries.QUERY_GET_LANGUAGES)


def add_new_language(language : str) -> int:
    """
    Adds a new language to the database and returns the ID of the newly added language.

    Parameters:
    language (str): The name of the language to be added.

    Returns:
    int: The ID of the newly added language.
    """
    retry_count = 3

    while retry_count > 0:
        retry_count -= 1

        df = get_languages()
        if language not in df[META_COLUMNS.LANGUAGE].to_list():
            execute_query(dbqueries.QUERY_ADD_LANGUAGE.format(
                            language, 
                            datetime.now().strftime('%d-%m-%Y %H:%M:%S')))
    
        df = get_languages()
        if language in df[META_COLUMNS.LANGUAGE].to_list():
            return int(df.loc[df[META_COLUMNS.LANGUAGE] == language, 'ID'].values[0])
        
    return 0


def add_meta(meta_type : META_COLUMNS, meta_value : str) -> int:
    """
    Adds a new metadata entry based on the specified type and value.

    Parameters:
    meta_type (META_COLUMNS): The type of metadata to add.
    meta_value (str): The value of the metadata to be added.

    Returns:
    int: An integer representing the id for the newly added metadata.
    """
    meta_mapping = {
        META_COLUMNS.GENRE    : add_new_genre,
        META_COLUMNS.LANGUAGE : add_new_language,
        META_COLUMNS.EDITION  : add_new_media_edition,
        META_COLUMNS.SOURCE   : add_new_media_source,
        META_COLUMNS.QUALITY  : add_new_media_quality
    }

    return meta_mapping[meta_type](meta_value)
    

def update_meta(meta_type : META_COLUMNS, meta_list) -> None:
    """
    Updates the metadata of a specified type by removing obsolete entries and adding new ones.

    Parameters:
    - meta_type (META_COLUMNS): The type of metadata to update. It determines which function to call 
      for retrieving existing metadata and which queries to use for deletion.
    - meta_list (list): A list of new metadata entries that should be present after the update.

    The function works by:
    1. Retrieving the existing metadata of the specified type using a function from the meta_mapping.
    2. Identifying metadata entries that need to be removed (present in the database but not in meta_list).
    3. Identifying metadata entries that need to be added (present in meta_list but not in the database).
    4. Removing obsolete metadata entries by executing delete queries.
    5. Adding new metadata entries using the add_meta function.
    """
    meta_mapping = {
        META_COLUMNS.GENRE   : {
            'func'           : get_genres,
            'delete_queries' : [ 
                dbqueries.QUERY_REMOVE_GENRE_MOVIES,
                dbqueries.QUERY_REMOVE_GENRE_SERIES,
                dbqueries.QUERY_REMOVE_GENRE
            ]
        },
        META_COLUMNS.SOURCE  : {
            'func'           : get_media_sources,
            'delete_queries' : [
                dbqueries.QUERY_REMOVE_SOURCE_MOVIES,
                dbqueries.QUERY_REMOVE_SOURCE_SERIES,
                dbqueries.QUERY_REMOVE_SOURCE
            ]
        },
        META_COLUMNS.QUALITY  : {
            'func'           : get_media_qualities,
            'delete_queries' : [
                dbqueries.QUERY_REMOVE_QUALITY_MOVIES,
                dbqueries.QUERY_REMOVE_QUALITY
            ]
        },
        META_COLUMNS.EDITION  : {
            'func'           : get_media_editions,
            'delete_queries' : [
                dbqueries.QUERY_REMOVE_QUALITY_MOVIES,
                dbqueries.QUERY_REMOVE_QUALITY
            ]
        }
    }

    existing_meta  = meta_mapping[meta_type]['func']()
    meta_to_remove = [x for x in existing_meta[meta_type].tolist() if x not in meta_list]
    meta_to_add    = [x for x in meta_list if x not in existing_meta[meta_type].tolist()]
        
    for meta in meta_to_remove:
        meta_id = existing_meta.loc[existing_meta[meta_type] == meta, 'ID'].get_values(0)
        for query in meta_mapping[meta_type]['delete_queries']:
            execute_query(query.format(id=meta_id))

    for meta in meta_to_add:
        add_meta(meta_type, meta)
    

def get_meta_values(meta_type : META_COLUMNS) -> pd.DataFrame:
    """
    Retrieves a list of genres or languages from the database.

    Args:
        meta_type (META_COLUMNS): The type of metadata to retrieve.

    Returns:
        pd.DataFrame: A DataFrame containing the requested metadata.
    """
    return get_genres() if meta_type == META_COLUMNS.GENRE else get_languages()


def get_templates(key : str) -> pd.DataFrame:
    """
    Retrieves template data from a JSON file and returns it as a pandas DataFrame.

    Parameters:
    key (str): A string key used to obtain the path to the template file.

    Returns:
    pandas.DataFrame: A DataFrame containing the data from the 'data' field of the JSON file.
    """
    import json

    template_path = get_app_config(key)
    config_data   = None

    with open(template_path + '/registry.json', 'r') as f:
        config_data = json.load(f)

    return pd.DataFrame(config_data['data'])

#=======================================================================