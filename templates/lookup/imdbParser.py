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

from imdb import Cinemagoer
from utils.constants import (
    MEDIA_COLUMNS, 
    MEDIA_DETAILS,
    MOVIE_COLUMNS,
    SERIES_COLUMNS, 
    EPISODE_COLUMNS
)

#=======================================================================
IMDB_DETAILS_URL  = 'http://www.omdbapi.com/?apikey=bb618462&i={media_id}'
IMDB_SEASON_URL   = 'http://www.omdbapi.com/?apikey=bb618462&i={media_id}&Season={season}'

COL_MAPPING       = {
    'Title'    : MEDIA_COLUMNS.ORIGINAL_TITLE,
    'Released' : MEDIA_COLUMNS.RELEASE_DATE,
    'Episode'  : EPISODE_COLUMNS.EPISODE,
    'Plot'     : MEDIA_COLUMNS.PLOT,
}

MOVIE_TYPES       = ['movie', 'short', 'video movie', 'tv special', 'tv movie']

#=======================================================================
def search_media(title : str) -> pd.DataFrame:
    """
    Searches for movies based on the given title and returns a DataFrame containing the results.

    Parameters:
    title (str): The title of the movie to search for.

    Returns:
    pandas.DataFrame: A DataFrame containing the search results with columns 'Title', 'Year', and 'imdbID'.
    """
    ia     = Cinemagoer()
    movies = ia.search_movie(title=title)
    data   = []

    for movie in movies:
        data.append({
            MEDIA_COLUMNS.TITLE     : movie.get('title'),
            MEDIA_COLUMNS.YEAR      : str(movie.get('year', '')),
            MEDIA_COLUMNS.ONLINE_ID : str(movie.movieID),
        })

    return pd.DataFrame(data)


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
    ia        = Cinemagoer()
    media     = ia.get_movie(online_id)
    rating    = 'Unknown' if 'certificates' not in media \
                else [c for c in media['certificates'] if c.startswith('United States:')]
    if isinstance(rating, list):
        if len(rating) == 0:
            rating = 'Unknown'
        elif media.get('kind') in MOVIE_TYPES:
            media_rating = [x.split(':')[1].strip() for x in rating if 'TV' not in x]
            rating       = media_rating[0] if len(media_rating) > 0 else rating[0]
            rating       = media_rating[1] if len(media_rating) > 1 and rating == 'Not Rated' else rating
        else:
            rating = rating[0].split(':')[1].strip()
    
    data   = {
        MEDIA_COLUMNS.ORIGINAL_TITLE : media.get('title'),
        MEDIA_COLUMNS.YEAR           : media.get('year', ''),
        MEDIA_COLUMNS.PLOT           : media.get('plot', [''])[0].replace('"', ''),
        MEDIA_COLUMNS.POSTER_URL     : media.get('full-size cover url', None),
        MEDIA_COLUMNS.COUNTRY        : ', '.join(media.get('countries', [])),
        MEDIA_COLUMNS.ONLINE_RATING  : media.get('rating', 0.0),
        MEDIA_COLUMNS.CERTIFICATION  : rating
    }

    if data[MEDIA_COLUMNS.POSTER_URL]:
        size = requests.get(data[MEDIA_COLUMNS.POSTER_URL], stream = True).headers['Content-length']
        if size and int(size) > 4000000 and '@' in data[MEDIA_COLUMNS.POSTER_URL]:
            cover_url = media.get('cover url', None)
            url_split = cover_url.split('@')
            url_parts = ['@']
            for i in url_split[1]:
                url_parts.append(i)
                if i == 'Y':
                    url_parts.append('2000_.jpg')
                    break

            data[MEDIA_COLUMNS.POSTER_URL] = url_split[0] + ''.join(url_parts)

    if media.get('kind') in MOVIE_TYPES:
        directors = '' if 'director' not in media else ', '.join([director['name'] for director in media['director']])
        writers   = []
        if media.get('writers', '') != '':
            for writer in media['writers']:
                if writer.data.get('name', '') != '':
                    writers.append(writer.data.get('name'))

        writers = ', '.join(writers)
        release = media.get('original air date') if 'original air date' in media else media.get('year', '')
        
        data[MEDIA_COLUMNS.DIRECTOR]     = directors
        data[MEDIA_COLUMNS.WRITER]       = writers
        data[MEDIA_COLUMNS.RELEASE_DATE] = release
        data[MOVIE_COLUMNS.RUNTIME]      = media.get('runtimes', [''])[0]
    else:
        sdata  = requests.get(IMDB_SEASON_URL.format(media_id=f'tt{online_id}', season=1)).json()
        epdata = requests.get(IMDB_DETAILS_URL.format(media_id=sdata['Episodes'][0]['imdbID'])).json()\
                    if 'Episodes' in sdata else None
        
        data[MEDIA_COLUMNS.DIRECTOR]     = epdata['Director'] if epdata else ''
        data[MEDIA_COLUMNS.WRITER]       = epdata['Writer'] if epdata else ''
        data[MEDIA_COLUMNS.RELEASE_DATE] = epdata['Released'] if epdata else ''
        data[SERIES_COLUMNS.SEASONS]     = int(sdata['totalSeasons']) if 'totalSeasons' in sdata else 0

    lookup_details = {'LOOKUP_SOURCE' : 'IMDB', 
                      'SOURCE_URL'    : 'https://www.imdb.com/title/tt{}/'.format(online_id)}

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
    data = requests.get(IMDB_SEASON_URL.format(media_id=f'tt{series_id}', season=season))
    df   = pd.json_normalize(data.json())

    if 'Episodes' in df.columns:
        df_episodes = pd.DataFrame(df.Episodes[0])
        for idx, row in df_episodes.iterrows():
            data = requests.get(IMDB_DETAILS_URL.format(media_id=row['imdbID']))
            df_episodes.loc[idx, 'Plot'] = json.loads(data.content)['Plot']

        df_episodes.drop([col for col in df_episodes.columns if col not in COL_MAPPING], axis=1, inplace=True)
        df_episodes.rename(columns=COL_MAPPING, inplace=True)
        df_episodes[EPISODE_COLUMNS.SEASON] = season

        return df_episodes
    
    return pd.DataFrame()


# def test():
#     sdata  = requests.get(IMDB_SEASON_URL.format(media_id=f'tt0944947', season=1)).json()
#     epdata = requests.get(IMDB_DETAILS_URL.format(media_id=sdata['Episodes'][0]['imdbID']))
#     print(epdata.json()['Director'])


#=======================================================================
#print(get_media_details('tt0944947', 0, MEDIA_TYPE.SERIES))
#print(get_season_episodes('tt0944947', 1))
#print(get_media_cast(1375666))
#print(search_media('the pirates of the caribbean 1', 'movie'))
#search_media('The Pirates of the Caribbean 1: The Curse of the Black Pearl', None)
#get_media_summary('1375666')
#test()
#=======================================================================