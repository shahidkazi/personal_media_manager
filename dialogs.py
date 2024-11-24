#=======================================================================
# Description:
# Contains all the Dialog Boxes for different operations in the application
#=======================================================================
import os
import model
import requests
import pandas as pd
import utils.metahelper as metahelper

from PySide6.QtCore     import Signal, QThreadPool, QRunnable, Slot, Qt, QRect
from PySide6.QtGui      import QPixmap, QImage
from PySide6.QtWidgets  import QDialog, QLabel, QFileDialog, QTableWidgetItem, QComboBox, QVBoxLayout, QHBoxLayout, QPushButton

from ui.ui_about        import Ui_AboutDialog
from ui.ui_addmedia     import Ui_AddNewMedia
from ui.ui_addepisode   import Ui_AddNewEpisode
from ui.ui_bulkupdate   import Ui_BulkUpdateDialog
from ui.ui_export       import Ui_ExportDialog
from ui.ui_faqs         import Ui_FAQDialog
from ui.ui_fetchdetails import Ui_FetchDetailsDialog
from ui.ui_filters      import Ui_FiltersDialog
from ui.ui_import       import Ui_ImportDialog
from ui.ui_preferences  import Ui_PreferencesDialog
from ui.ui_publish      import Ui_PublishDialog

from tablemodel         import TableModel

from utils.common       import getColIndexinTableView, isNumeric, getStatusStyleSheet
from utils.constants    import (
    MEDIA_TYPE,
    MEDIA_COLUMNS,
    MEDIA_DETAILS,
    META_COLUMNS,
    MOVIE_COLUMNS,
    SERIES_COLUMNS,
    EPISODE_COLUMNS,
    FILTER_COLUMNS,
    APP_CONFIG,
    MESSAGE_TYPE,
    DEFAULT_POSTER,
    DEFAULT_POSTER_PATH
)

#=======================================================================
class AboutDialog(QDialog):
    """
    A dialog class for displaying information about the application.

    Attributes:
    ui (Ui_AboutDialog): An instance of the UI setup for the About dialog.

    Methods:
    __init__(clsUi=None, parent=None):
        Initializes the AboutDialog with optional UI class and parent widget.
    """

    def __init__(self, clsUi=None, parent=None) -> None:
        """
        Initializes the AboutDialog with optional UI class and parent widget.

        Parameters:
        clsUi (optional): The UI class to be used for setting up the dialog.
        parent (optional): The parent widget for the dialog.
        """
        super().__init__(parent)
        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)


#=======================================================================
class AddNewMediaDialog(QDialog):
    """
    A dialog window for adding new media entries, such as movies or series, to the application.

    Attributes:
        parent (QWidget): The parent widget of this dialog.
        ui (Ui_AddNewMedia): The user interface setup for the dialog.

    Methods:
        __init__(clsUi=None, parent=None):
            Initializes the dialog, sets up the UI, and connects signals to slots.
        
        saveMedia():
            Saves the media entries input by the user. Determines the type of media (movie or series)
            and attempts to add each entry to the model. Displays a message box indicating success or
            failure for each entry.
    """

    def __init__(self, clsUi=None, parent=None) -> None:
        """
        Initializes the AddNewMediaDialog class, which sets up the user interface for adding new media.

        Parameters:
        clsUi (optional): The UI class to be used for the dialog. Default is None.
        parent (optional): The parent widget for this dialog. Default is None.

        This constructor performs the following actions:
        - Connects the accepted signal of the buttonBox to the saveMedia method.
        - Sets the current index of the mediaTypeComboBox to match the current index of the tbSummary in the parent UI.
        """
        super().__init__(parent)
        self.parent = parent
        self.ui = Ui_AddNewMedia()
        self.ui.setupUi(self)

        self.ui.btnSave.clicked.connect(self.saveMedia)
        self.ui.btnCancel.clicked.connect(self.close)
        self.ui.mediaTypeComboBox.setCurrentIndex(parent.ui.tbSummary.currentIndex())

    
    def writeStatus(self, message : str, message_type=MESSAGE_TYPE.INFO) -> None:
        """
        Updates the status label with a given message and style.
        
        Parameters:
            message (str): The status message to display.
            message_type (str, optional): The type of message (MESSAGE_TYPE.INFO or MESSAGE_TYPE.ERROR) to determine the style.
        """
        self.ui.lblStatus.setStyleSheet(getStatusStyleSheet(message_type))
        self.ui.lblStatus.setText(message)


    def saveMedia(self) -> None:
        """
        Saves a list of media entries (either movies or series) from a text input field to a database.

        This function retrieves a list of media names from a text input field, determines the type of media 
        (movie or series) based on a combo box selection, and attempts to add each media entry to a database. 
        If an entry fails to be added, it is recorded in a list of failed entries. A message box is displayed 
        to inform the user of the success or failure of the operation, and the media list is refreshed.

        Parameters:
        - self: The instance of the class containing this method. It is expected to have the following attributes:
        - ui: An object with the following attributes:
            - txtMediaList: A text input field containing the list of media entries.
            - mediaTypeComboBox: A combo box for selecting the type of media (either 'Movie' or 'Series').
        - parent: An object with a method `refreshMedia()` to refresh the media list.
        """
        try:
            media_list     = self.ui.txtMediaList.document().toPlainText().split('\n')
            failed_entries = []
            for media in media_list:
                media_id = model.add_new_movie(media) if self.ui.mediaTypeComboBox.currentText() == 'Movie' \
                      else model.add_new_series(media)
                
                if media_id == -1:
                    failed_entries.append(media)

            if len(failed_entries) > 0:
                self.writeStatus(f'Error adding: {', '.join(failed_entries)}', MESSAGE_TYPE.ERROR)
    
            self.close()
            self.parent.writeStatus('Entries added successfully...', MESSAGE_TYPE.INFO)
            self.parent.refreshMedia()
        except Exception as e:
            self.ui.parent.writeStatus(f'saveMedia: {e}', message_type=MESSAGE_TYPE.ERROR)


