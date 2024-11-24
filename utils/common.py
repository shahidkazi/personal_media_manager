#=======================================================================
# Description: 
# Utility module to host common functions used across the applciation
#=======================================================================
from PySide6.QtCore    import Qt
from PySide6.QtWidgets import QTableView
from utils.constants   import MESSAGE_TYPE

#=======================================================================
def getColIndexinTableView(tblView : QTableView, colname : str) -> int:
    """
    Retrieves the index of a specified column in a QTableView.

    Parameters:
    - tblView (QTableView): The table view to search within.
    - colname (str): The name of the column to find.

    Returns:
    - int: The index of the column if found, otherwise -1.
    """
    for col in range(tblView.model().columnCount()):
        if tblView.model().headerData(col, Qt.Horizontal, Qt.DisplayRole) == colname.replace('_', ' ').title():
            return col
        
    return -1


def isNumeric(value : object) -> bool:
    """
    Determines if the provided value can be converted to a float, indicating it is numeric.

    Parameters:
    value (any type): The value to be checked for numeric conversion.

    Returns:
    bool: True if the value can be converted to a float (is numeric), False otherwise.

    Exceptions:
    ValueError: Raised if the conversion to float fails, indicating the value is not numeric.
    """
    try:
        if value is not None and float(value):
            return True
    except ValueError:
        return False
    
    return False


def getStatusStyleSheet(message_type=MESSAGE_TYPE.INFO) -> str:
    """
    Returns a CSS style string based on the message type.

    Parameters:
    message_type (MESSAGE_TYPE): The type of message, which determines the style.

    Returns:
    str: A CSS style string for the given message type.
    """
    return ''            if message_type == MESSAGE_TYPE.INFO \
      else 'color: red;' if message_type == MESSAGE_TYPE.WARNING \
      else 'color: red;font-weight:bold;'

#=======================================================================