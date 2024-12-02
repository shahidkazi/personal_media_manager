#=======================================================================
# Description:
# Publisher module to publish data to Google Firebase
# ** This publisher is very tighly tied to the format that my website
# requires and not a generic module (Not everyone will need this).
# If you wish to retro fit it for yourself, please go ahead and do it.
#
# The only mandatory methods to implement are generateContent() and
# publishContent()
#=======================================================================
import pandas as pd

from json import loads, dumps

from utils.constants import MEDIA_TYPE, MEDIA_COLUMNS, MEDIA_DETAILS, EPISODE_COLUMNS
from templates.exportdata.exportCSV import export

#=======================================================================
FIREBASE_SITE_ID    = 'personal-mdb'
WEB_APP_LOCATION    = '/Users/shahidkazi/Downloads/Apps'

INDEX_TEMPLATE      = f'{WEB_APP_LOCATION}/movies/templates/index_template.html'
RES_MOVIE_SUMMARY   = f'{WEB_APP_LOCATION}/movies/data/results_summary.txt'
RES_MOVIE_DASHBOARD = '{0}/movies/data/results_{1}.txt'
RES_MOVIE_DETAIL    = '{0}/movies/data/{1}.txt'
RES_SHOW_SUMNMARY   = f'{WEB_APP_LOCATION}/movies/data/results_shows.txt'
RES_SHOW_DETAIL     = '{0}/movies/data/{1}.txt'

col_rename      = {
    MEDIA_COLUMNS.ID               : 'TMDBID',
    MEDIA_COLUMNS.TITLE            : 'Title',
    MEDIA_COLUMNS.YEAR             : 'Year',
    MEDIA_DETAILS.GENRES           : 'Genre',
    MEDIA_COLUMNS.WATCHED          : 'Watched',
    MEDIA_COLUMNS.TO_BURN          : 'ToBurn',
    MEDIA_COLUMNS.ONLINE_RATING    : 'Rating',
    MEDIA_COLUMNS.RATING           : 'UserRating',
    MEDIA_COLUMNS.BACKUP_DISC      : 'Note',
    MEDIA_COLUMNS.SIZE             : 'Size',
    MEDIA_COLUMNS.POSTER_URL       : 'Poster',
    MEDIA_COLUMNS.PLOT             : 'Plot',
    EPISODE_COLUMNS.EPISODE_SEASON : 'EpSeason',
    EPISODE_COLUMNS.EPISODE        : 'Episode',
    EPISODE_COLUMNS.EPISODE_TITLE  : 'EpTitle',
    EPISODE_COLUMNS.EPISODE_PLOT   : 'EpPlot'
}

#=======================================================================
def write_results(df_json, save_to):
    """
    Save DataFrame results to a JSON file.

    Args:
        df_json (pd.DataFrame): DataFrame to be saved.
        save_to (str): Path to save the JSON output.
    """
    result = df_json.to_json(orient='table', index=None)
    parsed = loads(result)
    res    = dumps(parsed, indent=4)

    with open (save_to, 'w') as f:
        f.write(res)


def calc_percent(df_main : pd.DataFrame, df_subset : pd.DataFrame) -> str:
    """
    Calculate the percentage of rows in df_subset compared to df_main.

    Args:
        df_main (pd.DataFrame): The main DataFrame.
        df_subset (pd.DataFrame): The subset DataFrame.

    Returns:
        str: The percentage as a string.
    """
    return '0' if len(df_main) == 0 else str((len(df_subset)/len(df_main))*100)


def generate_summary(df_4k : pd.DataFrame, df_hd : pd.DataFrame):
    """
    Generate summary statistics for 4K and HD media and write results to a file.

    Args:
        df_4k (pd.DataFrame): DataFrame containing 4K media entries.
        df_hd (pd.DataFrame): DataFrame containing HD media entries.
    """
    print('----- Creating Dashboard Files ------')

    to_burn_4k = df_4k[df_4k['ToBurn']  == True]
    unseen_4k  = df_4k[df_4k['Watched'] == False]
    to_burn_hd = df_hd[df_hd['ToBurn']  == True]
    unseen_hd  = df_hd[df_hd['Watched'] == False]

    df_stats = pd.DataFrame({'Total'    : [str(len(df_4k)), str(len(df_hd))],
                             'ToBurn'   : [str(len(to_burn_4k)), str(len(to_burn_hd))],
                             'ToBurnPC' : [calc_percent(df_4k, to_burn_4k), calc_percent(df_hd, to_burn_hd)],
                             'Unseen'   : [str(len(unseen_4k)), str(len(unseen_hd))],
                             'UnseenPC' : [calc_percent(df_4k, unseen_4k), calc_percent(df_hd, unseen_hd)]})

    write_results(df_stats, RES_MOVIE_SUMMARY)


