#=======================================================================
# Description:
# Contains all the different SQL queries used in the application
# for its CRUD operations
#=======================================================================
# META DATA QUERIES
#=======================================================================
QUERY_GET_ACTORS                = 'SELECT ID, NAME, SOURCE_URL FROM ACTORS'
QUERY_GET_ACTOR                 = 'SELECT ID FROM ACTORS WHERE NAME = "{name}" OR ONLINE_ID = "{online_id}"'
QUERY_ADD_ACTOR                 = '''INSERT INTO ACTORS (NAME, ONLINE_ID, LOOKUP_SOURCE, SOURCE_URL, CREATED_DATE)
                                     VALUES ("{name}", "{online_id}", "{lookup_source}", "{source_url}", "{created_date}")'''

QUERY_GET_APP_CONFIG            = '''SELECT ID,
                                            EXPORT_TEMPLATES,
                                            IMPORT_TEMPLATES,
                                            LOOKUP_TEMPLATES,
                                            PUBLISH_TEMPLATES,
                                            DEFAULT_LOOKUP,
                                            DEFAULT_PUBLISH,
                                            DEFAULT_POSTER_PATH
                                     FROM APP_CONFIG'''
QUERY_UPDATE_APP_CONFIG         = '''UPDATE APP_CONFIG
                                       SET EXPORT_TEMPLATES    = "{export_template}",
                                           IMPORT_TEMPLATES    = "{import_template}",
                                           LOOKUP_TEMPLATES    = "{lookup_template}",
                                           PUBLISH_TEMPLATES   = "{publish_template}",
                                           DEFAULT_LOOKUP      = "{default_lookup}",
                                           DEFAULT_PUBLISH     = "{default_publish}",
                                           DEFAULT_POSTER_PATH = "{default_poster}"'''

QUERY_GET_GENRES                = 'SELECT ID, GENRE FROM GENRES ORDER BY GENRE'
QUERY_ADD_GENRE                 = 'INSERT INTO GENRES (GENRE, CREATED_DATE) VALUES ("{}", "{}")'
QUERY_GET_MAX_GENRE_ID          = 'SELECT MAX(ID) AS ID FROM GENRES'
QUERY_REMOVE_GENRE_MOVIES       = 'DELETE FROM MOVIE_GENRES WHERE GENRE_ID={id}'
QUERY_REMOVE_GENRE_SERIES       = 'DELETE FROM TV_SERIES_GENRES WHERE GENRE_ID={id}'
QUERY_REMOVE_GENRE              = 'DELETE FROM GENRES WHERE ID={id}'

QUERY_GET_LANGUAGES             = 'SELECT ID, LANGUAGE FROM LANGUAGES ORDER BY LANGUAGE'
QUERY_ADD_LANGUAGE              = 'INSERT INTO LANGUAGES (LANGUAGE, CREATED_DATE) VALUES ("{}", "{}")'
QUERY_GET_MAX_LANGUAGE_ID       = 'SELECT MAX(ID) AS ID FROM LANGUAGES'

QUERY_GET_MEDIA_EDITION         = 'SELECT ID, EDITION FROM MEDIA_EDITION'
QUERY_ADD_MEDIA_EDITION         = 'INSERT INTO MEDIA_EDITION (EDITION, CREATED_DATE) VALUES ("{}", "{}")'
QUERY_REMOVE_EDITION_MOVIES     = 'UPDATE MOVIES SET EDITION_ID = NULL WHERE EDITION_ID={id}'
QUERY_REMOVE_EDITION            = 'DELETE FROM MEDIA_EDITION WHERE ID={id}'

QUERY_GET_MEDIA_QUALITY         = 'SELECT ID, QUALITY FROM MEDIA_QUALITY'
QUERY_ADD_MEDIA_QUALITY         = 'INSERT INTO MEDIA_QUALITY (QUALITY, CREATED_DATE) VALUES ("{}", "{}")'
QUERY_REMOVE_QUALITY_MOVIES     = 'UPDATE MOVIES SET QUALITY_ID = NULL WHERE QUALITY_ID={id}'
QUERY_REMOVE_QUALITY            = 'DELETE FROM MEDIA_QUALITY WHERE ID={id}'

