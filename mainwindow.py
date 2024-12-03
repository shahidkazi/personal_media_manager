#=======================================================================
# Description:
# Main Form UI handling code
#=======================================================================
import model
import utils.metahelper as metahelper

from tablemodel        import TableModel
from ui.ui_form        import Ui_MainWindow
from utils.common      import getColIndexinTableView, getStatusStyleSheet

from PySide6.QtGui     import QPixmap
from PySide6.QtCore    import Qt, QSortFilterProxyModel
from PySide6.QtWidgets import QMainWindow, QMessageBox, QHeaderView, QLabel, QFileDialog

from dialogs import (
    AboutDialog,
    AddNewEpiodeDialog,
    AddNewMediaDialog,
    BackupDialog,
    BulkUpdateDialog,
    ExportDialog,
    FAQsDialog,
    FetchDetailsDialog,
    FiltersDialog,
    ImagePopup,
    ImportDialog,
    PreferencesDialog,
    PublishDialog
)

from utils.constants import (
    MEDIA_TYPE,
    MEDIA_DETAILS,
    META_COLUMNS,
    MEDIA_COLUMNS,
    MOVIE_COLUMNS,
    SERIES_COLUMNS,
    EPISODE_COLUMNS,
    FILTER_COLUMNS,
    APP_CONFIG,
    MESSAGE_TYPE,
    MOVIE_SUMMARY_DISPLAY_COLS,
    MOVIE_CUSTOM_COL_WIDTHS,
    SERIES_SUMMARY_DISPLAY_COLS,
    SERIES_EPISODE_DISPLAY_COLS,
    SERIES_CUSTOM_COL_WIDTHS,
    EPISODES_CUSTOM_COL_WIDTHS,
    DEFAULT_POSTER
)


