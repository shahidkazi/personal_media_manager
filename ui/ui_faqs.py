#=======================================================================
# Description:
# UI component declaration for the FAQs Dialog box
#=======================================================================
from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, QUrl, Qt
from PySide6.QtWidgets import (
    QDialogButtonBox,
    QGroupBox, 
    QLabel, 
    QLayout, 
    QTextBrowser, 
    QVBoxLayout
)

#=======================================================================
class Ui_FAQDialog(object):
    """
    This class is responsible for setting up the user interface of the FAQ dialog window.

    Methods:
    --------
    setupUi(FAQDialog):
        Sets up the user interface for the FAQDialog window, including layout, widgets, and connections.

    retranslateUi(FAQDialog):
        Updates the user interface elements of the FAQDialog with translated text.
    """

    def setupUi(self, FAQDialog):
        """
        Sets up the user interface for the FAQDialog window.

        Parameters:
        -----------
        FAQDialog (QDialog): The dialog window that contains the FAQ content.
        """
        if not FAQDialog.objectName():
            FAQDialog.setObjectName(u"FAQDialog")
        FAQDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        FAQDialog.resize(633, 436)
        FAQDialog.setMinimumSize(QSize(700, 500))
        FAQDialog.setModal(True)

        self.verticalLayout = QVBoxLayout(FAQDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        
        self.groupBox = QGroupBox(FAQDialog)
        self.groupBox.setObjectName(u"groupBox")
        
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.verticalLayout_2.addWidget(self.label)

        self.tbFAQs = QTextBrowser(self.groupBox)
        self.tbFAQs.setObjectName(u"tbFAQs")
        self.tbFAQs.setMinimumSize(QSize(650, 425))
        self.tbFAQs.setSource(QUrl.fromLocalFile('faqs.html'))
        self.verticalLayout_2.addWidget(self.tbFAQs)
        self.verticalLayout.addWidget(self.groupBox)

        self.buttonBox = QDialogButtonBox(FAQDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.verticalLayout.addWidget(self.buttonBox)

        self.buttonBox.accepted.connect(FAQDialog.accept)
        self.buttonBox.rejected.connect(FAQDialog.reject)

        self.retranslateUi(FAQDialog)

        QMetaObject.connectSlotsByName(FAQDialog)
    # setupUi

    def retranslateUi(self, FAQDialog):
        """
        Updates the user interface elements of the FAQDialog with translated text.

        Parameters:
        FAQDialog (QDialog): The dialog window that contains the FAQ content.
        """
        FAQDialog.setWindowTitle(QCoreApplication.translate("FAQDialog", u"Dialog", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("FAQDialog", u"FAQs", None))
    # retranslateUi

#=======================================================================