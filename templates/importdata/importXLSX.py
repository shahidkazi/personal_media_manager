#=======================================================================
# Description:
# Utility to Import Movie / TV Series data from Excel. The import_media method is
# a common method that needs to be implemented in any custom importers
# created and an entry made in registry.json to use in the app.
#=======================================================================
import pandas as pd

from utils.constants import MEDIA_TYPE
from templates.importdata.importTools import save_movies, save_series

#=======================================================================
def import_media(media_type : MEDIA_TYPE, path : str, column_map : dict) -> bool:
    """
    Import media data from a CSV file and save it based on the specified media type.

    Args:
        media_type (MEDIA_TYPE): The type of media to import (MOVIE or SERIES).
        path (str): The file path to the CSV file containing the media data.
        column_map (dict): A mapping of column names from the input data to the desired format.

    Returns:
        bool: True if the import is successful, False otherwise.
    """
    try:
        if media_type not in [MEDIA_TYPE.MOVIE, MEDIA_TYPE.SERIES]:
            raise ValueError(f"Invalid media type: {media_type}")

        df = pd.read_excel(path)
        return save_movies(df, column_map) if media_type == MEDIA_TYPE.MOVIE \
            else save_series(df, column_map)
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return False

#=======================================================================