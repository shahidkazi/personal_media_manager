#=======================================================================
# Description: 
# Script for housing all the constants and configs that are static and
# better to be centralized than hardcoded across the application  
#=======================================================================
class MEDIA_TYPE:
   '''
   Types of media supported in the application
   '''
   MOVIE          = 'MOVIE'
   SERIES         = 'SERIES'


class MEDIA_COLUMNS:
   '''
   Class containing common db columns across Movies, TV Series and Episodes
   to avoid hardcoding and typo errors in the code when needed to access
   in the business logic
   '''
   ID             = 'ID'
   TITLE          = 'TITLE'
   ORIGINAL_TITLE = 'ORIGINAL_TITLE'
   YEAR           = 'YEAR'
   COUNTRY        = 'COUNTRY'
   WATCHED        = 'WATCHED'
   ONLINE_RATING  = 'ONLINE_RATING'
   RATING         = 'RATING'
   CERTIFICATION  = 'CERTIFICATION'
   RELEASE_DATE   = 'RELEASE_DATE'
   TAGLINE        = 'TAGLINE'
   PLOT           = 'PLOT'
   NOTES          = 'NOTES'
   QUALITY        = 'QUALITY'
   TO_BURN        = 'TO_BURN'
   BACKUP_DISC    = 'BACKUP_DISC'
   TAG            = 'TAG'
   SIZE           = 'SIZE'
   LOOKUP_SOURCE  = 'LOOKUP_SOURCE'
   SOURCE_URL     = 'SOURCE_URL'
   QUALITY_ID     = 'QUALITY_ID'
   NAME           = 'NAME'
   CHARACTER      = 'CHARACTER'
   DIRECTOR       = 'DIRECTOR'
   WRITER         = 'WRITER'
   POSTER_URL     = 'POSTER_URL'
   UPDATED_DATE   = 'UPDATED_DATE'
   ONLINE_ID      = 'ONLINE_ID'


class MOVIE_COLUMNS:
   '''
   DB Columns specific to the Movies media type
   '''
   RUNTIME        = 'RUNTIME'
   SOURCE         = 'SOURCE'
   EDITION        = 'EDITION'
   VIDEO_CODEC    = 'VIDEO_CODEC'
   AUDIO_CODEC    = 'AUDIO_CODEC'
   DISC_COUNT     = 'DISC_COUNT'
   SOURCE_ID      = 'SOURCE_ID'
   EDITION_ID     = 'EDITION_ID'


class SERIES_COLUMNS:
   '''
   DB Columns specific to the TV Series media type
   '''
   SEASONS        = 'SEASONS'
   EPISODES       = 'EPISODES'


class EPISODE_COLUMNS:
   '''
   DB Columns specific to TV Series episodes
   '''
   ID             = 'ID'
   SERIES_ID      = 'SERIES_ID'
   SEASON         = 'SEASON'
   EPISODE_SEASON = 'EPISODE_SEASON'
   EPISODE        = 'EPISODE'
   EPISODE_TITLE  = 'EPISODE_TITLE'
   EPISODE_PLOT   = 'EPISODE_PLOT'
   WATCHED        = 'WATCHED'
   QUALITY_ID     = 'QUALITY_ID'
   TO_BURN        = 'TO_BURN'
   BACKUP_DISC    = 'BACKUP_DISC'
   TAG            = 'TAG'
   SIZE           = 'SIZE'
   CREATED_DATE   = 'CREATED_DATE'
   UPDATED_DATE   = 'UPDATED_DATE'


class FILTER_COLUMNS: 
   '''
   DB columns used for filtering media
   '''
   TITLE          = 'TITLE'
   WATCHED        = 'WATCHED'
   TO_BURN        = 'TO_BURN'
   GENRE          = 'GENRE'
   QUALITY        = 'QUALITY'
   BACKUP_DISC    = 'BACKUP_DISC'
   DIRECTOR       = 'DIRECTOR'
   EDITION        = 'EDITION'
   SOURCE         = 'SOURCE'
   YEAR           = 'YEAR'
   ACTOR          = 'ACTOR'
   LANGUAGE       = 'LANGUAGE'


