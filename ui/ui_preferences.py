#=======================================================================
# Description:
# UI component declaration for the Preferences Dialog box
#=======================================================================
from PySide6.QtCore    import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui     import QIcon
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


class Ui_PreferencesDialog(object):
    def setupUi(self, PreferencesDialog):
        if not PreferencesDialog.objectName():
            PreferencesDialog.setObjectName(u"PreferencesDialog")

        PreferencesDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        PreferencesDialog.resize(582, 355)
        
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PreferencesDialog.sizePolicy().hasHeightForWidth())
        
        PreferencesDialog.setSizePolicy(sizePolicy)
        PreferencesDialog.setMinimumSize(QSize(560, 355))
        PreferencesDialog.setMaximumSize(QSize(589, 355))
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
        icon = QIcon()
        icon.addFile(u"images/icons/circle-xmark-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCancel.setIcon(icon)
        self.btnCancel.setIconSize(QSize(13, 13))
        self.horizontalLayout.addWidget(self.btnCancel)

        self.btnSave = QPushButton(self.groupBox)
        self.btnSave.setObjectName(u"btnSave")
        icon1 = QIcon()
        icon1.addFile(u"images/icons/circle-check-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSave.setIcon(icon1)
        self.btnSave.setIconSize(QSize(13, 13))
        self.horizontalLayout.addWidget(self.btnSave)

        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.tabWidget = QTabWidget(self.groupBox)
        self.tabWidget.setObjectName(u"tabWidget")

        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.formLayout_4.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        
        self.posterPathLabel = QLabel(self.tab)
        self.posterPathLabel.setObjectName(u"posterPathLabel")
        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.posterPathLabel)

        self.lookupTemplatesLabel = QLabel(self.tab)
        self.lookupTemplatesLabel.setObjectName(u"lookupTemplatesLabel")
        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.lookupTemplatesLabel)

        self.defaultLookupLabel = QLabel(self.tab)
        self.defaultLookupLabel.setObjectName(u"defaultLookupLabel")
        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.defaultLookupLabel)

        self.cbDefaultLookup = QComboBox(self.tab)
        self.cbDefaultLookup.setObjectName(u"cbDefaultLookup")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cbDefaultLookup.sizePolicy().hasHeightForWidth())
        self.cbDefaultLookup.setSizePolicy(sizePolicy2)
        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.cbDefaultLookup)

        self.publishTemplatesLabel = QLabel(self.tab)
        self.publishTemplatesLabel.setObjectName(u"publishTemplatesLabel")
        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.publishTemplatesLabel)

        self.defaultPublisherLabel = QLabel(self.tab)
        self.defaultPublisherLabel.setObjectName(u"defaultPublisherLabel")
        self.formLayout_4.setWidget(5, QFormLayout.LabelRole, self.defaultPublisherLabel)

        self.cbDefaultPublish = QComboBox(self.tab)
        self.cbDefaultPublish.setObjectName(u"cbDefaultPublish")
        sizePolicy2.setHeightForWidth(self.cbDefaultPublish.sizePolicy().hasHeightForWidth())
        self.cbDefaultPublish.setSizePolicy(sizePolicy2)
        self.formLayout_4.setWidget(5, QFormLayout.FieldRole, self.cbDefaultPublish)

        self.importTemplatesLabel = QLabel(self.tab)
        self.importTemplatesLabel.setObjectName(u"importTemplatesLabel")
        self.formLayout_4.setWidget(6, QFormLayout.LabelRole, self.importTemplatesLabel)

        self.exportTemplatesLabel = QLabel(self.tab)
        self.exportTemplatesLabel.setObjectName(u"exportTemplatesLabel")
        self.formLayout_4.setWidget(7, QFormLayout.LabelRole, self.exportTemplatesLabel)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.formLayout_4.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.txtPrfPoster = QLineEdit(self.tab)
        self.txtPrfPoster.setObjectName(u"txtPrfPoster")
        self.horizontalLayout_5.addWidget(self.txtPrfPoster)

        self.btnPrfPoster = QToolButton(self.tab)
        self.btnPrfPoster.setObjectName(u"btnPrfPoster")
        self.horizontalLayout_5.addWidget(self.btnPrfPoster)
        self.formLayout_4.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, -1, -1, -1)
        
        self.txtPrfLookup = QLineEdit(self.tab)
        self.txtPrfLookup.setObjectName(u"txtPrfLookup")
        self.horizontalLayout_7.addWidget(self.txtPrfLookup)

        self.btnPrfLookup = QToolButton(self.tab)
        self.btnPrfLookup.setObjectName(u"btnPrfLookup")
        self.horizontalLayout_7.addWidget(self.btnPrfLookup)
        self.formLayout_4.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_7)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, -1, -1, -1)
        self.txtPrfPublish = QLineEdit(self.tab)
        self.txtPrfPublish.setObjectName(u"txtPrfPublish")
        self.horizontalLayout_13.addWidget(self.txtPrfPublish)

        self.btnPrfPublish = QToolButton(self.tab)
        self.btnPrfPublish.setObjectName(u"btnPrfPublish")
        self.horizontalLayout_13.addWidget(self.btnPrfPublish)
        self.formLayout_4.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, -1, -1, -1)

        self.txtPrfImport = QLineEdit(self.tab)
        self.txtPrfImport.setObjectName(u"txtPrfImport")
        self.horizontalLayout_14.addWidget(self.txtPrfImport)

        self.btnPrfImport = QToolButton(self.tab)
        self.btnPrfImport.setObjectName(u"btnPrfImport")
        self.horizontalLayout_14.addWidget(self.btnPrfImport)
        self.formLayout_4.setLayout(6, QFormLayout.FieldRole, self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, -1, -1, -1)
        
        self.txtPrfExport = QLineEdit(self.tab)
        self.txtPrfExport.setObjectName(u"txtPrfExport")
        self.horizontalLayout_15.addWidget(self.txtPrfExport)

        self.btnPrfExport = QToolButton(self.tab)
        self.btnPrfExport.setObjectName(u"btnPrfExport")
        self.horizontalLayout_15.addWidget(self.btnPrfExport)
        self.formLayout_4.setLayout(7, QFormLayout.FieldRole, self.horizontalLayout_15)

        self.verticalLayout.addLayout(self.formLayout_4)

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
        self.lsPrfGenres.setMaximumSize(QSize(16777215, 230))
        self.verticalLayout_2.addWidget(self.lsPrfGenres)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")

        self.txtPrfGenre = QLineEdit(self.tab_2)
        self.txtPrfGenre.setObjectName(u"txtPrfGenre")
        self.horizontalLayout_8.addWidget(self.txtPrfGenre)

        self.btnPrfGenreAdd = QToolButton(self.tab_2)
        self.btnPrfGenreAdd.setObjectName(u"btnPrfGenreAdd")
        icon2 = QIcon()
        icon2.addFile(u"images/icons/circle-plus-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnPrfGenreAdd.setIcon(icon2)
        self.horizontalLayout_8.addWidget(self.btnPrfGenreAdd)

        self.btnPrfGenreDelete = QToolButton(self.tab_2)
        self.btnPrfGenreDelete.setObjectName(u"btnPrfGenreDelete")
        icon3 = QIcon()
        icon3.addFile(u"images/icons/trash-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnPrfGenreDelete.setIcon(icon3)
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
        self.lsPrfSources.setMaximumSize(QSize(16777215, 230))
        self.verticalLayout_3.addWidget(self.lsPrfSources)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.txtPrfSource = QLineEdit(self.tab_2)
        self.txtPrfSource.setObjectName(u"txtPrfSource")
        self.horizontalLayout_9.addWidget(self.txtPrfSource)

        self.btnPrfSourceAdd = QToolButton(self.tab_2)
        self.btnPrfSourceAdd.setObjectName(u"btnPrfSourceAdd")
        self.btnPrfSourceAdd.setIcon(icon2)
        self.horizontalLayout_9.addWidget(self.btnPrfSourceAdd)

        self.btnPrfSourceDelete = QToolButton(self.tab_2)
        self.btnPrfSourceDelete.setObjectName(u"btnPrfSourceDelete")
        self.btnPrfSourceDelete.setIcon(icon3)
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
        self.lsPrfQualities.setMaximumSize(QSize(16777215, 230))
        self.verticalLayout_4.addWidget(self.lsPrfQualities)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.txtPrfQuality = QLineEdit(self.tab_3)
        self.txtPrfQuality.setObjectName(u"txtPrfQuality")
        self.horizontalLayout_11.addWidget(self.txtPrfQuality)

        self.btnPrfQualityAdd = QToolButton(self.tab_3)
        self.btnPrfQualityAdd.setObjectName(u"btnPrfQualityAdd")
        self.btnPrfQualityAdd.setIcon(icon2)
        self.horizontalLayout_11.addWidget(self.btnPrfQualityAdd)

        self.btnPrfQualityDelete = QToolButton(self.tab_3)
        self.btnPrfQualityDelete.setObjectName(u"btnPrfQualityDelete")
        self.btnPrfQualityDelete.setIcon(icon3)
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
        self.lsPrfEditions.setMaximumSize(QSize(16777215, 230))
        self.verticalLayout_5.addWidget(self.lsPrfEditions)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.txtPrfEdition = QLineEdit(self.tab_3)
        self.txtPrfEdition.setObjectName(u"txtPrfEdition")
        self.horizontalLayout_12.addWidget(self.txtPrfEdition)

        self.btnPrfEditionAdd = QToolButton(self.tab_3)
        self.btnPrfEditionAdd.setObjectName(u"btnPrfEditionAdd")
        self.btnPrfEditionAdd.setIcon(icon2)
        self.horizontalLayout_12.addWidget(self.btnPrfEditionAdd)

        self.btnPrfEditionDelete = QToolButton(self.tab_3)
        self.btnPrfEditionDelete.setObjectName(u"btnPrfEditionDelete")
        self.btnPrfEditionDelete.setIcon(icon3)
        self.horizontalLayout_12.addWidget(self.btnPrfEditionDelete)

        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_10.addLayout(self.verticalLayout_5)
        self.gridLayout_5.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.tabWidget.setCurrentIndex(0)

        self.retranslateUi(PreferencesDialog)

        QMetaObject.connectSlotsByName(PreferencesDialog)
    # setupUi

    def retranslateUi(self, PreferencesDialog):
        PreferencesDialog.setWindowTitle(QCoreApplication.translate("PreferencesDialog", u"Dialog", None))
        self.groupBox.setTitle("")
        self.lblStatus.setText("")
        self.btnPrfGenreAdd.setText("")
        self.btnPrfGenreDelete.setText("")
        self.btnPrfSourceAdd.setText("")
        self.btnPrfSourceDelete.setText("")
        self.btnPrfQualityAdd.setText("")
        self.btnPrfQualityDelete.setText("")
        self.btnPrfEditionAdd.setText("")
        self.btnPrfEditionDelete.setText("")
        self.btnCancel.setText(QCoreApplication.translate("PreferencesDialog", u"Cencel", None))
        self.btnCancel.setAutoDefault(False)
        self.btnSave.setText(QCoreApplication.translate("PreferencesDialog", u"Save", None))
        self.posterPathLabel.setText(QCoreApplication.translate("PreferencesDialog", u"Poster Path", None))
        self.lookupTemplatesLabel.setText(QCoreApplication.translate("PreferencesDialog", u"Lookup Templates", None))
        self.defaultLookupLabel.setText(QCoreApplication.translate("PreferencesDialog", u"Default Lookup", None))
        self.publishTemplatesLabel.setText(QCoreApplication.translate("PreferencesDialog", u"Publish Templates", None))
        self.defaultPublisherLabel.setText(QCoreApplication.translate("PreferencesDialog", u"Default Publisher", None))
        self.importTemplatesLabel.setText(QCoreApplication.translate("PreferencesDialog", u"Import Templates", None))
        self.exportTemplatesLabel.setText(QCoreApplication.translate("PreferencesDialog", u"Export Templates", None))
        self.btnPrfPoster.setText(QCoreApplication.translate("PreferencesDialog", u"...", None))
        self.btnPrfLookup.setText(QCoreApplication.translate("PreferencesDialog", u"...", None))
        self.btnPrfPublish.setText(QCoreApplication.translate("PreferencesDialog", u"...", None))
        self.btnPrfImport.setText(QCoreApplication.translate("PreferencesDialog", u"...", None))
        self.btnPrfExport.setText(QCoreApplication.translate("PreferencesDialog", u"...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("PreferencesDialog", u"General", None))
        self.label.setText(QCoreApplication.translate("PreferencesDialog", u"Genres", None))
        self.label_2.setText(QCoreApplication.translate("PreferencesDialog", u"Sources", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("PreferencesDialog", u"Media", None))
        self.label_3.setText(QCoreApplication.translate("PreferencesDialog", u"Qualities", None))
        self.label_4.setText(QCoreApplication.translate("PreferencesDialog", u"Editions", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("PreferencesDialog", u"Metadata", None))
    # retranslateUi

