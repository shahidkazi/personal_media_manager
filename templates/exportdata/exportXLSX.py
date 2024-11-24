#=======================================================================
# Description:
# Utility to Export Movie / TV Series data to XLSX. The export method is
# a common method that needs to be implemented in any custom exporters
# created and an entry made in registry.json to use in the app.
#=======================================================================
import utils.constants as constants
import utils.dbhelper as dbhelper

from templates.exportdata.exportQueries import QUERY_EXPORT_MOVIES, QUERY_EXPORT_SERIES

#=======================================================================
def export_to_excel(media_type: constants.MEDIA_TYPE, path : str) -> bool:
    """
    Export media data to an Excel file based on the specified media type.

    Args:
        media_type (constants.MEDIA_TYPE): The type of media to export (MOVIE or SERIES).
        path (str): The file path where the Excel output will be saved.

    Returns:
        bool: True if the export is successful, False otherwise.
    """
    try:
        if media_type not in [constants.MEDIA_TYPE.MOVIE, constants.MEDIA_TYPE.SERIES]:
            raise ValueError(f"Invalid media type: {media_type}")

        query = QUERY_EXPORT_MOVIES if media_type == constants.MEDIA_TYPE.MOVIE \
           else QUERY_EXPORT_SERIES

        df_media = dbhelper.execute_read(query)
        df_media.to_excel(path, index=False)
        
        return True
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An error occurred while exporting data: {e}")

    return False

#=======================================================================