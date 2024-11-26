#=======================================================================
# Description:
# UI component declaration for the About Media Manager Dialog
#=======================================================================
from PySide6.QtCore import QCoreApplication,QMetaObject, Qt
from PySide6.QtWidgets import (
    QDialogButtonBox,
    QGridLayout, 
    QGroupBox, 
    QLabel, 
    QLayout,
    QSizePolicy, 
    QVBoxLayout 
)


#=======================================================================
class Ui_AboutDialog(object):
    """
    This class is responsible for setting up the user interface of the AboutDialog window in a PyQt application.
    It defines the layout and components of the dialog, including labels and buttons.

    Methods:
    --------
    setupUi(AboutDialog: QDialog):
        Sets up the user interface for the AboutDialog window.

    retranslateUi(AboutDialog: QDialog):
        Updates the text and titles of various UI components within the AboutDialog.
    """

    def setupUi(self, AboutDialog):
        """
        Sets up the user interface for the AboutDialog window.

        Parameters:
        - AboutDialog (QDialog): The dialog window that will be configured with the UI components.
        """
        if not AboutDialog.objectName():
            AboutDialog.setObjectName(u"AboutDialog")

        AboutDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        AboutDialog.resize(500, 380)
        AboutDialog.setModal(True)

        self.verticalLayout = QVBoxLayout(AboutDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        
        self.groupBox = QGroupBox(AboutDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-weight:bold; font-size:30px")
        self.label.setTextFormat(Qt.TextFormat.RichText)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)
        
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_6.addWidget(self.label_4)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.verticalLayout_6.addWidget(self.label_5)

        self.verticalLayout_2.addLayout(self.verticalLayout_6)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_6)

        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.verticalLayout.addWidget(self.groupBox)

        self.buttonBox = QDialogButtonBox(AboutDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Close)

        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AboutDialog)
        self.buttonBox.accepted.connect(AboutDialog.accept)
        self.buttonBox.rejected.connect(AboutDialog.reject)

        QMetaObject.connectSlotsByName(AboutDialog)
    # setupUi

    def retranslateUi(self, AboutDialog):
        """
        Updates the text and titles of various UI components within the AboutDialog.

        Parameters:
        - AboutDialog: The dialog window (type: QDialog) that contains the UI components to be updated.
        """
        AboutDialog.setWindowTitle(QCoreApplication.translate("AboutDialog", u"About", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("AboutDialog", u"Personal Media Manager v1.1.0", None))
        self.label_2.setText(QCoreApplication.translate("AboutDialog", u"Simple open source utility created with the soul purpose of managing your media (movie/tv series) collection. There were quite a few paid applications out there but none seem catered to what was needed by us and the paid versions were charging a bomb if you needed to customize. Feel free to customize as you need, but not forget to include reference to yours truly.", None))
        self.label_3.setText(QCoreApplication.translate("AboutDialog", u"Email: shahidskazi@hotmail.com", None))
        self.label_4.setText(QCoreApplication.translate("AboutDialog", u"Instagram: @shahidscornerblog", None))
        self.label_5.setText(QCoreApplication.translate("AboutDialog", u"Website: https://www.shahidscorner.com", None))
        self.label_6.setText(QCoreApplication.translate("AboutDialog", u"The UI was created using the Community Edition of QT Creator (https://www.qt.io/product/development-tools). This app is intended for Open Source usage only and not for any commercial purposes. If you intend to commecialize it, then please purchase the correct edition from QT and reach out to me for royalty.", None))
    # retranslateUi


#=======================================================================