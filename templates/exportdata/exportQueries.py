#=======================================================================
# Description:
# Queries to fetch data used for exporting by different exporters
#=======================================================================

QUERY_EXPORT_MOVIES = '''SELECT m.ID,
                                m.TITLE,
                                m.ORIGINAL_TITLE,
                                m.YEAR,
                                m.RUNTIME,
                                m.COUNTRY,
                                CASE WHEN m.WATCHED == 0 THEN 'False' ELSE 'True' END AS WATCHED,
                                m.ONLINE_RATING,
                                m.RATING,
                                m.CERTIFICATION,
                                m.RELEASE_DATE,
                                m.TAGLINE,
                                m.PLOT,
                                m.NOTES,
                                ms.SOURCE,
                                mq.QUALITY,
                                me.EDITION,
                                m.VIDEO_CODEC,
                                m.AUDIO_CODEC,
                                m.SIZE,
                                m.DISC_COUNT,
                                CASE WHEN m.TO_BURN == 0 THEN 'False' ELSE 'True' END AS TO_BURN,
                                m.BACKUP_DISC,
                                m.TAG,
                                m.LOOKUP_SOURCE,
                                m.SOURCE_URL,
                                IFNULL(m.POSTER_URL, '') AS POSTER_URL,
                                (SELECT GROUP_CONCAT(g.GENRE) 
                                FROM MOVIE_GENRES mg 
                                    INNER JOIN GENRES g ON mg.GENRE_ID = g.ID
                                WHERE MOVIE_ID = m.ID) AS GENRES,
                                (SELECT GROUP_CONCAT(l.LANGUAGE) 
                                FROM MOVIE_LANGUAGES ml 
                                    INNER JOIN LANGUAGES l ON ml.LANGUAGE_ID = l.ID
                                WHERE MOVIE_ID = m.ID) AS LANGUAGES
                        FROM MOVIES m
                        	LEFT JOIN MEDIA_SOURCE ms ON m.SOURCE_ID = ms.ID
                            LEFT JOIN MEDIA_QUALITY mq ON m.QUALITY_ID = mq.ID
                            LEFT JOIN MEDIA_EDITION me ON m.EDITION_ID = me.ID
                        ORDER BY m.TITLE'''


QUERY_EXPORT_SERIES = '''SELECT s.ID,
                                s.TITLE,
                                s.ORIGINAL_TITLE,
                                s.YEAR,
                                s.SEASONS,
                                s.COUNTRY,
                                CASE WHEN s.WATCHED == 0 THEN 'FALSE' ELSE 'TRUE' END AS WATCHED,
                                s.ONLINE_RATING,
                                s.RATING,
                                s.RELEASE_DATE,
                                s.CERTIFICATION,
                                s.TAGLINE,
                                s.PLOT,
                                s.NOTES,
                                s.LOOKUP_SOURCE,
                                s.SOURCE_URL,
                                IFNULL(s.POSTER_URL, '') AS POSTER_URL,
                                se.SEASON AS EPISODE_SEASON,
                                se.EPISODE,
                                se.TITLE AS EPISODE_TITLE,
                                se.PLOT AS EPISODE_PLOT,
                                CASE WHEN se.WATCHED == 0 THEN 'FALSE' ELSE 'TRUE' END AS EPISODE_WATCHED,
                                IFNULL(q.QUALITY, '') AS EPISODE_QUALITY,
                                CASE WHEN se.TO_BURN == 0 THEN 'FALSE' ELSE 'TRUE' END AS EPISODE_TO_BURN,
                                se.BACKUP_DISC AS EPISODE_BACKUP_DISC,
                                se.TAG AS EPISODE_TAG,
                                se.SIZE AS EPISODE_SIZE,
                                (SELECT GROUP_CONCAT(g.GENRE) 
                                FROM TV_SERIES_GENRES sg 
                                    INNER JOIN GENRES g ON sg.GENRE_ID = g.ID
                                WHERE SERIES_ID = s.ID) AS GENRES,
                                (SELECT GROUP_CONCAT(l.LANGUAGE) 
                                FROM TV_SERIES_LANGUAGES sl 
                                    INNER JOIN LANGUAGES l ON sl.LANGUAGE_ID = l.ID
                                WHERE SERIES_ID = s.ID) AS LANGUAGES
                        FROM TV_SERIES s
                            LEFT JOIN TV_SERIES_EPISODES se ON s.ID = se.SERIES_ID
                            LEFT JOIN MEDIA_QUALITY q ON se.QUALITY_ID = q.ID
                        ORDER BY s.TITLE, se.SEASON, se.EPISODE'''

#=======================================================================