class MEDIA_DETAILS:
   '''
   Paylod types when retrieving media details
   '''
   CAST           = 'CAST'
   CONTENT        = 'DETAILS'
   EPISODES       = 'EPISODES'
   GENRES         = 'GENRES'
   LANGUAGES      = 'LANGUAGES'
   OTHERS         = 'OTHERS'


class META_COLUMNS:
   '''
   DB columns for meta data used for all media types
   '''
   GENRE          = 'GENRE'
   EDITION        = 'EDITION'
   QUALITY        = 'QUALITY'
   SOURCE         = 'SOURCE'
   LANGUAGE       = 'LANGUAGE'
   CAST           = 'CAST'


class MESSAGE_TYPE:
   '''
   Type of message to identify and display accodingly in the UI
   '''
   INFO           = 'INFO'
   WARNING        = 'WARNING'
   ERROR          = 'ERROR'


class APP_CONFIG:
   '''
   Application Configuration ttributes available
   '''
   POSTER_PATH       = 'DEFAULT_POSTER_PATH'
   EXPORT_TEMPLATES  = 'EXPORT_TEMPLATES'
   IMPORT_TEMPLATES  = 'IMPORT_TEMPLATES'
   LOOKUP_TEMPLATES  = 'LOOKUP_TEMPLATES'
   PUBLISH_TEMPLATES = 'PUBLISH_TEMPLATES'
   DEFAULT_LOOKUP    = 'DEFAULT_LOOKUP'
   DEFAULT_PUBLISH   = 'DEFAULT_PUBLISH'

#=======================================================================
# PATH DECLARATIONS
#=======================================================================
DEFAULT_DB_PATH                = 'data/moviedb.db'
DEFAULT_POSTER                 = 'images/posters/noposter.jpg'

DEFAULT_TEMPLATES_PATH         = 'templates'
DEFAULT_EXPORT_TEMPLATES_PATH  = DEFAULT_TEMPLATES_PATH + '/exportdata'
DEFAULT_IMPORT_TEMPLATES_PATH  = DEFAULT_TEMPLATES_PATH + '/importdata'
DEFAULT_LOOKUP_TEMPLATES_PATH  = DEFAULT_TEMPLATES_PATH + '/lookup'
DEFAULT_PUBLISH_TEMPLATES_PATH = DEFAULT_TEMPLATES_PATH + '/publish'

#=======================================================================
# UI RELATED CONSTANTS
#=======================================================================
''' UI filter to DB column mapping based on media type '''
MEDIA_FILTER_COLUMNS           = { MEDIA_TYPE.MOVIE : {
                                       FILTER_COLUMNS.BACKUP_DISC : 'm.BACKUP_DISC',
                                       FILTER_COLUMNS.SOURCE      : 'm.SOURCE_ID',
                                       FILTER_COLUMNS.QUALITY     : 'm.QUALITY_ID',
                                       FILTER_COLUMNS.EDITION     : 'm.EDITION_ID',
                                       FILTER_COLUMNS.TO_BURN     : 'm.TO_BURN',
                                       FILTER_COLUMNS.WATCHED     : 'm.WATCHED',
                                       FILTER_COLUMNS.TITLE       : 'm.TITLE',
                                       FILTER_COLUMNS.DIRECTOR    : 'm.DIRECTOR',
                                       FILTER_COLUMNS.YEAR        : 'm.YEAR'
                                   },
                                   MEDIA_TYPE.SERIES : {
                                       FILTER_COLUMNS.BACKUP_DISC : 'BACKUP_DISC',
                                       FILTER_COLUMNS.SOURCE      : 't.SOURCE_ID',
                                       FILTER_COLUMNS.TO_BURN     : 'TO_BURN',
                                       FILTER_COLUMNS.WATCHED     : 't.WATCHED',
                                       FILTER_COLUMNS.TITLE       : 't.TITLE',
                                       FILTER_COLUMNS.DIRECTOR    : 't.DIRECTOR',
                                       FILTER_COLUMNS.YEAR        : 't.YEAR'
                                   }
                                 }

