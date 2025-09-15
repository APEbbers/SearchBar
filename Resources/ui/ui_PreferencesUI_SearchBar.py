# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PreferencesUI_SearchBarSBSbSs.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QSizePolicy, QSpacerItem, QWidget)
import Resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1008, 238)
        icon = QIcon()
        icon.addFile(u":/Resources/Icons/preferences-searchbar.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.EnableToolbar = Gui_PrefCheckBox(Form)
        self.EnableToolbar.setObjectName(u"EnableToolbar")
        self.EnableToolbar.setProperty(u"prefEntry", u"EnableToolbars")
        self.EnableToolbar.setProperty(u"prefPath", u"Mod/SearchBar")

        self.gridLayout_2.addWidget(self.EnableToolbar, 0, 0, 1, 1)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Sunken)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.EnableMouseBar = Gui_PrefCheckBox(self.frame)
        self.EnableMouseBar.setObjectName(u"EnableMouseBar")
        self.EnableMouseBar.setProperty(u"prefEntry", u"EnableMouseBar")
        self.EnableMouseBar.setProperty(u"prefPath", u"Mod/SearchBar")

        self.gridLayout.addWidget(self.EnableMouseBar, 0, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(25, 17, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(400, 100))
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label.setWordWrap(True)

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)

        self.ShowChangeLog = Gui_PrefCheckBox(Form)
        self.ShowChangeLog.setObjectName(u"ShowChangeLog")
        self.ShowChangeLog.setProperty(u"prefEntry", u"ShowChangeDialog")
        self.ShowChangeLog.setProperty(u"prefPath", u"Mod/SearchBar")

        self.gridLayout_2.addWidget(self.ShowChangeLog, 2, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 2)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setItalic(True)
        self.label_2.setFont(font)

        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"General", None))
        self.EnableToolbar.setText(QCoreApplication.translate("Form", u"Enable Search Bar toolbar", None))
        self.EnableMouseBar.setText(QCoreApplication.translate("Form", u"Enable the MouseBar", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:8pt; font-style:italic;\">When a shortcut key is pressed, the SearchBar will show at the mouse cursor. Pressing the shortcut key again will close the SearchBar. </span></p><p><span style=\" font-size:8pt; font-style:italic; \">The default shortcut is 'S'. This can be changed in FreeCAD's customize menu like with all other commands. Go to: 'Tools-&gt;Customize...-&gt;Keyboard. Find the category 'SearchBar'. There you can change the shortcut.</span></p></body></html>", None))
        self.ShowChangeLog.setText(QCoreApplication.translate("Form", u"Show 'What's new' dialog on startup", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"FreeCAD needs to be restarted before changes become active.", None))
    # retranslateUi

