#=======================================================================
# Description:
# UI component declaration for the Filters Dialog box
#=======================================================================
from PySide6.QtCore    import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui     import QIcon
from PySide6.QtWidgets import (
    QComboBox, 
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
class Ui_FiltersDialog(object):

    def setupUi(self, FiltersDialog):
        if not FiltersDialog.objectName():
            FiltersDialog.setObjectName(u"FiltersDialog")
        FiltersDialog.resize(493, 324)
        
        self.verticalLayout_2 = QVBoxLayout(FiltersDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 12)
        
        self.groupBox = QGroupBox(FiltersDialog)
        self.groupBox.setObjectName(u"groupBox")
        
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        
        self.seasonLabel = QLabel(self.groupBox)
        self.seasonLabel.setObjectName(u"seasonLabel")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.seasonLabel)

        self.txtActor = QLineEdit(self.groupBox)
        self.txtActor.setObjectName(u"txtActor")
        self.txtActor.setMinimumSize(QSize(350, 0))
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.txtActor)

        self.episodeNoLabel = QLabel(self.groupBox)
        self.episodeNoLabel.setObjectName(u"episodeNoLabel")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.episodeNoLabel)

        self.txtDirector = QLineEdit(self.groupBox)
        self.txtDirector.setObjectName(u"txtDirector")
        self.txtDirector.setMinimumSize(QSize(350, 0))
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.txtDirector)

        self.episodeTitleLabel = QLabel(self.groupBox)
        self.episodeTitleLabel.setObjectName(u"episodeTitleLabel")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.episodeTitleLabel)

        self.txtYear = QLineEdit(self.groupBox)
        self.txtYear.setObjectName(u"txtYear")
        self.txtYear.setMinimumSize(QSize(350, 0))
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.txtYear)

        self.sourceLabel = QLabel(self.groupBox)
        self.sourceLabel.setObjectName(u"sourceLabel")
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.sourceLabel)

        self.cbSource = QComboBox(self.groupBox)
        self.cbSource.addItem("")
        self.cbSource.setObjectName(u"cbSource")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbSource.sizePolicy().hasHeightForWidth())
        self.cbSource.setSizePolicy(sizePolicy)
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.cbSource)

        self.editionLabel = QLabel(self.groupBox)
        self.editionLabel.setObjectName(u"editionLabel")
        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.editionLabel)

        self.cbEdition = QComboBox(self.groupBox)
        self.cbEdition.addItem("")
        self.cbEdition.setObjectName(u"cbEdition")
        sizePolicy.setHeightForWidth(self.cbEdition.sizePolicy().hasHeightForWidth())
        self.cbEdition.setSizePolicy(sizePolicy)
        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.cbEdition)

        self.languageLabel = QLabel(self.groupBox)
        self.languageLabel.setObjectName(u"languageLabel")
        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.languageLabel)

        self.cbLanguage = QComboBox(self.groupBox)
        self.cbLanguage.addItem("")
        self.cbLanguage.setObjectName(u"cbLanguage")
        sizePolicy.setHeightForWidth(self.cbLanguage.sizePolicy().hasHeightForWidth())
        self.cbLanguage.setSizePolicy(sizePolicy)
        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.cbLanguage)

        self.toBurnLabel = QLabel(self.groupBox)
        self.toBurnLabel.setObjectName(u"toBurnLabel")
        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.toBurnLabel)

        self.cbToBurn = QComboBox(self.groupBox)
        self.cbToBurn.addItem("")
        self.cbToBurn.addItem("")
        self.cbToBurn.addItem("")
        self.cbToBurn.setObjectName(u"cbToBurn")
        sizePolicy.setHeightForWidth(self.cbToBurn.sizePolicy().hasHeightForWidth())
        self.cbToBurn.setSizePolicy(sizePolicy)
        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.cbToBurn)
        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblStatus = QLabel(self.groupBox)
        self.lblStatus.setObjectName(u"lblStatus")
        self.lblStatus.setStyleSheet(u"color: red;")
        self.horizontalLayout_2.addWidget(self.lblStatus)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnClose = QPushButton(self.groupBox)
        self.btnClose.setObjectName(u"btnClose")
        icon = QIcon()
        icon.addFile(u"images/icons/circle-xmark-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnClose.setIcon(icon)
        self.btnClose.setIconSize(QSize(13, 13))
        self.horizontalLayout_2.addWidget(self.btnClose)

        self.btnReset = QPushButton(self.groupBox)
        self.btnReset.setObjectName(u"btnReset")
        icon1 = QIcon()
        icon1.addFile(u"images/icons/circle-exclamation-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnReset.setIcon(icon1)
        self.btnReset.setIconSize(QSize(13, 13))
        self.horizontalLayout_2.addWidget(self.btnReset)

        self.btnApply = QPushButton(self.groupBox)
        self.btnApply.setObjectName(u"btnApply")
        icon2 = QIcon()
        icon2.addFile(u"images/icons/circle-check-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnApply.setIcon(icon2)
        self.btnApply.setIconSize(QSize(13, 13))
        self.horizontalLayout_2.addWidget(self.btnApply)

        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(FiltersDialog)

        QMetaObject.connectSlotsByName(FiltersDialog)
    # setupUi

    def retranslateUi(self, FiltersDialog):
        FiltersDialog.setWindowTitle(QCoreApplication.translate("FiltersDialog", u"Dialog", None))
        
        self.groupBox.setTitle("")
        self.lblStatus.setText("")

        self.seasonLabel.setText(QCoreApplication.translate("FiltersDialog", u"Actor", None))
        self.episodeNoLabel.setText(QCoreApplication.translate("FiltersDialog", u"Director", None))
        self.episodeTitleLabel.setText(QCoreApplication.translate("FiltersDialog", u"Year", None))
        self.sourceLabel.setText(QCoreApplication.translate("FiltersDialog", u"Source", None))
        self.cbSource.setItemText(0, QCoreApplication.translate("FiltersDialog", u"All Sources", None))

        self.editionLabel.setText(QCoreApplication.translate("FiltersDialog", u"Edition", None))
        self.cbEdition.setItemText(0, QCoreApplication.translate("FiltersDialog", u"All Editions", None))

        self.languageLabel.setText(QCoreApplication.translate("FiltersDialog", u"Language", None))
        self.cbLanguage.setItemText(0, QCoreApplication.translate("FiltersDialog", u"All Languages", None))

        self.toBurnLabel.setText(QCoreApplication.translate("FiltersDialog", u"To Burn", None))
        self.cbToBurn.setItemText(0, QCoreApplication.translate("FiltersDialog", u"All Status", None))
        self.cbToBurn.setItemText(1, QCoreApplication.translate("FiltersDialog", u"To Burn", None))
        self.cbToBurn.setItemText(2, QCoreApplication.translate("FiltersDialog", u"To Not Burn", None))

        self.btnClose.setText(QCoreApplication.translate("FiltersDialog", u"Cancel", None))
        self.btnClose.setAutoDefault(False)
        self.btnReset.setText(QCoreApplication.translate("FiltersDialog", u"Reset", None))
        self.btnReset.setAutoDefault(False)
        self.btnApply.setText(QCoreApplication.translate("FiltersDialog", u"Save", None))
    # retranslateUi