#=======================================================================
class BulkUpdateDialog(QDialog):
    """
    A dialog class for performing bulk updates on media entries. This dialog allows users to update multiple
    media records at once by selecting various attributes such as genre, source, edition, quality, and more.

    Attributes:
        parent (QWidget): The parent widget of the dialog.
        ui (Ui_BulkUpdateDialog): The user interface object for the dialog.

    Methods:
        __init__(clsUi=None, parent=None):
            Initializes the dialog with optional UI class and parent widget.
        
        setGenreComboBox():
            Populates the genre combo box with available genres from the metadata helper.
        
        setSourceComboBox():
            Populates the source combo box with available media sources from the metadata helper.
        
        setEditionComboBox():
            Populates the edition combo box with available media editions from the metadata helper.
        
        setQualityComboBox():
            Populates the quality combo box with available media qualities from the metadata helper.
        
        updateMedia():
            Updates the selected media entries based on the user's selections in the dialog.
    """

    def __init__(self, clsUi=None, parent=None) -> None:
        """
        Initializes the BulkUpdateDialog.

        Parameters:
            clsUi (optional): The UI class for the dialog. Defaults to None.
            parent (QWidget, optional): The parent widget of the dialog. Defaults to None.
        """
        super().__init__(parent)
        self.parent = parent
        self.ui     = Ui_BulkUpdateDialog()
        self.ui.setupUi(self)

        self.setGenreComboBox()
        self.setSourceComboBox()
        self.setEditionComboBox()
        self.setQualityComboBox()

        self.ui.btnSave.clicked.connect(self.updateMedia)
        self.ui.btnCancel.clicked.connect(self.close)

    
    def writeStatus(self, message : str, message_type=MESSAGE_TYPE.INFO) -> None:
        """
        Updates the status label with a given message and style.
        
        Parameters:
            message (str): The status message to display.
            message_type (str, optional): The type of message (MESSAGE_TYPE.INFO or MESSAGE_TYPE.ERROR) to determine the style.
        """
        self.ui.lblStatus.setStyleSheet(getStatusStyleSheet(message_type))
        self.ui.lblStatus.setText(message)

    
    def setGenreComboBox(self) -> None:
        """
        Populates the genre combo box with available genres from the metadata helper.
        """
        try:
            self.ui.cbBulkGenre.clear()
            df = metahelper.get_genres()
            for _, row in df.iterrows():
                self.ui.cbBulkGenre.addItem(row[META_COLUMNS.GENRE], row[MEDIA_COLUMNS.ID])
        except Exception as e:
            self.writeStatus(f'setGenreComboBox: {e}', MESSAGE_TYPE.ERROR)


    def setSourceComboBox(self) -> None:
        """
        Populates the source combo box with available media sources from the metadata helper.
        """
        try:
            self.ui.cbBulkSource.clear()
            df = metahelper.get_media_sources()
            for _, row in df.iterrows():
                self.ui.cbBulkSource.addItem(row[META_COLUMNS.SOURCE], row[MEDIA_COLUMNS.ID])
        except Exception as e:
            self.writeStatus(f'setSourceComboBox: {e}', MESSAGE_TYPE.ERROR)


    def setEditionComboBox(self) -> None:
        """
        Populates the edition combo box with available media editions from the metadata helper.
        """
        try:
            self.ui.cbBulkEdition.clear()
            df = metahelper.get_media_editions()
            for _, row in df.iterrows():
                self.ui.cbBulkEdition.addItem(row[META_COLUMNS.EDITION], row[MEDIA_COLUMNS.ID])

            self.ui.cbBulkEdition.setCurrentText('Theatrical Edition')
        except Exception as e:
            self.writeStatus(f'setEditionComboBox: {e}', MESSAGE_TYPE.ERROR)


    def setQualityComboBox(self) -> None:
        """
        Populates the Quality combo box with available media qualities from the metadata helper.
        """
        try:
            self.ui.cbBulkQuality.clear()

            df = metahelper.get_media_qualities()
            for _, row in df.iterrows():
                self.ui.cbBulkQuality.addItem(row[META_COLUMNS.QUALITY], row[MEDIA_COLUMNS.ID])
        except Exception as e:
            self.writeStatus(f'setQualityComboBox: {e}', MESSAGE_TYPE.ERROR)


    def updateMedia(self) -> None:
        """
        Updates the media information for selected movies in the UI table.

        This method collects the selected movie IDs from the table and updates their attributes based on the user's input
        in various UI components. The updates are then applied in bulk to the movie model, and the media view is refreshed.

        Parameters:
        - self: The instance of the class containing this method.

        Functionality:
        - Collects selected movie IDs from the UI table.
        - Gathers updates from various UI components (checkboxes, text fields, combo boxes).
        - Updates include source ID, video codec, quality ID, edition ID, watched status, burn status, backup disc number,
        tag, and genre.
        - Applies the updates to the movie model in bulk.
        - Refreshes the media view to reflect the changes.
        """
        try:
            if self.parent.ui.tblMovies.selectionModel():
                updates   = {}
                movie_ids = set()
                for selected in self.parent.ui.tblMovies.selectedIndexes():
                    movie_ids.add(
                        selected.sibling(
                            selected.row(), 
                            getColIndexinTableView(self.parent.ui.tblMovies, MEDIA_COLUMNS.ID)
                        ).data()
                    )

                updates[MEDIA_COLUMNS.ID] = ','.join(movie_ids)

                if self.ui.chkSource.isChecked():
                    updates[MOVIE_COLUMNS.SOURCE_ID]   = self.ui.cbBulkSource.currentData()

                if self.ui.chkCodec.isChecked():
                    updates[MOVIE_COLUMNS.VIDEO_CODEC] = self.ui.txtBulkCodec.text()

                if self.ui.chkQuality.isChecked():
                    updates[MEDIA_COLUMNS.QUALITY_ID]  = self.ui.cbBulkQuality.currentData()

                if self.ui.chkEdition.isChecked():
                    updates[MOVIE_COLUMNS.EDITION_ID]  = self.ui.cbBulkEdition.currentData()

                if self.ui.chkWatched.isChecked():
                    updates[MEDIA_COLUMNS.WATCHED]     = 1 if self.ui.chkBulkWatched.isChecked() else 0

                if self.ui.chkToBurn.isChecked():
                    updates[MEDIA_COLUMNS.TO_BURN]     = 1 if self.ui.chkBulkToBurn.isChecked() else 0

                if self.ui.chkDiscNo.isChecked():
                    updates[MEDIA_COLUMNS.BACKUP_DISC] = self.ui.txtBulkDisc.text()

                if self.ui.chkTag.isChecked():
                    updates[MEDIA_COLUMNS.TAG]         = self.ui.txtBulkTag.text()

                if self.ui.chkGenre.isChecked():
                    updates[META_COLUMNS.GENRE]        = self.ui.cbBulkGenre.currentData()

            model.bulk_update_movies(updates)

            self.close()
            self.parent.writeStatus('Entries updated successfully...', MESSAGE_TYPE.INFO)
            self.parent.refreshMedia()
        except Exception as e:
            self.writeStatus(f'updateMedia: {e}', MESSAGE_TYPE.ERROR)


#=======================================================================
class ExportDialog(QDialog):
    """
    A dialog class for exporting media data using predefined templates. This class provides a user interface
    for selecting export templates, specifying a destination file, and executing the export process.

    Attributes:
        ui (Ui_ExportDialog): The user interface for the export dialog.
        parent (QWidget): The parent widget of the dialog.
        templates (DataFrame): A DataFrame containing available export templates.

    Methods:
        __init__(clsUi=None, parent=None):
            Initializes the ExportDialog with the given UI class and parent widget.
        
        writeStatus(message, message_type=MESSAGE_TYPE.INFO):
            Updates the status label with a given message and style.
        
        displayTemplates():
            Populates the template list with available export templates.
        
        exportMedia():
            Initiates the export process for the selected media type and template.
        
        selectFile():
            Opens a file dialog to select the destination file for export and updates the destination text field.
    """

    def __init__(self, clsUi=None, parent=None) -> None:
        """
        Initializes the ExportDialog class which sets up the user interface for exporting media.

        Parameters:
        clsUi (optional): The UI class to be used for the dialog. Default is None.
        parent (optional): The parent widget of this dialog. Default is None.
        """
        super().__init__(parent)
        self.ui = Ui_ExportDialog()
        self.ui.setupUi(self)
        self.parent = parent

        self.templates = metahelper.get_templates(APP_CONFIG.EXPORT_TEMPLATES)
        
        self.ui.btnSave.clicked.connect(self.exportMedia)
        self.ui.btnCancel.clicked.connect(self.close)
        self.ui.btnBrowse.clicked.connect(self.selectFile)
        self.displayTemplates()


    def writeStatus(self, message : str, message_type=MESSAGE_TYPE.INFO) -> None:
        """
        Updates the status label with a given message and style.
        
        Parameters:
            message (str): The status message to display.
            message_type (str, optional): The type of message (MESSAGE_TYPE.INFO or MESSAGE_TYPE.ERROR) to determine the style.
        """
        self.ui.lblStatus.setStyleSheet(getStatusStyleSheet(message_type))
        self.ui.lblStatus.setText(message)


    def displayTemplates(self) -> None:
        """
        Populates the template list with available export templates.
        """
        try:
            self.ui.lsTemplates.addItems(self.templates['Title'].tolist())
        except Exception as e:
            self.writeStatus(f'displayTemplates: {e}', MESSAGE_TYPE.ERROR)


    def exportMedia(self) -> None:
        """
        Initiates the export process for the selected media type and template.
        """
        import importlib

        try:
            self.writeStatus('Exporting data...')

            selected   = self.ui.lsTemplates.currentItem().text()
            media_type = MEDIA_TYPE.MOVIE if self.parent.ui.tbSummary.currentIndex() == 0 \
                    else MEDIA_TYPE.SERIES
            module     = self.templates.loc[self.templates['Title'] == selected, 'Module'].values[0]

            exporter   = importlib.import_module(module)
            response   = exporter.export(media_type, self.ui.txtDestination.text())

            if response:
                self.close()
                self.parent.writeStatus('Entries exported successfully...', MESSAGE_TYPE.INFO)
            else:
                self.writeStatus('Export failed!', MESSAGE_TYPE.ERROR)
        except Exception as e:
            self.writeStatus(f'exportMedia: {e}', MESSAGE_TYPE.ERROR)


    def selectFile(self) -> None:
        """
        Opens a file dialog to select the destination file for export and updates the destination text field.
        """
        try:
            filename, _ = QFileDialog.getSaveFileName(
                                self, 
                                "Save As", 
                                "export.csv", 
                                "Data Files (*.csv *.xlsx *.json)",
                                options=QFileDialog.Option.DontUseNativeDialog )
            
            self.ui.txtDestination.setText(filename)
        except Exception as e:
            self.writeStatus(f'selectFile: {e}', MESSAGE_TYPE.ERROR)


