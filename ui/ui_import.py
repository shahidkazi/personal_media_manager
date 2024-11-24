#=======================================================================
# Description:
# UI component declaration for the Import Dialog box
#=======================================================================
from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
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
    QPushButton,
    QSizePolicy, 
    QSpacerItem, 
    QTableWidget, 
    QToolButton, 
    QVBoxLayout
)


#=======================================================================
class Ui_ImportDialog(object):
    """
    This class defines the user interface for an Import Dialog.

    Methods:
    --------
    setupUi(ImportDialog):
        Configures the UI components and layout for the ImportDialog.

    retranslateUi(ImportDialog):
        Sets the text for the UI components to support internationalization.
    """

    def setupUi(self, ImportDialog):
        """
        Configures the UI components and layout for the ImportDialog.

        Parameters:
        - ImportDialog: QWidget
            The dialog window where the UI components will be set up.
        """
        if not ImportDialog.objectName():
            ImportDialog.setObjectName(u"ImportDialog")
        ImportDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        ImportDialog.resize(602, 400)

        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ImportDialog.sizePolicy().hasHeightForWidth())
        ImportDialog.setSizePolicy(sizePolicy)
        ImportDialog.setModal(True)

        self.gridLayout = QGridLayout(ImportDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        
        self.groupBox = QGroupBox(ImportDialog)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.setContentsMargins(-1, 0, -1, -1)
        
        self.selectFileCsvXlsJsonLabel = QLabel(self.groupBox)
        self.selectFileCsvXlsJsonLabel.setObjectName(u"selectFileCsvXlsJsonLabel")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.selectFileCsvXlsJsonLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        
        self.txtSource = QLineEdit(self.groupBox)
        self.txtSource.setObjectName(u"txtSource")
        self.txtSource.setMinimumSize(QSize(345, 0))
        self.txtSource.setReadOnly(True)
        self.horizontalLayout.addWidget(self.txtSource)

        self.btnBrowse = QToolButton(self.groupBox)
        self.btnBrowse.setObjectName(u"btnBrowse")
        self.horizontalLayout.addWidget(self.btnBrowse)
        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout)

        self.mediaTypeLabel = QLabel(self.groupBox)
        self.mediaTypeLabel.setObjectName(u"mediaTypeLabel")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.mediaTypeLabel)

        self.cbMediaType = QComboBox(self.groupBox)
        self.cbMediaType.addItem("")
        self.cbMediaType.addItem("")
        self.cbMediaType.setObjectName(u"cbMediaType")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cbMediaType.sizePolicy().hasHeightForWidth())
        self.cbMediaType.setSizePolicy(sizePolicy2)
        self.cbMediaType.setMinimumSize(QSize(375, 0))
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.cbMediaType)
        self.verticalLayout_2.addLayout(self.formLayout)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.verticalLayout_2.addWidget(self.label_2)

        self.tblImport = QTableWidget(self.groupBox)
        self.tblImport.setObjectName(u"tblImport")
        self.tblImport.setMinimumSize(QSize(500, 0))
        self.tblImport.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.tblImport)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.lblStatus = QLabel(self.groupBox)
        self.lblStatus.setObjectName(u"lblStatus")
        self.lblStatus.setStyleSheet(u"")
        self.horizontalLayout_2.addWidget(self.lblStatus)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnCancel = QPushButton(self.groupBox)
        self.btnCancel.setObjectName(u"btnCancel")
        icon = QIcon()
        icon.addFile(u"images/icons/circle-xmark-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCancel.setIcon(icon)
        self.btnCancel.setIconSize(QSize(13, 13))
        self.horizontalLayout_2.addWidget(self.btnCancel)

        self.btnAccept = QPushButton(self.groupBox)
        self.btnAccept.setObjectName(u"btnAccept")
        icon1 = QIcon()
        icon1.addFile(u"images/icons/circle-check-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnAccept.setIcon(icon1)
        self.btnAccept.setIconSize(QSize(13, 13))
        self.horizontalLayout_2.addWidget(self.btnAccept)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(ImportDialog)

        QMetaObject.connectSlotsByName(ImportDialog)
    # setupUi

    def retranslateUi(self, ImportDialog):
        """
        Updates the text of various UI components within the ImportDialog to support internationalization.

        Parameters:
        ImportDialog (QDialog): The dialog window that is being translated.
        """
        self.lblStatus.setText("")
        self.groupBox.setTitle("")
        ImportDialog.setWindowTitle(QCoreApplication.translate("ImportDialog", u"Import Data...", None))
        self.selectFileCsvXlsJsonLabel.setText(QCoreApplication.translate("ImportDialog", u"Select File (csv, xls, json):", None))
        self.btnBrowse.setText(QCoreApplication.translate("ImportDialog", u"...", None))
        self.mediaTypeLabel.setText(QCoreApplication.translate("ImportDialog", u"Media Type:", None))
        self.cbMediaType.setItemText(0, QCoreApplication.translate("ImportDialog", u"Movies", None))
        self.cbMediaType.setItemText(1, QCoreApplication.translate("ImportDialog", u"TV Series", None))
        self.label_2.setText(QCoreApplication.translate("ImportDialog", u"Select columns to import", None))
        self.btnCancel.setText(QCoreApplication.translate("ImportDialog", u"Cancel", None))
        self.btnCancel.setAutoDefault(False)
        self.btnAccept.setText(QCoreApplication.translate("ImportDialog", u"Import", None))
    # retranslateUi

#=======================================================================