def generate_movie_results(df : pd.DataFrame, df_4k : pd.DataFrame, df_hd : pd.DataFrame):
    """
    Generates and writes movie results for 4K and 1080p quality, 
    along with detailed movie data.

    Args:
        df (pd.DataFrame): DataFrame containing all movie data.
        df_4k (pd.DataFrame): DataFrame filtered for 4K quality movies.
        df_hd (pd.DataFrame): DataFrame filtered for non-4K (1080p) movies.
    """
    print('----- Generating Results ---------')

    # Columns to include in the summary results
    results_cols = ['TMDBID', 'Title', 'Year', 'Genre', 'Watched', 'ToBurn', 'Note']
    config       = {'4K': df_4k, '1080p': df_hd}

    # Generate and write dashboard results for each quality level
    for quality, df_quality in config.items():
        df_summary = df_quality[results_cols].copy()
        write_results(df_summary, RES_MOVIE_DASHBOARD.format(WEB_APP_LOCATION, quality))

    print('----- Creating Detail Data ------')

    # Columns to include in the detailed movie data
    results_cols = [
        'TMDBID', 'IMDBID', 'Title', 'Year', 'Genre', 'Watched', 'ToBurn', 
        'Rating', 'UserRating', 'Note', 'Size', 'Poster', 'Plot'
    ]

    # Generate and write detailed results for each movie
    df_details = df[results_cols].copy()
    for _, row in df_details.iterrows():
        write_results(row.to_frame().T, RES_MOVIE_DETAIL.format(WEB_APP_LOCATION, str(row['TMDBID'])))


def generate_series_results(df : pd.DataFrame):
    """
    Generates results for TV series from the provided dataframe, creating
    summaries of episodes, seasons, and individual series.

    Args:
        df (pd.DataFrame): DataFrame containing series data.
    """
    df['TMDBID'] = df['TMDBID'].apply(lambda x: f's{x}' if pd.notnull(x) else '')

    df_shows = (
        df.groupby(by=['TMDBID', 'IMDBID', 'Title', 'EpSeason'])['Watched']
        .count()
        .reset_index()
        .rename(columns={'Watched': 'Episodes'})
    )

    df_seasons = (
        df_shows.groupby(by=['TMDBID', 'IMDBID', 'Title'])['EpSeason']
        .nunique()
        .reset_index()
        .rename(columns={'EpSeason': 'Seasons'})
    )

    df_shows = (
        df_shows.groupby(by=['TMDBID', 'IMDBID', 'Title'])['Episodes']
        .sum()
        .reset_index()
    )
    df_shows = df_shows.merge(df_seasons, on=['TMDBID', 'IMDBID', 'Title'], how="left")

    episode_cols = ['TMDBID', 'IMDBID', 'Title', 'Rating', 'Poster', 'Plot', 'EpSeason', 'Episode', 'EpTitle', 'EpPlot']
    df_episodes  = df[episode_cols].merge(df_shows, on=['TMDBID', 'IMDBID', 'Title'], how="left")

    for _, row in df_shows.iterrows():
        filtered_df = df_episodes[df_episodes['TMDBID'] == row['TMDBID']]
        write_results(filtered_df, RES_SHOW_DETAIL.format(WEB_APP_LOCATION, row['TMDBID']))

    write_results(df_shows, RES_SHOW_SUMNMARY)


def generateContent(media_type : MEDIA_TYPE):
    """
    Generates content based on the specified media type by exporting data, 
    processing it, and generating summaries and results.

    Args:
        media_type (MEDIA_TYPE): The type of media (e.g., movie or series).
    """
    export_path = 'templates/publish/temp/mediaExport.csv'
    export(media_type=media_type, path=export_path)

    df = pd.read_csv(export_path, keep_default_na=False)
    df.rename(columns=col_rename, inplace=True)
    
    df['IMDBID'] = df['SOURCE_URL'].apply(lambda x: x.rsplit('/', 2)[1] if len(x) > 0 else '')

    if media_type == MEDIA_TYPE.MOVIE:
        df['TMDBID'] = df['TMDBID'].apply(lambda x: 'm' + str(x))
        df['Genre']  = df['Genre'].apply(lambda x: x.replace('Science Fiction', 'SciFi'))

        df_4k = df[df['QUALITY'] == '4K (2160p)']
        df_hd = df[df['QUALITY'] != '4K (2160p)']

        generate_summary(df_4k, df_hd)
        generate_movie_results(df, df_4k, df_hd)
    else:
        print('----- Generating TV Series Data ------')
        generate_series_results(df)

    print('----- Complete ------')


def publishContent() -> bool:
    """
    Deploys content to Firebase Hosting for the specified website.

    Returns:
        bool: True if deployment is successful, False otherwise.
    """
    import subprocess

    command = ["firebase", "deploy", "--only", f"hosting:{FIREBASE_SITE_ID}"]
    result = subprocess.run(
        command,
        capture_output = True,
        text           = True,
        check          = True,
        cwd            = WEB_APP_LOCATION
    )
    print(result.stdout)

    return True

#=======================================================================