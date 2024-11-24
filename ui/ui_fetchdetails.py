#=======================================================================
# Description:
# UI component declaration for the Fetch Details (Online) Dialog box
#=======================================================================
from PySide6.QtCore    import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui     import QIcon
from PySide6.QtWidgets import (
    QAbstractItemView, 
    QCheckBox, 
    QComboBox,
    QFormLayout, 
    QGridLayout, 
    QGroupBox,
    QHBoxLayout, 
    QLabel, 
    QLayout,
    QLineEdit, 
    QPlainTextEdit, 
    QProgressBar, 
    QPushButton,
    QSizePolicy, 
    QSpacerItem, 
    QTableView, 
    QVBoxLayout,
)

#=======================================================================
class Ui_FetchDetailsDialog(object):
    """
    This class is responsible for setting up the user interface of the FetchDetailsDialog. 

    Methods:
    --------
    setupUi(FetchDetailsDialog: QDialog) -> None:
        Configures the UI components of the FetchDetailsDialog, setting their properties and layout.
    
    retranslateUi(FetchDetailsDialog: QDialog) -> None:
        Updates the text of various UI components within the FetchDetailsDialog to the appropriate translations.
    """

    def setupUi(self, FetchDetailsDialog):
        """
        Sets up the user interface for the FetchDetailsDialog.

        Parameters:
        FetchDetailsDialog (QDialog): The dialog window where the UI components will be set up.
        """
        if not FetchDetailsDialog.objectName():
            FetchDetailsDialog.setObjectName(u"FetchDetailsDialog")
        FetchDetailsDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        FetchDetailsDialog.resize(900, 600)

        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FetchDetailsDialog.sizePolicy().hasHeightForWidth())
        
        FetchDetailsDialog.setSizePolicy(sizePolicy)
        FetchDetailsDialog.setMinimumSize(QSize(0, 0))
        FetchDetailsDialog.setMaximumSize(QSize(900, 600))
        FetchDetailsDialog.setModal(True)
        
        self.gridLayout = QGridLayout(FetchDetailsDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        
        self.groupBox = QGroupBox(FetchDetailsDialog)
        self.groupBox.setObjectName(u"groupBox")
        
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        
        self.titleLabel = QLabel(self.groupBox)
        self.titleLabel.setObjectName(u"titleLabel")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.titleLabel)

        self.txtSearchTitle = QLineEdit(self.groupBox)
        self.txtSearchTitle.setObjectName(u"txtSearchTitle")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.txtSearchTitle.sizePolicy().hasHeightForWidth())
        self.txtSearchTitle.setSizePolicy(sizePolicy1)
        self.txtSearchTitle.setStyleSheet(u"margin-left: 5px")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.txtSearchTitle)

        self.sourceLabel = QLabel(self.groupBox)
        self.sourceLabel.setObjectName(u"sourceLabel")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.sourceLabel)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.cbSearchSource = QComboBox(self.groupBox)
        self.cbSearchSource.addItem("")
        self.cbSearchSource.setObjectName(u"cbSearchSource")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cbSearchSource.sizePolicy().hasHeightForWidth())
        self.cbSearchSource.setSizePolicy(sizePolicy2)
        self.horizontalLayout_4.addWidget(self.cbSearchSource)

        self.chkDontOverwrite = QCheckBox(self.groupBox)
        self.chkDontOverwrite.setObjectName(u"chkDontOverwrite")
        sizePolicy2.setHeightForWidth(self.chkDontOverwrite.sizePolicy().hasHeightForWidth())
        self.chkDontOverwrite.setSizePolicy(sizePolicy2)
        self.horizontalLayout_4.addWidget(self.chkDontOverwrite)

        self.btnFetch = QPushButton(self.groupBox)
        self.btnFetch.setObjectName(u"btnFetch")
        icon13 = QIcon()
        icon13.addFile(u"images/icons/magnifying-glass-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnFetch.setIcon(icon13)
        self.btnFetch.setIconSize(QSize(13, 13))
        self.horizontalLayout_4.addWidget(self.btnFetch)

        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.tblSearchResults = QTableView(self.groupBox)
        self.tblSearchResults.setObjectName(u"tblSearchResults")
        self.tblSearchResults.setMinimumSize(QSize(300, 0))
        self.tblSearchResults.setMaximumSize(QSize(350, 16777215))
        self.tblSearchResults.setAlternatingRowColors(True)
        self.tblSearchResults.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.verticalLayout_3.addWidget(self.tblSearchResults)
        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.lblPoster = QLabel(self.groupBox)
        self.lblPoster.setObjectName(u"lblPoster")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lblPoster.sizePolicy().hasHeightForWidth())
        self.lblPoster.setSizePolicy(sizePolicy3)
        self.lblPoster.setMinimumSize(QSize(128, 192))
        self.lblPoster.setMaximumSize(QSize(128, 192))
        self.lblPoster.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_5.addWidget(self.lblPoster)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.formLayout_4.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        
        self.titleLabel_2 = QLabel(self.groupBox)
        self.titleLabel_2.setObjectName(u"titleLabel_2")
        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.titleLabel_2)

        self.yearLabel = QLabel(self.groupBox)
        self.yearLabel.setObjectName(u"yearLabel")
        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.yearLabel)

        self.txtResYear = QLineEdit(self.groupBox)
        self.txtResYear.setObjectName(u"txtResYear")
        self.txtResYear.setReadOnly(True)
        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.txtResYear)

        self.txtResTitle = QPlainTextEdit(self.groupBox)
        self.txtResTitle.setObjectName(u"txtResTitle")
        self.txtResTitle.setMaximumSize(QSize(16777215, 50))
        self.txtResTitle.setReadOnly(True)
        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.txtResTitle)

        self.genresLabel = QLabel(self.groupBox)
        self.genresLabel.setObjectName(u"genresLabel")
        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.genresLabel)

        self.txtResGenres = QLineEdit(self.groupBox)
        self.txtResGenres.setObjectName(u"txtResGenres")
        self.txtResGenres.setReadOnly(True)
        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.txtResGenres)

        self.directorLabel = QLabel(self.groupBox)
        self.directorLabel.setObjectName(u"directorLabel")
        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.directorLabel)

        self.txtResDirector = QLineEdit(self.groupBox)
        self.txtResDirector.setObjectName(u"txtResDirector")
        self.txtResDirector.setReadOnly(True)

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.txtResDirector)
        self.horizontalLayout_5.addLayout(self.formLayout_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 0, -1, -1)
        
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.verticalLayout_9.addWidget(self.label)

        self.txtResPlot = QPlainTextEdit(self.groupBox)
        self.txtResPlot.setObjectName(u"txtResPlot")
        self.txtResPlot.setMinimumSize(QSize(306, 0))
        self.txtResPlot.setReadOnly(True)
        self.verticalLayout_9.addWidget(self.txtResPlot)

        self.verticalLayout_4.addLayout(self.verticalLayout_9)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.lblStatus = QLabel(self.groupBox)
        self.lblStatus.setObjectName(u"lblStatus")
        self.horizontalLayout_2.addWidget(self.lblStatus)

        self.prgStatus = QProgressBar(self.groupBox)
        self.prgStatus.setObjectName(u"prgStatus")
        sizePolicy1.setHeightForWidth(self.prgStatus.sizePolicy().hasHeightForWidth())
        self.prgStatus.setSizePolicy(sizePolicy1)
        self.prgStatus.setValue(0)
        self.horizontalLayout_2.addWidget(self.prgStatus)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnCancel = QPushButton(self.groupBox)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setObjectName(u"btnCancel")
        icon = QIcon()
        icon.addFile(u"images/icons/circle-xmark-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCancel.setIcon(icon)
        self.btnCancel.setIconSize(QSize(13, 13))
        self.horizontalLayout_2.addWidget(self.btnCancel)

        self.btnSave = QPushButton(self.groupBox)
        self.btnSave.setObjectName(u"btnSave")
        icon2 = QIcon()
        icon2.addFile(u"images/icons/circle-check-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSave.setIcon(icon2)
        self.btnSave.setIconSize(QSize(13, 13))
        self.horizontalLayout_2.addWidget(self.btnSave)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(FetchDetailsDialog)

        QMetaObject.connectSlotsByName(FetchDetailsDialog)
    # setupUi

    def retranslateUi(self, FetchDetailsDialog):
        """
        Updates the text of various UI components within the FetchDetailsDialog to the appropriate translations.
        
        Parameters:
        FetchDetailsDialog (QDialog): The dialog window whose UI components are being updated with translated text.
        """
        self.lblStatus.setText("")
        self.groupBox.setTitle("")
        FetchDetailsDialog.setWindowTitle(QCoreApplication.translate("FetchDetailsDialog", u"Dialog", None))
        self.titleLabel.setText(QCoreApplication.translate("FetchDetailsDialog", u"Search Title", None))
        self.sourceLabel.setText(QCoreApplication.translate("FetchDetailsDialog", u"Online Source", None))
        self.cbSearchSource.setItemText(0, QCoreApplication.translate("FetchDetailsDialog", u"IMDB", None))
        self.chkDontOverwrite.setText(QCoreApplication.translate("FetchDetailsDialog", u"Do not overwrite existing data", None))
        self.btnFetch.setText(QCoreApplication.translate("FetchDetailsDialog", u"Search", None))
        self.btnFetch.setAutoDefault(False)
        self.lblPoster.setText(QCoreApplication.translate("FetchDetailsDialog", u"Poster", None))
        self.titleLabel_2.setText(QCoreApplication.translate("FetchDetailsDialog", u"Title", None))
        self.yearLabel.setText(QCoreApplication.translate("FetchDetailsDialog", u"Year", None))
        self.genresLabel.setText(QCoreApplication.translate("FetchDetailsDialog", u"Genres", None))
        self.directorLabel.setText(QCoreApplication.translate("FetchDetailsDialog", u"Director", None))
        self.label.setText(QCoreApplication.translate("FetchDetailsDialog", u"Plot", None))
        self.btnCancel.setText(QCoreApplication.translate("FetchDetailsDialog", u"Cancel", None))
        self.btnCancel.setAutoDefault(False)
        self.btnSave.setText(QCoreApplication.translate("FetchDetailsDialog", u"Save", None))
    # retranslateUi

#=======================================================================