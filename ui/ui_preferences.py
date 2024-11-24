#=======================================================================
# Description:
# UI component declaration for the Preferences Dialog box
#=======================================================================
from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QComboBox, 
    QFormLayout,
    QGridLayout, 
    QGroupBox, 
    QHBoxLayout, 
    QLabel,
    QLayout, 
    QLineEdit, 
    QListWidget, 
    QPushButton, 
    QSizePolicy, 
    QSpacerItem, 
    QTabWidget,
    QToolButton, 
    QVBoxLayout, 
    QWidget
)


#=======================================================================
class Ui_PreferencesDialog(object):
    """
    This class is responsible for setting up the user interface of a Preferences Dialog in a PyQt application.
    It defines the layout and components of the dialog, including buttons, labels, text fields, and tabs.

    Methods:
    --------
    setupUi(PreferencesDialog):
        Sets up the UI components and layout for the PreferencesDialog.

    retranslateUi(PreferencesDialog):
        Updates the text of various UI components within the PreferencesDialog to support internationalization.
    """

    def setupUi(self, PreferencesDialog):
        """
        Sets up the UI components and layout for the PreferencesDialog.

        Parameters:
        PreferencesDialog (QDialog): The dialog window to which the UI components are added.
        """
        if not PreferencesDialog.objectName():
            PreferencesDialog.setObjectName(u"PreferencesDialog")
        PreferencesDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        PreferencesDialog.resize(582, 300)

        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PreferencesDialog.sizePolicy().hasHeightForWidth())

        PreferencesDialog.setSizePolicy(sizePolicy)
        PreferencesDialog.setMinimumSize(QSize(560, 300))
        PreferencesDialog.setMaximumSize(QSize(589, 300))
        PreferencesDialog.setModal(True)
        
        self.gridLayout = QGridLayout(PreferencesDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        
        self.groupBox = QGroupBox(PreferencesDialog)
        self.groupBox.setObjectName(u"groupBox")
        
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        
        self.tabWidget = QTabWidget(self.groupBox)
        self.tabWidget.setObjectName(u"tabWidget")
        
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        
        self.formLayout = QFormLayout(self.tab)
        self.formLayout.setObjectName(u"formLayout")
        
        self.lookupScriptsLabel = QLabel(self.tab)
        self.lookupScriptsLabel.setObjectName(u"lookupScriptsLabel")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lookupScriptsLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.txtPrfLookup = QLineEdit(self.tab)
        self.txtPrfLookup.setObjectName(u"txtPrfLookup")
        self.txtPrfLookup.setMinimumSize(QSize(350, 0))
        self.horizontalLayout_2.addWidget(self.txtPrfLookup)

        self.btnPrfLookup = QToolButton(self.tab)
        self.btnPrfLookup.setObjectName(u"btnPrfLookup")
        self.horizontalLayout_2.addWidget(self.btnPrfLookup)
        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.defaultLookupLabel = QLabel(self.tab)
        self.defaultLookupLabel.setObjectName(u"defaultLookupLabel")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.defaultLookupLabel)

        self.cbDefaultLookup = QComboBox(self.tab)
        self.cbDefaultLookup.setObjectName(u"cbDefaultLookup")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cbDefaultLookup.sizePolicy().hasHeightForWidth())
        self.cbDefaultLookup.setSizePolicy(sizePolicy2)
        self.cbDefaultLookup.setMinimumSize(QSize(360, 0))
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.cbDefaultLookup)

        self.publishScriptsLabel = QLabel(self.tab)
        self.publishScriptsLabel.setObjectName(u"publishScriptsLabel")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.publishScriptsLabel)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.txtPrfPublish = QLineEdit(self.tab)
        self.txtPrfPublish.setObjectName(u"txtPrfPublish")
        self.txtPrfPublish.setMinimumSize(QSize(350, 0))
        self.horizontalLayout_3.addWidget(self.txtPrfPublish)

        self.btnPrfPublish = QToolButton(self.tab)
        self.btnPrfPublish.setObjectName(u"btnPrfPublish")
        self.horizontalLayout_3.addWidget(self.btnPrfPublish)
        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.defaultPublishLabel = QLabel(self.tab)
        self.defaultPublishLabel.setObjectName(u"defaultPublishLabel")
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.defaultPublishLabel)

        self.cbDefaultPublish = QComboBox(self.tab)
        self.cbDefaultPublish.setObjectName(u"cbDefaultPublish")
        sizePolicy2.setHeightForWidth(self.cbDefaultPublish.sizePolicy().hasHeightForWidth())
        self.cbDefaultPublish.setSizePolicy(sizePolicy2)
        self.cbDefaultPublish.setMinimumSize(QSize(360, 0))
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.cbDefaultPublish)

        self.importTemplatesLabel = QLabel(self.tab)
        self.importTemplatesLabel.setObjectName(u"importTemplatesLabel")
        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.importTemplatesLabel)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, -1, -1, -1)

        self.txtPrfImport = QLineEdit(self.tab)
        self.txtPrfImport.setObjectName(u"txtPrfImport")
        self.txtPrfImport.setMinimumSize(QSize(350, 0))
        self.horizontalLayout_7.addWidget(self.txtPrfImport)

        self.btnPrfImport = QToolButton(self.tab)
        self.btnPrfImport.setObjectName(u"btnPrfImport")
        self.horizontalLayout_7.addWidget(self.btnPrfImport)
        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_7)

        self.exportTemplatesLabel = QLabel(self.tab)
        self.exportTemplatesLabel.setObjectName(u"exportTemplatesLabel")
        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.exportTemplatesLabel)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        
        self.txtPrfExport = QLineEdit(self.tab)
        self.txtPrfExport.setObjectName(u"txtPrfExport")
        self.txtPrfExport.setMinimumSize(QSize(350, 0))
        self.horizontalLayout_5.addWidget(self.txtPrfExport)

        self.btnPrfExport = QToolButton(self.tab)
        self.btnPrfExport.setObjectName(u"btnPrfExport")
        self.horizontalLayout_5.addWidget(self.btnPrfExport)

        self.formLayout.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout_5)
        self.tabWidget.addTab(self.tab, "")
        
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        self.verticalLayout_2.addWidget(self.label)

        self.lsPrfGenres = QListWidget(self.tab_2)
        self.lsPrfGenres.setObjectName(u"lsPrfGenres")
        self.lsPrfGenres.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout_2.addWidget(self.lsPrfGenres)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.txtPrfGenre = QLineEdit(self.tab_2)
        self.txtPrfGenre.setObjectName(u"txtPrfGenre")
        self.horizontalLayout_8.addWidget(self.txtPrfGenre)

        self.btnPrfGenreAdd = QToolButton(self.tab_2)
        self.btnPrfGenreAdd.setObjectName(u"btnPrfGenreAdd")
        iconadd = QIcon()
        iconadd.addFile(u"images/icons/circle-plus-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnPrfGenreAdd.setIcon(iconadd)
        self.btnPrfGenreAdd.setIconSize(QSize(13, 13))
        self.horizontalLayout_8.addWidget(self.btnPrfGenreAdd)

        self.btnPrfGenreDelete = QToolButton(self.tab_2)
        self.btnPrfGenreDelete.setObjectName(u"btnPrfGenreDelete")
        icondel = QIcon()
        icondel.addFile(u"images/icons/trash-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnPrfGenreDelete.setIcon(icondel)
        self.btnPrfGenreDelete.setIconSize(QSize(13, 13))
        self.horizontalLayout_8.addWidget(self.btnPrfGenreDelete)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.verticalLayout_3.addWidget(self.label_2)

        self.lsPrfSources = QListWidget(self.tab_2)
        self.lsPrfSources.setObjectName(u"lsPrfSources")
        self.lsPrfSources.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout_3.addWidget(self.lsPrfSources)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.txtPrfSource = QLineEdit(self.tab_2)
        self.txtPrfSource.setObjectName(u"txtPrfSource")
        self.horizontalLayout_9.addWidget(self.txtPrfSource)

        self.btnPrfSourceAdd = QToolButton(self.tab_2)
        self.btnPrfSourceAdd.setObjectName(u"btnPrfSourceAdd")
        self.btnPrfSourceAdd.setIcon(iconadd)
        self.btnPrfSourceAdd.setIconSize(QSize(13, 13))
        self.horizontalLayout_9.addWidget(self.btnPrfSourceAdd)

        self.btnPrfSourceDelete = QToolButton(self.tab_2)
        self.btnPrfSourceDelete.setObjectName(u"btnPrfSourceDelete")
        self.btnPrfSourceDelete.setIcon(icondel)
        self.btnPrfSourceDelete.setIconSize(QSize(13, 13))
        self.horizontalLayout_9.addWidget(self.btnPrfSourceDelete)

        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        
        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")
        self.verticalLayout_4.addWidget(self.label_3)

        self.lsPrfQualities = QListWidget(self.tab_3)
        self.lsPrfQualities.setObjectName(u"lsPrfQualities")
        self.lsPrfQualities.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout_4.addWidget(self.lsPrfQualities)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.txtPrfQuality = QLineEdit(self.tab_3)
        self.txtPrfQuality.setObjectName(u"txtPrfQuality")
        self.horizontalLayout_11.addWidget(self.txtPrfQuality)

        self.btnPrfQualityAdd = QToolButton(self.tab_3)
        self.btnPrfQualityAdd.setObjectName(u"btnPrfQualityAdd")
        self.btnPrfQualityAdd.setIcon(iconadd)
        self.btnPrfQualityAdd.setIconSize(QSize(13, 13))
        self.horizontalLayout_11.addWidget(self.btnPrfQualityAdd)

        self.btnPrfQualityDelete = QToolButton(self.tab_3)
        self.btnPrfQualityDelete.setObjectName(u"btnPrfQualityDelete")
        self.btnPrfQualityDelete.setIcon(icondel)
        self.btnPrfQualityDelete.setIconSize(QSize(13, 13))
        self.horizontalLayout_11.addWidget(self.btnPrfQualityDelete)

        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_10.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.tab_3)
        self.label_4.setObjectName(u"label_4")
        self.verticalLayout_5.addWidget(self.label_4)

        self.lsPrfEditions = QListWidget(self.tab_3)
        self.lsPrfEditions.setObjectName(u"lsPrfEditions")
        self.lsPrfEditions.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout_5.addWidget(self.lsPrfEditions)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.txtPrfEdition = QLineEdit(self.tab_3)
        self.txtPrfEdition.setObjectName(u"txtPrfEdition")
        self.horizontalLayout_12.addWidget(self.txtPrfEdition)

        self.btnPrfEditionAdd = QToolButton(self.tab_3)
        self.btnPrfEditionAdd.setObjectName(u"btnPrfEditionAdd")
        self.btnPrfEditionAdd.setIcon(iconadd)
        self.btnPrfEditionAdd.setIconSize(QSize(13, 13))
        self.horizontalLayout_12.addWidget(self.btnPrfEditionAdd)

        self.btnPrfEditionDelete = QToolButton(self.tab_3)
        self.btnPrfEditionDelete.setObjectName(u"btnPrfEditionDelete")
        self.btnPrfEditionDelete.setIcon(icondel)
        self.btnPrfEditionDelete.setIconSize(QSize(13, 13))
        self.horizontalLayout_12.addWidget(self.btnPrfEditionDelete)

        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_10.addLayout(self.verticalLayout_5)
        self.gridLayout_5.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, 0, -1)
        self.lblStatus = QLabel(self.groupBox)
        self.lblStatus.setObjectName(u"lblStatus")
        self.horizontalLayout.addWidget(self.lblStatus)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnCancel = QPushButton(self.groupBox)
        self.btnCancel.setObjectName(u"btnCancel")
        icon2 = QIcon()
        icon2.addFile(u"images/icons/circle-xmark-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCancel.setIcon(icon2)
        self.btnCancel.setIconSize(QSize(13, 13))
        self.horizontalLayout.addWidget(self.btnCancel)

        self.btnSave = QPushButton(self.groupBox)
        self.btnSave.setObjectName(u"btnSave")
        icon3 = QIcon()
        icon3.addFile(u"images/icons/circle-check-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSave.setIcon(icon3)
        self.btnSave.setIconSize(QSize(13, 13))
        self.horizontalLayout.addWidget(self.btnSave)

        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(PreferencesDialog)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(PreferencesDialog)
    # setupUi

    def retranslateUi(self, PreferencesDialog):
        """
        Updates the text of various UI components within the PreferencesDialog to support internationalization.

        Parameters:
        PreferencesDialog (QDialog): The dialog window whose UI components are being updated.
        """
        self.lblStatus.setText("")
        self.groupBox.setTitle("")
        self.btnPrfGenreAdd.setText("")
        self.btnPrfGenreDelete.setText("")
        self.btnPrfSourceAdd.setText("")
        self.btnPrfSourceDelete.setText("")
        self.btnPrfQualityAdd.setText("")
        self.btnPrfQualityDelete.setText("")
        self.btnPrfEditionAdd.setText("")
        self.btnPrfEditionDelete.setText("")
        PreferencesDialog.setWindowTitle(QCoreApplication.translate("PreferencesDialog", u"Dialog", None))
        self.lookupScriptsLabel.setText(QCoreApplication.translate("PreferencesDialog", u"Lookup Scripts", None))
        self.btnPrfLookup.setText(QCoreApplication.translate("PreferencesDialog", u"...", None))
        self.defaultLookupLabel.setText(QCoreApplication.translate("PreferencesDialog", u"Default Lookup", None))
        self.publishScriptsLabel.setText(QCoreApplication.translate("PreferencesDialog", u"Publish Scripts", None))
        self.btnPrfPublish.setText(QCoreApplication.translate("PreferencesDialog", u"...", None))
        self.defaultPublishLabel.setText(QCoreApplication.translate("PreferencesDialog", u"Default Publish", None))
        self.importTemplatesLabel.setText(QCoreApplication.translate("PreferencesDialog", u"Import Templates", None))
        self.btnPrfImport.setText(QCoreApplication.translate("PreferencesDialog", u"...", None))
        self.exportTemplatesLabel.setText(QCoreApplication.translate("PreferencesDialog", u"Export Templates", None))
        self.btnPrfExport.setText(QCoreApplication.translate("PreferencesDialog", u"...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("PreferencesDialog", u"General", None))
        self.label.setText(QCoreApplication.translate("PreferencesDialog", u"Genres", None))
        self.label_2.setText(QCoreApplication.translate("PreferencesDialog", u"Sources", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("PreferencesDialog", u"Media", None))
        self.label_3.setText(QCoreApplication.translate("PreferencesDialog", u"Qualities", None))
        self.label_4.setText(QCoreApplication.translate("PreferencesDialog", u"Editions", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("PreferencesDialog", u"Metadata", None))
        self.btnCancel.setText(QCoreApplication.translate("PreferencesDialog", u"Cencel", None))
        self.btnCancel.setAutoDefault(False)
        self.btnSave.setText(QCoreApplication.translate("PreferencesDialog", u"Save", None))
    # retranslateUi

