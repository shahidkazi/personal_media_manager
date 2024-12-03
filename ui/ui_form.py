#=======================================================================
# Description:
# UI component declaration for the Application Main Window
#=======================================================================
from PySide6.QtCore    import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui     import QAction, QIcon
from PySide6.QtWidgets import (
    QAbstractItemView, 
    QCheckBox, 
    QComboBox,
    QDoubleSpinBox, 
    QFormLayout, 
    QFrame, 
    QGridLayout,
    QGroupBox, 
    QHBoxLayout, 
    QLabel,
    QLayout, 
    QLineEdit, 
    QListWidget, 
    QMenu, 
    QMenuBar, 
    QPlainTextEdit,
    QRadioButton, 
    QSizePolicy, 
    QStatusBar, 
    QTabWidget,
    QTableView, 
    QToolBar, 
    QToolButton, 
    QVBoxLayout,
    QWidget
)

#=======================================================================
class Ui_MainWindow(object):
    '''
    UI component declaration for the Application Main Window

    This class represents the main window of the application, containing various UI elements and layouts.
    '''

    def setupUi(self, MainWindow) -> None:
        """
		Sets up the user interface for the given MainWindow. This method initializes various UI components,
		including actions, widgets, layouts, and menus, and configures their properties such as size, icons,
		and behavior.

		Parameters:
		- MainWindow: The main window object (QMainWindow) where the UI components will be set up
		"""
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1269, 1232)
        
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(100, 0))
        MainWindow.setBaseSize(QSize(48, 64))
        
        icon = QIcon()
        icon.addFile(u"images/icons/pmm.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(False)
        
        self.actionAddNew = QAction(MainWindow)
        self.actionAddNew.setObjectName(u"actionAddNew")
        self.actionAddNew.setEnabled(True)
        icon1 = QIcon()
        icon1.addFile(u"images/icons/circle-plus-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionAddNew.setIcon(icon1)
        self.actionAddNew.setMenuRole(QAction.MenuRole.TextHeuristicRole)
        self.actionAddNew.setIconVisibleInMenu(True)
        self.actionAddNew.setShortcutVisibleInContextMenu(True)
        
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        icon2 = QIcon()
        icon2.addFile(u"images/icons/sliders-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionPreferences.setIcon(icon2)
        self.actionPreferences.setMenuRole(QAction.MenuRole.PreferencesRole)
        self.actionPreferences.setIconVisibleInMenu(True)
        self.actionPreferences.setShortcutVisibleInContextMenu(True)
        
        self.actionImportData = QAction(MainWindow)
        self.actionImportData.setObjectName(u"actionImportData")
        icon3 = QIcon()
        icon3.addFile(u"images/icons/circle-arrow-down-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionImportData.setIcon(icon3)
        self.actionImportData.setIconVisibleInMenu(True)
        self.actionImportData.setShortcutVisibleInContextMenu(True)
        
        self.actionExportData = QAction(MainWindow)
        self.actionExportData.setObjectName(u"actionExportData")
        icon4 = QIcon()
        icon4.addFile(u"images/icons/circle-arrow-up-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionExportData.setIcon(icon4)
        self.actionExportData.setIconVisibleInMenu(True)
        self.actionExportData.setShortcutVisibleInContextMenu(True)

        self.actionBackup = QAction(MainWindow)
        self.actionBackup.setObjectName(u"actionBackup")
        iconb = QIcon()
        iconb.addFile(u"images/icons/upload-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionBackup.setIcon(iconb)
        self.actionBackup.setIconVisibleInMenu(True)
        self.actionBackup.setShortcutVisibleInContextMenu(True)
        
        self.actionRestore = QAction(MainWindow)
        self.actionRestore.setObjectName(u"actionRestore")
        iconr = QIcon()
        iconr.addFile(u"images/icons/download-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionRestore.setIcon(iconr)
        self.actionRestore.setIconVisibleInMenu(True)
        self.actionRestore.setShortcutVisibleInContextMenu(True)
        
        self.actionPublish = QAction(MainWindow)
        self.actionPublish.setObjectName(u"actionPublish")
        icon5 = QIcon()
        icon5.addFile(u"images/icons/google-brands-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionPublish.setIcon(icon5)
        self.actionPublish.setIconVisibleInMenu(True)
        self.actionPublish.setShortcutVisibleInContextMenu(True)
        
        self.actionFAQs = QAction(MainWindow)
        self.actionFAQs.setObjectName(u"actionFAQs")
        icon7 = QIcon()
        icon7.addFile(u"images/icons/circle-question-regular.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionFAQs.setIcon(icon7)
        self.actionFAQs.setIconVisibleInMenu(True)
        self.actionFAQs.setShortcutVisibleInContextMenu(True)
        
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon8 = QIcon()
        icon8.addFile(u"images/icons/circle-info-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionAbout.setIcon(icon8)
        self.actionAbout.setMenuRole(QAction.MenuRole.TextHeuristicRole)
        self.actionAbout.setIconVisibleInMenu(True)
        self.actionAbout.setShortcutVisibleInContextMenu(True)
        
        self.actionUpdate = QAction(MainWindow)
        self.actionUpdate.setObjectName(u"actionUpdate")
        icon9 = QIcon()
        icon9.addFile(u"images/icons/pen-to-square-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionUpdate.setIcon(icon9)
        self.actionUpdate.setIconVisibleInMenu(True)
        self.actionUpdate.setShortcutVisibleInContextMenu(True)
        
        self.actionDelete = QAction(MainWindow)
        self.actionDelete.setObjectName(u"actionDelete")
        icon10 = QIcon()
        icon10.addFile(u"images/icons/trash-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionDelete.setIcon(icon10)
        self.actionDelete.setIconVisibleInMenu(True)
        self.actionDelete.setShortcutVisibleInContextMenu(True)
        
        self.actionBulkUpdate = QAction(MainWindow)
        self.actionBulkUpdate.setObjectName(u"actionBulkUpdate")
        icon11 = QIcon()
        icon11.addFile(u"images/icons/layer-group-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionBulkUpdate.setIcon(icon11)
        self.actionBulkUpdate.setIconVisibleInMenu(True)
        self.actionBulkUpdate.setShortcutVisibleInContextMenu(True)
        
        self.actionFetchDetails = QAction(MainWindow)
        self.actionFetchDetails.setObjectName(u"actionFetchDetails")
        icon12 = QIcon()
        icon12.addFile(u"images/icons/imdb-brands-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionFetchDetails.setIcon(icon12)
        self.actionFetchDetails.setIconVisibleInMenu(True)
        self.actionFetchDetails.setShortcutVisibleInContextMenu(True)
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        
        self.tbSummary = QTabWidget(self.groupBox_2)
        self.tbSummary.setObjectName(u"tbSummary")

        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        
        self.horizontalLayout_18 = QHBoxLayout(self.tab)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        
        self.tblMovies = QTableView(self.tab)
        self.tblMovies.setObjectName(u"tblMovies")
        self.tblMovies.setAlternatingRowColors(True)
        self.tblMovies.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblMovies.horizontalHeader().setStretchLastSection(False)
        self.tblMovies.verticalHeader().setVisible(False)

        self.horizontalLayout_18.addWidget(self.tblMovies)
        icon = QIcon('images/icons/film-solid.svg')
        self.tbSummary.addTab(self.tab, icon, "")
        
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        
        self.horizontalLayout_7 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        
        self.tblSeries = QTableView(self.tab_2)
        self.tblSeries.setObjectName(u"tblSeries")
        self.tblSeries.setAlternatingRowColors(True)
        self.tblSeries.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblSeries.horizontalHeader().setStretchLastSection(False)
        self.tblSeries.verticalHeader().setVisible(False)

        self.horizontalLayout_7.addWidget(self.tblSeries)
        icon = QIcon('images/icons/tv-solid.svg')
        self.tbSummary.addTab(self.tab_2, icon, "")
        self.verticalLayout_14.addWidget(self.tbSummary)
        self.gridLayout.addLayout(self.verticalLayout_14, 5, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.chkApplyFilter = QCheckBox(self.groupBox_2)
        self.chkApplyFilter.setObjectName(u"chkApplyFilter")
        self.horizontalLayout_4.addWidget(self.chkApplyFilter)

        self.cbFilterWatched = QComboBox(self.groupBox_2)
        self.cbFilterWatched.addItem("")
        self.cbFilterWatched.addItem("")
        self.cbFilterWatched.addItem("")
        self.cbFilterWatched.setObjectName(u"cbFilterWatched")
        self.cbFilterWatched.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cbFilterWatched.sizePolicy().hasHeightForWidth())
        self.cbFilterWatched.setSizePolicy(sizePolicy2)
        self.horizontalLayout_4.addWidget(self.cbFilterWatched)

        self.cbFilterQuality = QComboBox(self.groupBox_2)
        self.cbFilterQuality.addItem("")
        self.cbFilterQuality.setObjectName(u"cbFilterQuality")
        self.cbFilterQuality.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.cbFilterQuality.sizePolicy().hasHeightForWidth())
        self.cbFilterQuality.setSizePolicy(sizePolicy2)
        self.horizontalLayout_4.addWidget(self.cbFilterQuality)

        self.cbFilterGenres = QComboBox(self.groupBox_2)
        self.cbFilterGenres.addItem("")
        self.cbFilterGenres.setObjectName(u"cbFilterGenres")
        self.cbFilterGenres.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.cbFilterGenres.sizePolicy().hasHeightForWidth())
        self.cbFilterGenres.setSizePolicy(sizePolicy2)
        self.cbFilterGenres.setEditable(False)
        self.horizontalLayout_4.addWidget(self.cbFilterGenres)

        self.cbFilterDiscNo = QComboBox(self.groupBox_2)
        self.cbFilterDiscNo.addItem("")
        self.cbFilterDiscNo.setObjectName(u"cbFilterDiscNo")
        self.cbFilterDiscNo.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.cbFilterDiscNo.sizePolicy().hasHeightForWidth())
        self.cbFilterDiscNo.setSizePolicy(sizePolicy2)
        self.horizontalLayout_4.addWidget(self.cbFilterDiscNo)

        self.btnMoreFilters = QToolButton(self.groupBox_2)
        self.btnMoreFilters.setObjectName(u"btnMoreFilters")
        self.btnMoreFilters.setEnabled(False)
        icon13 = QIcon()
        icon13.addFile(u"images/icons/magnifying-glass-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnMoreFilters.setIcon(icon13)
        self.horizontalLayout_4.addWidget(self.btnMoreFilters)
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 0, -1, -1)
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.horizontalLayout_20.addWidget(self.label)

        self.txtFilterTitle = QLineEdit(self.groupBox_2)
        self.txtFilterTitle.setObjectName(u"txtFilterTitle")
        self.horizontalLayout_20.addWidget(self.txtFilterTitle)
        self.gridLayout.addLayout(self.horizontalLayout_20, 0, 0, 1, 1)

        self.horizontalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy3)
        
        self.verticalLayout_6 = QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        
        self.tabWidget = QTabWidget(self.groupBox)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy4)
        
        self.tabGeneral = QWidget()
        self.tabGeneral.setObjectName(u"tabGeneral")
        
        self.gridLayout_6 = QGridLayout(self.tabGeneral)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_11.addLayout(self.verticalLayout_10)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, -1, -1, -1)

        self.lblPoster = QLabel(self.tabGeneral)
        self.lblPoster.setObjectName(u"lblPoster")
        self.lblPoster.setMinimumSize(QSize(128, 192))
        self.lblPoster.setMaximumSize(QSize(128, 192))
        self.verticalLayout_5.addWidget(self.lblPoster)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")

        self.btnAddPoster = QToolButton(self.tabGeneral)
        self.btnAddPoster.setObjectName(u"btnAddPoster")
        sizePolicy2.setHeightForWidth(self.btnAddPoster.sizePolicy().hasHeightForWidth())
        self.btnAddPoster.setSizePolicy(sizePolicy2)
        self.btnAddPoster.setIcon(icon1)
        self.horizontalLayout_8.addWidget(self.btnAddPoster)

        self.btnRemovePoster = QToolButton(self.tabGeneral)
        self.btnRemovePoster.setObjectName(u"btnRemovePoster")
        sizePolicy2.setHeightForWidth(self.btnRemovePoster.sizePolicy().hasHeightForWidth())
        self.btnRemovePoster.setSizePolicy(sizePolicy2)
        self.btnRemovePoster.setIcon(icon10)
        self.horizontalLayout_8.addWidget(self.btnRemovePoster)

        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_11.addLayout(self.verticalLayout_5)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        
        self.titleLabel = QLabel(self.tabGeneral)
        self.titleLabel.setObjectName(u"titleLabel")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.titleLabel)

        self.txtTitle = QLineEdit(self.tabGeneral)
        self.txtTitle.setObjectName(u"txtTitle")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.txtTitle)

        self.originalTitleLabel = QLabel(self.tabGeneral)
        self.originalTitleLabel.setObjectName(u"originalTitleLabel")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.originalTitleLabel)

        self.txtOriginalTitle = QLineEdit(self.tabGeneral)
        self.txtOriginalTitle.setObjectName(u"txtOriginalTitle")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.txtOriginalTitle)

        self.yearLabel = QLabel(self.tabGeneral)
        self.yearLabel.setObjectName(u"yearLabel")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.yearLabel)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, -1, -1, -1)
        self.txtYear = QLineEdit(self.tabGeneral)
        self.txtYear.setObjectName(u"txtYear")
        self.horizontalLayout_12.addWidget(self.txtYear)

        self.lblRuntime = QLabel(self.tabGeneral)
        self.lblRuntime.setObjectName(u"lblRuntime")
        self.horizontalLayout_12.addWidget(self.lblRuntime)

        self.txtRuntime = QLineEdit(self.tabGeneral)
        self.txtRuntime.setObjectName(u"txtRuntime")
        self.horizontalLayout_12.addWidget(self.txtRuntime)

        self.lblSeasons = QLabel(self.tabGeneral)
        self.lblSeasons.setObjectName(u"lblSeasons")
        self.horizontalLayout_12.addWidget(self.lblSeasons)

        self.txtSeasons = QLineEdit(self.tabGeneral)
        self.txtSeasons.setObjectName(u"txtSeasons")
        self.horizontalLayout_12.addWidget(self.txtSeasons)
        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_12)

        self.ratingLabel = QLabel(self.tabGeneral)
        self.ratingLabel.setObjectName(u"ratingLabel")
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.ratingLabel)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, -1, -1, -1)
        self.dsRating = QDoubleSpinBox(self.tabGeneral)
        self.dsRating.setObjectName(u"dsRating")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.dsRating.sizePolicy().hasHeightForWidth())
        self.dsRating.setSizePolicy(sizePolicy5)
        self.horizontalLayout_16.addWidget(self.dsRating)

        self.label_6 = QLabel(self.tabGeneral)
        self.label_6.setObjectName(u"label_6")
        self.horizontalLayout_16.addWidget(self.label_6)

        self.dsUserRating = QDoubleSpinBox(self.tabGeneral)
        self.dsUserRating.setObjectName(u"dsUserRating")
        sizePolicy5.setHeightForWidth(self.dsUserRating.sizePolicy().hasHeightForWidth())
        self.dsUserRating.setSizePolicy(sizePolicy5)
        self.horizontalLayout_16.addWidget(self.dsUserRating)
        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout_16)

        self.tagsLabel = QLabel(self.tabGeneral)
        self.tagsLabel.setObjectName(u"tagsLabel")
        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.tagsLabel)

        self.sourceLabel = QLabel(self.tabGeneral)
        self.sourceLabel.setObjectName(u"sourceLabel")
        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.sourceLabel)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.txtCountry = QLineEdit(self.tabGeneral)
        self.txtCountry.setObjectName(u"txtCountry")
        self.horizontalLayout_5.addWidget(self.txtCountry)
        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, -1, -1)

        self.cbCertification = QComboBox(self.tabGeneral)
        self.cbCertification.addItem("")
        self.cbCertification.addItem("")
        self.cbCertification.addItem("")
        self.cbCertification.addItem("")
        self.cbCertification.addItem("")
        self.cbCertification.addItem("")
        self.cbCertification.addItem("")
        self.cbCertification.addItem("")
        self.cbCertification.addItem("")
        self.cbCertification.addItem("")
        self.cbCertification.addItem("")
        self.cbCertification.addItem("")
        self.cbCertification.addItem("")
        self.cbCertification.addItem("")
        self.cbCertification.addItem("")
        self.cbCertification.setObjectName(u"cbCertification")
        sizePolicy5.setHeightForWidth(self.cbCertification.sizePolicy().hasHeightForWidth())
        self.cbCertification.setSizePolicy(sizePolicy5)
        self.horizontalLayout_6.addWidget(self.cbCertification)

        self.label_12 = QLabel(self.tabGeneral)
        self.label_12.setObjectName(u"label_12")
        self.horizontalLayout_6.addWidget(self.label_12)

        self.txtReleaseDate = QLineEdit(self.tabGeneral)
        self.txtReleaseDate.setObjectName(u"txtReleaseDate")
        self.horizontalLayout_6.addWidget(self.txtReleaseDate)
        self.formLayout.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout_6)

        self.sourceLabel_2 = QLabel(self.tabGeneral)
        self.sourceLabel_2.setObjectName(u"sourceLabel_2")
        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.sourceLabel_2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, -1, -1, -1)
        self.cbSource = QComboBox(self.tabGeneral)
        self.cbSource.setObjectName(u"cbSource")
        sizePolicy5.setHeightForWidth(self.cbSource.sizePolicy().hasHeightForWidth())
        self.cbSource.setSizePolicy(sizePolicy5)
        self.horizontalLayout_9.addWidget(self.cbSource)

        self.chkWatched = QCheckBox(self.tabGeneral)
        self.chkWatched.setObjectName(u"chkWatched")
        self.horizontalLayout_9.addWidget(self.chkWatched)
        self.formLayout.setLayout(6, QFormLayout.FieldRole, self.horizontalLayout_9)

        self.horizontalLayout_11.addLayout(self.formLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")

        self.label_2 = QLabel(self.tabGeneral)
        self.label_2.setObjectName(u"label_2")
        self.verticalLayout_12.addWidget(self.label_2)

        self.lsGenres = QListWidget(self.tabGeneral)
        self.lsGenres.setObjectName(u"lsGenres")
        self.verticalLayout_12.addWidget(self.lsGenres)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        
        self.cbGenres = QComboBox(self.tabGeneral)
        self.cbGenres.setObjectName(u"cbGenres")
        self.horizontalLayout_14.addWidget(self.cbGenres)

        self.btnAddGenre = QToolButton(self.tabGeneral)
        self.btnAddGenre.setObjectName(u"btnAddGenre")
        self.btnAddGenre.setIcon(icon1)
        self.horizontalLayout_14.addWidget(self.btnAddGenre)

        self.btnRemoveGenre = QToolButton(self.tabGeneral)
        self.btnRemoveGenre.setObjectName(u"btnRemoveGenre")
        self.btnRemoveGenre.setIcon(icon10)
        self.horizontalLayout_14.addWidget(self.btnRemoveGenre)
        self.verticalLayout_12.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_10.addLayout(self.verticalLayout_12)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_5 = QLabel(self.tabGeneral)
        self.label_5.setObjectName(u"label_5")
        self.verticalLayout_11.addWidget(self.label_5)

        self.lsLanguages = QListWidget(self.tabGeneral)
        self.lsLanguages.setObjectName(u"lsLanguages")
        self.verticalLayout_11.addWidget(self.lsLanguages)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.txtLanguage = QLineEdit(self.tabGeneral)
        self.txtLanguage.setObjectName(u"txtLanguage")
        self.horizontalLayout_15.addWidget(self.txtLanguage)

        self.btnAddLanguage = QToolButton(self.tabGeneral)
        self.btnAddLanguage.setObjectName(u"btnAddLanguage")
        self.btnAddLanguage.setIcon(icon1)
        self.horizontalLayout_15.addWidget(self.btnAddLanguage)

        self.btnRemoveLanguage = QToolButton(self.tabGeneral)
        self.btnRemoveLanguage.setObjectName(u"btnRemoveLanguage")
        self.btnRemoveLanguage.setIcon(icon10)
        self.horizontalLayout_15.addWidget(self.btnRemoveLanguage)

        self.verticalLayout_11.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_10.addLayout(self.verticalLayout_11)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_11 = QLabel(self.tabGeneral)
        self.label_11.setObjectName(u"label_11")
        self.verticalLayout_9.addWidget(self.label_11)

        self.txtTagLine = QLineEdit(self.tabGeneral)
        self.txtTagLine.setObjectName(u"txtTagLine")
        self.verticalLayout_9.addWidget(self.txtTagLine)

        self.label_3 = QLabel(self.tabGeneral)
        self.label_3.setObjectName(u"label_3")
        self.verticalLayout_9.addWidget(self.label_3)

        self.txtPlot = QPlainTextEdit(self.tabGeneral)
        self.txtPlot.setObjectName(u"txtPlot")
        self.verticalLayout_9.addWidget(self.txtPlot)
        self.verticalLayout_4.addLayout(self.verticalLayout_9)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_4 = QLabel(self.tabGeneral)
        self.label_4.setObjectName(u"label_4")
        self.verticalLayout_7.addWidget(self.label_4)

        self.txtNotes = QPlainTextEdit(self.tabGeneral)
        self.txtNotes.setObjectName(u"txtNotes")
        self.verticalLayout_7.addWidget(self.txtNotes)
        self.verticalLayout_4.addLayout(self.verticalLayout_7)

        self.gridLayout_6.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        icon = QIcon('images/icons/rectangle-list-regular.svg')
        self.tabWidget.addTab(self.tabGeneral, icon, "")

        self.tabMedia = QWidget()
        self.tabMedia.setObjectName(u"tabMedia")
        
        self.gridLayout_7 = QGridLayout(self.tabMedia)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        
        self.groupBox_3 = QGroupBox(self.tabMedia)
        self.groupBox_3.setObjectName(u"groupBox_3")
        
        self.horizontalLayout_19 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.formLayout_2.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        
        self.editionLabel = QLabel(self.groupBox_3)
        self.editionLabel.setObjectName(u"editionLabel")
        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.editionLabel)

        self.codeLabel = QLabel(self.groupBox_3)
        self.codeLabel.setObjectName(u"codeLabel")
        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.codeLabel)

        self.toBackupBurnLabel = QLabel(self.groupBox_3)
        self.toBackupBurnLabel.setObjectName(u"toBackupBurnLabel")
        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.toBackupBurnLabel)

        self.txtCodec = QLineEdit(self.groupBox_3)
        self.txtCodec.setObjectName(u"txtCodec")
        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.txtCodec)

        self.cbEdition = QComboBox(self.groupBox_3)
        self.cbEdition.setObjectName(u"cbEdition")
        sizePolicy5.setHeightForWidth(self.cbEdition.sizePolicy().hasHeightForWidth())
        self.cbEdition.setSizePolicy(sizePolicy5)
        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.cbEdition)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, -1, -1, -1)
        self.rbToBurnYes = QRadioButton(self.groupBox_3)
        self.rbToBurnYes.setObjectName(u"rbToBurnYes")
        self.horizontalLayout_23.addWidget(self.rbToBurnYes)

        self.rbToBurnNo = QRadioButton(self.groupBox_3)
        self.rbToBurnNo.setObjectName(u"rbToBurnNo")
        self.rbToBurnNo.setChecked(True)
        self.horizontalLayout_23.addWidget(self.rbToBurnNo)
        self.formLayout_2.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout_23)

        self.discCountLabel = QLabel(self.groupBox_3)
        self.discCountLabel.setObjectName(u"discCountLabel")
        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.discCountLabel)

        self.txtDiscCount = QLineEdit(self.groupBox_3)
        self.txtDiscCount.setObjectName(u"txtDiscCount")
        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.txtDiscCount)
        self.horizontalLayout_19.addLayout(self.formLayout_2)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.formLayout_3.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        
        self.qualityLabel = QLabel(self.groupBox_3)
        self.qualityLabel.setObjectName(u"qualityLabel")
        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.qualityLabel)

        self.cbQuality = QComboBox(self.groupBox_3)
        self.cbQuality.setObjectName(u"cbQuality")
        sizePolicy5.setHeightForWidth(self.cbQuality.sizePolicy().hasHeightForWidth())
        self.cbQuality.setSizePolicy(sizePolicy5)
        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.cbQuality)

        self.sizeLabel = QLabel(self.groupBox_3)
        self.sizeLabel.setObjectName(u"sizeLabel")
        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.sizeLabel)

        self.discLabel = QLabel(self.groupBox_3)
        self.discLabel.setObjectName(u"discLabel")
        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.discLabel)

        self.txtDiscNo = QLineEdit(self.groupBox_3)
        self.txtDiscNo.setObjectName(u"txtDiscNo")
        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.txtDiscNo)

        self.audioCodecLabel = QLabel(self.groupBox_3)
        self.audioCodecLabel.setObjectName(u"audioCodecLabel")
        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.audioCodecLabel)

        self.txtAudioCodec = QLineEdit(self.groupBox_3)
        self.txtAudioCodec.setObjectName(u"txtAudioCodec")
        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.txtAudioCodec)

        self.txtSize = QLineEdit(self.groupBox_3)
        self.txtSize.setObjectName(u"txtSize")
        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.txtSize)

        self.horizontalLayout_19.addLayout(self.formLayout_3)
        self.horizontalLayout_17.addWidget(self.groupBox_3)
        self.verticalLayout_13.addLayout(self.horizontalLayout_17)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_9 = QLabel(self.tabMedia)
        self.label_9.setObjectName(u"label_9")
        self.verticalLayout_15.addWidget(self.label_9)

        self.tblOtherMedia = QTableView(self.tabMedia)
        self.tblOtherMedia.setObjectName(u"tblOtherMedia")
        self.tblOtherMedia.setWordWrap(False)
        self.tblOtherMedia.horizontalHeader().setStretchLastSection(True)
        self.tblOtherMedia.verticalHeader().setHighlightSections(False)
        self.verticalLayout_15.addWidget(self.tblOtherMedia)
        self.verticalLayout_13.addLayout(self.verticalLayout_15)

        self.gridLayout_7.addLayout(self.verticalLayout_13, 0, 0, 1, 1)
        icon = QIcon('images/icons/compact-disc-solid.svg')
        self.tabWidget.addTab(self.tabMedia, icon, "")

        self.tabEpisodes = QWidget()
        self.tabEpisodes.setObjectName(u"tabEpisodes")

        self.verticalLayout_19 = QVBoxLayout(self.tabEpisodes)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        
        self.groupBox_4 = QGroupBox(self.tabEpisodes)
        self.groupBox_4.setObjectName(u"groupBox_4")
        
        self.verticalLayout_21 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.formLayout_4.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        
        self.seasonLabel = QLabel(self.groupBox_4)
        self.seasonLabel.setObjectName(u"seasonLabel")
        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.seasonLabel)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")

        self.cbSeason = QComboBox(self.groupBox_4)
        self.cbSeason.setObjectName(u"cbSeason")
        sizePolicy5.setHeightForWidth(self.cbSeason.sizePolicy().hasHeightForWidth())
        self.cbSeason.setSizePolicy(sizePolicy5)
        self.horizontalLayout_27.addWidget(self.cbSeason)

        self.chkWatchedSeason = QCheckBox(self.groupBox_4)
        self.chkWatchedSeason.setObjectName(u"chkWatchedSeason")

        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.chkWatchedSeason.sizePolicy().hasHeightForWidth())
        self.chkWatchedSeason.setSizePolicy(sizePolicy6)
        self.horizontalLayout_27.addWidget(self.chkWatchedSeason)
        
        self.formLayout_4.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_27)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")

        self.tblEpisodes = QTableView(self.groupBox_4)
        self.tblEpisodes.setObjectName(u"tblEpisodes")
        self.tblEpisodes.setMinimumSize(QSize(450, 267))
        self.tblEpisodes.setAlternatingRowColors(True)
        self.tblEpisodes.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblEpisodes.horizontalHeader().setCascadingSectionResizes(False)
        self.tblEpisodes.horizontalHeader().setMinimumSectionSize(5)
        self.tblEpisodes.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.tblEpisodes.verticalHeader().setVisible(False)
        self.horizontalLayout_13.addWidget(self.tblEpisodes)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 20, 0, 20)

        self.btnAddNewEpisode = QToolButton(self.groupBox_4)
        self.btnAddNewEpisode.setObjectName(u"btnAddNewEpisode")
        self.btnAddNewEpisode.setIcon(icon1)
        self.verticalLayout_3.addWidget(self.btnAddNewEpisode)

        self.btnDeleteEpisode = QToolButton(self.groupBox_4)
        self.btnDeleteEpisode.setObjectName(u"btnDeleteEpisode")
        self.btnDeleteEpisode.setIcon(icon10)
        self.verticalLayout_3.addWidget(self.btnDeleteEpisode)

        self.btnWatched = QToolButton(self.groupBox_4)
        self.btnWatched.setObjectName(u"btnWatched")
        icon14 = QIcon()
        icon14.addFile(u"images/icons/eye-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnWatched.setIcon(icon14)
        self.verticalLayout_3.addWidget(self.btnWatched)

        self.btnNotWatched = QToolButton(self.groupBox_4)
        self.btnNotWatched.setObjectName(u"btnNotWatched")
        icon15 = QIcon()
        icon15.addFile(u"images/icons/eye-slash-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnNotWatched.setIcon(icon15)
        self.verticalLayout_3.addWidget(self.btnNotWatched)

        self.horizontalLayout_13.addLayout(self.verticalLayout_3)

        self.verticalLayout_21.addLayout(self.formLayout_4)
        self.verticalLayout_21.addLayout(self.horizontalLayout_13)
        self.verticalLayout_16.addWidget(self.groupBox_4)
        self.verticalLayout_19.addLayout(self.verticalLayout_16)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")

        self.groupBox_6 = QGroupBox(self.tabEpisodes)
        self.groupBox_6.setObjectName(u"groupBox_6")

        self.verticalLayout_20 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.formLayout_5.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.titleLabel_2 = QLabel(self.groupBox_6)
        self.titleLabel_2.setObjectName(u"titleLabel_2")
        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.titleLabel_2)

        self.txtEpisodeTitle = QLineEdit(self.groupBox_6)
        self.txtEpisodeTitle.setObjectName(u"txtEpisodeTitle")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.txtEpisodeTitle.sizePolicy().hasHeightForWidth())
        self.txtEpisodeTitle.setSizePolicy(sizePolicy7)
        self.txtEpisodeTitle.setMinimumSize(QSize(500, 0))
        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.txtEpisodeTitle)

        self.seasonLabel_2 = QLabel(self.groupBox_6)
        self.seasonLabel_2.setObjectName(u"seasonLabel_2")
        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.seasonLabel_2)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.cbEpisodeSeason = QComboBox(self.groupBox_6)
        self.cbEpisodeSeason.setObjectName(u"cbEpisodeSeason")
        sizePolicy7.setHeightForWidth(self.cbEpisodeSeason.sizePolicy().hasHeightForWidth())
        self.cbEpisodeSeason.setSizePolicy(sizePolicy7)
        self.cbEpisodeSeason.setMinimumSize(QSize(227, 0))
        self.horizontalLayout_21.addWidget(self.cbEpisodeSeason)

        self.label_7 = QLabel(self.groupBox_6)
        self.label_7.setObjectName(u"label_7")
        self.horizontalLayout_21.addWidget(self.label_7)

        self.txtEpisodeNo = QLineEdit(self.groupBox_6)
        self.txtEpisodeNo.setObjectName(u"txtEpisodeNo")
        sizePolicy5.setHeightForWidth(self.txtEpisodeNo.sizePolicy().hasHeightForWidth())
        self.txtEpisodeNo.setSizePolicy(sizePolicy5)
        self.txtEpisodeNo.setMinimumSize(QSize(202, 21))
        self.horizontalLayout_21.addWidget(self.txtEpisodeNo)
        self.formLayout_5.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_21)

        self.qualityLabel_2 = QLabel(self.groupBox_6)
        self.qualityLabel_2.setObjectName(u"qualityLabel_2")
        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.qualityLabel_2)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.cbEpisodeQuality = QComboBox(self.groupBox_6)
        self.cbEpisodeQuality.setObjectName(u"cbEpisodeQuality")
        sizePolicy7.setHeightForWidth(self.cbEpisodeQuality.sizePolicy().hasHeightForWidth())
        self.cbEpisodeQuality.setSizePolicy(sizePolicy7)
        self.cbEpisodeQuality.setMinimumSize(QSize(227, 0))
        self.horizontalLayout_22.addWidget(self.cbEpisodeQuality)

        self.label_10 = QLabel(self.groupBox_6)
        self.label_10.setObjectName(u"label_10")
        self.horizontalLayout_22.addWidget(self.label_10)

        self.txtEpisodeReleased = QLineEdit(self.groupBox_6)
        self.txtEpisodeReleased.setObjectName(u"txtEpisodeReleased")
        self.txtEpisodeReleased.setSizePolicy(sizePolicy5)
        self.txtEpisodeReleased.setMinimumSize(QSize(202, 21))
        self.horizontalLayout_22.addWidget(self.txtEpisodeReleased)
    
        self.formLayout_5.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_22)

        self.backupDiscLabel = QLabel(self.groupBox_6)
        self.backupDiscLabel.setObjectName(u"backupDiscLabel")
        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.backupDiscLabel)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.txtEpisodeDiscNo = QLineEdit(self.groupBox_6)
        self.txtEpisodeDiscNo.setObjectName(u"txtEpisodeDiscNo")
        sizePolicy7.setHeightForWidth(self.txtEpisodeDiscNo.sizePolicy().hasHeightForWidth())
        self.txtEpisodeDiscNo.setSizePolicy(sizePolicy7)
        self.txtEpisodeDiscNo.setMinimumSize(QSize(223, 21))
        self.horizontalLayout_24.addWidget(self.txtEpisodeDiscNo)

        self.chkEpisodeToBurn = QCheckBox(self.groupBox_6)
        self.chkEpisodeToBurn.setObjectName(u"chkEpisodeToBurn")
        self.chkEpisodeToBurn.setMinimumSize(QSize(130, 0))
        self.horizontalLayout_24.addWidget(self.chkEpisodeToBurn)

        self.chkWatchedEpisode = QCheckBox(self.groupBox_6)
        self.chkWatchedEpisode.setObjectName(u"chkWatchedEpisode")
        self.chkWatchedEpisode.setMinimumSize(QSize(100, 0))
        self.horizontalLayout_24.addWidget(self.chkWatchedEpisode)

        self.formLayout_5.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout_24)

        self.sizeLabel_2 = QLabel(self.groupBox_6)
        self.sizeLabel_2.setObjectName(u"sizeLabel_2")
        self.formLayout_5.setWidget(4, QFormLayout.LabelRole, self.sizeLabel_2)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.txtEpisodeSize = QLineEdit(self.groupBox_6)
        self.txtEpisodeSize.setObjectName(u"txtEpisodeSize")
        self.txtEpisodeSize.setMinimumSize(QSize(223, 0))
        self.horizontalLayout_25.addWidget(self.txtEpisodeSize)

        self.tagsLabel_2 = QLabel(self.groupBox_6)
        self.tagsLabel_2.setObjectName(u"tagsLabel_2")
        self.horizontalLayout_25.addWidget(self.tagsLabel_2)

        self.txtEpisodeTags = QLineEdit(self.groupBox_6)
        self.txtEpisodeTags.setObjectName(u"txtEpisodeTags")
        sizePolicy7.setHeightForWidth(self.txtEpisodeTags.sizePolicy().hasHeightForWidth())
        self.txtEpisodeTags.setSizePolicy(sizePolicy7)
        self.txtEpisodeTags.setMinimumSize(QSize(202, 21))
        self.horizontalLayout_25.addWidget(self.txtEpisodeTags)

        self.formLayout_5.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_25)

        self.verticalLayout_20.addLayout(self.formLayout_5)

        self.line = QFrame(self.groupBox_6)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_20.addWidget(self.line)

        self.horizontlLayout_a23 = QHBoxLayout()
        self.horizontlLayout_a23.setObjectName(u"horizontlLayout_a23")
        self.label_8 = QLabel(self.groupBox_6)
        self.label_8.setObjectName(u"label_8")
        self.horizontlLayout_a23.addWidget(self.label_8)

        self.txtEpisodePlot = QPlainTextEdit(self.groupBox_6)
        self.txtEpisodePlot.setObjectName(u"txtEpisodePlot")
        self.txtEpisodePlot.setMaximumSize(QSize(16777215, 100))
        self.horizontlLayout_a23.addWidget(self.txtEpisodePlot)

        self.verticalLayout_20.addLayout(self.horizontlLayout_a23)
        self.verticalLayout_18.addWidget(self.groupBox_6)

        self.verticalLayout_19.addLayout(self.verticalLayout_18)
        icon = QIcon('images/icons/photo-film-solid.svg')
        self.tabWidget.addTab(self.tabEpisodes, icon, "")
        
        self.tabCast = QWidget()
        self.tabCast.setObjectName(u"tabCast")
        
        self.gridLayout_5 = QGridLayout(self.tabCast)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        
        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        
        self.directorSLabel = QLabel(self.tabCast)
        self.directorSLabel.setObjectName(u"directorSLabel")
        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.directorSLabel)

        self.txtDirector = QLineEdit(self.tabCast)
        self.txtDirector.setObjectName(u"txtDirector")
        sizePolicy7.setHeightForWidth(self.txtDirector.sizePolicy().hasHeightForWidth())
        self.txtDirector.setSizePolicy(sizePolicy7)
        self.txtDirector.setMinimumSize(QSize(530, 0))
        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.txtDirector)

        self.writerSLabel = QLabel(self.tabCast)
        self.writerSLabel.setObjectName(u"writerSLabel")
        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.writerSLabel)

        self.txtWriter = QLineEdit(self.tabCast)
        self.txtWriter.setObjectName(u"txtWriter")
        sizePolicy7.setHeightForWidth(self.txtWriter.sizePolicy().hasHeightForWidth())
        self.txtWriter.setSizePolicy(sizePolicy7)
        self.txtWriter.setMinimumSize(QSize(530, 0))
        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.txtWriter)
        self.verticalLayout.addLayout(self.formLayout_7)

        self.tblCast = QTableView(self.tabCast)
        self.tblCast.setObjectName(u"tblCast")
        self.tblCast.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tblCast.setAlternatingRowColors(True)
        self.tblCast.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblCast.setWordWrap(False)
        self.tblCast.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.tblCast.horizontalHeader().setStretchLastSection(False)
        self.tblCast.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tblCast)
        self.gridLayout_5.addLayout(self.verticalLayout, 0, 0, 1, 1)
        
        icon = QIcon('images/icons/masks-theater-solid.svg')
        self.tabWidget.addTab(self.tabCast, icon, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout_6.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1269, 24))
        self.menu_File = QMenu(self.menuBar)
        self.menu_File.setObjectName(u"menu_File")
        self.menuMedia = QMenu(self.menuBar)
        self.menuMedia.setObjectName(u"menuMedia")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menuBar)

        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menu_File.menuAction())
        self.menuBar.addAction(self.menuMedia.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.menu_File.addAction(self.actionPreferences)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionImportData)
        self.menu_File.addAction(self.actionExportData)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionPublish)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionBackup)
        self.menu_File.addAction(self.actionRestore)
        
        self.menuMedia.addAction(self.actionAddNew)
        self.menuMedia.addAction(self.actionUpdate)
        self.menuMedia.addAction(self.actionDelete)
        self.menuMedia.addSeparator()
        self.menuMedia.addAction(self.actionBulkUpdate)
        self.menuMedia.addSeparator()
        self.menuMedia.addAction(self.actionFetchDetails)
        
        self.menuHelp.addAction(self.actionFAQs)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        
        self.toolBar.addAction(self.actionAddNew)
        self.toolBar.addAction(self.actionUpdate)
        self.toolBar.addAction(self.actionBulkUpdate)
        self.toolBar.addAction(self.actionDelete)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionFetchDetails)
        self.toolBar.addAction(self.actionPublish)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionImportData)
        self.toolBar.addAction(self.actionExportData)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionBackup)
        self.toolBar.addAction(self.actionRestore)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPreferences)
        self.toolBar.addAction(self.actionFAQs)

        self.retranslateUi(MainWindow)

        self.tbSummary.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        """
        Updates the UI elements of the MainWindow with translated text.

        Parameters:
        MainWindow (QMainWindow): The main window object whose UI elements are to be updated.

        This function sets the translated text for various UI components such as buttons, labels, 
        actions, and tabs within the MainWindow. It uses the QCoreApplication.translate method to 
        retrieve the appropriate translations for each UI element. The function does not return any 
        value and does not raise any exceptions.

        The translations are applied to:
        - Window title
        - Group boxes
        - Labels and buttons
        - Menu actions and shortcuts
        - Tab texts
        - ComboBox items
        - Tooltips for buttons

        This function is typically used in applications that support multiple languages, allowing 
        the UI to be updated dynamically based on the selected language.
        """
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Personal Media Manager", None))

        self.groupBox.setTitle("")
        self.groupBox_2.setTitle("")
        self.groupBox_3.setTitle("")
        self.groupBox_4.setTitle("")
        self.lblPoster.setText("")
        self.btnMoreFilters.setText("")
        self.btnAddPoster.setText("")
        self.btnRemovePoster.setText("")
        self.btnAddGenre.setText("")
        self.btnRemoveGenre.setText("")
        self.btnAddLanguage.setText("")
        self.btnRemoveLanguage.setText("")
        self.btnAddNewEpisode.setText("")
        self.btnDeleteEpisode.setText("")
        self.btnWatched.setText("")
        self.btnNotWatched.setText("")

        self.actionAddNew.setText(QCoreApplication.translate("MainWindow", u"Add &New", None))
        self.actionAddNew.setToolTip(QCoreApplication.translate("MainWindow", u"Add New", None))
        self.actionAddNew.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N, Ctrl+M", None))

        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"&Preferences", None))
        self.actionPreferences.setToolTip(QCoreApplication.translate("MainWindow", u"Preferences", None))

        self.actionImportData.setText(QCoreApplication.translate("MainWindow", u"&Import Data", None))
        self.actionImportData.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))

        self.actionExportData.setText(QCoreApplication.translate("MainWindow", u"&Export Data", None))
        self.actionExportData.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))

        self.actionPublish.setText(QCoreApplication.translate("MainWindow", u"&Publish", None))
        self.actionPublish.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))

        self.actionBackup.setText(QCoreApplication.translate("MainWindow", u"&Backup", None))
        self.actionBackup.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+B", None))

        self.actionRestore.setText(QCoreApplication.translate("MainWindow", u"&Restore", None))
        self.actionRestore.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))

        self.actionFAQs.setText(QCoreApplication.translate("MainWindow", u"&FAQs", None))
        self.actionFAQs.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+H", None))

        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"&About", None))
        
        self.actionUpdate.setText(QCoreApplication.translate("MainWindow", u"&Update", None))
        self.actionUpdate.setToolTip(QCoreApplication.translate("MainWindow", u"Update", None))
        self.actionUpdate.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+U, Ctrl+M", None))

        self.actionDelete.setText(QCoreApplication.translate("MainWindow", u"&Delete", None))
        self.actionDelete.setToolTip(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.actionDelete.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D, Ctrl+M", None))

        self.actionBulkUpdate.setText(QCoreApplication.translate("MainWindow", u"&Bulk Update", None))
        self.actionBulkUpdate.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+B, Ctrl+U", None))

        self.actionFetchDetails.setText(QCoreApplication.translate("MainWindow", u"&Fetch Details...", None))
        self.actionFetchDetails.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+F, Ctrl+D", None))
        
        self.tbSummary.setTabText(self.tbSummary.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Movies", None))
        self.tbSummary.setTabText(self.tbSummary.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"TV Series", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGeneral), QCoreApplication.translate("MainWindow", u"General", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMedia), QCoreApplication.translate("MainWindow", u"Media", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabEpisodes), QCoreApplication.translate("MainWindow", u"Episodes", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCast), QCoreApplication.translate("MainWindow", u"Cast", None))
        
        self.chkApplyFilter.setText(QCoreApplication.translate("MainWindow", u"Filter(s)", None))

        self.cbFilterWatched.setItemText(0, QCoreApplication.translate("MainWindow", u"All Media", None))
        self.cbFilterWatched.setItemText(1, QCoreApplication.translate("MainWindow", u"Watched", None))
        self.cbFilterWatched.setItemText(2, QCoreApplication.translate("MainWindow", u"Not Watched", None))
        
        self.cbFilterQuality.setItemText(0, QCoreApplication.translate("MainWindow", u"All Quality", None))
        
        self.cbFilterGenres.setItemText(0, QCoreApplication.translate("MainWindow", u"All Genres", None))
        self.cbFilterGenres.setCurrentText(QCoreApplication.translate("MainWindow", u"All Genres", None))
        
        self.cbFilterDiscNo.setItemText(0, QCoreApplication.translate("MainWindow", u"All Discs", None))
        
        self.btnMoreFilters.setToolTip(QCoreApplication.translate("MainWindow", u"More Filters...", None))
        self.btnAddNewEpisode.setToolTip(QCoreApplication.translate("MainWindow", u"Add New Episode", None))
        self.btnDeleteEpisode.setToolTip(QCoreApplication.translate("MainWindow", u"Remove Selected Episode(s)", None))
        self.btnWatched.setToolTip(QCoreApplication.translate("MainWindow", u"Set selected as Watched", None))
        self.btnNotWatched.setToolTip(QCoreApplication.translate("MainWindow", u"Set selected as not Watched", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Search Title:", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.originalTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Original Title", None))
        self.yearLabel.setText(QCoreApplication.translate("MainWindow", u"Year", None))
        self.lblRuntime.setText(QCoreApplication.translate("MainWindow", u"Runtime", None))
        self.lblSeasons.setText(QCoreApplication.translate("MainWindow", u"Seasons", None))
        self.ratingLabel.setText(QCoreApplication.translate("MainWindow", u"Rating", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"User Rating", None))
        self.tagsLabel.setText(QCoreApplication.translate("MainWindow", u"Country", None))
        self.sourceLabel.setText(QCoreApplication.translate("MainWindow", u"Certification", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Release", None))
        self.sourceLabel_2.setText(QCoreApplication.translate("MainWindow", u"Source", None))
        self.chkWatched.setText(QCoreApplication.translate("MainWindow", u"Watched", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Genres", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Languages", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Tags", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Notes", None))
        self.editionLabel.setText(QCoreApplication.translate("MainWindow", u"Edition", None))
        self.codeLabel.setText(QCoreApplication.translate("MainWindow", u"Video Codec", None))
        self.toBackupBurnLabel.setText(QCoreApplication.translate("MainWindow", u"To Burn", None))
        self.rbToBurnYes.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.rbToBurnNo.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.discCountLabel.setText(QCoreApplication.translate("MainWindow", u"No of Discs", None))
        self.qualityLabel.setText(QCoreApplication.translate("MainWindow", u"Quality", None))
        self.sizeLabel.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.discLabel.setText(QCoreApplication.translate("MainWindow", u"Disc #", None))
        self.audioCodecLabel.setText(QCoreApplication.translate("MainWindow", u"Audio Codec", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"All Media on Disc", None))
        self.seasonLabel.setText(QCoreApplication.translate("MainWindow", u"Season", None))
        self.chkWatchedSeason.setText(QCoreApplication.translate("MainWindow", u"Watched Season", None))
        self.titleLabel_2.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.seasonLabel_2.setText(QCoreApplication.translate("MainWindow", u"Season", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Episode  ", None))
        self.qualityLabel_2.setText(QCoreApplication.translate("MainWindow", u"Quality", None))
        self.chkWatchedEpisode.setText(QCoreApplication.translate("MainWindow", u"Watched", None))
        self.backupDiscLabel.setText(QCoreApplication.translate("MainWindow", u"Backup Disc", None))
        self.chkEpisodeToBurn.setText(QCoreApplication.translate("MainWindow", u"To Burn  ", None))
        self.sizeLabel_2.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Released", None))
        self.tagsLabel_2.setText(QCoreApplication.translate("MainWindow", u"Tags       ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u" Plot               ", None))
        self.directorSLabel.setText(QCoreApplication.translate("MainWindow", u"Director(s)", None))
        self.writerSLabel.setText(QCoreApplication.translate("MainWindow", u"Writer(s)", None))

        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menuMedia.setTitle(QCoreApplication.translate("MainWindow", u"Media", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))

        self.cbCertification.setItemText(0, QCoreApplication.translate("MainWindow", u"G", None))
        self.cbCertification.setItemText(1, QCoreApplication.translate("MainWindow", u"PG", None))
        self.cbCertification.setItemText(2, QCoreApplication.translate("MainWindow", u"PG-13", None))
        self.cbCertification.setItemText(3, QCoreApplication.translate("MainWindow", u"R", None))
        self.cbCertification.setItemText(4, QCoreApplication.translate("MainWindow", u"NC-17", None))
        self.cbCertification.setItemText(5, QCoreApplication.translate("MainWindow", u"Passed", None))
        self.cbCertification.setItemText(6, QCoreApplication.translate("MainWindow", u"Approved", None))
        self.cbCertification.setItemText(7, QCoreApplication.translate("MainWindow", u"TV-Y", None))
        self.cbCertification.setItemText(8, QCoreApplication.translate("MainWindow", u"TV-Y7", None))
        self.cbCertification.setItemText(9, QCoreApplication.translate("MainWindow", u"TV-G", None))
        self.cbCertification.setItemText(10, QCoreApplication.translate("MainWindow", u"TV-PG", None))
        self.cbCertification.setItemText(11, QCoreApplication.translate("MainWindow", u"TV-14", None))
        self.cbCertification.setItemText(12, QCoreApplication.translate("MainWindow", u"TV-MA", None))
        self.cbCertification.setItemText(13, QCoreApplication.translate("MainWindow", u"not rated", None))
        self.cbCertification.setItemText(14, QCoreApplication.translate("MainWindow", u"Unknown", None))
        
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