#=======================================================================
class FAQsDialog(QDialog):
    """
    A dialog class for displaying Frequently Asked Questions (FAQs) in a GUI application.

    Attributes:
    ui (Ui_FAQDialog): An instance of the Ui_FAQDialog class responsible for setting up the UI components of the dialog.
    """
    
    def __init__(self, clsUi=None, parent=None) -> None:
        """
        Initializes the FAQsDialog with optional UI class and parent widget.

        Parameters:
        clsUi (optional): A class responsible for the UI setup. Defaults to None.
        parent (QWidget, optional): The parent widget of this dialog. Defaults to None.
        """
        super().__init__(parent)
        self.ui = Ui_FAQDialog()
        self.ui.setupUi(self)


#=======================================================================
class Worker(QRunnable):
    """
    Worker class that inherits from QRunnable to handle running a function in a separate thread.

    Attributes:
        fn (callable): The function to be executed by the worker.
        originating_PID (int): The process ID of the process that created this worker.
        _running (bool): A flag indicating whether the worker is currently running.

    Methods:
        run(): Executes the function `fn` in a separate thread.
    """

    def __init__(self, fn) -> None:
        """
        Initializes the Worker with a function to execute.

        Parameters:
            fn (callable): The function to be executed by the worker.
        """
        super(Worker, self).__init__()
        self.fn = fn
        self.originating_PID = os.getpid()
        self._running = True


    @Slot()
    def run(self) -> None:
        """
        Executes the function `fn` in a separate thread.
        """
        self.fn()


