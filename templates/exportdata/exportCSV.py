#=======================================================================
# Description:
# Utility to Export Movie / TV Series data to CSV. The export method is
# a common method that needs to be implemented in any custom exporters
# created and an entry made in registry.json to use in the app.
#=======================================================================

import utils.constants as constants
import utils.dbhelper as dbhelper

from templates.exportdata.exportQueries import QUERY_EXPORT_MOVIES, QUERY_EXPORT_SERIES


#=======================================================================
def export(media_type : constants.MEDIA_TYPE, path : str) -> bool:
    """
    Export media data to a CSV file based on the specified media type.
    
    Args:
        media_type (constants.MEDIA_TYPE): Type of media (MOVIE or SERIES).
        path (str): File path for the exported CSV file.
    
    Returns:
        bool: True if export is successful, False otherwise.
    """
    try:
        query    = QUERY_EXPORT_MOVIES if media_type == constants.MEDIA_TYPE.MOVIE \
              else QUERY_EXPORT_SERIES
        
        df_media = dbhelper.execute_read(query)
        df_media.to_csv(path, index=False)
    except Exception as e:
        print(f"Error occurred while exporting data: {e}")
        return False

    return True


#=======================================================================