''' Boolean columns for displaying as tick/cross icon in UI '''
MEDIA_BOOLEAN_COLUMNS         = [ MEDIA_COLUMNS.WATCHED, 
                                  MEDIA_COLUMNS.TO_BURN ]

''' Columns widths for displaying movie list in main screen '''
MOVIE_CUSTOM_COL_WIDTHS       = { MEDIA_COLUMNS.YEAR    : 50,
                                  MEDIA_COLUMNS.WATCHED : 25,
                                  MEDIA_COLUMNS.TO_BURN : 25,
                                  MEDIA_COLUMNS.RATING  : 50,
                                  MEDIA_COLUMNS.SIZE    : 75 }

''' Columns to be center aligned when shown in any table '''
MEDIA_CENTER_ALIGN_COLUMNS    = [ MEDIA_COLUMNS.YEAR,
                                  MEDIA_COLUMNS.RATING,
                                  MEDIA_COLUMNS.BACKUP_DISC,
                                  SERIES_COLUMNS.SEASONS,
                                  EPISODE_COLUMNS.SEASON,
                                  EPISODE_COLUMNS.EPISODE ]

''' Columns to be displayed in Movie Tab on main screen '''
MOVIE_SUMMARY_DISPLAY_COLS    = [ MEDIA_COLUMNS.TITLE,
                                  MEDIA_COLUMNS.YEAR,
                                  MEDIA_COLUMNS.WATCHED, 
                                  MEDIA_COLUMNS.TO_BURN,
                                  MEDIA_COLUMNS.RATING,
                                  MEDIA_COLUMNS.SIZE ]

''' Icons to be used in place of text in table headers '''
HEADER_ICON_COLUMNS           = { MEDIA_COLUMNS.WATCHED : 'images/icons/seen.png',
                                  MEDIA_COLUMNS.TO_BURN : 'images/icons/compact-disc-solid.svg' }

SERIES_SUMMARY_DISPLAY_COLS   = [ MEDIA_COLUMNS.TITLE,
                                  MEDIA_COLUMNS.YEAR,
                                  MEDIA_COLUMNS.WATCHED, 
                                  MEDIA_COLUMNS.TO_BURN,
                                  MEDIA_COLUMNS.RATING,
                                  SERIES_COLUMNS.SEASONS ]

''' Column widths for displaying coluns for TV Series '''
SERIES_CUSTOM_COL_WIDTHS      = { MEDIA_COLUMNS.YEAR     : 50,
                                  MEDIA_COLUMNS.WATCHED  : 25,
                                  MEDIA_COLUMNS.TO_BURN  : 25,
                                  MEDIA_COLUMNS.RATING   : 50,
                                  SERIES_COLUMNS.SEASONS : 70 }

''' Columns to be displayed for TV Series in the main UI '''
SERIES_EPISODE_DISPLAY_COLS   = [ EPISODE_COLUMNS.SEASON,
                                  EPISODE_COLUMNS.EPISODE,
                                  MEDIA_COLUMNS.TITLE,
                                  EPISODE_COLUMNS.WATCHED, 
                                  EPISODE_COLUMNS.BACKUP_DISC,
                                  EPISODE_COLUMNS.SIZE ]

''' Columns widths for Episodes Table '''
EPISODES_CUSTOM_COL_WIDTHS    = { EPISODE_COLUMNS.SEASON      : 60,
                                  EPISODE_COLUMNS.EPISODE     : 50,
                                  EPISODE_COLUMNS.WATCHED     : 25,
                                  EPISODE_COLUMNS.BACKUP_DISC : 75,
                                  EPISODE_COLUMNS.SIZE        : 50 }

''' Columns to be hidden for the Cast Tab in Details section '''
CAST_HIDE_COLUMNS             = [ MEDIA_COLUMNS.ID ]

#=======================================================================