#=======================================================================
# Description:
# Model class for all QTableView elements in the form
#=======================================================================
import numpy  as np
import pandas as pd

from PySide6.QtCore    import Qt, QAbstractTableModel, QModelIndex
from PySide6.QtGui     import QIcon
from PySide6.QtWidgets import QApplication, QStyle
from utils.constants   import (
    MEDIA_CENTER_ALIGN_COLUMNS, 
    HEADER_ICON_COLUMNS,
    MEDIA_TYPE
)

#=======================================================================
class TableModel(QAbstractTableModel):
    """
    A custom table model for displaying data in a QTableView. This model supports displaying
    data with icons for boolean values and custom header icons.

    Attributes:
        _data (DataFrame): The data to be displayed in the table.
        _media_type (MEDIA_TYPE): The type of media being represented, default is MEDIA_TYPE.MOVIE.

    Methods:
        __init__(data, media_type=MEDIA_TYPE.MOVIE):
            Initializes the TableModel with the given data and media type.

        rowCount(parent=None):
            Returns the number of rows in the data.

        columnCount(parent=None):
            Returns the number of columns in the data.

        data(index, role=Qt.DisplayRole):
            Returns the data for the given index and role. Supports displaying icons for boolean
            values and aligning text for specific columns.

        headerData(col, orientation, role):
            Returns the header data for the given column, orientation, and role. Supports displaying
            icons for specific columns in the header.

    Parameters:
        data (DataFrame): The data to be displayed in the table.
        media_type (MEDIA_TYPE, optional): The type of media being represented. Defaults to MEDIA_TYPE.MOVIE.

    Returns:
        Various methods return different types:
        - rowCount and columnCount return int, representing the number of rows and columns respectively.
        - data and headerData return QVariant, representing the data or header information for the given index.
    """

    def __init__(self, data : pd.DataFrame, media_type=MEDIA_TYPE.MOVIE) -> None:
        """
        Initializes the TableModel with the provided data and media type.

        Parameters:
        - data: DataFrame
            The data to be displayed in the table. This is expected to be a pandas DataFrame.
        - media_type: MEDIA_TYPE, optional
            The type of media being represented in the table. Defaults to MEDIA_TYPE.MOVIE.
        """
        super(TableModel, self).__init__()
        self._data       = data
        self._media_type = media_type


    def rowCount(self, parent=None) -> int:
        """
        Returns the number of rows in the data.

        Parameters:
        - parent (optional): This parameter is not used in the function, but it is included to match the signature of 
        similar functions that might require a parent parameter. It can be of any type.

        Returns:
        - int: The number of rows in the data, which is determined by the number of rows in the `_data` attribute.
        """
        return self._data.shape[0]


    def columnCount(self, parnet=None) -> int:
        """
        Returns the number of columns in the data structure.

        Parameters:
        parent (optional): This parameter is not used in the function. It is included for compatibility with certain interfaces or frameworks that might require it.

        Returns:
        int: The number of columns in the data structure represented by `self._data`.
        """
        return self._data.shape[1]


    def data(self, index : QModelIndex, role=Qt.DisplayRole):
        """
        Retrieves the data for a given index and role from a data model.

        Parameters:
        - index: QModelIndex
            The index in the data model for which data is requested.
        - role: int, optional
            The role for which the data is requested. Default is Qt.DisplayRole.

        Returns:
        - QVariant or None
            Returns a QVariant containing the data for the given index and role.
            If the role is Qt.DecorationRole and the value is a boolean, it returns
            a QIcon representing the boolean state. If the role is Qt.DisplayRole,
            it returns the string representation of the value. If the role is
            Qt.TextAlignmentRole and the column is in MEDIA_CENTER_ALIGN_COLUMNS,
            it returns the alignment flags for center alignment. Returns None if
            the index is invalid or the role is not handled.
        """
        if index.isValid():
            value = self._data.iloc[index.row(), index.column()]
            if isinstance(value, np.bool_):
                if role == Qt.DecorationRole:
                    if value:
                        return QIcon(QApplication.style().standardIcon(QStyle.StandardPixmap.SP_DialogApplyButton))

                    return QIcon(QApplication.style().standardIcon(QStyle.StandardPixmap.SP_DialogCancelButton))
            else:
                if role == Qt.DisplayRole:
                    return str(value)
                
                if role == Qt.TextAlignmentRole:
                    cols = (x for x in MEDIA_CENTER_ALIGN_COLUMNS)
                    if self._data.columns[index.column()] in cols:
                        return Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter

        return None


    def headerData(self, col : int, orientation : Qt.Orientation, role : int):
        """
        Provides header data for a table view, specifically for horizontal headers.

        Parameters:
        - col (int): The column index for which the header data is requested.
        - orientation (Qt.Orientation): The orientation of the header. This function specifically handles Qt.Horizontal.
        - role (int): The role for which the data is requested. This function handles Qt.DecorationRole and Qt.DisplayRole.

        Returns:
        - QIcon or str or None: Returns a QIcon if the column is in HEADER_ICON_COLUMNS and the role is Qt.DecorationRole.
        Returns a formatted string (column name with underscores replaced by spaces and title-cased) if the role is Qt.DisplayRole
        and the column is not in HEADER_ICON_COLUMNS. Returns None if no conditions are met.
        """
        if orientation == Qt.Horizontal and role == Qt.DecorationRole:
            if self._data.columns[col] in (x for x in HEADER_ICON_COLUMNS):
                return QIcon(HEADER_ICON_COLUMNS[self._data.columns[col]])

        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            if self._data.columns[col] not in (x for x in HEADER_ICON_COLUMNS):
                return self._data.columns[col].replace('_', ' ').title()
        
        return None
    
#=======================================================================