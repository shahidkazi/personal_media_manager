#=======================================================================
# Description:
# Parser module to fetch movie / series information from IMDB
# Mandatory methods to implement:
# search_media()
# get_media_details() 
# get_season_episodes()
#=======================================================================
import json
import requests
import pandas as pd
from typing import Dict, List, Optional

from utils.constants import (
    MEDIA_COLUMNS, 
    MEDIA_DETAILS,
    MOVIE_COLUMNS,
    SERIES_COLUMNS, 
    EPISODE_COLUMNS
)

#=======================================================================
TMDB_BASE_URL     = 'https://api.themoviedb.org/3'

COL_MAPPING       = {
    'Title'    : MEDIA_COLUMNS.ORIGINAL_TITLE,
    'Released' : MEDIA_COLUMNS.RELEASE_DATE,
    'Episode'  : EPISODE_COLUMNS.EPISODE,
    'Plot'     : MEDIA_COLUMNS.PLOT,
}

MOVIE_TYPES       = ['movie', 'short', 'video movie', 'tv special', 'tv movie']

API_KEY           = '121b177abc08a1012fb7ec76ec6f0c27'
HEADERS           = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

#=======================================================================
def search_media(title : str) -> pd.DataFrame:
    """
    Searches for movies based on the given title and returns a DataFrame containing the results.

    Parameters:
    title (str): The title of the movie to search for.

    Returns:
    pandas.DataFrame: A DataFrame containing the search results with columns 'Title', 'Year', and 'imdbID'.
    """
    try:
        endpoint    = f"{TMDB_BASE_URL}/search/movie"
        params      = {
            "api_key"   : API_KEY,
            "query"     : title,
            "language"  : "en-US",
            "page"      : 1
        }
        response    = requests.get(endpoint, headers=HEADERS, params=params)
        response.raise_for_status()
        movies      = response.json()
        data        = []

        for movie in movies['results']:
            data.append({
                MEDIA_COLUMNS.TITLE     : movie.get('title'),
                MEDIA_COLUMNS.YEAR      : str(movie.get('release_date', '    ')[:4]),
                MEDIA_COLUMNS.ONLINE_ID : str(movie.get('id')),
            })

        return pd.DataFrame(data)
    except:
        return pd.DataFrame


def get_media_details(online_id : str):
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
    endpoint    = f"{TMDB_BASE_URL}/movie/{online_id}"
    params      = {
        "api_key"            : API_KEY,
        "language"           : "en-US",
        "append_to_response" : "credits,images,release_dates"
    }
    
    response    = requests.get(endpoint, params=params)
    response.raise_for_status()
    media       = response.json()
    rating      = 'Unknown'

    if media.get('release_dates', {}):
        for result in media['release_dates'].get('results', []):
            if result.get('iso_3166_1') in ('US', 'IN'):
                for release in result.get('release_dates', []):
                    rating = release.get('certification', 'Unknown')

    directors   = []
    writers     = []
    if media['credits'] and media['credits']['crew']:
        for staff in media['credits']['crew']:
            if staff.get('job') == 'Director':
                directors.append(staff.get('name'))
            if staff.get('job') == 'Screenplay':
                writers.append(staff.get('name'))

    poster_path = f"https://image.tmdb.org/t/p/w1280/{media.get('poster_path')}" if media.get('poster_path') else None
        
    data        = {
        MEDIA_COLUMNS.ORIGINAL_TITLE : media.get('original_title'),
        MEDIA_COLUMNS.YEAR           : str(media.get('release_date', '    ')[:4]),
        MEDIA_COLUMNS.PLOT           : media.get('overview', ''),
        MEDIA_COLUMNS.POSTER_URL     : poster_path,
        MEDIA_COLUMNS.COUNTRY        : ', '.join(media.get('origin_country', [])),
        MEDIA_COLUMNS.ONLINE_RATING  : media.get('vote_average', 0.0),
        MEDIA_COLUMNS.CERTIFICATION  : rating,
        MEDIA_COLUMNS.DIRECTOR       : ', '.join(directors),
        MEDIA_COLUMNS.WRITER         : ', '.join(writers),
        MEDIA_COLUMNS.RELEASE_DATE   : media.get('release_date', ''),
        MOVIE_COLUMNS.RUNTIME        : media.get('runtime', '')
    }

    lookup_details = {'LOOKUP_SOURCE' : 'IMDB' if media.get('imdb_id', '') != '' else 'TMDB', 
                     f'SOURCE_URL'    : f"https://www.imdb.com/title/{media.get('imdb_id', '')}" \
                                        if media.get('imdb_id', '') != '' else \
                                        f'https://www.themoviedb.org/movie/{online_id}'}

    genres = [item['name'] for item in media.get('genres', [])]

    actors = {}
    if media.get('credits') and media['credits'].get('cast'):
        count = 1
        for cast in media['credits'].get('cast'):
            if cast['known_for_department'] == 'Acting':
                actors[cast['id']] = {
                    MEDIA_COLUMNS.NAME      : cast['name'], 
                    MEDIA_COLUMNS.CHARACTER : cast['character'],
                    SERIES_COLUMNS.EPISODES : 1}

            if count == 50:
                break

            count += 1

    return { MEDIA_DETAILS.CONTENT   : data, 
             MEDIA_DETAILS.OTHERS    : lookup_details, 
             MEDIA_DETAILS.GENRES    : genres, 
             MEDIA_DETAILS.LANGUAGES : [item['english_name'] for item in media.get('spoken_languages', [])], 
             MEDIA_DETAILS.CAST      : actors }

# def test():
#      sdata  = requests.get(IMDB_SEASON_URL.format(media_id=f'tt0944947', season=1)).json()
#      epdata = requests.get(IMDB_DETAILS_URL.format(media_id=sdata['Episodes'][0]['imdbID']))
#      print(epdata.json()['Director'])


#=======================================================================
#print(get_media_details('tt0944947', 0, MEDIA_TYPE.SERIES))
#print(get_season_episodes('tt0944947', 1))
#print(get_media_cast(1375666))
#print(search_media('the pirates of the caribbean 1', 'movie'))
#search_media('The Pirates of the Caribbean 1: The Curse of the Black Pearl', None)
#search_media('A House of Dynamite')
#print(get_media_details('155'))
#test()
#=======================================================================