QUERY_GET_MEDIA_SOURCE          = 'SELECT ID, SOURCE FROM MEDIA_SOURCE'
QUERY_ADD_MEDIA_SOURCE          = 'INSERT INTO MEDIA_SOURCE (SOURCE, CREATED_DATE) VALUES ("{}", "{}")'
QUERY_REMOVE_SOURCE_MOVIES      = 'UPDATE MOVIES SET SOURCE_ID = NULL WHERE SOURCE_ID={id}'
QUERY_REMOVE_SOURCE_SERIES      = 'UPDATE TV_SERIES SET SOURCE_ID = NULL WHERE SOURCE_ID={id}'
QUERY_REMOVE_SOURCE             = 'DELETE FROM MEDIA_SOURCE WHERE ID={id}'

#=======================================================================
# MOVIE QUERIES
#=======================================================================
QUERY_GET_TOTAL_MOVIE_COUNT     = '''SELECT COUNT(*) AS COUNT FROM MOVIES'''
QUERY_GET_MAX_MOVIE_ID          = '''SELECT MAX(ID) AS ID FROM MOVIES'''

QUERY_GET_MOVIES                = '''SELECT m.ID,
                                            m.TITLE, 
                                            IFNULL (m.YEAR, '') AS YEAR,
                                            m.WATCHED,
                                            m.TO_BURN,
                                            m.RATING,
                                            IFNULL (m.SIZE, '') AS SIZE,
                                            m.CREATED_DATE
                                     FROM MOVIES m
                                        LEFT JOIN MEDIA_SOURCE s ON m.SOURCE_ID = s.ID
                                        LEFT JOIN MEDIA_QUALITY q on m.QUALITY_ID = q.ID
                                        LEFT JOIN MEDIA_EDITION e on m.EDITION_ID = e.ID
                                     {where}
                                     ORDER BY m.TITLE'''

QUERY_GET_MOVIE                 = '''SELECT m.ID, 
                                            m.TITLE, 
                                            IFNULL (m.ORIGINAL_TITLE, '') AS ORIGINAL_TITLE,
                                            IFNULL (m.YEAR, '') AS YEAR,
                                            m.WATCHED,
                                            m.TO_BURN,
                                            m.RATING,
                                            IFNULL (m.SIZE, '') AS SIZE,
                                            m.ONLINE_RATING,
                                            IFNULL (m.BACKUP_DISC, '') AS BACKUP_DISC,
                                            IFNULL (m.TAG, '') AS TAG,
                                            IFNULL (m.RUNTIME, '') AS RUNTIME,
                                            IFNULL (m.COUNTRY, '') AS COUNTRY,
                                            m.CERTIFICATION,
                                            IFNULL (m.RELEASE_DATE, '') AS RELEASE_DATE,
                                            IFNULL (m.TAGLINE, '') AS TAGLINE,
                                            IFNULL (m.PLOT, '') AS PLOT,
                                            IFNULL (m.NOTES, '') AS NOTES,
                                            IFNULL (s.SOURCE, '') AS SOURCE,
                                            IFNULL (q.QUALITY, '') AS QUALITY,
                                            IFNULL (e.EDITION, '') AS EDITION,
                                            IFNULL (m.VIDEO_CODEC, '') AS VIDEO_CODEC,
                                            IFNULL (m.AUDIO_CODEC, '') AS AUDIO_CODEC,
                                            m.DISC_COUNT,
                                            IFNULL (m.DIRECTOR, '') AS DIRECTOR,
                                            IFNULL (m.WRITER, '') AS WRITER,
                                            m.CREATED_DATE
                                     FROM MOVIES m
                                        LEFT JOIN MEDIA_SOURCE  s ON m.SOURCE_ID  = s.ID
                                        LEFT JOIN MEDIA_QUALITY q ON m.QUALITY_ID = q.ID
                                        LEFT JOIN MEDIA_EDITION e ON m.EDITION_ID = e.ID
                                     WHERE m.ID = {id}'''

QUERY_GET_MOVIE_GENRES          = '''SELECT g.ID, g.GENRE
                                     FROM MOVIE_GENRES m
                                        INNER JOIN GENRES g ON g.ID = m.GENRE_ID
                                     WHERE m.MOVIE_ID = {id}
                                     ORDER BY g.GENRE'''

QUERY_GET_MOVIE_LANGUAGES       = '''SELECT l.LANGUAGE
                                     FROM MOVIE_LANGUAGES m
                                        INNER JOIN LANGUAGES l ON l.ID = m.LANGUAGE_ID
                                     WHERE m.MOVIE_ID = {id}
                                     ORDER BY l.LANGUAGE'''

QUERY_GET_MOVIE_CAST            = '''SELECT a.NAME,
                                            m.CHARACTER,
                                            m.ID
                                     FROM MOVIE_CAST m
                                        INNER JOIN ACTORS a ON a.ID = m.ACTOR_ID
                                     WHERE m.MOVIE_ID = {id}
                                     ORDER BY a.NAME'''