#=======================================================================
class FetchDetailsDialog(QDialog):
    """
    A dialog class for fetching and displaying media details such as movies or series.
    
    Signals:
        progressChanged (int): Emitted to update the progress bar value.
        noMovieFound (str): Emitted when no movie is found during the search.
        saveFinished (bool): Emitted when the save operation is completed.

    Methods:
        __init__(clsUi=None, parent=None): Initializes the dialog.
        showMessage(message): Displays a warning message.
        writeStatus(message, message_type=MESSAGE_TYPE.INFO): Writes a status message with a specific style.
        setSearchText(): Sets the search text based on the selected media.
        resetForm(): Resets the form fields to their default values.
        fetchDetails(): Initiates the process to fetch media details.
        fetchMovieDetails(): Fetches movie details using a scraper module.
        getColumnValue(colname): Retrieves the value of a specified column from the selected row.
        showMediaDetails(): Initiates the process to show media details.
        showDetails(): Fetches and displays detailed information about the selected media.
        saveSelected(): Initiates the process to save the selected media details.
        saveComplete(isSuccessful): Handles the completion of the save operation.
        saveMedia(): Saves the media details to the database.
    """
    progressChanged = Signal(int)
    noMovieFound    = Signal(str)
    saveFinished    = Signal(bool)

    def __init__(self, clsUi=None, parent=None) -> None:
        """
        Initializes a new instance of the FetchDetailsDialog class.

        Parameters:
        clsUi (optional): The UI class to be used for the dialog. Default is None.
        parent (optional): The parent widget of this dialog. Default is None.
        """
        super().__init__(parent)
        self.ui = Ui_FetchDetailsDialog()
        self.ui.setupUi(self)

        self.parent         = parent
        self.templates      = metahelper.get_templates(APP_CONFIG.LOOKUP_TEMPLATES)
        self.media_id       = None
        self.threadpool     = QThreadPool()
        self.media_type     = MEDIA_TYPE.MOVIE if self.parent.ui.tbSummary.currentIndex() == 0 \
                         else MEDIA_TYPE.SERIES
        self.tblParent      = self.parent.ui.tblMovies if self.media_type == MEDIA_TYPE.MOVIE \
                         else self.parent.ui.tblSeries
        self.selected       = self.tblParent.selectedIndexes()
        self.selectedMedia  = None

        self.currentSelectedIndex = 0

        self.ui.btnFetch.clicked.connect(self.fetchDetails)
        self.ui.btnCancel.clicked.connect(self.close)
        self.ui.btnSave.clicked.connect(self.saveSelected)

        self.ui.lblPoster.setScaledContents(True)
        self.ui.lblPoster.setPixmap(QPixmap(DEFAULT_POSTER))
        
        self.ui.prgStatus.setValue(0)
        self.setSearchText()
        
        self.progressChanged.connect(self.ui.prgStatus.setValue)
        self.noMovieFound.connect(self.showMessage)
        self.saveFinished.connect(self.saveComplete)

        self.fetchDetails()

    
    def showMessage(self, message : str) -> None:
        '''
        Signal triggered class for printing progress messages
        '''
        self.writeStatus(message, MESSAGE_TYPE.WARNING)


    def writeStatus(self, message : str, message_type=MESSAGE_TYPE.INFO) -> None:
        """
        Updates the status label with a message and style based on the message type.

        Parameters:
            message (str): The status message to display.
            message_type (str): The type of message ('INFO', 'WARNING', 'ERROR'). Defaults to 'INFO'.
        """
        self.ui.lblStatus.setStyleSheet(getStatusStyleSheet(message_type))
        self.ui.lblStatus.setText(message)


    def setSearchText(self) -> None:
        """
        Updates the search text field in the user interface with the title of the currently selected media item.

        Parameters:
        - self: The instance of the class containing this method. It is expected to have the following attributes:
        - selected: A list or collection containing media items.
        - currentSelectedIndex: An integer representing the index of the currently selected media item.
        - tblParent: The table view widget containing the media items.
        - ui: An object with a txtSearchTitle attribute, which is a text field in the user interface.
        """
        try:
            media         = self.selected[self.currentSelectedIndex]
            self.media_id = media.sibling(media.row(), 
                                          getColIndexinTableView(self.tblParent, MEDIA_COLUMNS.ID)).data()
            media_title   = media.sibling(media.row(), 
                                          getColIndexinTableView(self.tblParent, MEDIA_COLUMNS.TITLE)).data()
            self.ui.txtSearchTitle.setText(media_title)
        except Exception as e:
            self.writeStatus(f'setSearchText: {e}', MESSAGE_TYPE.ERROR)


    def resetForm(self) -> None:
        """
        Resets the form fields and UI elements to their default state.

        This method clears all input fields, resets the status label and progress bar,
        and sets the search results table to an empty model with predefined columns.

        Parameters:
        - self: The instance of the class containing the UI elements to be reset.
        """
        try:
            self.ui.lblPoster.setPixmap(QPixmap(DEFAULT_POSTER))
            self.ui.txtResTitle.setPlainText('')
            self.ui.txtResYear.setText('')
            self.ui.txtResPlot.setPlainText('')
            self.ui.txtSearchTitle.setText('')
            self.ui.lblStatus.setText('')
            self.ui.prgStatus.setValue(0)
            self.ui.txtResGenres.setText('')
            self.ui.txtResDirector.setText('')
            
            self.ui.tblSearchResults.setModel(
                TableModel(pd.DataFrame({
                            MEDIA_COLUMNS.TITLE : [], 
                            MEDIA_COLUMNS.YEAR  : []
                           })
                )
            )
        except Exception as e:
            self.writeStatus(f'resetForm: {e}', MESSAGE_TYPE.ERROR)


    def fetchDetails(self) -> None:
        """
        Initiates the process of fetching movie details by creating a worker thread.

        This method sets up a worker thread to execute the `fetchMovieDetails` function asynchronously.
        It utilizes a thread pool to manage the worker thread.

        Parameters:
        - self: The instance of the class containing this method.
        """
        self.worker = Worker(self.fetchMovieDetails)
        self.threadpool.start(self.worker)


    def fetchMovieDetails(self) -> None:
        """
        Fetches movie details based on the current search source and search title input by the user.
        
        This function updates the UI to reflect the search progress and results. It dynamically imports
        a module specified in the templates, uses it to search for media data, and displays the results
        in a table. If no results are found, it notifies the user.

        Parameters:
        - self: The instance of the class containing this method. It is expected to have the following attributes:
        - ui: An object with attributes `cbSearchSource`, `txtSearchTitle`, `tblSearchResults`, and `lblStatus` 
            for interacting with the UI components.
        - templates: A DataFrame containing a 'Source' column to match with the current search source and a 
            'Module' column specifying the module to import for scraping.
        - writeStatus: A method to update the status message in the UI.
        - progressChanged: A signal to emit progress updates.
        """
        import importlib
        from PySide6.QtWidgets import QHeaderView

        try:
            self.writeStatus('Searching...')
            self.progressChanged.emit(0)

            module  = self.templates.loc[self.templates['Source'] == self.ui.cbSearchSource.currentText(), 'Module'].values[0]
            scraper = importlib.import_module(module)

            self.progressChanged.emit(25)

            data    = scraper.search_media(self.ui.txtSearchTitle.text())

            self.progressChanged.emit(50)

            if len(data) > 0:
                tableModel = TableModel(data)
                self.ui.tblSearchResults.setModel(tableModel)
                self.ui.tblSearchResults.verticalHeader().hide()
                self.ui.tblSearchResults.setColumnWidth(1, 75)
                self.ui.tblSearchResults.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)

                for col in range(2, len(data.columns)):
                    self.ui.tblSearchResults.setColumnHidden(col, True)

                self.progressChanged.emit(75)
                self.writeStatus('')

                self.ui.tblSearchResults.selectionModel().selectionChanged.connect(self.showMediaDetails)
                self.ui.tblSearchResults.selectRow(0)
            else:
                self.writeStatus('No Movie found. Try searching with a different title value...', MESSAGE_TYPE.WARNING)

            self.ui.lblStatus.setText('')
            self.progressChanged.emit(100)
        except Exception as e:
            self.writeStatus(f'fetchMovieDetails: {e}', MESSAGE_TYPE.ERROR)
            self.progressChanged.emit(100)


    def getColumnValue(self, colname : str) -> None:
        """
        Retrieves the value of a specified column from the currently selected row in a table view.

        Parameters:
        colname (str): The name of the column whose value is to be retrieved.

        Returns:
        QVariant: The data value of the specified column in the currently selected row.
        """
        index   = self.ui.tblSearchResults.selectionModel().currentIndex()
        return index.sibling(index.row(), getColIndexinTableView(self.ui.tblSearchResults, colname)).data()
    

    def showMediaDetails(self) -> None:
        """
        Initiates the process to display media details by creating a worker thread.

        This method sets up a worker thread to execute the `showDetails` function asynchronously.
        It utilizes a thread pool to manage the worker thread, allowing the application to remain
        responsive while processing media details.
        """
        self.worker = Worker(self.showDetails)
        self.threadpool.start(self.worker)


    def showDetails(self) -> None:
        """
        Fetches and displays detailed information about a selected media item.

        This method retrieves media details from a specified source module and updates the UI with the fetched information.
        It emits progress updates at various stages of the process.

        The method performs the following steps:
        1. Retrieves the module name from the templates based on the selected source and imports it.
        2. Calls the `get_media_details` function from the imported module to fetch media details using the online ID.
        3. Updates various UI elements with the fetched media details, including title, year, plot, genres, and director.
        4. Loads the media poster image from a URL and updates the UI with the image.
        """
        import importlib

        try:
            self.writeStatus('Fetching details...')
            self.progressChanged.emit(0)

            module  = self.templates.loc[self.templates['Source'] == self.ui.cbSearchSource.currentText(), 'Module'].values[0]
            scraper = importlib.import_module(module)

            self.selectedMedia = scraper.get_media_details(self.getColumnValue(MEDIA_COLUMNS.ONLINE_ID))

            self.progressChanged.emit(75)

            self.ui.txtResTitle.setPlainText(self.selectedMedia[MEDIA_DETAILS.CONTENT][MEDIA_COLUMNS.ORIGINAL_TITLE])
            self.ui.txtResYear.setText(str(self.selectedMedia[MEDIA_DETAILS.CONTENT][MEDIA_COLUMNS.YEAR]).replace('.0', ''))
            self.ui.txtResPlot.setPlainText(self.selectedMedia[MEDIA_DETAILS.CONTENT][MEDIA_COLUMNS.PLOT])
            self.ui.txtResGenres.setText(', '.join(self.selectedMedia[MEDIA_DETAILS.GENRES]))
            self.ui.txtResDirector.setText(self.selectedMedia[MEDIA_DETAILS.CONTENT][MEDIA_COLUMNS.DIRECTOR])

            poster = self.selectedMedia[MEDIA_DETAILS.CONTENT][MEDIA_COLUMNS.POSTER_URL]
            if poster == None:
                poster_image = QPixmap(DEFAULT_POSTER)
            else:
                p_image = QImage()
                p_image.loadFromData(requests.get(poster).content)
                poster_image = QPixmap().fromImage(p_image)
            
            self.ui.lblPoster.setScaledContents(True)
            self.ui.lblPoster.setPixmap(poster_image)

            self.writeStatus('')
            self.progressChanged.emit(100)
        except Exception as e:
            self.writeStatus(f'showDetails: {e}', MESSAGE_TYPE.ERROR)
            self.progressChanged.emit(100)


    def saveSelected(self) -> None:
        """
        Initiates the saving process for selected media by creating a Worker 
        instance and starting it in a thread pool.
        """
        self.worker = Worker(self.saveMedia)
        self.threadpool.start(self.worker)


    def saveComplete(self, isSuccessful : bool) -> None:
        """
        Handles the completion of a save operation and updates the UI accordingly.

        Parameters:
        isSuccessful (bool): A flag indicating whether the save operation was successful.
        """
        try:
            current_row = self.selected[self.currentSelectedIndex].row()
            max_row     = self.selected[len(self.selected) - 1].row()

            if current_row == max_row:
                self.parent.refreshMedia()
                self.parent.writeStatus('Details fetched successfully...', MESSAGE_TYPE.INFO)
                self.close()
            else:
                while current_row == self.selected[self.currentSelectedIndex].row() \
                    and self.currentSelectedIndex < len(self.selected) - 1:
                    self.currentSelectedIndex += 1
                    current_row = self.selected[self.currentSelectedIndex].row()

                self.resetForm()
                self.setSearchText()
        except Exception as e:
            self.writeStatus(f'saveComplete: {e}', MESSAGE_TYPE.ERROR)


    def saveMedia(self) -> None:
        """
        Saves media information to the database and updates the progress status.

        This function handles the saving of media data, including movies and series, 
        by updating the database with the relevant details. It emits progress updates 
        at various stages of the process.

        Process:
        1. Imports the module specified in the templates for scraping.
        2. Retrieves the online ID for the media.
        3. Updates the selected media's ID.
        4. Depending on the media type (movie or series), updates the database with the media details.
        5. For series, retrieves and updates episode information.
        6. Updates the media actors in the database.
        """
        import importlib

        try:
            self.writeStatus('Saving...')
            self.progressChanged.emit(0)

            module     = self.templates.loc[self.templates['Source'] == self.ui.cbSearchSource.currentText(), 
                                            'Module'].values[0]
            scraper    = importlib.import_module(module)
            online_id  = self.getColumnValue(MEDIA_COLUMNS.ONLINE_ID)            

            self.progressChanged.emit(25)

            self.selectedMedia[MEDIA_DETAILS.CONTENT][MEDIA_COLUMNS.ID] = self.media_id
            self.selectedMedia[MEDIA_DETAILS.OTHERS][MEDIA_COLUMNS.ID]  = self.media_id

            self.progressChanged.emit(75)

            if self.media_type == MEDIA_TYPE.MOVIE:
                model.update_movie(
                    self.selectedMedia[MEDIA_DETAILS.CONTENT], 
                    self.selectedMedia[MEDIA_DETAILS.OTHERS], 
                    self.selectedMedia[MEDIA_DETAILS.GENRES], 
                    self.selectedMedia[MEDIA_DETAILS.LANGUAGES] )
            else:
                self.writeStatus('Updating Episodes...')
                model.update_series(
                    self.selectedMedia[MEDIA_DETAILS.CONTENT], 
                    self.selectedMedia[MEDIA_DETAILS.OTHERS], 
                    None, 
                    self.selectedMedia[MEDIA_DETAILS.GENRES], 
                    self.selectedMedia[MEDIA_DETAILS.LANGUAGES] )
                
                if self.selectedMedia[MEDIA_DETAILS.CONTENT][SERIES_COLUMNS.SEASONS] > 0:
                    episodes = []
                    for season in range(1, self.selectedMedia[MEDIA_DETAILS.CONTENT][SERIES_COLUMNS.SEASONS] + 1):
                        episodes.append(scraper.get_season_episodes(online_id, season))

                    episodes = pd.concat(episodes, ignore_index=True)
                    episodes[EPISODE_COLUMNS.EPISODE] = episodes[EPISODE_COLUMNS.EPISODE].astype('int64')

                    existing_episodes = model.get_series_episodes(self.media_id)
                    existing_episodes = existing_episodes[[EPISODE_COLUMNS.ID, 
                                                        EPISODE_COLUMNS.SEASON, 
                                                        EPISODE_COLUMNS.EPISODE]]

                    df = episodes.merge( 
                            existing_episodes, 
                            how='left', 
                            on=[EPISODE_COLUMNS.SEASON, EPISODE_COLUMNS.EPISODE] )

                    for _, row in df.iterrows():
                        if str(row[MEDIA_COLUMNS.ID]) == 'nan':
                            model.add_new_episode(
                                row[EPISODE_COLUMNS.SEASON],
                                row[EPISODE_COLUMNS.EPISODE],
                                row[MEDIA_COLUMNS.ORIGINAL_TITLE],
                                row[MEDIA_COLUMNS.PLOT],
                                row[MEDIA_COLUMNS.RELEASE_DATE],
                                self.media_id )
                        else:
                            episode_details = {}
                            episode_details[MEDIA_COLUMNS.TITLE]        = row[MEDIA_COLUMNS.ORIGINAL_TITLE]
                            episode_details[MEDIA_COLUMNS.PLOT]         = row[MEDIA_COLUMNS.PLOT]
                            episode_details[MEDIA_COLUMNS.ID]           = row[MEDIA_COLUMNS.ID]
                            episode_details[MEDIA_COLUMNS.RELEASE_DATE] = row[MEDIA_COLUMNS.RELEASE_DATE] 
                            model.update_episode(episode_details)

            model.update_media_actors(
                self.media_type, 
                self.media_id, 
                self.selectedMedia[MEDIA_DETAILS.CAST], 
                self.ui.cbSearchSource.currentText(), 
                None )
            
            poster = self.selectedMedia[MEDIA_DETAILS.CONTENT][MEDIA_COLUMNS.POSTER_URL]
            if poster:
                poster_path = DEFAULT_POSTER_PATH.format(self.media_type.lower()) + str(self.media_id) + '.jpg'
                with open(poster_path, 'wb') as f:
                    f.write(requests.get(poster).content)

            self.progressChanged.emit(100)
            self.saveFinished.emit(True)
        except Exception as e:
            self.writeStatus(f'saveMedia: {e}', MESSAGE_TYPE.ERROR)


