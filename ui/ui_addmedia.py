#=======================================================================
# Description:
# UI component declaration for the Add New Media Dialog
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
    QPlainTextEdit, 
    QPushButton, 
    QSizePolicy,
    QSpacerItem, 
    QVBoxLayout
)

#=======================================================================
class Ui_AddNewMedia(object):
    """
    This class is responsible for setting up the user interface for the 'Add New Media' dialog.

    Methods:
    --------
    setupUi(AddNewMedia):
        Sets up the user interface for the 'Add New Media' dialog.

    retranslateUi(AddNewMedia):
        Sets the text for the UI elements to support internationalization.
    """

    def setupUi(self, AddNewMedia):
        """
        Sets up the user interface for the AddNewMedia dialog.

        Parameters:
        AddNewMedia (QDialog): The dialog window to which the UI components are added.
        """
        if not AddNewMedia.objectName():
            AddNewMedia.setObjectName(u"AddNewMedia")
        AddNewMedia.setWindowModality(Qt.WindowModality.ApplicationModal)
        AddNewMedia.resize(450, 300)

        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddNewMedia.sizePolicy().hasHeightForWidth())
        AddNewMedia.setSizePolicy(sizePolicy)
        AddNewMedia.setMaximumSize(QSize(450, 300))
        AddNewMedia.setModal(True)

        self.gridLayout = QGridLayout(AddNewMedia)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)

        self.groupBox = QGroupBox(AddNewMedia)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.formLayout.setFormAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        
        self.mediaTypeLabel = QLabel(self.groupBox)
        self.mediaTypeLabel.setObjectName(u"mediaTypeLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.mediaTypeLabel)

        self.mediaTypeComboBox = QComboBox(self.groupBox)
        self.mediaTypeComboBox.addItem("")
        self.mediaTypeComboBox.addItem("")
        self.mediaTypeComboBox.setObjectName(u"mediaTypeComboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mediaTypeComboBox.sizePolicy().hasHeightForWidth())
        self.mediaTypeComboBox.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.mediaTypeComboBox)
        self.verticalLayout.addLayout(self.formLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.verticalLayout_2.addWidget(self.label)

        self.txtMediaList = QPlainTextEdit(self.groupBox)
        self.txtMediaList.setObjectName(u"txtMediaList")
        self.txtMediaList.setMinimumSize(QSize(400, 0))
        self.verticalLayout_2.addWidget(self.txtMediaList)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
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

        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(AddNewMedia)

        QMetaObject.connectSlotsByName(AddNewMedia)
    # setupUi

    def retranslateUi(self, AddNewMedia):
        """
        Updates the UI elements of the AddNewMedia window with translated text.

        Parameters:
        AddNewMedia (QWidget): The widget representing the Add New Media window.
        """
        AddNewMedia.setWindowTitle(QCoreApplication.translate("AddNewMedia", u"Add New Media", None))
        self.groupBox.setTitle("")
        self.lblStatus.setText("")
        self.mediaTypeLabel.setText(QCoreApplication.translate("AddNewMedia", u"Media Type", None))
        self.mediaTypeComboBox.setItemText(0, QCoreApplication.translate("AddNewMedia", u"Movie", None))
        self.mediaTypeComboBox.setItemText(1, QCoreApplication.translate("AddNewMedia", u"TV Series", None))
        self.label.setText(QCoreApplication.translate("AddNewMedia", u"Titles (New Line seperated)", None))
        self.btnCancel.setText(QCoreApplication.translate("AddNewMedia", u"Cancel", None))
        self.btnCancel.setAutoDefault(False)
        self.btnSave.setText(QCoreApplication.translate("AddNewMedia", u"Save", None))
    # retranslateUi

#=======================================================================