QUERY_FILTER_MOVIE_GENRES       = '''SELECT GENRE_ID 
                                     FROM MOVIE_GENRES 
                                     WHERE MOVIE_ID = m.ID'''

QUERY_FILTER_MOVIE_LANGUAGE     = '''SELECT LANGUAGE_ID 
                                     FROM MOVIE_LANGUAGES 
                                     WHERE MOVIE_ID = m.ID'''

QUERY_FILTER_MOVIE_CAST         = '''SELECT a.NAME 
                                     FROM MOVIE_CAST c 
                                       INNER JOIN ACTORS a ON a.ID = c.ACTOR_ID 
                                     WHERE c.MOVIE_ID = m.ID 
                                       AND a.NAME LIKE "%{actor}%"'''

QUERY_GET_MOVIE_OTHERS          = '''SELECT TITLE 
                                     FROM MOVIES 
                                     WHERE BACKUP_DISC = (SELECT BACKUP_DISC 
                                                          FROM MOVIES 
                                                          WHERE ID = {id})
                                     ORDER BY TITLE'''

QUERY_GET_MOVIE_DISCS           = '''SELECT DISTINCT BACKUP_DISC 
                                     FROM MOVIES 
                                     WHERE BACKUP_DISC IS NOT NULL
                                     ORDER BY BACKUP_DISC'''

QUERY_ADD_NEW_MOVIE             = '''INSERT INTO MOVIES (TITLE, CREATED_DATE, UPDATED_DATE)
                                     VALUES ("{0}", "{1}", "{2}")'''

QUERY_DELETE_MOVIE_CAST         = '''DELETE FROM MOVIE_CAST WHERE MOVIE_ID={id}'''
QUERY_DELETE_MOVIE_LANGUAGES    = '''DELETE FROM MOVIE_LANGUAGES WHERE MOVIE_ID={id}'''
QUERY_DELETE_MOVIE_GENRES       = '''DELETE FROM MOVIE_GENRES WHERE MOVIE_ID={id}'''
QUERY_DELETE_MOVIE              = '''DELETE FROM MOVIES WHERE ID={id}'''

QUERY_UPDATE_MOVIE              = '''UPDATE MOVIES SET {updates} WHERE ID = {id}'''
QUERY_UPDATE_MOVIE_BULK         = '''UPDATE MOVIES SET {updates} WHERE ID IN ({id})'''

QUERY_UPDATE_MOVIE_SOURCE       = '''UPDATE MOVIES
                                     SET LOOKUP_SOURCE = "{source}",
                                        SOURCE_URL     = "{source_url}"
                                     WHERE ID = {id}'''

QUERY_ADD_MOVIE_GENRE           = '''INSERT INTO MOVIE_GENRES (MOVIE_ID, GENRE_ID, CREATED_DATE)
                                     VALUES ({}, {}, "{}")'''

QUERY_REMOVE_MOVIE_GENRE        = '''DELETE FROM MOVIE_GENRES 
                                     WHERE GENRE_ID = (SELECT ID 
                                                       FROM GENRES 
                                                       WHERE GENRE = "{}") 
                                       AND MOVIE_ID = {}'''

QUERY_ADD_MOVIE_LANGUAGE        = '''INSERT INTO MOVIE_LANGUAGES (MOVIE_ID, LANGUAGE_ID, CREATED_DATE)
                                     VALUES ({}, {}, "{}")'''

QUERY_REMOVE_MOVIE_LANGUAGE     = '''DELETE FROM MOVIE_LANGUAGES 
                                     WHERE LANGUAGE_ID = (SELECT ID 
                                                          FROM LANGUAGES 
                                                          WHERE LANGUAGE = "{}") 
                                       AND MOVIE_ID = {}'''

QUERY_ADD_MOVIE_CAST            = '''INSERT INTO MOVIE_CAST (MOVIE_ID, ACTOR_ID, CHARACTER, CREATED_DATE)
                                     VALUES ({}, {}, "{}", "{}")'''

QUERY_REMOVE_MOVIE_CAST         = '''DELETE FROM MOVIE_CAST WHERE ID = {id}'''

#=======================================================================
# TV SERIES QUERIES
#=======================================================================
QUERY_GET_TOTAL_SERIES_COUNT    = '''SELECT COUNT(*) AS COUNT FROM TV_SERIES'''
QUERY_GET_MAX_SERIES_ID         = '''SELECT MAX(ID) AS ID FROM TV_SERIES'''
QUERY_GET_MAX_EPISODE_ID        = '''SELECT MAX(ID) AS ID FROM TV_SERIES_EPISODES'''

