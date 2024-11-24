#=======================================================================
# Description:
# UI component declaration for the Add New Episode Dialog
#=======================================================================
from PySide6.QtCore    import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui     import QIcon
from PySide6.QtWidgets import (
    QFormLayout, 
    QGroupBox,
    QHBoxLayout, 
    QLabel, 
    QLineEdit, 
    QPushButton,
    QSizePolicy, 
    QSpacerItem, 
    QVBoxLayout
)


#=======================================================================
class Ui_AddNewEpisode(object):
    """
    This class is responsible for setting up the user interface for adding a new episode in a PyQt application.

    Methods:
    --------
    setupUi(AddNewEpisode):
        Sets up the user interface for the AddNewEpisode dialog.

    retranslateUi(AddNewEpisode):
        Sets the text for the UI elements to support internationalization.
    """

    def setupUi(self, AddNewEpisode):
        """
        Sets up the user interface for the AddNewEpisode dialog by creating and arranging widgets.

        Parameters:
        - AddNewEpisode (QWidget): The widget representing the dialog where the UI elements will be added.
        """

        if not AddNewEpisode.objectName():
            AddNewEpisode.setObjectName(u"AddNewEpisode")

        AddNewEpisode.resize(493, 187)

        self.horizontalLayout = QHBoxLayout(AddNewEpisode)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(AddNewEpisode)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        
        self.seasonLabel = QLabel(self.groupBox)
        self.seasonLabel.setObjectName(u"seasonLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.seasonLabel)

        self.txtEpisodeSeason = QLineEdit(self.groupBox)
        self.txtEpisodeSeason.setObjectName(u"txtEpisodeSeason")
        self.txtEpisodeSeason.setMinimumSize(QSize(350, 0))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.txtEpisodeSeason)

        self.episodeNoLabel = QLabel(self.groupBox)
        self.episodeNoLabel.setObjectName(u"episodeNoLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.episodeNoLabel)

        self.txtEpisodeNo = QLineEdit(self.groupBox)
        self.txtEpisodeNo.setObjectName(u"txtEpisodeNo")
        self.txtEpisodeNo.setMinimumSize(QSize(350, 0))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.txtEpisodeNo)

        self.episodeTitleLabel = QLabel(self.groupBox)
        self.episodeTitleLabel.setObjectName(u"episodeTitleLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.episodeTitleLabel)

        self.txtEpisodeTitle = QLineEdit(self.groupBox)
        self.txtEpisodeTitle.setObjectName(u"txtEpisodeTitle")
        self.txtEpisodeTitle.setMinimumSize(QSize(350, 0))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.txtEpisodeTitle)

        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblStatus = QLabel(self.groupBox)
        self.lblStatus.setObjectName(u"lblStatus")
        self.lblStatus.setStyleSheet(u"color: red;")

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

        self.btnSave = QPushButton(self.groupBox)
        self.btnSave.setObjectName(u"btnSave")
        icon2 = QIcon()
        icon2.addFile(u"images/icons/circle-check-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSave.setIcon(icon2)
        self.btnSave.setIconSize(QSize(13, 13))
        self.horizontalLayout_2.addWidget(self.btnSave)

        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi(AddNewEpisode)

        QMetaObject.connectSlotsByName(AddNewEpisode)
    # setupUi

    def retranslateUi(self, AddNewEpisode):
        """
        Sets the text for the UI elements to support internationalization.

        Parameters:
        - AddNewEpisode (QWidget): The widget representing the dialog where the UI elements are located.
        """
        AddNewEpisode.setWindowTitle(QCoreApplication.translate("AddNewEpisode", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("AddNewEpisode", u"Add New Episode", None))
        self.seasonLabel.setText(QCoreApplication.translate("AddNewEpisode", u"Season", None))
        self.episodeNoLabel.setText(QCoreApplication.translate("AddNewEpisode", u"Episode No", None))
        self.episodeTitleLabel.setText(QCoreApplication.translate("AddNewEpisode", u"Episode Title", None))
        self.btnCancel.setText(QCoreApplication.translate("AddNewEpisode", u"Cancel", None))
        self.btnCancel.setAutoDefault(False)
        self.btnSave.setText(QCoreApplication.translate("AddNewEpisode", u"Save", None))
        self.lblStatus.setText("")
    # retranslateUi

#=======================================================================