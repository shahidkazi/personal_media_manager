import json
import requests
import pandas as pd

# Import your relevant libraries IMDb, TMDb, etc
from utils.constants import (
    MEDIA_COLUMNS, 
    MOVIE_COLUMNS, 
    SERIES_COLUMNS, 
    EPISODE_COLUMNS, 
    MEDIA_DETAILS,
    DEFAULT_POSTER_PATH
)

def search_media(title : str) -> pd.DataFrame:
    """
    Searches for movies based on the given title and returns a DataFrame containing the results.

    Parameters:
    title (str): The title of the movie to search for.

    Returns:
    pandas.DataFrame: A DataFrame containing the search results with columns 'Title', 'Year', and 'imdbID'.
    """
    movies = None # Fetch movies / series details from your parser
    data   = []

    if movies:
        for movie in movies:
            data.append({
                MEDIA_COLUMNS.TITLE     : movie.get('title'),
                MEDIA_COLUMNS.YEAR      : movie.get('year'),
                MEDIA_COLUMNS.ONLINE_ID : movie.get('movieID')
            })

    return pd.DataFrame(data)


def get_media_summary(media_id : str, online_id : str):
    """
    Retrieves a summary of media information from the IMDb database using the Cinemagoer library.

    Parameters:
    media_id (str): The unique identifier for the media in the local database.
    online_id (str): The IMDb identifier for the media.

    Returns:
    dict: A dictionary containing:
        - 'media_details': A dictionary with keys corresponding to media attributes such as title, year, plot, poster URL, country, online rating, director, writer, certification, and release date.
        - 'lookup_details': A dictionary with keys 'ID', 'LOOKUP_SOURCE', and 'SOURCE_URL' for tracking the source of the information.
        - 'genres': A string of comma-separated genres of the media.
        - 'languages': A string of comma-separated languages of the media.
        - 'cast': A dictionary of actors with their IMDb IDs as keys, containing their name, character, and episodes.
    """
    media  = None # Fetch movie / series details
    
    # Fetch and save basic media details
    data   = {
        MEDIA_COLUMNS.ORIGINAL_TITLE : media.get('title'),
        MEDIA_COLUMNS.YEAR           : media.get('year', ''),
        MEDIA_COLUMNS.PLOT           : media.get('plot', ''),
        MEDIA_COLUMNS.POSTER_URL     : media.get('cover url'),
        MEDIA_COLUMNS.COUNTRY        : ', '.join(media.get('countries', [])),
        MEDIA_COLUMNS.ONLINE_RATING  : media.get('rating', ''),
        MEDIA_COLUMNS.DIRECTOR       : ', '.join(media.get('directors', [])),
        MEDIA_COLUMNS.WRITER         : ', '.join(media.get('writers', [])),
        MEDIA_COLUMNS.CERTIFICATION  : media.get('certification', ''),
        MEDIA_COLUMNS.RELEASE_DATE   : media.get('release', '')
    }

    # Save poster locally
    if media.get('cover url', '') != '':
        poster_path = DEFAULT_POSTER_PATH.format(media.get('kind').replace('tv ', '')) + str(media_id) + '.jpg'
        with open(poster_path, 'wb') as f:
            f.write(requests.get(media.get('cover url')).content)

    # Add runtime or season count basis movie or tv series
    if media.get('kind') == 'movie':
        data[MOVIE_COLUMNS.RUNTIME]  = media.get('runtimes', [''])[0]
    else:
        data[SERIES_COLUMNS.SEASONS] = media.get('seasons')

    # Add information source details
    lookup_details = {MEDIA_COLUMNS.ID            : media_id,
                      MEDIA_COLUMNS.LOOKUP_SOURCE : 'IMDB', 
                      MEDIA_COLUMNS.SOURCE_URL    : 'https://www.imdb.com/title/{}/'.format(online_id)}

    # Add cast
    cast   = media['cast'][:20] if 'cast' in media else []
    actors = {}
    for person in cast:
        character = ', '.join([char.get('name', '') for char in person.currentRole]) \
                    if 'RolesList' in str(type(person.currentRole)) \
                    else person.currentRole.get('name', '')
        actors['nm' + person.personID] = {MEDIA_COLUMNS.NAME      : person['name'], 
                                          MEDIA_COLUMNS.CHARACTER : character,
                                          SERIES_COLUMNS.EPISODES : person.notes}

    return { MEDIA_DETAILS.CONTENT   : data, 
             MEDIA_DETAILS.OTHERS    : lookup_details, 
             MEDIA_DETAILS.GENRES    : media.get('genres', []), 
             MEDIA_DETAILS.LANGUAGES : media.get('languages', []), 
             MEDIA_DETAILS.CAST      : actors }


def get_season_episodes(series_id : str, season : int) -> pd.DataFrame:
    """
    Retrieves episode information for a specific season of a TV series from the IMDB database.

    Parameters:
    series_id (str): The unique identifier for the TV series.
    season (int): The season number for which the episodes are to be retrieved.

    Returns:
    pd.DataFrame: A DataFrame containing details of the episodes in the specified season, including the plot.
    """
    data = None # Fetch episodes by season for a series
    df_episodes = pd.DataFrame(data)

    # Rename to ensure the following columns exist
    # ORIGINAL_TITLE
    # EPISODE
    # RELEASE_DATE
    # PLOT
    # SEASON

    df_episodes[EPISODE_COLUMNS.SEASON] = season

    return df_episodes