QUERY_GET_SERIES                = '''SELECT t.ID,
                                            t.TITLE,
                                            IFNULL (t.YEAR, '') AS YEAR,
                                            t.WATCHED,
                                            CASE 
                                                WHEN (SELECT COUNT(*)  
                                                      FROM TV_SERIES_EPISODES  
                                                      WHERE SERIES_ID=t.ID 
                                                        AND TO_BURN=1) > 0  
                                                THEN 1 
                                                ELSE 0 
                                            END AS TO_BURN,
                                            t.RATING,
                                            IFNULL (t.SEASONS, '') AS SEASONS,
                                            t.CREATED_DATE
                                     FROM TV_SERIES t
                                       LEFT JOIN MEDIA_SOURCE s ON t.SOURCE_ID  = s.ID
                                     {where}
                                     ORDER BY t.TITLE'''

QUERY_GET_SERIES_DETAIL         = '''SELECT t.ID,
                                            t.TITLE, 
                                            IFNULL (t.ORIGINAL_TITLE, '') AS ORIGINAL_TITLE,
                                            IFNULL (t.YEAR, '') AS YEAR,
                                            t.WATCHED,
                                            t.RATING,
                                            t.ONLINE_RATING,
                                            IFNULL (t.SEASONS, '') AS SEASONS,
                                            IFNULL (t.COUNTRY, '') AS COUNTRY,
                                            t.CERTIFICATION,
                                            IFNULL (s.SOURCE, '') AS SOURCE,
                                            IFNULL (t.RELEASE_DATE, '') AS RELEASE_DATE,
                                            IFNULL (t.TAGLINE, '') AS TAGLINE,
                                            IFNULL (t.PLOT, '') AS PLOT,
                                            IFNULL (t.NOTES, '') AS NOTES,
                                            IFNULL (t.DIRECTOR, '') AS DIRECTOR,
                                            IFNULL (t.WRITER, '') AS WRITER,
                                            t.CREATED_DATE
                                     FROM TV_SERIES t
                                       LEFT JOIN MEDIA_SOURCE s ON t.SOURCE_ID  = s.ID
                                     WHERE t.ID ={id}'''

QUERY_GET_SERIES_EPISODES       = '''SELECT t.ID,
                                            t.SEASON,
                                            t.EPISODE,
                                            t.TITLE,
                                            t.WATCHED,
                                            t.BACKUP_DISC,
                                            t.SIZE
                                     FROM TV_SERIES_EPISODES t
                                     WHERE t.SERIES_ID = {id}
                                     {where_clause}
                                     ORDER BY t.SEASON, t.EPISODE'''

QUERY_GET_SERIES_GENRES         = '''SELECT g.GENRE
                                     FROM TV_SERIES_GENRES t
                                        INNER JOIN GENRES g ON g.ID = t.GENRE_ID
                                     WHERE t.SERIES_ID = {id}
                                     ORDER BY g.GENRE'''

QUERY_GET_SERIES_LANGUAGES      = '''SELECT l.LANGUAGE
                                     FROM TV_SERIES_LANGUAGES t
                                        INNER JOIN LANGUAGES l ON l.ID = t.LANGUAGE_ID
                                     WHERE t.SERIES_ID = {id}
                                     ORDER BY l.LANGUAGE'''

QUERY_GET_SERIES_CAST           = '''SELECT a.NAME,
                                            t.CHARACTER,
                                            t.EPISODES
                                     FROM TV_SERIES_CAST t
                                        INNER JOIN ACTORS a ON a.ID = t.ACTOR_ID
                                     WHERE t.SERIES_ID = {id}
                                     ORDER BY a.NAME'''

QUERY_FILTER_SERIES_GENRES      = '''SELECT GENRE_ID 
                                     FROM TV_SERIES_GENRES 
                                     WHERE SERIES_ID = t.ID'''

QUERY_FILTER_SERIES_LANGUAGE    = '''SELECT LANGUAGE_ID 
                                     FROM TV_SERIES_LANGUAGES 
                                     WHERE SERIES_ID = t.ID'''

QUERY_FILTER_SERIES_CAST        = '''SELECT a.NAME 
                                     FROM TV_SERIES_CAST c 
                                       INNER JOIN ACTORS a ON a.ID = c.ACTOR_ID 
                                     WHERE c.SERIES_ID = t.ID 
                                       AND a.NAME LIKE "%{actor}%"'''