#=======================================================================
class MainWindow(QMainWindow):
    """
    MainWindow class is the primary interface for managing and displaying media content such as movies and series.
    It initializes the UI components, sets up actions, filters, and manages the display of media details.

    Methods:
        setupActions()                     : Connects UI actions to their respective slots.
        setupFilters()                     : Connects filter UI components to their respective slots.
        setupMovies()                      : Sets up the movie-related UI components and their connections.
        setupSeries()                      : Sets up the series-related UI components and their connections.
        setGenreComboBoxes()               : Populates genre combo boxes with available genres.
        setSourceComboBox()                : Populates the source combo box with available media sources.
        setEditionComboBox()               : Populates the edition combo box with available media editions.
        setQualityComboBoxes()             : Populates quality combo boxes with available media qualities.
        setDiscFilterComboBox()            : Populates the disc filter combo box with available discs.
        get_filters()                      : Retrieves the current filter settings.
        displayMovies()                    : Displays the list of movies based on current filters.
        displaySeries()                    : Displays the list of series based on current filters.
        setMediaTabDetails(data)           : Sets the media tab details for the selected media.
        setEpisodeTabDetails(data)         : Sets the episode tab details for the selected series.
        filterSeasonEpisodes(i)            : Filters episodes based on the selected season.
        displayMovieDetails(row)           : Displays details of the selected movie.
        displaySeriesDetails()             : Displays details of the selected series.
        resetEpisodeDetails()              : Resets the episode details form.
        displayEpisodeDetails(row)         : Displays details of the selected episode.
        toggleFilter()                     : Toggles the filter settings.
        toggleMediaTab(i)                  : Toggles between movie and series tabs.
        refreshMedia()                     : Refreshes the media display based on current filters.
        onAboutDialogTriggered()           : Opens the About dialog.
        onAddNewMediaTriggered()           : Opens the Add New Media dialog.
        onBulkUpdateTriggered()            : Opens the Bulk Update dialog.
        onDeleteTriggered()                : Deletes the selected media.
        resetForm()                        : Resets the media details form.
        onExportTriggered()                : Opens the Export dialog.
        onFAQsTriggered()                  : Opens the FAQs dialog.
        onFetchDetailsTriggered()          : Opens the Fetch Details dialog.
        onImportTriggered()                : Opens the Import dialog.
        onPreferencesTriggered()           : Opens the Preferences dialog.
        onPublishTriggered()               : Opens the Publish dialog.
        getMovieUpdatedDetails(movie_id)   : Retrieves updated details for a movie.
        getSeriesUpdatedDetails(series_id) : Retrieves updated details for a series.
        updateMediaTriggered()             : Updates the details of the selected media.
        addGenre()                         : Adds a genre to the list of genres.
        removeGenre()                      : Removes a genre from the list of genres.
        addLanguage()                      : Adds a language to the list of languages.
        removeLanguage()                   : Removes a language from the list of languages.
        onAddNewEpisodeTriggered()         : Opens the Add New Episode dialog.
        onDeleteEpisodeTriggered()         : Deletes the selected episodes.
        onWatchedEpisodeTriggered(value=1) : Marks the selected episodes as watched.
        onNotWatchedEpisodeTriggered()     : Marks the selected episodes as not watched.

        setGeneralTabDetails(media_type, data)                  : Sets the general tab details for the selected media.
        setCastTabDetails(data, director, writer)               : Sets the cast tab details for the selected media.
        getSeriesEpisodeUpdatedDetails(episode_id, season)      : Retrieves updated details for a series episode.
        writeStatus(message, message_type=MESSAGE_TYPE.INFO)    : Writes a status message to the status label.
        writeStats(visible, total, media_type=MEDIA_TYPE.MOVIE) : Writes statistics about the media to the stats label. 
    """

    def __init__(self, parent=None) -> None:
        """
        Initializes the main window of the application.

        Parameters:
        parent (QWidget, optional): The parent widget of the main window. Defaults to None.

        This constructor sets up the user interface and initializes various components and settings for the main window.
        It performs the following actions:
        - Initializes the UI using Ui_MainWindow and sets it up.
        - Calls setup methods for actions, filters, movies, and series.
        - Sets a default poster image and configures the poster label to scale its contents.
        - Initializes status and stats labels and adds them to the status bar.
        - Initializes counters for total movies and series.
        - Configures combo boxes for genre, source, edition, quality, and disc filter.
        - Displays the series and movies in the UI.
        """
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.loading = True

        self.setupActions()
        self.setupFilters()
        self.setupMovies()
        self.setupSeries()

        self.ui.lblPoster.setScaledContents(True)

        self.lblStatus = QLabel('')
        self.lblStats  = QLabel('')
        self.statusBar().addPermanentWidget(self.lblStats, 1)
        self.statusBar().addPermanentWidget(self.lblStatus, 1)

        self.total_movies       = 0
        self.total_series       = 0
        self.additional_filters = {}
        
        self.current_poster     = DEFAULT_POSTER
        self.ui.lblPoster.setPixmap(QPixmap(self.current_poster))

        self.setGenreComboBoxes()
        self.setSourceComboBox()
        self.setEditionComboBox()
        self.setQualityComboBoxes()
        self.setDiscFilterComboBox()

        self.displaySeries()
        self.displayMovies()

        self.loading = False


    def setupActions(self) -> None:
        """
        Connects UI actions to their respective handler methods. This method sets up the connections
        between user interface actions (such as menu items or buttons) and the functions that should
        be executed when these actions are triggered.

        Parameters:
        - self: The instance of the class containing this method. It is assumed to have an attribute
        `ui` which contains the UI elements with actions that need to be connected.
        """
        self.ui.actionAbout.triggered.connect(self.onAboutDialogTriggered)
        self.ui.actionAddNew.triggered.connect(self.onAddNewMediaTriggered)
        self.ui.actionBulkUpdate.triggered.connect(self.onBulkUpdateTriggered)
        self.ui.actionDelete.triggered.connect(self.onDeleteTriggered)
        self.ui.actionExportData.triggered.connect(self.onExportTriggered)
        self.ui.actionFAQs.triggered.connect(self.onFAQsTriggered)
        self.ui.actionFetchDetails.triggered.connect(self.onFetchDetailsTriggered)
        self.ui.actionImportData.triggered.connect(self.onImportTriggered)
        self.ui.actionPreferences.triggered.connect(self.onPreferencesTriggered)
        self.ui.actionPublish.triggered.connect(self.onPublishTriggered)
        self.ui.actionUpdate.triggered.connect(self.updateMediaTriggered)
        self.ui.actionBackup.triggered.connect(self.onBackupTriggered)
        self.ui.actionRestore.triggered.connect(self.onRestoreTriggered)


    def setupFilters(self) -> None:
        """
        Sets up the connections for various UI filter components to their respective event handlers.
        
        This method connects the state change and index change events of filter UI components to 
        the appropriate methods that handle these events, allowing the application to respond to 
        user interactions with the filters.

        Parameters:
        - self: The instance of the class containing the UI components and methods.
        """
        self.ui.chkApplyFilter.stateChanged.connect(self.toggleFilter)
        self.ui.cbFilterWatched.currentIndexChanged.connect(self.refreshMedia)
        self.ui.cbFilterGenres.currentIndexChanged.connect(self.refreshMedia)
        self.ui.cbFilterDiscNo.currentIndexChanged.connect(self.refreshMedia)
        self.ui.cbFilterQuality.currentIndexChanged.connect(self.refreshMedia)
        self.ui.txtFilterTitle.textChanged.connect(self.refreshMedia)
        self.ui.btnMoreFilters.clicked.connect(self.onMoreFiltersTriggered)


    def setupMovies(self) -> None:
        """
        Sets up the movie-related UI components and their event connections.

        This method connects various UI elements to their respective event handlers
        to manage movie details, genres, and languages within the application.
        """
        self.ui.tblMovies.clicked.connect(self.displayMovieDetails)
        self.ui.tabWidget.setTabVisible(2, False)
        self.ui.tbSummary.currentChanged.connect(self.toggleMediaTab)
        self.ui.btnAddGenre.clicked.connect(self.addGenre)
        self.ui.btnRemoveGenre.clicked.connect(self.removeGenre)
        self.ui.btnAddLanguage.clicked.connect(self.addLanguage)
        self.ui.btnRemoveLanguage.clicked.connect(self.removeLanguage)
        self.ui.lblPoster.mousePressEvent  = self.onPosterClickTriggered
        self.ui.btnAddPoster.clicked.connect(self.changePoster)
        self.ui.btnRemovePoster.clicked.connect(self.removePoster)
    

    def setupSeries(self) -> None:
        """
        Sets up the connections and visibility for the series management UI components.

        This method connects various UI components to their respective event handlers and 
        manages the visibility of certain UI elements related to series and episodes.

        Parameters:
        - self: The instance of the class containing this method.
        """
        self.ui.tblSeries.clicked.connect(self.displaySeriesDetails)
        self.ui.tblEpisodes.clicked.connect(self.displayEpisodeDetails)
        self.ui.cbSeason.currentIndexChanged.connect(self.filterSeasonEpisodes)
        self.ui.lblSeasons.setVisible(False)
        self.ui.txtSeasons.setVisible(False)
        self.ui.btnAddNewEpisode.clicked.connect(self.onAddNewEpisodeTriggered)
        self.ui.btnDeleteEpisode.clicked.connect(self.onDeleteEpisodeTriggered)
        self.ui.btnWatched.clicked.connect(self.onWatchedEpisodeTriggered)
        self.ui.btnNotWatched.clicked.connect(self.onNotWatchedEpisodeTriggered)


    def writeStatus(self, message : str, message_type=MESSAGE_TYPE.INFO) -> None:
        """
        Updates the status label with a given message and styles it according to the message type.

        Parameters:
        - message (str): The message to be displayed on the status label.
        - message_type (str, optional): The type of message, which determines the styling. 
        It can be 'INFO', 'WARNING', or 'ERROR'. Defaults to 'INFO'.

        The function aligns the status label to the right and vertically centers it. 
        If the message type is 'WARNING', the text color is set to red. 
        If the message type is 'ERROR', the text color is set to red and the font is bold.
        """
        from PySide6.QtCore import Qt

        self.lblStatus.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.lblStatus.setStyleSheet(getStatusStyleSheet(message_type))
        self.lblStatus.setText(f'{message}      ')

    
    def writeStats(self, visible : int, total : int, media_type=MEDIA_TYPE.MOVIE) -> None:
        '''
        Updates the statistics label with the number of visible and total media items.

        Parameters:
        visible (int): The number of media items currently visible.
        total (int): The total number of media items.
        media_type (MEDIA_TYPE, optional): The type of media, default is MEDIA_TYPE.MOVIE.
        '''
        media = media_type.title() + ('s' if media_type == MEDIA_TYPE.MOVIE else '')
        self.lblStats.setText(f'              Showing {visible}/{total} {media}')


    def setGenreComboBoxes(self) -> None:
        """
        Populates the genre combo boxes in the user interface with available genres.

        This method clears any existing items in the genre combo boxes and then populates them
        with genres retrieved from a data source. It adds an "All Genres" option to the filter
        combo box with an ID of 0, followed by each genre from the data source.
        """
        try:
            self.ui.cbGenres.clear()
            self.ui.cbFilterGenres.clear()
            self.ui.cbFilterGenres.addItem('All Genres', 0)

            df = metahelper.get_genres()
            for _, row in df.iterrows():
                self.ui.cbGenres.addItem(row[META_COLUMNS.GENRE], row[MEDIA_COLUMNS.ID])
                self.ui.cbFilterGenres.addItem(row[META_COLUMNS.GENRE], row[MEDIA_COLUMNS.ID])
        except Exception as e:
            self.writeStatus(f'setGenre: {e}', MESSAGE_TYPE.ERROR)


    def setSourceComboBox(self) -> None:
        """
        Populates the source combo box in the user interface with media sources.

        This method clears the existing items in the combo box and retrieves a 
        DataFrame of media sources using the `metahelper.get_media_sources()` 
        function. It then iterates over each row in the DataFrame, adding each 
        source to the combo box with the source name as the display text and 
        the media ID as the associated data.
        """
        try:
            self.ui.cbSource.clear()
            df = metahelper.get_media_sources()
            for _, row in df.iterrows():
                self.ui.cbSource.addItem(row[META_COLUMNS.SOURCE], row[MEDIA_COLUMNS.ID])
        except Exception as e:
            self.writeStatus(f'setSource: {e}', MESSAGE_TYPE.ERROR)


    def setEditionComboBox(self) -> None:
        """
        Populates the edition combo box in the user interface with available media editions.

        This method clears the current items in the combo box and retrieves a DataFrame of media editions
        using the `metahelper.get_media_editions()` function. It iterates over each row in the DataFrame,
        adding each edition to the combo box with the edition name as the display text and the media ID
        as the associated data. Finally, it sets the default selected text in the combo box to 'Theatrical Edition'.
        """
        try:
            self.ui.cbEdition.clear()
            df = metahelper.get_media_editions()
            for _, row in df.iterrows():
                self.ui.cbEdition.addItem(row[META_COLUMNS.EDITION], row[MEDIA_COLUMNS.ID])

            self.ui.cbEdition.setCurrentText('Theatrical Edition')
        except Exception as e:
            self.writeStatus(f'setEdition: {e}', MESSAGE_TYPE.ERROR)


    def setQualityComboBoxes(self) -> None:
        """
        Populates the quality combo boxes in the user interface with available media qualities.

        This method clears existing items in the combo boxes for quality, filter quality, and episode quality,
        and then populates them with data retrieved from the media qualities metadata.
        """
        try:
            self.ui.cbQuality.clear()
            self.ui.cbFilterQuality.clear()
            self.ui.cbEpisodeQuality.clear()

            self.ui.cbFilterQuality.addItem('All Qualities', 0)

            df = metahelper.get_media_qualities()
            for _, row in df.iterrows():
                self.ui.cbQuality.addItem(row[META_COLUMNS.QUALITY], row[MEDIA_COLUMNS.ID])
                self.ui.cbFilterQuality.addItem(row[META_COLUMNS.QUALITY], row[MEDIA_COLUMNS.ID])
                self.ui.cbEpisodeQuality.addItem(row[META_COLUMNS.QUALITY], row[MEDIA_COLUMNS.ID])
        except Exception as e:
            self.writeStatus(f'setQuality: {e}', MESSAGE_TYPE.ERROR)


    def setDiscFilterComboBox(self) -> None:
        """
        Updates the disc filter combo box in the user interface with available disc numbers.

        This method clears the current items in the combo box and adds a default item 'All Discs'.
        It then retrieves disc data based on the current media type (either MOVIE or SERIES) and
        populates the combo box with the backup disc numbers from the retrieved data.
        """
        try:
            self.ui.cbFilterDiscNo.clear()
            self.ui.cbFilterDiscNo.addItem('All Discs')

            data = model.get_discs(MEDIA_TYPE.MOVIE if self.ui.tbSummary.currentIndex() == 0 else MEDIA_TYPE.SERIES)
            for _, row in data.iterrows():
                self.ui.cbFilterDiscNo.addItem(row[MEDIA_COLUMNS.BACKUP_DISC])
        except Exception as e:
            self.writeStatus(f'setDiscFilter: {e}', MESSAGE_TYPE.ERROR)


    def get_filters(self, isSeries=False) -> dict:
        """
        Constructs a dictionary of filters based on the current state of the UI elements.

        This method checks various UI components to determine which filters should be applied
        and constructs a dictionary where the keys are filter column identifiers and the values
        are the corresponding filter criteria.

        Returns:
            dict: A dictionary containing filter criteria. The keys are constants from 
            FILTER_COLUMNS, and the values are the user-specified filter values.

        Notes:
            - The filter for the title is applied if the text field is not empty.
            - The 'watched' filter is applied if the corresponding checkbox is checked and 
            the selected index is greater than 0. It maps to 1 if the index is 1, otherwise 0.
            - The genre filter is applied if the genre combobox index is greater than 0.
            - The backup disc filter is applied if the disc number combobox index is greater than 0.
            - The quality filter is applied if the quality combobox is enabled and its index is greater than 0.
        """
        filters = {}

        try:
            if len(self.ui.txtFilterTitle.text()) > 0:
                filters[FILTER_COLUMNS.TITLE] = self.ui.txtFilterTitle.text()

            if self.ui.chkApplyFilter.isChecked():
                if self.ui.cbFilterWatched.currentIndex() > 0:
                    filters[FILTER_COLUMNS.WATCHED] = 1 if self.ui.cbFilterWatched.currentIndex() == 1 else 0

                if self.ui.cbFilterGenres.currentIndex() > 0:
                    filters[FILTER_COLUMNS.GENRE] = self.ui.cbFilterGenres.currentData()

                if self.ui.cbFilterDiscNo.currentIndex() > 0:
                    filters[FILTER_COLUMNS.BACKUP_DISC] = self.ui.cbFilterDiscNo.currentText()

                if self.ui.cbFilterQuality.isEnabled() and self.ui.cbFilterQuality.currentIndex() > 0 and not isSeries:
                    filters[FILTER_COLUMNS.QUALITY] = self.ui.cbFilterQuality.currentData()

                if len(self.additional_filters) > 0:
                    filters.update(self.additional_filters)
        except Exception as e:
            self.writeStatus(f'get_filters: {e}', MESSAGE_TYPE.ERROR)
            
        return filters


    def displayMovies(self, updateScroll=True) -> None:
        """
        Displays a list of movies in a table format within the user interface.

        This function retrieves movie data using the `get_media` method from the `model` object, 
        which filters the data based on the current filters set in the application. It then sets 
        up a table model with the retrieved data and configures the table view to display only 
        the specified columns. The function also adjusts column widths and connects a selection 
        change event to display additional movie details.
        """
        try:
            v_scroll_pos = self.ui.tblMovies.verticalScrollBar().value()
            h_scroll_pos = self.ui.tblMovies.horizontalScrollBar().value()

            curr_idx     = self.ui.tblMovies.selectionModel().currentIndex().row() \
                        if self.ui.tblMovies.selectionModel() and self.ui.tblMovies.selectionModel().currentIndex() \
                      else 0

            df, total    = model.get_media(MEDIA_TYPE.MOVIE, self.get_filters())
            tableModel   = TableModel(df)

            proxy_model = QSortFilterProxyModel()
            proxy_model.setSourceModel(tableModel)

            self.ui.tblMovies.setModel(proxy_model)
            self.ui.tblMovies.setSortingEnabled(True)
            self.ui.tblMovies.verticalHeader().hide()
            
            displayCols = list(x for x in MOVIE_SUMMARY_DISPLAY_COLS)
            for idx, col in enumerate(df.columns):
                self.ui.tblMovies.setColumnHidden(idx, col not in displayCols)

            self.ui.tblMovies.resizeColumnsToContents()
            for col in MOVIE_CUSTOM_COL_WIDTHS:
                self.ui.tblMovies.setColumnWidth(df.columns.get_loc(col), MOVIE_CUSTOM_COL_WIDTHS[col])

            title_idx = df.columns.get_loc(MEDIA_COLUMNS.TITLE)
            self.ui.tblMovies.sortByColumn(title_idx, Qt.AscendingOrder)
            self.ui.tblMovies.horizontalHeader().setSectionResizeMode(title_idx, QHeaderView.Stretch)
            
            self.ui.tblMovies.selectionModel().selectionChanged.connect(self.displayMovieDetails)
            if updateScroll:
                if self.ui.tbSummary.currentIndex() == 0 and self.ui.tblMovies.model().rowCount() > 0:
                    self.ui.tblMovies.selectRow(curr_idx)
                    self.ui.tblMovies.setFocus()

                self.ui.tblMovies.verticalScrollBar().setValue(v_scroll_pos)
                self.ui.tblMovies.horizontalScrollBar().setValue(h_scroll_pos)

            self.total_movies = total
            self.writeStats(len(df), total)
        except Exception as e:
            self.writeStatus(f'displayMovies: {e}', MESSAGE_TYPE.ERROR)


    def displaySeries(self, updateScroll=True) -> None:
        """
        Displays a series of media items in a table view within the user interface.

        This function retrieves media data of type 'SERIES' using the model's `get_media` method,
        applies filters, and sets up a table model to display the data. It configures the table
        to hide certain columns, set custom column widths, and adjust the title column to stretch.
        It also connects the selection change event to a detail display function and updates
        statistics related to the series.
        """
        try:
            v_scroll_pos = self.ui.tblSeries.verticalScrollBar().value()
            h_scroll_pos = self.ui.tblSeries.horizontalScrollBar().value()

            curr_idx     = self.ui.tblSeries.selectionModel().currentIndex().row() \
                        if self.ui.tblSeries.selectionModel() and self.ui.tblSeries.selectionModel().currentIndex() \
                      else 0

            df, total    = model.get_media(MEDIA_TYPE.SERIES, self.get_filters(True))
            tableModel   = TableModel(df, MEDIA_TYPE.SERIES)
            proxy_model  = QSortFilterProxyModel()
            proxy_model.setSourceModel(tableModel)

            self.ui.tblSeries.setModel(proxy_model)
            self.ui.tblSeries.setSortingEnabled(True)
            self.ui.tblSeries.verticalHeader().hide()
            
            displayCols = list(x for x in SERIES_SUMMARY_DISPLAY_COLS)
            for idx, col in enumerate(df.columns):
                self.ui.tblSeries.setColumnHidden(idx, col not in displayCols)

            for col in SERIES_CUSTOM_COL_WIDTHS:
                self.ui.tblSeries.setColumnWidth(
                    df.columns.get_loc(col), 
                    SERIES_CUSTOM_COL_WIDTHS[col] )

            title_idx = df.columns.get_loc(MEDIA_COLUMNS.TITLE)
            self.ui.tblSeries.sortByColumn(title_idx, Qt.AscendingOrder)
            self.ui.tblSeries.horizontalHeader().setSectionResizeMode(title_idx, QHeaderView.Stretch)
            
            self.ui.tblSeries.selectionModel().selectionChanged.connect(self.displaySeriesDetails)
            if updateScroll:
                if self.ui.tbSummary.currentIndex() == 1 and self.ui.tblSeries.model().rowCount() > 0:
                    self.ui.tblSeries.selectRow(curr_idx)
                    self.ui.tblSeries.setFocus()

                self.ui.tblSeries.verticalScrollBar().setValue(v_scroll_pos)
                self.ui.tblSeries.horizontalScrollBar().setValue(h_scroll_pos)

            self.total_series = total
            self.writeStats(len(df), total, MEDIA_TYPE.SERIES)
        except Exception as e:
            self.writeStatus(f'displaySeries: {e}', MESSAGE_TYPE.ERROR)
    

    def setGeneralTabDetails(self, media_type : str, data : dict) -> None:
        """
        Sets the general tab details of a media item in the user interface.

        Parameters:
        media_type (str): The type of media, either 'MOVIE' or 'SERIES'.
        data (dict): A dictionary containing media details, including content, genres, and languages.
        """
        import os.path 

        try:
            details      = data[MEDIA_DETAILS.CONTENT]
            poster_path  = f'{metahelper.get_app_config(APP_CONFIG.POSTER_PATH)}/{media_type.lower()}/{str(details[MEDIA_COLUMNS.ID][0])}.jpg'
            self.current_poster = poster_path if os.path.isfile(poster_path) else DEFAULT_POSTER
            
            self.ui.lblPoster.setPixmap(QPixmap(self.current_poster))
            self.ui.txtTitle.setText(details[MEDIA_COLUMNS.TITLE][0])
            self.ui.txtTitle.setCursorPosition(0)
            self.ui.txtOriginalTitle.setText(details[MEDIA_COLUMNS.ORIGINAL_TITLE][0])
            self.ui.txtOriginalTitle.setCursorPosition(0)
            self.ui.txtYear.setText(str(details[MEDIA_COLUMNS.YEAR][0]))

            if media_type == MEDIA_TYPE.MOVIE:
                self.ui.txtRuntime.setText(details[MOVIE_COLUMNS.RUNTIME][0])
            else:
                self.ui.txtSeasons.setText(str(details[SERIES_COLUMNS.SEASONS][0]))

            self.ui.dsRating.setValue(details[MEDIA_COLUMNS.ONLINE_RATING][0])
            self.ui.dsUserRating.setValue(details[MEDIA_COLUMNS.RATING][0])
            self.ui.chkWatched.setChecked(bool(details[MEDIA_COLUMNS.WATCHED][0]))
            self.ui.txtCountry.setText(details[MEDIA_COLUMNS.COUNTRY][0])
            self.ui.txtCountry.setCursorPosition(0)
            self.ui.txtReleaseDate.setText(details[MEDIA_COLUMNS.RELEASE_DATE][0])

            if details[META_COLUMNS.SOURCE][0]:
                self.ui.cbSource.setCurrentText(details[META_COLUMNS.SOURCE][0])
            else:
                self.ui.cbSource.setCurrentIndex(0)

            if details[MEDIA_COLUMNS.CERTIFICATION][0]:
                self.ui.cbCertification.setCurrentText(details[MEDIA_COLUMNS.CERTIFICATION][0])
            else:
                self.ui.cbCertification.setCurrentIndex(0)

            self.ui.lsGenres.clear()
            self.ui.lsGenres.addItems(data[MEDIA_DETAILS.GENRES][META_COLUMNS.GENRE].tolist())
            self.ui.lsLanguages.clear()
            self.ui.lsLanguages.addItems(data[MEDIA_DETAILS.LANGUAGES][META_COLUMNS.LANGUAGE].tolist())

            self.ui.txtTagLine.setText(details[MEDIA_COLUMNS.TAGLINE][0])
            self.ui.txtPlot.setPlainText(details[MEDIA_COLUMNS.PLOT][0])
            self.ui.txtNotes.setPlainText(details[MEDIA_COLUMNS.NOTES][0])
        except Exception as e:
            self.writeStatus(f'setGeneralTab: {e}', MESSAGE_TYPE.ERROR)


    def setMediaTabDetails(self, data : dict) -> None:
        """
        Updates the media tab details in the user interface with the provided data.

        Parameters:
        data (dict): A dictionary containing media details. It should include keys from MEDIA_DETAILS.CONTENT
                     and MEDIA_DETAILS.OTHERS, where each key maps to another dictionary with specific media
                     attributes.

        The function performs the following updates:
        - Sets the current text of the edition combo box based on the edition details.
        - Sets the current text of the quality combo box based on the quality details.
        - Updates text fields for codec, audio codec, disc count, size, and disc number.
        - Sets radio buttons for the 'To Burn' option based on the provided data.
        - Updates the table model for other media details.
        """
        try:
            details = data[MEDIA_DETAILS.CONTENT]

            if details[META_COLUMNS.EDITION][0]:
                self.ui.cbEdition.setCurrentText(details[MOVIE_COLUMNS.EDITION][0])
            else:
                self.ui.cbEdition.setCurrentIndex(0)

            if details[MEDIA_COLUMNS.QUALITY][0]:
                self.ui.cbQuality.setCurrentText(details[META_COLUMNS.QUALITY][0])
            else:
                self.ui.cbQuality.setCurrentIndex(0)

            self.ui.txtCodec.setText(details[MOVIE_COLUMNS.VIDEO_CODEC][0])
            self.ui.txtAudioCodec.setText(details[MOVIE_COLUMNS.AUDIO_CODEC][0])
            self.ui.txtDiscCount.setText(str(details[MOVIE_COLUMNS.DISC_COUNT][0]))
            self.ui.txtSize.setText(details[MEDIA_COLUMNS.SIZE][0])
            self.ui.txtDiscNo.setText(str(details[MEDIA_COLUMNS.BACKUP_DISC][0]))

            self.ui.rbToBurnNo.setChecked(details[MEDIA_COLUMNS.TO_BURN][0] == 0)
            self.ui.rbToBurnYes.setChecked(details[MEDIA_COLUMNS.TO_BURN][0] == 1)

            tableModel = TableModel(data[MEDIA_DETAILS.OTHERS])
            self.ui.tblOtherMedia.setModel(tableModel)
            self.ui.tblOtherMedia.verticalHeader().hide()
        except Exception as e:
            self.writeStatus(f'setMediaTab: {e}', MESSAGE_TYPE.ERROR)


    def setEpisodeTabDetails(self, data : dict) -> None:
        """
        Configures the episode tab details in the user interface.

        Parameters:
        data (DataFrame): A pandas DataFrame containing episode information. It is expected to have columns
                          corresponding to EPISODE_COLUMNS and MEDIA_COLUMNS.

        This method performs the following actions:
        - Clears and populates the season combo boxes with available seasons from the data.
        - Sets the 'watched' checkbox based on whether all episodes in the data are marked as watched.
        - Initializes and sets a table model for the episode table view using the provided data.
        - Hides columns in the episode table that are not part of the SERIES_EPISODE_DISPLAY_COLS.
        - Sets custom column widths for specified columns in the episode table.
        - Adjusts the title column to stretch within the table view.
        - Resets episode details and connects the selection change event to update episode details display.
        - Selects the first row in the episode table by default.
        """
        try:
            self.ui.cbSeason.clear()
            self.ui.cbEpisodeSeason.clear()
            self.ui.cbSeason.addItem('All Seasons')

            seasons = data[EPISODE_COLUMNS.SEASON].unique().astype(str).tolist()
            for season in seasons:
                self.ui.cbSeason.addItem(season)
                self.ui.cbEpisodeSeason.addItem(season)

            watched = len(data[MEDIA_COLUMNS.WATCHED].unique()) == 1 and data[MEDIA_COLUMNS.WATCHED][0] == 1
            self.ui.chkWatchedSeason.setChecked(watched)

            v_scroll_pos = self.ui.tblEpisodes.verticalScrollBar().value()
            h_scroll_pos = self.ui.tblEpisodes.horizontalScrollBar().value()

            tableModel   = TableModel(data)
            proxy_model  = QSortFilterProxyModel()
            proxy_model.setSourceModel(tableModel)

            self.ui.tblEpisodes.setModel(proxy_model)
            self.ui.tblEpisodes.setSortingEnabled(True)
            self.ui.tblEpisodes.verticalHeader().hide()

            displayCols = list(x for x in SERIES_EPISODE_DISPLAY_COLS)
            for idx, col in enumerate(data.columns):
                self.ui.tblEpisodes.setColumnHidden(idx, col not in displayCols)

            for col in EPISODES_CUSTOM_COL_WIDTHS:
                self.ui.tblEpisodes.setColumnWidth(
                    data.columns.get_loc(col), 
                    EPISODES_CUSTOM_COL_WIDTHS[col] )

            self.ui.tblEpisodes.sortByColumn(
                data.columns.get_loc(EPISODE_COLUMNS.SEASON), 
                Qt.AscendingOrder)
            self.ui.tblEpisodes.horizontalHeader().setSectionResizeMode(
                data.columns.get_loc(MEDIA_COLUMNS.TITLE), 
                QHeaderView.Stretch)
            
            self.resetEpisodeDetails()

            self.ui.tblEpisodes.selectionModel().selectionChanged.connect(self.displayEpisodeDetails)

            self.ui.tblEpisodes.verticalScrollBar().setValue(v_scroll_pos)
            self.ui.tblEpisodes.horizontalScrollBar().setValue(h_scroll_pos)
        except Exception as e:
            self.writeStatus(f'setEpisodeTab: {e}', MESSAGE_TYPE.ERROR)


    def filterSeasonEpisodes(self) -> None:
        """
        Filters and displays episodes of a selected series season in a table view.

        Parameters:
        i (int): Index passed by the currentIndexChanged event

        Functionality:
        - Retrieves the currently selected series from a table view.
        - Fetches episodes for the selected series and season.
        - Sets the fetched episodes data into a table model and updates the UI table view.
        - Hides columns that are not specified in the display columns list.
        - Sets custom column widths for specified columns.
        - Adjusts the title column to stretch for better visibility.
        """
        try:
            index       = self.ui.tblSeries.selectionModel().currentIndex()
            series_id   = index.sibling(index.row(), 
                                        getColIndexinTableView(self.ui.tblSeries, MEDIA_COLUMNS.ID)).data()
            data        = model.get_series_episodes(series_id, self.ui.cbSeason.currentText())

            tableModel  = TableModel(data)
            self.ui.tblEpisodes.setModel(tableModel)
            self.ui.tblEpisodes.verticalHeader().hide()

            displayCols = list(x for x in SERIES_EPISODE_DISPLAY_COLS)
            for idx, col in enumerate(data.columns):
                self.ui.tblEpisodes.setColumnHidden(idx, col not in displayCols)

            for col in EPISODES_CUSTOM_COL_WIDTHS:
                self.ui.tblEpisodes.setColumnWidth(
                    data.columns.get_loc(col), 
                    EPISODES_CUSTOM_COL_WIDTHS[col] )

            self.ui.tblEpisodes.horizontalHeader().setSectionResizeMode(
                data.columns.get_loc(MEDIA_COLUMNS.TITLE), 
                QHeaderView.Stretch )
        except Exception as e:
            self.writeStatus(f'filterSeasonEp: {e}', MESSAGE_TYPE.ERROR)
        

    def setCastTabDetails(self, data : dict, director : str, writer : str) -> None:
        """
        Configures the cast tab details in the user interface.

        Parameters:
        data (dict): A dictionary containing the data to be displayed in the cast table.
        director (str): The name of the director to be displayed in the director text field.
        writer (str): The name of the writer to be displayed in the writer text field.
        """
        try:
            tableModel = TableModel(data)
            self.ui.tblCast.setModel(tableModel)
            self.ui.tblCast.verticalHeader().hide()

            self.ui.tblCast.setColumnWidth(2, 175) # Set fixed width for Comments in TV Series
            self.ui.tblCast.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
            self.ui.tblCast.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

            if self.ui.tbSummary.currentIndex() == 0:
                self.ui.tblCast.setColumnHidden(2, True)

            self.ui.txtDirector.setText(director)
            self.ui.txtWriter.setText(writer)
        except Exception as e:
            self.writeStatus(f'setCastTab: {e}', MESSAGE_TYPE.ERROR)


    def displayMovieDetails(self) -> None:
        """
        Displays the details of a selected movie in the UI.

        Parameters:
        - row: The row index of the selected movie in the table view.

        This function retrieves the movie ID from the currently selected row in the movie table,
        fetches the movie details using the model, and updates various tabs in the UI with the
        retrieved data. It sets the general, media, and cast details tabs with the relevant
        information.
        """
        try:
            index     = self.ui.tblMovies.selectionModel().currentIndex()
            movie_id  = index.sibling(index.row(), 
                                      getColIndexinTableView(self.ui.tblMovies, MEDIA_COLUMNS.ID)).data()
            data      = model.get_movie_details(movie_id)
            
            self.setGeneralTabDetails(MEDIA_TYPE.MOVIE, data)
            self.setMediaTabDetails(data)
            self.setCastTabDetails(
                data[MEDIA_DETAILS.CAST], 
                data[MEDIA_DETAILS.CONTENT][MEDIA_COLUMNS.DIRECTOR][0],
                data[MEDIA_DETAILS.CONTENT][MEDIA_COLUMNS.WRITER][0])
        except Exception as e:
            self.writeStatus(f'displayMovie: {e}', MESSAGE_TYPE.ERROR)

    
    def displaySeriesDetails(self) -> None:
        """
        Displays the details of a selected series in the user interface.

        This method retrieves the currently selected series from a table view,
        fetches its details from the model, and updates various tabs in the UI
        with the retrieved information.

        Parameters:
        - self: The instance of the class containing this method.
        """
        try:
            index     = self.ui.tblSeries.selectionModel().currentIndex()
            series_id = index.sibling(index.row(), 
                                    getColIndexinTableView(self.ui.tblSeries, MEDIA_COLUMNS.ID)).data()
            data      = model.get_series_details(series_id)
            
            self.setGeneralTabDetails(MEDIA_TYPE.SERIES, data)
            self.setEpisodeTabDetails(data[MEDIA_DETAILS.EPISODES])
            self.setCastTabDetails(
                data[MEDIA_DETAILS.CAST], 
                data[MEDIA_DETAILS.CONTENT][MEDIA_COLUMNS.DIRECTOR][0],
                data[MEDIA_DETAILS.CONTENT][MEDIA_COLUMNS.WRITER][0] )
        except Exception as e:
            self.writeStatus(f'displaySeries: {e}', MESSAGE_TYPE.ERROR)

    
    def resetEpisodeDetails(self) -> None:
        """
        Resets the episode details in the user interface to their default values.

        This method clears or resets various UI components related to episode details:
        - Sets the episode number text field to an empty string.
        - Sets the episode title text field to an empty string.
        - Resets the episode quality combo box to its first item (index 0).
        - Unchecks the watched episode checkbox.
        - Sets the episode disc number text field to an empty string.
        - Unchecks the episode to burn checkbox.
        - Sets the episode tags text field to an empty string.
        - Sets the episode size text field to an empty string.
        - Clears the episode plot text area.
        """
        try:
            self.ui.txtEpisodeNo.setText('')
            self.ui.txtEpisodeTitle.setText('')
            self.ui.cbEpisodeQuality.setCurrentIndex(0)
            self.ui.chkWatchedEpisode.setChecked(False)
            self.ui.txtEpisodeDiscNo.setText('')
            self.ui.chkEpisodeToBurn.setChecked(False)
            self.ui.txtEpisodeTags.setText('')
            self.ui.txtEpisodeSize.setText('')
            self.ui.txtEpisodePlot.setPlainText('')
        except Exception as e:
            self.writeStatus(f'resetEpisode: {e}', MESSAGE_TYPE.ERROR)


    def displayEpisodeDetails(self) -> None:
        """
        Displays the details of an episode based on the given row.

        Parameters:
            row: The row index of the selected episode in the episodes table.
        """
        try:
            index      = self.ui.tblEpisodes.selectionModel().currentIndex()
            episode_id = index.sibling(index.row(), 
                                    getColIndexinTableView(self.ui.tblEpisodes, MEDIA_COLUMNS.ID)).data()
            data       = model.get_episode_details(episode_id)

            self.ui.cbEpisodeSeason.setCurrentText(str(data[EPISODE_COLUMNS.SEASON][0]))
            self.ui.txtEpisodeNo.setText(str(data[EPISODE_COLUMNS.EPISODE][0]))
            self.ui.txtEpisodeTitle.setText(data[MEDIA_COLUMNS.TITLE][0])
            self.ui.cbEpisodeQuality.setCurrentText(data[MEDIA_COLUMNS.QUALITY][0])
            self.ui.chkWatchedEpisode.setChecked(bool(data[MEDIA_COLUMNS.WATCHED][0]))
            self.ui.txtEpisodeDiscNo.setText(data[MEDIA_COLUMNS.BACKUP_DISC][0])
            self.ui.chkEpisodeToBurn.setChecked(bool(data[MEDIA_COLUMNS.TO_BURN][0]))
            self.ui.txtEpisodeTags.setText(data[MEDIA_COLUMNS.TAG][0])
            self.ui.txtEpisodeSize.setText(data[MEDIA_COLUMNS.SIZE][0])
            self.ui.txtEpisodePlot.setPlainText(data[MEDIA_COLUMNS.PLOT][0])
            self.ui.txtEpisodeReleased.setText(data[MEDIA_COLUMNS.RELEASE_DATE][0])
        except Exception as e:
            self.writeStatus(f'displayEpisode: {e}', MESSAGE_TYPE.ERROR)


    def toggleFilter(self) -> None:
        """
        Toggles the filter settings in the user interface based on the status of a checkbox.

        This method checks the status of the 'Apply Filter' checkbox and enables or disables
        various filter options accordingly. If the checkbox is unchecked, it resets the filter
        options to their default values and updates the display to show either movies or series
        based on the current tab index.
        """
        try:
            status = self.ui.chkApplyFilter.isChecked()

            self.ui.cbFilterWatched.setEnabled(status)
            self.ui.cbFilterGenres.setEnabled(status)
            self.ui.cbFilterDiscNo.setEnabled(status)
            self.ui.cbFilterQuality.setEnabled(status and self.ui.tbSummary.currentIndex() == 0)
            self.ui.btnMoreFilters.setEnabled(status)

            if not status:
                self.ui.cbFilterWatched.setCurrentIndex(0)
                self.ui.cbFilterGenres.setCurrentIndex(0)
                self.ui.cbFilterQuality.setCurrentIndex(0)
                self.ui.cbFilterDiscNo.setCurrentIndex(0)
                self.additional_filters = {}

                if self.ui.tbSummary.currentIndex() == 0:
                    self.displayMovies()
                else:
                    self.displaySeries()
        except Exception as e:
            self.writeStatus(f'toggleFilter: {e}', MESSAGE_TYPE.ERROR)


    def toggleMediaTab(self, i : int) -> None:
        """
        Toggles the visibility and enabled state of various UI components based on the provided index.

        Parameters:
        i (int): An integer index that determines which media tab to display. 
                If `i` is 0, the function will display the movie-related UI components.
                If `i` is 1, the function will display the series-related UI components.
        """
        try:
            self.ui.tabWidget.setTabVisible(1, i == 0)
            self.ui.lblRuntime.setVisible(i == 0)
            self.ui.txtRuntime.setVisible(i == 0)
            self.ui.cbSource.setEnabled(i == 0)
            self.ui.actionBulkUpdate.setEnabled(i == 0)

            self.ui.tabWidget.setTabVisible(2, i == 1)
            self.ui.lblSeasons.setVisible(i == 1)
            self.ui.txtSeasons.setVisible(i == 1)

            self.ui.cbFilterQuality.setEnabled(self.ui.chkApplyFilter.isChecked() and self.ui.tbSummary.currentIndex() == 0)

            self.writeStats(
                self.ui.tblMovies.model().rowCount() if i == 0 else self.ui.tblSeries.model().rowCount(), 
                self.total_movies if i == 0 else self.total_series, 
                MEDIA_TYPE.MOVIE if i == 0 else MEDIA_TYPE.SERIES )

            self.resetForm()
        except Exception as e:
            self.writeStatus(f'toggleMediaTab: {e}', MESSAGE_TYPE.ERROR)


    def refreshMedia(self) -> None:
        """
        Refreshes the media display by updating the series and movies shown in the UI.
        
        This method performs the following actions:
        - Calls `displaySeries()` to update the series display.
        - Calls `displayMovies()` to update the movies display.
        - Determines the current index of the summary tab and writes the statistics 
        for either movies or series based on the current tab selection.
        """
        try:
            if not self.loading:
                self.displaySeries(updateScroll=False)
                self.displayMovies(updateScroll=False)

                i = self.ui.tbSummary.currentIndex()
                self.writeStats(
                    self.ui.tblMovies.model().rowCount() if i == 0 else self.ui.tblSeries.model().rowCount(), 
                    self.total_movies if i == 0 else self.total_series, 
                    MEDIA_TYPE.MOVIE if i == 0 else MEDIA_TYPE.SERIES )
        except Exception as e:
            self.writeStatus(f'refreshMedia: {e}', MESSAGE_TYPE.ERROR)


    def onAboutDialogTriggered(self) -> None:
        '''
        Displays the About Dialog Box
        '''
        widget = AboutDialog()
        widget.exec()


    def onAddNewMediaTriggered(self) -> None:
        '''
        Displays the Add New Media Dialog Box
        '''
        widget = AddNewMediaDialog(parent=self)
        widget.open()


    def onBulkUpdateTriggered(self) -> None:
        '''
        Displays the Bulk Update Dialog Box
        '''
        widget = BulkUpdateDialog(parent=self)
        widget.open()


    def onDeleteTriggered(self) -> None:
        """
        Handles the deletion of selected media entries from the user interface.

        This method is triggered when the delete action is initiated by the user. It prompts the user for confirmation
        before proceeding with the deletion of selected media entries (either movies or series) from the database.

        Parameters:
        - self: The instance of the class containing this method.

        The method performs the following steps:
        1. Displays a confirmation dialog to the user asking if they are sure about the deletion.
        2. Determines the type of media (movie or series) based on the current tab index.
        3. Collects the IDs of the selected media entries to be deleted.
        4. Attempts to delete each selected media entry using the model.delete_media method.
        5. Updates the UI to reflect the changes by refreshing the display of movies and series.
        6. Writes a status message indicating the number of successfully deleted entries.
        """
        try:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle('Delete Confirmation')
            msg_box.setText('Are you sure you want to delete?')
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg_box.setDefaultButton(QMessageBox.No)
            custom_icon = QPixmap('images/icons/pmm-256.png')
            msg_box.setIconPixmap(custom_icon)
            
            reply = msg_box.exec()

            failed_entries = 0

            if reply == QMessageBox.Yes:
                media_type = MEDIA_TYPE.MOVIE if self.ui.tbSummary.currentIndex() == 0 else MEDIA_TYPE.SERIES
                selected   = self.ui.tblMovies.selectedIndexes() if media_type == MEDIA_TYPE.MOVIE \
                        else self.ui.tblSeries.selectedIndexes()
                to_delete  = set()
                for media in selected:
                    to_delete.add(
                        media.sibling(media.row(), 
                        getColIndexinTableView(self.ui.tblMovies, MEDIA_COLUMNS.ID)).data() )
                    
                for media_id in to_delete:
                    status   = model.delete_media(media_type, media_id)
                    if not status:
                        failed_entries += 1

                self.ui.lblPoster.setPixmap(QPixmap(DEFAULT_POSTER))
                self.current_poster = DEFAULT_POSTER

                self.displayMovies()
                self.displaySeries()

                self.writeStatus(f'{str(len(to_delete) - failed_entries)}/{str(len(to_delete))} deleted successfully...')
        except Exception as e:
            self.writeStatus(f'onDelete: {e}', MESSAGE_TYPE.ERROR)

    
    def resetForm(self) -> None:
        """
        Resets all fields in the user interface form to their default values. This method is typically used to clear
        any existing data from the form, preparing it for new input.

        The method performs the following actions:
        - Clears text fields for audio codec, codec, country, disc count, disc number, episode disc number, episode number,
          episode plot, episode tags, episode size, episode title, episode release date, language, notes, original title,
          plot, release date, runtime, seasons, size, tagline, title, and year.
        - Unchecks checkboxes for episode to burn, watched, watched episode, and watched season.
        - Clears list selections for genres and languages.
        - Resets combo boxes for certification, edition, episode quality, genres, quality, and source to their first item.
        - Clears the season combo box.
        - Sets the rating and user rating spin boxes to 0.00.
        - Sets the models for cast and episodes tables to None, effectively clearing them.
        - Unchecks the apply filter checkbox.
        - Sets the poster label to a default image using a QPixmap.
        """
        try:
            self.ui.txtAudioCodec.setText('')
            self.ui.txtCodec.setText('')
            self.ui.txtCountry.setText('')
            self.ui.txtDiscCount.setText('')
            self.ui.txtDiscNo.setText('')

            self.ui.txtEpisodeDiscNo.setText('')
            self.ui.txtEpisodeNo.setText('')
            self.ui.txtEpisodePlot.setPlainText('')
            self.ui.txtEpisodeTags.setText('')
            self.ui.txtEpisodeSize.setText('')
            self.ui.txtEpisodeTitle.setText('')
            self.ui.txtEpisodeReleased.setText('')

            self.ui.txtLanguage.setText('')
            self.ui.txtNotes.setPlainText('')
            self.ui.txtOriginalTitle.setText('')
            self.ui.txtPlot.setPlainText('')
            self.ui.txtReleaseDate.setText('')
            self.ui.txtRuntime.setText('')
            self.ui.txtSeasons.setText('')
            self.ui.txtSize.setText('')
            self.ui.txtTagLine.setText('')
            self.ui.txtTitle.setText('')
            self.ui.txtYear.setText('')

            self.ui.txtDirector.setText('')
            self.ui.txtWriter.setText('')

            self.ui.chkEpisodeToBurn.setChecked(False)
            self.ui.chkWatched.setChecked(False)
            self.ui.chkWatchedEpisode.setChecked(False)
            self.ui.chkWatchedSeason.setChecked(False)
            self.ui.chkApplyFilter.setChecked(False)

            self.ui.lsGenres.clear()
            self.ui.lsLanguages.clear()

            self.ui.cbCertification.setCurrentIndex(0)
            self.ui.cbEdition.setCurrentIndex(0)
            self.ui.cbEpisodeQuality.setCurrentIndex(0)
            self.ui.cbGenres.setCurrentIndex(0)
            self.ui.cbQuality.setCurrentIndex(0)
            self.ui.cbSeason.clear()
            self.ui.cbSource.setCurrentIndex(0)

            self.ui.dsRating.setValue(0.00)
            self.ui.dsUserRating.setValue(0.00)

            self.ui.tblCast.setModel(None)
            self.ui.tblEpisodes.setModel(None)

            self.ui.lblPoster.setPixmap(QPixmap(DEFAULT_POSTER))
            self.current_poster = DEFAULT_POSTER
        except Exception as e:
            self.writeStatus(f'resetForm: {e}', MESSAGE_TYPE.ERROR)


    def onExportTriggered(self) -> None:
        '''
        Displays the Export Dialog Box
        '''
        widget = ExportDialog(parent=self)
        widget.open()


    def onFAQsTriggered(self) -> None:
        '''
        Displays the FAQs Dialog Box
        '''
        widget = FAQsDialog()
        widget.exec()


    def onFetchDetailsTriggered(self) -> None:
        '''
        Displays the Fetch Details Dialog Box
        '''
        widget = FetchDetailsDialog(parent=self)
        widget.open()


    def onImportTriggered(self) -> None:
        '''
        Displays the Import Dialog Box
        '''
        widget = ImportDialog(parent=self)
        widget.open()


    def onPreferencesTriggered(self) -> None:
        '''
        Displays the Preferences Dialog Box
        '''
        widget = PreferencesDialog(parent=self)
        widget.open()


    def onPublishTriggered(self) -> None:
        '''
        Displays the Publish Dialog Box
        '''
        widget = PublishDialog(parent=self)
        widget.open()


    def getMovieUpdatedDetails(self, movie_id : int) -> dict:
        """
        Retrieves updated movie details from the user interface and returns them as a dictionary.

        Parameters:
        - movie_id (int): The unique identifier for the movie.

        Returns:
        - dict: A dictionary containing the updated movie details.
        """
        movie_details = {}

        try:
            movie_details[MEDIA_COLUMNS.TITLE]           = self.ui.txtTitle.text()
            movie_details[MEDIA_COLUMNS.ORIGINAL_TITLE]  = self.ui.txtOriginalTitle.text()
            movie_details[MEDIA_COLUMNS.YEAR]            = self.ui.txtYear.text()
            movie_details[MOVIE_COLUMNS.RUNTIME]         = self.ui.txtRuntime.text()
            movie_details[MEDIA_COLUMNS.COUNTRY]         = self.ui.txtCountry.text()
            movie_details[MEDIA_COLUMNS.WATCHED]         = 1 if self.ui.chkWatched.isChecked() else 0
            movie_details[MEDIA_COLUMNS.ONLINE_RATING]   = self.ui.dsRating.text()
            movie_details[MEDIA_COLUMNS.RATING]          = self.ui.dsUserRating.text()
            movie_details[MEDIA_COLUMNS.CERTIFICATION]   = self.ui.cbCertification.currentText()
            movie_details[MEDIA_COLUMNS.RELEASE_DATE]    = self.ui.txtReleaseDate.text()
            movie_details[MEDIA_COLUMNS.TAGLINE]         = self.ui.txtTagLine.text()
            movie_details[MEDIA_COLUMNS.PLOT]            = self.ui.txtPlot.toPlainText()
            movie_details[MEDIA_COLUMNS.NOTES]           = self.ui.txtNotes.toPlainText()
            movie_details[MOVIE_COLUMNS.SOURCE_ID]       = self.ui.cbSource.currentData()
            movie_details[MEDIA_COLUMNS.QUALITY_ID]      = self.ui.cbQuality.currentData()
            movie_details[MOVIE_COLUMNS.EDITION_ID]      = self.ui.cbEdition.currentData()
            movie_details[MOVIE_COLUMNS.VIDEO_CODEC]     = self.ui.txtCodec.text()
            movie_details[MOVIE_COLUMNS.AUDIO_CODEC]     = self.ui.txtAudioCodec.text()
            movie_details[MEDIA_COLUMNS.SIZE]            = self.ui.txtSize.text()
            movie_details[MOVIE_COLUMNS.DISC_COUNT]      = self.ui.txtDiscCount.text()
            movie_details[MEDIA_COLUMNS.TO_BURN]         = 1 if self.ui.rbToBurnYes.isChecked() else 0
            movie_details[MEDIA_COLUMNS.BACKUP_DISC]     = self.ui.txtDiscNo.text()
            movie_details[MEDIA_COLUMNS.TAG]             = None
            movie_details[MEDIA_COLUMNS.DIRECTOR]        = self.ui.txtDirector.text()
            movie_details[MEDIA_COLUMNS.WRITER]          = self.ui.txtWriter.text()
            movie_details[MEDIA_COLUMNS.ID]              = movie_id
        except Exception as e:
            self.writeStatus(f'getMovie: {e}', MESSAGE_TYPE.ERROR)

        return movie_details
    

    def getSeriesUpdatedDetails(self, series_id : int) -> dict:
        """
        Retrieves updated details of a series from the user interface and returns them as a dictionary.

        Parameters:
        - series_id (int): The unique identifier for the series.

        Returns:
        - dict: A dictionary containing the latest details of the series from the UI.
        """
        series_details = {}

        try:
            series_details[MEDIA_COLUMNS.TITLE]          = self.ui.txtTitle.text()
            series_details[MEDIA_COLUMNS.ORIGINAL_TITLE] = self.ui.txtOriginalTitle.text()
            series_details[MEDIA_COLUMNS.YEAR]           = self.ui.txtYear.text()
            series_details[SERIES_COLUMNS.SEASONS]       = self.ui.txtSeasons.text()
            series_details[MEDIA_COLUMNS.COUNTRY]        = self.ui.txtCountry.text()
            series_details[MEDIA_COLUMNS.WATCHED]        = 1 if self.ui.chkWatched.isChecked() else 0
            series_details[MEDIA_COLUMNS.ONLINE_RATING]  = self.ui.dsRating.text()
            series_details[MEDIA_COLUMNS.RATING]         = self.ui.dsUserRating.text()
            series_details[MEDIA_COLUMNS.CERTIFICATION]  = self.ui.cbCertification.currentText()
            series_details[MOVIE_COLUMNS.SOURCE_ID]      = self.ui.cbSource.currentData()
            series_details[MEDIA_COLUMNS.RELEASE_DATE]   = self.ui.txtReleaseDate.text()
            series_details[MEDIA_COLUMNS.TAGLINE]        = self.ui.txtTagLine.text()
            series_details[MEDIA_COLUMNS.PLOT]           = self.ui.txtPlot.toPlainText()
            series_details[MEDIA_COLUMNS.NOTES]          = self.ui.txtNotes.toPlainText()
            series_details[MEDIA_COLUMNS.DIRECTOR]       = self.ui.txtDirector.text()
            series_details[MEDIA_COLUMNS.WRITER]         = self.ui.txtWriter.text()
            series_details[MEDIA_COLUMNS.ID]             = series_id
        except Exception as e:
            self.writeStatus(f'getSeries: {e}', MESSAGE_TYPE.ERROR)

        return series_details
    

    def getSeriesEpisodeUpdatedDetails(self, episode_id : int, season : int) -> dict:
        """
        Retrieves and constructs a dictionary containing updated details of a series episode.

        Parameters:
        - episode_id (int): The unique identifier for the episode.
        - season (int): The season number to which the episode belongs.
        
        Returns:
        - dict: A dictionary containing the updated details of the episode.
        """
        series_details = {}

        try:
            series_details[EPISODE_COLUMNS.SEASON]       = int(season)
            series_details[EPISODE_COLUMNS.EPISODE]      = int(self.ui.txtEpisodeNo.text().strip())
            series_details[MEDIA_COLUMNS.TITLE]          = self.ui.txtEpisodeTitle.text().strip()
            series_details[MEDIA_COLUMNS.PLOT]           = self.ui.txtEpisodePlot.toPlainText().strip()
            series_details[EPISODE_COLUMNS.WATCHED]      = 1 if self.ui.chkWatchedEpisode.isChecked() else 0
            series_details[EPISODE_COLUMNS.QUALITY_ID]   = self.ui.cbQuality.currentData()
            series_details[EPISODE_COLUMNS.TO_BURN]      = 1 if self.ui.chkEpisodeToBurn.isChecked() else 0
            series_details[EPISODE_COLUMNS.BACKUP_DISC]  = self.ui.txtEpisodeDiscNo.text().strip()
            series_details[EPISODE_COLUMNS.TAG]          = self.ui.txtEpisodeTags.text().strip()
            series_details[EPISODE_COLUMNS.SIZE]         = self.ui.txtEpisodeSize.text().strip()
            series_details[MEDIA_COLUMNS.RELEASE_DATE]   = self.ui.txtEpisodeReleased.text().strip()
            series_details[EPISODE_COLUMNS.ID]           = episode_id
        except Exception as e:
            self.writeStatus(f'getSeriesEpisode: {e}', MESSAGE_TYPE.ERROR)
        
        return series_details


    def updateMediaTriggered(self) -> None:
        """
        Handles the update of media details when triggered by the user. This function prompts the user for confirmation
        before proceeding with the update. Depending on the selected media type (movie or series), it retrieves the 
        necessary details and updates the media information in the model. After updating, it refreshes the display 
        and writes a status message.
        """
        try:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle('Update Confirmation')
            msg_box.setText('Are you sure you want to update details?')
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg_box.setDefaultButton(QMessageBox.No)
            custom_icon = QPixmap('images/icons/pmm-256.png')
            msg_box.setIconPixmap(custom_icon)
            
            reply = msg_box.exec()

            failed_entries = 0

            if reply == QMessageBox.Yes:
                media_type = MEDIA_TYPE.MOVIE if self.ui.tbSummary.currentIndex() == 0 \
                        else MEDIA_TYPE.SERIES
                index      = self.ui.tblMovies.selectionModel().currentIndex() if media_type == MEDIA_TYPE.MOVIE \
                        else self.ui.tblSeries.selectionModel().currentIndex()
                media_id   = index.sibling(
                                index.row(), 
                                getColIndexinTableView(
                                    self.ui.tblMovies if media_type == MEDIA_TYPE.MOVIE else self.ui.tblSeries, 
                                    MEDIA_COLUMNS.ID)).data()
                
                if media_type == MEDIA_TYPE.MOVIE:
                    model.update_movie(
                        movie_details  = self.getMovieUpdatedDetails(media_id),
                        lookup_details = [],
                        genres         = [self.ui.lsGenres.item(row).text() for row in range(self.ui.lsGenres.count())],
                        languages      = [self.ui.lsLanguages.item(row).text() for row in range(self.ui.lsLanguages.count())] )
                    self.displayMovies()
                else:
                    index      = self.ui.tblEpisodes.currentIndex()
                    season     = index.sibling(index.row(), 
                                               getColIndexinTableView(self.ui.tblEpisodes, EPISODE_COLUMNS.SEASON)).data()
                    episode_id = index.sibling(index.row(), 
                                               getColIndexinTableView(self.ui.tblEpisodes, MEDIA_COLUMNS.ID)).data()

                    model.update_series(
                        series_details  = self.getSeriesUpdatedDetails(media_id),
                        lookup_details  = [],
                        episode_details = self.getSeriesEpisodeUpdatedDetails(episode_id, season) if index.row() > -1 else None,
                        genres          = [self.ui.lsGenres.item(row).text() for row in range(self.ui.lsGenres.count())],
                        languages       = [self.ui.lsLanguages.item(row).text() for row in range(self.ui.lsLanguages.count())])
                    self.displaySeries()

                self.writeStatus('Details updated successfully...')
        except Exception as e:
            self.writeStatus(f'updateMedia: {e}', MESSAGE_TYPE.ERROR)

    
    def addGenre(self) -> None:
        """
        Adds a new genre to the list of existing genres if it is not already present.

        This method retrieves the current list of genres from a UI component, checks if the 
        selected genre from a combo box is already in the list, and if not, adds it to the list. 
        The list is then sorted and updated in the UI.
        """
        try:
            existing_genres = [self.ui.lsGenres.item(row).text() for row in range(self.ui.lsGenres.count())]
            if self.ui.cbGenres.currentText() not in existing_genres:
                existing_genres.append(self.ui.cbGenres.currentText())

                self.ui.lsGenres.clear()
                self.ui.lsGenres.addItems(sorted(existing_genres))
        except Exception as e:
            self.writeStatus(f'addGenre: {e}', MESSAGE_TYPE.ERROR)


    def removeGenre(self) -> None:
        """
        Remove a Genre entry from the Genre List View
        """
        try:
            if self.ui.lsGenres.currentRow() > -1:
                self.ui.lsGenres.takeItem(self.ui.lsGenres.currentRow())
        except Exception as e:
            self.writeStatus(f'removeGenre: {e}', MESSAGE_TYPE.ERROR)


    def addLanguage(self) -> None:
        """
        Adds a new language to the list of existing languages in the UI if it is not already present.

        This method retrieves the current list of languages from a UI component, checks if the language
        selected in a combo box is not already in the list, and if not, adds the language from a text
        input field to the list. The list is then sorted and updated in the UI.
        """
        try:
            existing_languages = [self.ui.lsLanguages.item(row).text() for row in range(self.ui.lsLanguages.count())]
            if self.ui.cbGenres.currentText().strip() not in existing_languages:
                existing_languages.append(self.ui.txtLanguage.text().strip())

                self.ui.lsLanguages.clear()
                self.ui.lsLanguages.addItems(sorted(existing_languages))

            self.ui.txtLanguage.setText('')
        except Exception as e:
            self.writeStatus(f'addLanguage: {e}', MESSAGE_TYPE.ERROR)

    
    def removeLanguage(self) -> None:
        """
        Remove a Genre entry from the Genre List View
        """
        try:
            if self.ui.lsLanguages.currentRow() > -1:
                self.ui.lsLanguages.takeItem(self.ui.lsLanguages.currentRow())
        except Exception as e:
            self.writeStatus(f'removeLanguage: {e}', MESSAGE_TYPE.ERROR)


    def onAddNewEpisodeTriggered(self) -> None:
        """
        Displays the Add New Episode Dialog Box
        """
        widget = AddNewEpiodeDialog(parent=self)
        widget.open()


    def onDeleteEpisodeTriggered(self) -> None:
        """
        Handles the event triggered when the user attempts to delete selected episodes from the UI.

        This function prompts the user with a confirmation dialog to ensure they want to proceed with
        deleting the selected episodes. If the user confirms, it collects the IDs of the selected episodes
        and attempts to delete them using the model's `delete_series_episodes` method. It updates the UI
        based on the success or failure of the deletion operation.
        """
        try:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle('Delete Confirmation')
            msg_box.setText('Are you sure you want to delete?')
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg_box.setDefaultButton(QMessageBox.No)
            custom_icon = QPixmap('images/icons/pmm-256.png')
            msg_box.setIconPixmap(custom_icon)
            
            reply = msg_box.exec()
            
            if reply == QMessageBox.Yes:
                episode_ids = set()
                for selected in self.ui.tblEpisodes.selectedIndexes():
                    episode_ids.add(
                        selected.sibling(selected.row(), 
                        getColIndexinTableView(self.ui.tblEpisodes, MEDIA_COLUMNS.ID)).data() )
                    
                if len(episode_ids) > 0:
                    result = model.delete_series_episodes(episode_ids=episode_ids)
                    if result:
                        self.displaySeriesDetails()
                    else:
                        self.writeStatus('There was an error deleting episodes', MESSAGE_TYPE.ERROR)
                else:
                    self.writeStatus('No episode(s) selected!', MESSAGE_TYPE.WARNING)
        except Exception as e:
            self.writeStatus(f'onDeleteEpisode: {e}', MESSAGE_TYPE.ERROR)


    def onWatchedEpisodeTriggered(self, value=1) -> None:
        """
        Sets the selected episode(s) as watched or not watched based on the value parameter.

        Parameters:
            value (int): 1 for watched, 0 for not watched. Defaults to 1.
        """
        try:
            curr_idx = self.ui.tblEpisodes.selectionModel().currentIndex().row() \
                    if self.ui.tblEpisodes.selectionModel() and self.ui.tblEpisodes.selectionModel().currentIndex() \
                  else 0

            episode_ids = set()
            for selected in self.ui.tblEpisodes.selectedIndexes():
                episode_ids.add(
                    selected.sibling(
                        selected.row(), 
                        getColIndexinTableView(self.ui.tblEpisodes, MEDIA_COLUMNS.ID)
                    ).data()
                )
                
            if len(episode_ids) > 0:
                for episode in episode_ids:
                    model.update_episode(episode_details={
                        MEDIA_COLUMNS.ID      : episode,
                        MEDIA_COLUMNS.WATCHED : value
                    })

                self.displaySeriesDetails()
                if self.ui.chkWatchedSeason.isChecked():
                    index    = self.ui.tblSeries.selectionModel().currentIndex()
                    media_id = index.sibling(index.row(), 
                                             getColIndexinTableView(self.ui.tblSeries, MEDIA_COLUMNS.ID)).data()
                    model.update_series(
                        series_details  = {
                            MEDIA_COLUMNS.ID      : media_id,
                            MEDIA_COLUMNS.WATCHED : 1
                        },
                        lookup_details  = None,
                        episode_details = None,
                        genres          = None,
                        languages       = None)
                    self.displaySeries()

                self.ui.tblEpisodes.selectRow(curr_idx)
                self.ui.tblEpisodes.setFocus()
            else:   
                self.writeStatus('No episode(s) selected!', MESSAGE_TYPE.WARNING)
        except Exception as e:
            self.writeStatus(f'onWatchedEpisode: {e}', MESSAGE_TYPE.ERROR)


    def onNotWatchedEpisodeTriggered(self) -> None:
        '''
        Sets the selected episode(s) as not watched
        '''
        self.onWatchedEpisodeTriggered(0)


    def onPosterClickTriggered(self, event) -> None:
        '''
        Opens a popup window to display the full-size poster image when clicked.
        '''
        popup = ImagePopup(self.current_poster, self)
        popup.show()


    def changePoster(self) -> None:
        '''
        Changes the poster image for the current series or movie.
        '''
        try:
            filename, _ = QFileDialog.getOpenFileName(
                                self, 
                                "Select Poster", 
                                "", 
                                "Image Files (*.jpg *.bmp *.png)", 
                                options=QFileDialog.Option.DontUseNativeDialog )
            
            if filename:
                import shutil
                import os
                
                destination = os.path.join(os.path.dirname(self.current_poster), os.path.basename(filename))
                shutil.copy2(filename, destination)
                
                self.current_poster = destination
                self.ui.lblPoster.setPixmap(QPixmap(self.current_poster))
                
                self.writeStatus('Poster changed successfully...')
        except Exception as e:
            self.writeStatus(f'changePoster: {e}', MESSAGE_TYPE.ERROR)


    def removePoster(self) -> None:
        '''
        Removes the current poster image for the series or movie.
        '''
        try:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle('Delete Confirmation')
            msg_box.setText('Are you sure you want to delete the poster?')
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg_box.setDefaultButton(QMessageBox.No)
            custom_icon = QPixmap('images/icons/pmm-256.png')
            msg_box.setIconPixmap(custom_icon)
            
            reply = msg_box.exec()

            if reply == QMessageBox.Yes:
                import os
                os.remove(self.current_poster)

                self.current_poster = DEFAULT_POSTER
                self.ui.lblPoster.setPixmap(QPixmap(self.current_poster))

                self.writeStatus('Poster deleted successfully...')
        except Exception as e:
            self.writeStatus(f'removePoster: {e}', MESSAGE_TYPE.ERROR)


    def onMoreFiltersTriggered(self) -> None:
        '''
        Opens a popup window to display the popup with additional filters when clicked.
        '''
        widget = FiltersDialog(parent=self)
        widget.open()


    def onBackupTriggered(self) -> None:
        '''
        Opens a popup window to backup the db to local file system.
        '''
        widget = BackupDialog(parent=self)
        widget.open()


    def onRestoreTriggered(self) -> None:
        '''
        Opens a popup window to restore the db to local file system.
        '''
        widget = BackupDialog(parent=self, mode='restore')
        widget.open()


#=======================================================================