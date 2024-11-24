#=======================================================================
# Description:
# UI Component declaration for the Bulk Update Dialog box
#=======================================================================
from PySide6.QtCore    import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui     import QIcon
from PySide6.QtWidgets import (
    QCheckBox, 
    QComboBox,
    QFormLayout, 
    QGridLayout,
    QGroupBox, 
    QLayout,
    QHBoxLayout, 
    QLabel,
    QLineEdit, 
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout
)

#=======================================================================
class Ui_BulkUpdateDialog(object):
    """
    This class is responsible for setting up the user interface for a Bulk Update Dialog.

    Methods:
        setupUi(BulkUpdateDialog):
            Sets up the UI components and layout for the BulkUpdateDialog.

        retranslateUi(BulkUpdateDialog):
            Sets the text for the UI components to support internationalization.
    """
    def setupUi(self, BulkUpdateDialog):
        """
        Sets up the user interface for the BulkUpdateDialog.

        Parameters:
        - BulkUpdateDialog: QDialog
            The dialog window that will be set up with the UI components.
        """
        if not BulkUpdateDialog.objectName():
            BulkUpdateDialog.setObjectName(u"BulkUpdateDialog")
        BulkUpdateDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        BulkUpdateDialog.resize(600, 380)

        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BulkUpdateDialog.sizePolicy().hasHeightForWidth())
        
        BulkUpdateDialog.setSizePolicy(sizePolicy)
        BulkUpdateDialog.setMinimumSize(QSize(500, 380))
        BulkUpdateDialog.setMaximumSize(QSize(16777215, 380))
        BulkUpdateDialog.setBaseSize(QSize(600, 403))
        BulkUpdateDialog.setModal(True)
        
        self.gridLayout = QGridLayout(BulkUpdateDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        
        self.groupBox = QGroupBox(BulkUpdateDialog)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        
        self.chkSource = QCheckBox(self.groupBox)
        self.chkSource.setObjectName(u"chkSource")
        self.chkSource.setStyleSheet(u"margin-top:5px")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.chkSource)

        self.cbBulkSource = QComboBox(self.groupBox)
        self.cbBulkSource.setObjectName(u"cbBulkSource")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cbBulkSource.sizePolicy().hasHeightForWidth())
        self.cbBulkSource.setSizePolicy(sizePolicy2)
        self.cbBulkSource.setMinimumSize(QSize(400, 0))
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cbBulkSource)

        self.chkCodec = QCheckBox(self.groupBox)
        self.chkCodec.setObjectName(u"chkCodec")
        self.chkCodec.setStyleSheet(u"margin-top: 5px")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.chkCodec)

        self.txtBulkCodec = QLineEdit(self.groupBox)
        self.txtBulkCodec.setObjectName(u"txtBulkCodec")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.txtBulkCodec)

        self.chkQuality = QCheckBox(self.groupBox)
        self.chkQuality.setObjectName(u"chkQuality")
        self.chkQuality.setStyleSheet(u"margin-top: 7px")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.chkQuality)

        self.cbBulkQuality = QComboBox(self.groupBox)
        self.cbBulkQuality.setObjectName(u"cbBulkQuality")
        sizePolicy2.setHeightForWidth(self.cbBulkQuality.sizePolicy().hasHeightForWidth())
        self.cbBulkQuality.setSizePolicy(sizePolicy2)
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cbBulkQuality)

        self.chkEdition = QCheckBox(self.groupBox)
        self.chkEdition.setObjectName(u"chkEdition")
        self.chkEdition.setStyleSheet(u"margin-top: 5px")
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.chkEdition)

        self.cbBulkEdition = QComboBox(self.groupBox)
        self.cbBulkEdition.setObjectName(u"cbBulkEdition")
        sizePolicy2.setHeightForWidth(self.cbBulkEdition.sizePolicy().hasHeightForWidth())
        self.cbBulkEdition.setSizePolicy(sizePolicy2)
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.cbBulkEdition)

        self.chkWatched = QCheckBox(self.groupBox)
        self.chkWatched.setObjectName(u"chkWatched")
        self.chkWatched.setStyleSheet(u"margin-top: -1px")
        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.chkWatched)

        self.chkBulkWatched = QCheckBox(self.groupBox)
        self.chkBulkWatched.setObjectName(u"chkBulkWatched")
        self.chkBulkWatched.setStyleSheet(u"margin-left: 10px;")
        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.chkBulkWatched)

        self.chkToBurn = QCheckBox(self.groupBox)
        self.chkToBurn.setObjectName(u"chkToBurn")
        self.chkToBurn.setStyleSheet(u"margin-top: 5px")
        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.chkToBurn)

        self.chkBulkToBurn = QCheckBox(self.groupBox)
        self.chkBulkToBurn.setObjectName(u"chkBulkToBurn")
        self.chkBulkToBurn.setStyleSheet(u"margin-top: 5px; margin-left: 10px;")
        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.chkBulkToBurn)

        self.chkDiscNo = QCheckBox(self.groupBox)
        self.chkDiscNo.setObjectName(u"chkDiscNo")
        self.chkDiscNo.setStyleSheet(u"margin-top: 5px")
        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.chkDiscNo)

        self.txtBulkDisc = QLineEdit(self.groupBox)
        self.txtBulkDisc.setObjectName(u"txtBulkDisc")
        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.txtBulkDisc)

        self.chkGenre = QCheckBox(self.groupBox)
        self.chkGenre.setObjectName(u"chkGenre")
        self.chkGenre.setStyleSheet(u"margin-top: 7px")
        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.chkGenre)

        self.cbBulkGenre = QComboBox(self.groupBox)
        self.cbBulkGenre.setObjectName(u"cbBulkGenre")
        sizePolicy2.setHeightForWidth(self.cbBulkGenre.sizePolicy().hasHeightForWidth())
        self.cbBulkGenre.setSizePolicy(sizePolicy2)
        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.cbBulkGenre)

        self.chkTag = QCheckBox(self.groupBox)
        self.chkTag.setObjectName(u"chkTag")
        self.chkTag.setStyleSheet(u"margin-top: 5px")
        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.chkTag)

        self.txtBulkTag = QLineEdit(self.groupBox)
        self.txtBulkTag.setObjectName(u"txtBulkTag")
        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.txtBulkTag)

        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
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
        self.horizontalLayout.addWidget(self.btnSave)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(BulkUpdateDialog)

        QMetaObject.connectSlotsByName(BulkUpdateDialog)
    # setupUi

    def retranslateUi(self, BulkUpdateDialog):
        """
        Updates the UI elements of the BulkUpdateDialog with translated text.

        Parameters:
        BulkUpdateDialog (QDialog): The dialog window that will have its UI elements updated with translated text.
        """
        self.groupBox.setTitle("")
        self.lblStatus.setText("")
        BulkUpdateDialog.setWindowTitle(QCoreApplication.translate("BulkUpdateDialog", u"Bulk Update", None))
        self.chkSource.setText(QCoreApplication.translate("BulkUpdateDialog", u"Source", None))
        self.chkCodec.setText(QCoreApplication.translate("BulkUpdateDialog", u"Codec", None))
        self.chkQuality.setText(QCoreApplication.translate("BulkUpdateDialog", u"Quality", None))
        self.chkEdition.setText(QCoreApplication.translate("BulkUpdateDialog", u"Edition", None))
        self.chkWatched.setText(QCoreApplication.translate("BulkUpdateDialog", u"Watched", None))
        self.chkToBurn.setText(QCoreApplication.translate("BulkUpdateDialog", u"To Burn", None))
        self.chkDiscNo.setText(QCoreApplication.translate("BulkUpdateDialog", u"Disc #", None))
        self.chkGenre.setText(QCoreApplication.translate("BulkUpdateDialog", u"Genre", None))
        self.chkTag.setText(QCoreApplication.translate("BulkUpdateDialog", u"Tag", None))
        self.btnCancel.setText(QCoreApplication.translate("BulkUpdateDialog", u"Cancel", None))
        self.btnCancel.setAutoDefault(False)
        self.btnSave.setText(QCoreApplication.translate("BulkUpdateDialog", u"Save", None))
    # retranslateUi