QUERY_GET_EPISODE_DETAILS       = '''SELECT t.ID,
                                            t.SEASON, 
                                            t.EPISODE,
                                            t.TITLE,
                                            t.WATCHED,
                                            IFNULL (t.BACKUP_DISC, '') AS BACKUP_DISC,
                                            IFNULL (t.SIZE, '') AS SIZE,
                                            IFNULL (q.QUALITY, '') AS QUALITY,
                                            IFNULL (t.RELEASE_DATE, '') AS RELEASE_DATE,
                                            t.TO_BURN,
                                            IFNULL (t.TAG, '') AS TAG,
                                            IFNULL (t.PLOT, '') AS PLOT
                                     FROM TV_SERIES_EPISODES t
                                        LEFT JOIN MEDIA_QUALITY q ON t.QUALITY_ID = q.ID
                                     WHERE t.ID = {id}'''

QUERY_GET_SERIES_DISCS          = '''SELECT DISTINCT BACKUP_DISC 
                                     FROM TV_SERIES_EPISODES 
                                     WHERE BACKUP_DISC IS NOT NULL
                                     ORDER BY BACKUP_DISC'''

QUERY_ADD_NEW_SERIES            = '''INSERT INTO TV_SERIES (TITLE, CREATED_DATE, UPDATED_DATE)
                                     VALUES ("{0}", "{1}", "{2}")'''

QUERY_ADD_NEW_EPISODE            = '''INSERT INTO TV_SERIES_EPISODES (SEASON, EPISODE, TITLE, SERIES_ID, PLOT, RELEASE_DATE, CREATED_DATE, UPDATED_DATE)
                                     VALUES ({0}, {1}, "{2}", {3}, "{4}", "{5}", "{6}", "{7}")'''

QUERY_DELETE_SERIES_CAST        = '''DELETE FROM TV_SERIES_CAST WHERE SERIES_ID={id}'''
QUERY_DELETE_SERIES_LANGUAGES   = '''DELETE FROM TV_SERIES_LANGUAGES WHERE SERIES_ID={id}'''
QUERY_DELETE_SERIES_GENRES      = '''DELETE FROM TV_SERIES_GENRES WHERE SERIES_ID={id}'''
QUERY_DELETE_SERIES_EPISODES    = '''DELETE FROM TV_SERIES_EPISODES WHERE SERIES_ID={id}'''
QUERY_DELETE_SERIES_EPISODE     = '''DELETE FROM TV_SERIES_EPISODES WHERE ID IN ({id})'''
QUERY_DELETE_SERIES             = '''DELETE FROM TV_SERIES WHERE ID={id}'''

QUERY_UPDATE_SERIES             = '''UPDATE TV_SERIES SET {updates} WHERE ID = {id}'''
QUERY_UPDATE_SERIES_EPISODE     = '''UPDATE TV_SERIES_EPISODES SET {updates} WHERE ID = {id}'''

QUERY_UPDATE_SERIES_SOURCE      = '''UPDATE TV_SERIES
                                     SET LOOKUP_SOURCE = "{source}",
                                         SOURCE_URL    = "{source_url}"
                                     WHERE ID = {id}'''

QUERY_ADD_SERIES_GENRE           = '''INSERT INTO TV_SERIES_GENRES (SERIES_ID, GENRE_ID, CREATED_DATE)
                                     VALUES ({}, {}, "{}")'''

QUERY_REMOVE_SERIES_GENRE        = '''DELETE FROM TV_SERIES_GENRES 
                                      WHERE GENRE_ID = (SELECT ID 
                                                        FROM GENRES 
                                                        WHERE GENRE = "{}") 
                                       AND SERIES_ID = {}'''

QUERY_ADD_SERIES_LANGUAGE       = '''INSERT INTO TV_SERIES_LANGUAGES (SERIES_ID, LANGUAGE_ID, CREATED_DATE)
                                     VALUES ({}, {}, "{}")'''

QUERY_REMOVE_SERIES_LANGUAGE    = '''DELETE FROM TV_SERIES_LANGUAGES 
                                     WHERE LANGUAGE_ID = (SELECT ID 
                                                          FROM LANGUAGES 
                                                          WHERE LANGUAGE = "{}") 
                                       AND SERIES_ID = {}'''

QUERY_ADD_SERIES_CAST           = '''INSERT INTO TV_SERIES_CAST (SERIES_ID, ACTOR_ID, CHARACTER, EPISODES, CREATED_DATE)
                                     VALUES ({}, {}, "{}", "{}", "{}")'''

QUERY_REMOVE_SERIES_CAST        = '''DELETE FROM SERIES_CAST WHERE ID = {id}'''

#=======================================================================