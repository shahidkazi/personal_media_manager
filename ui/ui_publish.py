#=======================================================================
# Description:
# UI component declaration for the Publish Dialog box
#=======================================================================

from PySide6.QtCore    import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui     import QIcon
from PySide6.QtWidgets import (
    QGridLayout, 
    QGroupBox,
    QHBoxLayout, 
    QLabel, 
    QLayout, 
    QListWidget,
    QProgressBar, 
    QPushButton, 
    QSizePolicy,
    QVBoxLayout
)


#=======================================================================
class Ui_PublishDialog(object):
    """
    This class defines the user interface for a Publish Dialog.

    Methods:
    --------
    setupUi(PublishDialog):
        Configures the UI elements of the PublishDialog.

    retranslateUi(PublishDialog):
        Sets the text for the UI elements, allowing for internationalization.
    """

    def setupUi(self, PublishDialog):
        """
        Configures the UI elements of the PublishDialog, including setting the window modality, size policies,
        layout, and adding widgets such as labels, list widgets, progress bars, and buttons.

        Parameters:
        - PublishDialog (QDialog): The dialog window to be set up.
        """
        if not PublishDialog.objectName():
            PublishDialog.setObjectName(u"PublishDialog")
        PublishDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        PublishDialog.resize(574, 372)

        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PublishDialog.sizePolicy().hasHeightForWidth())
        PublishDialog.setSizePolicy(sizePolicy)
        PublishDialog.setMinimumSize(QSize(500, 0))
        PublishDialog.setModal(True)
        self.gridLayout = QGridLayout(PublishDialog)

        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        
        self.groupBox = QGroupBox(PublishDialog)
        self.groupBox.setObjectName(u"groupBox")
        
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.verticalLayout.addWidget(self.label)

        self.lsPublishTemplate = QListWidget(self.groupBox)
        self.lsPublishTemplate.setObjectName(u"lsPublishTemplate")
        self.lsPublishTemplate.setMinimumSize(QSize(500, 250))
        self.verticalLayout.addWidget(self.lsPublishTemplate)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)

        self.prgProgress = QProgressBar(self.groupBox)
        self.prgProgress.setObjectName(u"prgProgress")
        self.prgProgress.setValue(24)
        self.horizontalLayout.addWidget(self.prgProgress)

        self.lblStatus = QLabel(self.groupBox)
        self.lblStatus.setObjectName(u"lblStatus")
        self.horizontalLayout.addWidget(self.lblStatus)

        self.btnCancel = QPushButton(self.groupBox)
        self.btnCancel.setObjectName(u"btnCancel")
        icon = QIcon()
        icon.addFile(u"images/icons/circle-xmark-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCancel.setIcon(icon)
        self.btnCancel.setIconSize(QSize(13, 13))
        self.horizontalLayout.addWidget(self.btnCancel)

        self.btnPublish = QPushButton(self.groupBox)
        self.btnPublish.setObjectName(u"btnPublish")
        icon1 = QIcon()
        icon1.addFile(u"images/icons/circle-check-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnPublish.setIcon(icon1)
        self.btnPublish.setIconSize(QSize(13, 13))
        self.horizontalLayout.addWidget(self.btnPublish)

        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(PublishDialog)

        QMetaObject.connectSlotsByName(PublishDialog)
    # setupUi

    def retranslateUi(self, PublishDialog):
        """
        Updates the text of various UI components within the PublishDialog to support internationalization.

        Parameters:
        PublishDialog (QDialog): The dialog window whose UI components are being updated.
        """
        self.lblStatus.setText("")
        self.groupBox.setTitle("")
        PublishDialog.setWindowTitle(QCoreApplication.translate("PublishDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("PublishDialog", u"Pick Template for publishing data", None))
        self.btnCancel.setText(QCoreApplication.translate("PublishDialog", u"Cancel", None))
        self.btnCancel.setAutoDefault(False)
        self.btnPublish.setText(QCoreApplication.translate("PublishDialog", u"Publish", None))
    # retranslateUi

#=======================================================================