#=======================================================================
class ImportDialog(QDialog):
    """
    A dialog class for importing media data from files into the application. It provides a user interface
    for selecting files, mapping columns, and importing data.

    Attributes:
        ui (Ui_ImportDialog): The user interface for the import dialog.
        parent (QWidget): The parent widget of the dialog.
        templates (DataFrame): Templates for import configurations.
        data (DataFrame): The data to be imported.

    Methods:
        __init__(clsUi=None, parent=None):
            Initializes the ImportDialog with optional UI class and parent widget.
        
        loadImportedFile():
            Loads and processes the selected file, mapping its columns to database columns.
        
        selectFile():
            Opens a file dialog to select a file for import and loads the file.
        
        writeStatus(message, message_type=MESSAGE_TYPE.INFO):
            Updates the status label with a message and style based on the message type.
        
        importMedia():
            Imports the media data using the mapped columns and selected file.
    """

    def __init__(self, clsUi=None, parent=None) -> None:
        """
        Initializes the ImportDialog.

        Parameters:
            clsUi (Ui_ImportDialog, optional): The UI class for the dialog. Defaults to None.
            parent (QWidget, optional): The parent widget of the dialog. Defaults to None.
        """
        super().__init__(parent)
        self.ui     = Ui_ImportDialog()
        self.ui.setupUi(self)

        self.parent    = parent
        self.templates = metahelper.get_templates(APP_CONFIG.IMPORT_TEMPLATES)
        self.data      = None
        
        self.ui.btnAccept.clicked.connect(self.importMedia)
        self.ui.btnCancel.clicked.connect(self.close)
        self.ui.btnBrowse.clicked.connect(self.selectFile)
        self.ui.cbMediaType.currentIndexChanged.connect(self.loadImportedFile)


    def loadImportedFile(self) -> None:
        """
        Loads the selected file and maps its columns to the database columns.
        Supports CSV, XLSX, and JSON file formats.
        """
        try:
            if self.ui.txtSource.text() != '':
                import pandas as pd

                db_columns  = [name for name in dir(MEDIA_COLUMNS) if not name.startswith('__')]
                if self.ui.cbMediaType.currentText() == 'Movies':
                    db_columns += [name for name in dir(MOVIE_COLUMNS) if not name.startswith('__')]
                else:
                    db_columns += [name for name in dir(SERIES_COLUMNS) if not name.startswith('__')]
                    db_columns += [name if name == EPISODE_COLUMNS.EPISODE else 'EPISODE_' + name \
                                    for name in dir(EPISODE_COLUMNS) if not name.startswith('__')]

                db_columns += [MEDIA_DETAILS.GENRES, MEDIA_DETAILS.LANGUAGES]
                db_columns.sort()

                extension = self.ui.txtSource.text().rsplit('.', 1)[-1]
                if extension == 'csv':
                    data = pd.read_csv(self.ui.txtSource.text())
                elif extension == 'xlsx':
                    data = pd.read_excel(self.ui.txtSource.text())
                else:
                    data = pd.read_json(self.ui.txtSource.text(), orient='table')

                self.ui.tblImport.setRowCount(len(data.columns))
                self.ui.tblImport.setColumnCount(2)
                self.ui.tblImport.setHorizontalHeaderLabels(['Imported Column', 'Maps To'])
                self.ui.tblImport.verticalHeader().hide()
                self.ui.tblImport.setColumnWidth(0, self.ui.tblImport.width() // 2)

                import_cols = data.columns.to_list()

                for row in range(len(import_cols)):
                    for col in range(2):
                        item = QTableWidgetItem(import_cols[row] if col == 0 else '')
                        self.ui.tblImport.setItem(row, col, item)

                        if col == 1:
                            combo_delegate = QComboBox()
                            combo_delegate.addItems([''] + db_columns)
                            combo_delegate.setCurrentText(import_cols[row].upper())

                            self.ui.tblImport.setCellWidget(row, col, combo_delegate)
            else:
                self.writeStatus('Select a file to import', MESSAGE_TYPE.WARNING)
        except Exception as e:
            self.writeStatus(f'loadImportedFile: {e}', MESSAGE_TYPE.ERROR)


    def selectFile(self) -> None:
        """
        Opens a file dialog to select a file for import and loads the file.
        """
        try:
            filename, path = QFileDialog.getOpenFileName(
                                self, 
                                "Select File to Import", 
                                "", 
                                "Data Files (*.csv *.xlsx *.json)", 
                                options=QFileDialog.Option.DontUseNativeDialog )
            
            self.ui.txtSource.setText(filename)
            self.loadImportedFile()
        except Exception as e:
            self.writeStatus(f'selectFile: {e}', MESSAGE_TYPE.ERROR)


    def writeStatus(self, message : str, message_type=MESSAGE_TYPE.INFO) -> None:
        """
        Updates the status label with a message and style based on the message type.

        Parameters:
            message (str): The status message to display.
            message_type (str): The type of message ('INFO', 'WARNING', 'ERROR'). Defaults to 'INFO'.
        """
        self.ui.lblStatus.setStyleSheet(getStatusStyleSheet(message_type))
        self.ui.lblStatus.setText(message)


    def importMedia(self) -> None:
        """
        Imports the media data using the mapped columns and selected file.
        Displays a success message if the import is successful, otherwise shows an error or warning.
        """
        import importlib

        try:
            column_map = {}
            has_title  = False

            self.writeStatus('Importing data...')

            for row in range(self.ui.tblImport.rowCount()):
                value = self.ui.tblImport.indexWidget(self.ui.tblImport.model().index(row,1)).currentText()
                if value != '':
                    column_map[value] = self.ui.tblImport.item(row, 0).text()
                    has_title         = (value == MEDIA_COLUMNS.TITLE) if not has_title else has_title

            if has_title:
                module     = self.templates.loc[self.templates['Type'] == self.ui.txtSource.text().rsplit('.', 1)[-1], 
                                                'Module'].values[0]
                importer   = importlib.import_module(module)

                media_type = MEDIA_TYPE.MOVIE if self.ui.cbMediaType.currentText() == 'Movies' else MEDIA_TYPE.SERIES
                response   = importer.import_media(media_type, self.ui.txtSource.text(), column_map)
                
                if response:
                    self.parent.writeStatus('Imported entries successfully...', MESSAGE_TYPE.INFO)
                    self.parent.refreshMedia()
                    self.close()
                else:
                    self.writeStatus('Import Failed!', MESSAGE_TYPE.ERROR)
            else:
                self.writeStatus('Imported data does not have Title column.', MESSAGE_TYPE.WARNING)
        except Exception as e:
            self.writeStatus(f'importMedia: {e}', MESSAGE_TYPE.ERROR)


#=======================================================================
class PreferencesDialog(QDialog):
    """
    A dialog class for managing user preferences in the application. This class provides
    methods to set up and display various preference lists and configurations.

    Attributes:
        ui (Ui_PreferencesDialog): The user interface for the preferences dialog.

    Methods:
        __init__(clsUi=None, parent=None):
            Initializes the PreferencesDialog with optional UI class and parent widget.

        setGenreListView():
            Populates the genre list view with available genres from the metadata helper.

        setSourceListView():
            Populates the source list view with available media sources from the metadata helper.

        setEditionListView():
            Populates the edition list view with available media editions from the metadata helper.

        setQualityListView():
            Populates the quality list view with available media qualities from the metadata helper.

        setAppConfig():
            Sets the application configuration fields with data from the metadata helper.
    """

    def __init__(self, clsUi=None, parent=None) -> None:
        """
        Initializes an instance of the class, setting up the user interface and configuring various list views.

        Parameters:
        clsUi (optional): The UI class to be used for setting up the interface. Default is None.
        parent (optional): The parent widget for this dialog. Default is None.
        """
        super().__init__(parent)
        self.ui = Ui_PreferencesDialog()
        self.ui.setupUi(self)

        self.ui.btnSave.clicked.connect(self.saveAppConfig)
        self.ui.btnCancel.clicked.connect(self.close)

        self.setGenreListView()
        self.setSourceListView()
        self.setEditionListView()
        self.setQualityListView()
        self.setAppConfig()


    def writeStatus(self, message : str, message_type=MESSAGE_TYPE.INFO) -> None:
        """
        Updates the status label with a given message and style.
        
        Parameters:
            message (str): The status message to display.
            message_type (str, optional): The type of message (MESSAGE_TYPE.INFO or MESSAGE_TYPE.ERROR) to determine the style.
        """
        self.ui.lblStatus.setStyleSheet(getStatusStyleSheet(message_type))
        self.ui.lblStatus.setText(message)


    def setGenreListView(self) -> None:
        """
        Populates the genre list view with available genres from the metadata helper.
        """
        try:
            self.ui.lsPrfGenres.clear()
            df = metahelper.get_genres()
            for _, row in df.iterrows():
                self.ui.lsPrfGenres.addItem(row[META_COLUMNS.GENRE])
        except Exception as e:
            self.writeStatus(f'setGenreListView: {e}', MESSAGE_TYPE.ERROR)


    def setSourceListView(self) -> None:
        """
        Populates the source list view with available media sources from the metadata helper.
        """
        try:
            self.ui.lsPrfSources.clear()
            df = metahelper.get_media_sources()
            for _, row in df.iterrows():
                self.ui.lsPrfSources.addItem(row[META_COLUMNS.SOURCE])
        except Exception as e:
            self.writeStatus(f'setSourceListView: {e}', MESSAGE_TYPE.ERROR)


    def setEditionListView(self) -> None:
        """
        Populates the edition list view with available media editions from the metadata helper.
        """
        try:
            self.ui.lsPrfEditions.clear()
            df = metahelper.get_media_editions()
            for _, row in df.iterrows():
                self.ui.lsPrfEditions.addItem(row[META_COLUMNS.EDITION])
        except Exception as e:
            self.writeStatus(f'Error: {e}', MESSAGE_TYPE.ERROR)
            

    def setQualityListView(self) -> None:
        """
        Populates the quality list view with available media qualities from the metadata helper.
        """
        try:
            self.ui.lsPrfQualities.clear()

            df = metahelper.get_media_qualities()
            for _, row in df.iterrows():
                self.ui.lsPrfQualities.addItem(row[META_COLUMNS.QUALITY])
        except Exception as e:
            self.writeStatus(f'setEditionListView: {e}', MESSAGE_TYPE.ERROR)

    
    def setAppConfig(self) -> None:
        """
        Sets the application configuration fields with data from the metadata helper.
        """
        try:
            df = metahelper.get_app_config()
            self.ui.txtPrfLookup.setText(df[APP_CONFIG.LOOKUP_TEMPLATES][0])
            self.ui.cbDefaultLookup.setCurrentText(df[APP_CONFIG.DEFAULT_LOOKUP][0])

            self.ui.txtPrfPublish.setText(df[APP_CONFIG.PUBLISH_TEMPLATES][0])
            self.ui.cbDefaultPublish.setCurrentText(df[APP_CONFIG.DEFAULT_PUBLISH][0])

            self.ui.txtPrfImport.setText(df[APP_CONFIG.IMPORT_TEMPLATES][0])
            self.ui.txtPrfExport.setText(df[APP_CONFIG.EXPORT_TEMPLATES][0])
        except Exception as e:
            self.writeStatus(f'setAppConfig: {e}', MESSAGE_TYPE.ERROR)


    def saveAppConfig(self) -> None:
        """
        Save Application configuration to the database
        """
        try:
            metahelper.update_app_config(
                export_template  = self.ui.txtPrfExport.text(),
                import_template  = self.ui.txtPrfImport.text(),
                lookup_template  = self.ui.txtPrfLookup.text(),
                publish_template = self.ui.txtPrfPublish.text(),
                default_lookup   = self.ui.cbDefaultLookup.currentText(),
                default_publish  = self.ui.cbDefaultPublish.currentText()
            )

            genres = [self.ui.lsPrfGenres.item(row).text() for row in range(self.ui.lsPrfGenres.count())]
            metahelper.update_meta(META_COLUMNS.GENRE, genres)

            editions = [self.ui.lsPrfEditions.item(row).text() for row in range(self.ui.lsPrfEditions.count())]
            metahelper.update_meta(META_COLUMNS.EDITION, editions)

            qualities = [self.ui.lsPrfQualities.item(row).text() for row in range(self.ui.lsPrfQualities.count())]
            metahelper.update_meta(META_COLUMNS.QUALITY, qualities)

            sources = [self.ui.lsPrfSources.item(row).text() for row in range(self.ui.lsPrfSources.count())]
            metahelper.update_meta(META_COLUMNS.GENRE, sources)

            self.parent.ui.writeStatus('Preferences updated successfully...')
            self.close()
        except Exception as e:
            self.writeStatus(f'saveAppConfig: {e}', MESSAGE_TYPE.ERROR)


#=======================================================================
class PublishDialog(QDialog):
    """
    A dialog class for publishing media content. It provides a user interface for selecting templates
    and publishing media content using those templates. The class handles the UI setup, template display,
    and the publishing process, including progress updates and error handling.

    Signals:
        progressChanged (int): Emitted to update the progress bar with the current progress percentage.
        saveFinished (bool): Emitted when the publishing process is finished, indicating success or failure.

    Methods:
        __init__(clsUi=None, parent=None):
            Initializes the PublishDialog with the given UI class and parent widget.
        
        writeStatus(message, message_type=MESSAGE_TYPE.INFO):
            Updates the status label with the given message and style.
        
        displayTemplates():
            Displays the available publishing templates in the UI list widget.
        
        publishContent():
            Initiates the publishing process by starting a worker thread.
        
        publishMedia():
            Handles the media publishing process, including content generation and publishing.
            Emits progress updates and handles exceptions.
        
        publishComplete(isSuccessful):
            Handles the completion of the publishing process, displaying a success or error message.
    """

    progressChanged  = Signal(int)
    saveFinished     = Signal(bool)

    def __init__(self, clsUi=None, parent=None) -> None:
        """
        Initializes the PublishDialog class.

        Parameters:
        clsUi (optional): The UI class to be used for the dialog. Default is None.
        parent (optional): The parent widget for this dialog. Default is None.
        """
        super().__init__(parent)
        self.ui = Ui_PublishDialog()
        self.ui.setupUi(self)

        self.parent     = parent
        self.templates  = metahelper.get_templates(APP_CONFIG.PUBLISH_TEMPLATES)
        self.threadpool = QThreadPool()

        self.ui.btnCancel.clicked.connect(self.close)
        self.ui.btnPublish.clicked.connect(self.publishContent)

        self.progressChanged.connect(self.ui.prgProgress.setValue)
        self.saveFinished.connect(self.publishComplete)

        self.displayTemplates()

    
    def writeStatus(self, message, message_type=MESSAGE_TYPE.INFO) -> None:
        """
        Updates the status label with a message and style based on the message type.

        Parameters:
            message (str): The status message to display.
            message_type (str): The type of message ('INFO', 'WARNING', 'ERROR'). Defaults to 'INFO'.
        """
        self.ui.lblStatus.setStyleSheet(getStatusStyleSheet(message_type))
        self.ui.lblStatus.setText(message)


    def displayTemplates(self) -> None:
        """
        Displays a list of publishing templates and resets the UI status elements.

        This method populates the list widget `lsPublishTemplate` with publishing templates
        from the 'Publisher' key of the `self.templates` dictionary. Additionally, it resets 
        the status label text and progress bar value to provide a fresh state before displaying templates.
        """
        try:
            self.ui.lsPublishTemplate.addItems(self.templates['Publisher'].tolist())
            self.ui.lblStatus.setText('')
            self.ui.prgProgress.setValue(0)
        except Exception as e:
            self.writeStatus(f'displayTemplates: {e}', MESSAGE_TYPE.ERROR)


    def publishContent(self) -> None:
        """
        Initiates the publishing of media content in a separate thread.

        This method creates a worker task to execute the `publishMedia` function
        in a background thread using the thread pool. It allows long-running
        operations to occur asynchronously, preventing the blocking of the main UI
        thread during the publishing process.
        """
        self.worker = Worker(self.publishMedia)
        self.threadpool.start(self.worker)


    def publishMedia(self) -> None:
        """
        Publishes media content by generating and extracting data for movies and series, 
        and then publishing the content using a specified template module.

        Description:
        - Writes a status message indicating the start of content generation.
        - Emits a progress signal with an initial value of 0.
        - Dynamically imports a module specified in the templates based on the selected publisher template.
        - Extracts and generates content for movies and series, updating the progress at each step.
        - Publishes the generated content and updates the progress to 100%.
        - Emits a signal indicating successful completion if no exceptions occur.
        - Catches any exceptions, logs an error message, and emits a signal indicating failure.
        """
        try:
            self.writeStatus('Generating content for publish')
            self.progressChanged.emit(0)

            import importlib
            module     = self.templates.loc[self.templates['Publisher'] == self.ui.lsPublishTemplate.currentItem().text(), 
                                            'Module'].values[0]
            publisher  = importlib.import_module(module)

            self.writeStatus('Extracting movie data...')
            publisher.generateContent(MEDIA_TYPE.MOVIE)
            self.progressChanged.emit(25)

            self.writeStatus('Extracting series data...')
            publisher.generateContent(MEDIA_TYPE.SERIES)
            self.progressChanged.emit(50)

            self.writeStatus('Publishing content...')
            publisher.publishContent()
            self.progressChanged.emit(100)
            
            self.saveFinished.emit(True)
        except Exception as e:
            self.progressChanged.emit(100)
            self.writeStatus('publishMedia: {}'.format(e), MESSAGE_TYPE.ERROR)
            self.saveFinished.emit(False)


    def publishComplete(self, isSuccessful : bool) -> None:
        """
        Handles the completion of a media publishing process by displaying a message box
        and closing the window if successful, or writing an error status if not.

        Parameters:
        isSuccessful (bool): A boolean indicating whether the publishing was successful.
        """
        if isSuccessful:
            self.parent.writeStatus('Published successfully...')
            self.close()


#=======================================================================
class AddNewEpiodeDialog(QDialog):
    """
    A dialog class for adding a new episode to a series. This class provides a user interface
    for entering episode details such as season number, episode number, and title, and handles
    the logic for validating and saving the new episode.

    Attributes:
        ui (Ui_AddNewEpisode): The user interface object for the dialog.
        parent (QWidget): The parent widget of the dialog.

    Methods:
        __init__(clsUi=None, parent=None):
            Initializes the dialog with the given UI class and parent widget.

        addNewEpisode():
            Validates the input fields and adds a new episode to the series if valid.
    """

    def __init__(self, clsUi=None, parent=None) -> None:
        """
        Initializes the AddNewEpisodeDialog class, which sets up the user interface for adding a new episode.

        Parameters:
        clsUi (optional): The UI class to be used for setting up the dialog. Defaults to None.
        parent (optional): The parent widget of this dialog. Defaults to None.

        This constructor performs the following actions:
        - Calls the superclass initializer with the parent parameter.
        - Initializes the UI using the Ui_AddNewEpisode class.
        - Sets up the UI components.
        - Connects the 'Cancel' button to the close method to close the dialog.
        - Connects the 'Save' button to the addNewEpisode method to handle saving a new episode.
        """
        super().__init__(parent)
        self.ui     = Ui_AddNewEpisode()
        self.ui.setupUi(self)
        self.parent = parent

        self.ui.btnCancel.clicked.connect(self.close)
        self.ui.btnSave.clicked.connect(self.addNewEpisode)


    def writeStatus(self, message : str, message_type=MESSAGE_TYPE.INFO) -> None:
        """
        Updates the status label with a given message and style.
        
        Parameters:
            message (str): The status message to display.
            message_type (str, optional): The type of message (MESSAGE_TYPE.INFO or MESSAGE_TYPE.ERROR) to determine the style.
        """
        self.ui.lblStatus.setStyleSheet(getStatusStyleSheet(message_type))
        self.ui.lblStatus.setText(message)

    
    def addNewEpisode(self) -> None:
        """
        Adds a new episode to the series.

        This method retrieves the season number, episode number, and title from the UI input fields.
        It validates the inputs to ensure they are not empty and that the season and episode numbers are numeric.
        If the inputs are valid, it attempts to add the new episode to the series model and updates the UI.
        If any error occurs during this process, it displays an error message in the status label.

        Parameters:
        - self: The instance of the class containing this method.
        """
        try:
            season  = self.ui.txtEpisodeSeason.text().strip()
            episode = self.ui.txtEpisodeNo.text().strip()
            title   = self.ui.txtEpisodeTitle.text().strip()

            if season == '' or episode == '' or title == '':
                self.writeStatus('All fields are mandatory', MESSAGE_TYPE.WARNING)
            elif not isNumeric(season) or not isNumeric(episode):
                self.writeStatus('Season & Episode are numeric fields...', MESSAGE_TYPE.WARNING)
            else:
                index     = self.parent.ui.tblSeries.selectionModel().currentIndex()
                series_id = index.sibling(index.row(), 
                                        getColIndexinTableView(self.parent.ui.tblSeries, MEDIA_COLUMNS.ID)).data()
                
                model.add_new_episode(int(season), int(episode), title, None, None, series_id)

                self.parent.writeStatus('Episode added successfully...')
                self.parent.displaySeriesDetails()
                self.close()
        except Exception as e:
            self.writeStatus(f'addNewEpisode: {e}', MESSAGE_TYPE.ERROR)


#=======================================================================
class ImagePopup(QDialog):
    """
    A class to create a frameless modal dialog for displaying an image in a popup window.

    Attributes:
    -----------
    image_label : QLabel
        A label widget to display the image.

    Methods:
    --------
    __init__(image_path: str, parent: QWidget = None):
        Initializes the ImagePopup dialog with the specified image and parent widget.
    """
    
    def __init__(self, image_path : str, parent=None) -> None:
        """
        Initializes a frameless modal dialog to display an image with a close button.

        Parameters:
        image_path (str): The file path to the image that will be displayed in the dialog.
        parent (QWidget, optional): The parent widget of the dialog. Defaults to None.

        This constructor sets up a dialog with the following features:
        - Frameless window with application modality, ensuring it stays on top of the parent application.
        - Semi-transparent gray background.
        - Geometry calculated to cover only the central widget of the parent.
        - A close button styled with a transparent background and white color, which turns red on hover.
        - An image label that displays the image from the provided path, scaled to fit within 80% of the available screen space while maintaining the aspect ratio.
        """
        super().__init__(parent)

        # Frameless modal dialog
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        # Set background to semi-transparent gray
        self.setStyleSheet("background-color: rgba(0, 0, 0, 150);")

        # Calculate the geometry to cover only the central widget
        central_widget = parent.centralWidget()
        geometry = QRect(parent.mapToGlobal(central_widget.geometry().topLeft()), central_widget.size())
        self.setGeometry(geometry)

        # Create a layout for the dialog
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # Create a close button
        close_button = QPushButton("✖")
        close_button.setFixedSize(30, 30)
        close_button.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                color: white;
                font-size: 18px;
                border: none;
            }
            QPushButton:hover {
                color: red;
            }
            """
        )
        close_button.clicked.connect(self.close)

        # Add the close button to a horizontal layout
        header_layout = QHBoxLayout()
        header_layout.addStretch()  # Push the button to the right
        header_layout.addWidget(close_button)
        header_layout.setContentsMargins(10, 10, 10, 10)

        # Create label to display the image
        self.image_label = QLabel(self)
        pixmap = QPixmap(image_path)

        # Scale the image to fit within the available screen space
        available_size = self.screen().availableGeometry().size()
        max_width = available_size.width() * 0.8  # Use 80% of screen width
        max_height = available_size.height() * 0.8  # Use 80% of screen height
        scaled_pixmap = pixmap.scaled(max_width, max_height, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.image_label.setPixmap(scaled_pixmap)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setStyleSheet("background: transparent;")

        # Add header and image to the main layout
        layout.addLayout(header_layout)
        layout.addWidget(self.image_label)


#=======================================================================
class FiltersDialog(QDialog):


    def __init__(self, clsUi=None, parent=None) -> None:
        """
        Initializes the AddNewMediaDialog class, which sets up the user interface for applying additional filters.

        Parameters:
        clsUi (optional): The UI class to be used for the dialog. Default is None.
        parent (optional): The parent widget for this dialog. Default is None.
        """
        super().__init__(parent)
        self.parent = parent
        self.ui = Ui_FiltersDialog()
        self.ui.setupUi(self)

        self.ui.btnApply.clicked.connect(self.applyFilters)
        self.ui.btnClose.clicked.connect(self.close)
        self.ui.btnReset.clicked.connect(self.resetForm)

        self.setSourceCombo()
        self.setEditionCombo()
        self.setLanguageCombo()

        self.showExistingFilters()

    
    def writeStatus(self, message : str, message_type=MESSAGE_TYPE.INFO) -> None:
        """
        Updates the status label with a given message and style.
        
        Parameters:
            message (str): The status message to display.
            message_type (str, optional): The type of message (MESSAGE_TYPE.INFO or MESSAGE_TYPE.ERROR) to determine the style.
        """
        self.ui.lblStatus.setStyleSheet(getStatusStyleSheet(message_type))
        self.ui.lblStatus.setText(message)


    def showExistingFilters(self) -> None:
        """
        Updates the UI elements with existing filter values from the parent object's additional_filters attribute.

        This method retrieves filter values for actor, director, year, source, edition, language, and to_burn status
        from the parent object's additional_filters dictionary and updates the corresponding UI elements with these values.
        """
        try:
            filters = self.parent.additional_filters
            if len(filters) > 0:
                self.ui.txtActor.setText(filters[FILTER_COLUMNS.ACTOR] if FILTER_COLUMNS.ACTOR in filters else '')
                self.ui.txtDirector.setText(filters[FILTER_COLUMNS.DIRECTOR] if FILTER_COLUMNS.DIRECTOR in filters else '')
                self.ui.txtYear.setText(filters[FILTER_COLUMNS.YEAR] if FILTER_COLUMNS.YEAR in filters else '')

                index = self.ui.cbSource.findData(filters[FILTER_COLUMNS.SOURCE]) if FILTER_COLUMNS.SOURCE in filters else 0
                self.ui.cbSource.setCurrentIndex(index)

                index = self.ui.cbEdition.findData(filters[FILTER_COLUMNS.EDITION]) if FILTER_COLUMNS.EDITION in filters else 0
                self.ui.cbEdition.setCurrentIndex(index)

                index = self.ui.cbLanguage.findData(filters[FILTER_COLUMNS.LANGUAGE]) if FILTER_COLUMNS.LANGUAGE in filters else 0
                self.ui.cbLanguage.setCurrentIndex(index)

                index = 0 if FILTER_COLUMNS.TO_BURN not in filters else 1 if filters[FILTER_COLUMNS.TO_BURN] == 1 else 2
                self.ui.cbToBurn.setCurrentIndex(index)
        except Exception as e:
            self.writeStatus(f'showExistingFilters: {e}', message_type=MESSAGE_TYPE.ERROR)


    def resetForm(self) -> None:
        """
        Resets the form fields in the user interface to their default values.

        This method sets the current index of several combo boxes to 0 and clears the text fields for actor and director.
        It is designed to be used when the form needs to be reset to its initial state.
        """
        try:
            self.ui.cbSource.setCurrentIndex(0)
            self.ui.cbEdition.setCurrentIndex(0)
            self.ui.cbLanguage.setCurrentIndex(0)
            self.ui.cbToBurn.setCurrentIndex(0)

            self.ui.txtActor.setText('')
            self.ui.txtDirector.setText('')
            self.ui.txtDirector.setText('')
        except Exception as e:
            self.writeStatus(f'resetForm: {e}', message_type=MESSAGE_TYPE.ERROR)


    def setSourceCombo(self) -> None:
        """
        Populates the source combo box with available media sources from the metadata helper.
        """
        try:
            df = metahelper.get_media_sources()
            for _, row in df.iterrows():
                self.ui.cbSource.addItem(row[META_COLUMNS.SOURCE], row[MEDIA_COLUMNS.ID])
        except Exception as e:
            self.writeStatus(f'setSource: {e}', MESSAGE_TYPE.ERROR)


    def setEditionCombo(self) -> None:
        """
        Populates the edition combo box with available media editions from the metadata helper.
        """
        try:
            if self.parent.ui.tbSummary.currentIndex() == 0:
                self.ui.cbEdition.setEnabled(True)
                df = metahelper.get_media_editions()
                for _, row in df.iterrows():
                    self.ui.cbEdition.addItem(row[META_COLUMNS.EDITION], row[MEDIA_COLUMNS.ID])
            else:
                self.ui.cbEdition.setEnabled(False)
        except Exception as e:
            self.writeStatus(f'setEdition: {e}', MESSAGE_TYPE.ERROR)
            

    def setLanguageCombo(self) -> None:
        """
        Populates the language combobox with available languages from the metadata helper.
        """
        try:
            df = metahelper.get_languages()
            for _, row in df.iterrows():
                self.ui.cbLanguage.addItem(row[META_COLUMNS.LANGUAGE], row[MEDIA_COLUMNS.ID])
        except Exception as e:
            self.writeStatus(f'setLanguage: {e}', MESSAGE_TYPE.ERROR)


    def applyFilters(self):
        """
        Applies a set of filters based on user input from the UI and updates the parent component with these filters.

        This method collects filter criteria from various UI elements such as text fields and combo boxes, 
        constructs a dictionary of filters, and assigns it to the `additional_filters` attribute of the parent component. 
        It then triggers a refresh of the media display and closes the current window.
        """
        try:
            filters = {}

            actor = self.ui.txtActor.text().strip()
            if actor != '':
                filters[FILTER_COLUMNS.ACTOR] = actor

            director = self.ui.txtDirector.text().strip()
            if director != '':
                filters[FILTER_COLUMNS.DIRECTOR] = director

            year = self.ui.txtYear.text().strip()
            if year != '':
                filters[FILTER_COLUMNS.YEAR] = year

            if self.ui.cbSource.currentIndex() > 0:
                filters[FILTER_COLUMNS.SOURCE] = self.ui.cbSource.currentData()

            if self.ui.cbEdition.currentIndex() > 0:
                filters[FILTER_COLUMNS.EDITION] = self.ui.cbEdition.currentData()

            if self.ui.cbLanguage.currentIndex() > 0:
                filters[FILTER_COLUMNS.LANGUAGE] = self.ui.cbLanguage.currentData()

            if self.ui.cbToBurn.currentIndex() > 0:
                filters[FILTER_COLUMNS.TO_BURN] = 1 if self.ui.cbToBurn.currentIndex() == 1 else 0

            self.parent.additional_filters = filters
            self.parent.refreshMedia()
            self.close()
        except Exception as e:
            self.writeStatus(f'applyFilters: {e}', MESSAGE_TYPE.ERROR)