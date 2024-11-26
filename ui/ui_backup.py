#=======================================================================
# Description:
# UI Component declaration for the Backup / Restore Dialog box
#=======================================================================
from PySide6.QtCore    import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui     import QIcon
from PySide6.QtWidgets import (
    QGroupBox, 
    QHBoxLayout,
    QLabel, 
    QLayout, 
    QLineEdit, 
    QPushButton,
    QSizePolicy, 
    QSpacerItem, 
    QToolButton, 
    QVBoxLayout
)

#=======================================================================
class Ui_BackupDialog(object):
    """
    This class is responsible for setting up the user interface of a Backup Dialog in a PyQt application.
    It defines the layout and components of the dialog, including labels, buttons, and input fields.

    Methods:
    --------
    setupUi(BackupDialog):
        Configures the UI components and layout for the BackupDialog.

    retranslateUi(BackupDialog):
        Updates the text of various UI components within the BackupDialog to support internationalization.
    """
    
    def setupUi(self, BackupDialog):
        """
        Configures the UI components and layout for the BackupDialog.

        Parameters:
        BackupDialog (QDialog): The dialog window to be set up.
        """
        if not BackupDialog.objectName():
            BackupDialog.setObjectName(u"BackupDialog")
        BackupDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        BackupDialog.resize(500, 125)
        
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BackupDialog.sizePolicy().hasHeightForWidth())
        BackupDialog.setSizePolicy(sizePolicy)
        BackupDialog.setModal(True)
        
        self.verticalLayout = QVBoxLayout(BackupDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        
        self.groupBox = QGroupBox(BackupDialog)
        self.groupBox.setObjectName(u"groupBox")
        
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.horizontalLayout.addWidget(self.label)

        self.txtPath = QLineEdit(self.groupBox)
        self.txtPath.setObjectName(u"txtPath")
        self.txtPath.setMinimumSize(QSize(300, 0))
        self.horizontalLayout.addWidget(self.txtPath)

        self.btnSelect = QToolButton(self.groupBox)
        self.btnSelect.setObjectName(u"btnSelect")
        self.horizontalLayout.addWidget(self.btnSelect)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        
        self.lblStatus = QLabel(self.groupBox)
        self.lblStatus.setObjectName(u"lblStatus")
        self.horizontalLayout_2.addWidget(self.lblStatus)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnCancel = QPushButton(self.groupBox)
        self.btnCancel.setObjectName(u"btnCancel")
        icon = QIcon()
        icon.addFile(u"images/icons/circle-xmark-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCancel.setIcon(icon)
        self.btnCancel.setIconSize(QSize(13, 13))
        self.btnCancel.setAutoDefault(False)
        self.horizontalLayout_2.addWidget(self.btnCancel)

        self.btnSave = QPushButton(self.groupBox)
        self.btnSave.setObjectName(u"btnSave")
        icon1 = QIcon()
        icon1.addFile(u"images/icons/circle-check-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSave.setIcon(icon1)
        self.btnSave.setIconSize(QSize(13, 13))
        self.horizontalLayout_2.addWidget(self.btnSave)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(BackupDialog)

        QMetaObject.connectSlotsByName(BackupDialog)
    # setupUi

    def retranslateUi(self, BackupDialog):
        """
        Updates the text of various UI components within the BackupDialog to support internationalization.

        Parameters:
        BackupDialog (QDialog): The dialog window whose UI components are being updated.
        """
        BackupDialog.setWindowTitle(QCoreApplication.translate("BackupDialog", u"Dialog", None))
        self.groupBox.setTitle("")
        self.lblStatus.setText("")
        self.label.setText(QCoreApplication.translate("BackupDialog", u"Location", None))
        self.btnSelect.setText(QCoreApplication.translate("BackupDialog", u"...", None))
        self.btnCancel.setText(QCoreApplication.translate("BackupDialog", u"Cancel", None))
        self.btnSave.setText(QCoreApplication.translate("BackupDialog", u"Apply", None))
    # retranslateUi

#=======================================================================