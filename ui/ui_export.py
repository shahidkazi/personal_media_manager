#=======================================================================
# Description: 
# UI Component declaration for the Export Dialog
#=======================================================================
from PySide6.QtCore    import QCoreApplication, QMetaObject, QSize
from PySide6.QtGui     import QIcon
from PySide6.QtWidgets import (
    QDialogButtonBox,
    QHBoxLayout, 
    QGroupBox,
    QLabel, 
    QLayout, 
    QLineEdit,
    QListWidget, 
    QPushButton, 
    QSizePolicy,
    QSpacerItem, 
    QVBoxLayout
)

#=======================================================================
class Ui_ExportDialog(object):
    """
    A class to set up and manage the user interface for an Export Dialog.
    """

    def setupUi(self, ExportDialog):
        """
        Sets up the user interface for the ExportDialog.

        This method initializes and arranges the widgets within the ExportDialog. It configures layouts, labels, 
        list widgets, line edits, button boxes, and push buttons to create a structured dialog for exporting data.

        Parameters:
        - ExportDialog: The dialog window (QDialog) where the UI components will be set up.
        """
        if not ExportDialog.objectName():
            ExportDialog.setObjectName(u"ExportDialog")
        ExportDialog.resize(528, 317)

        self.verticalLayout_2 = QVBoxLayout(ExportDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)

        self.groupBox = QGroupBox(ExportDialog)
        self.groupBox.setObjectName(u"groupBox")
        
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.verticalLayout_3.addWidget(self.label_2)

        self.lsTemplates = QListWidget(self.groupBox)
        self.lsTemplates.setObjectName(u"lsTemplates")
        self.lsTemplates.setMinimumSize(QSize(500, 0))
        self.verticalLayout_3.addWidget(self.lsTemplates)
        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.horizontalLayout_2.addWidget(self.label)

        self.txtDestination = QLineEdit(self.groupBox)
        self.txtDestination.setObjectName(u"txtDestination")
        self.txtDestination.setReadOnly(True)
        self.horizontalLayout_2.addWidget(self.txtDestination)

        self.btnBrowse = QDialogButtonBox(self.groupBox)
        self.btnBrowse.setObjectName(u"btnBrowse")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBrowse.sizePolicy().hasHeightForWidth())
        self.btnBrowse.setSizePolicy(sizePolicy)
        self.btnBrowse.setStandardButtons(QDialogButtonBox.StandardButton.Open)
        self.horizontalLayout_2.addWidget(self.btnBrowse)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

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

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(ExportDialog)

        QMetaObject.connectSlotsByName(ExportDialog)
    # setupUi

    def retranslateUi(self, ExportDialog):
        """
        Updates the text of various UI elements in the ExportDialog to the current language settings.

        Parameters:
        ExportDialog (QDialog): The dialog window whose UI elements are being updated.
        """
        self.lblStatus.setText("")
        ExportDialog.setWindowTitle(QCoreApplication.translate("ExportDialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("ExportDialog", u"Select Export Template", None))
        self.label.setText(QCoreApplication.translate("ExportDialog", u"Destination", None))
        self.btnCancel.setText(QCoreApplication.translate("ExportDialog", u"Cancel", None))
        self.btnCancel.setAutoDefault(False)
        self.btnSave.setText(QCoreApplication.translate("ExportDialog", u"Export", None))
    # retranslateUi

#=======================================================================