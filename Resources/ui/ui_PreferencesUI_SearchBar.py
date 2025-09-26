# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PreferencesUI_SearchBarErsQZN.ui'
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
from PySide.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QLabel, QSizePolicy, QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1008, 834)
        icon = QIcon()
        icon.addFile(u":/Resources/Icons/preferences-searchbar.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.gridLayout_6 = QGridLayout(Form)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setCheckable(False)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.EnableHighlight = Gui_PrefCheckBox(self.groupBox)
        self.EnableHighlight.setObjectName(u"EnableHighlight")
        self.EnableHighlight.setChecked(True)
        self.EnableHighlight.setProperty(u"prefEntry", u"EnableHighlight")
        self.EnableHighlight.setProperty(u"prefPath", u"Mod/SearchBar")

        self.gridLayout_2.addWidget(self.EnableHighlight, 9, 0, 1, 3)

        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Sunken)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.addWidget(self.frame, 2, 2, 1, 1)

        self.seAutoFocusMousBar = Gui_PrefCheckBox(self.groupBox)
        self.seAutoFocusMousBar.setObjectName(u"seAutoFocusMousBar")
        self.seAutoFocusMousBar.setChecked(True)
        self.seAutoFocusMousBar.setProperty(u"prefEntry", u"AutoFocusMouseBarEnabled")
        self.seAutoFocusMousBar.setProperty(u"prefPath", u"Mod/SearchBar")

        self.gridLayout_2.addWidget(self.seAutoFocusMousBar, 5, 0, 1, 3)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 6, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(400, 100))
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label, 2, 1, 1, 1)

        self.EnableToolbar = Gui_PrefCheckBox(self.groupBox)
        self.EnableToolbar.setObjectName(u"EnableToolbar")
        self.EnableToolbar.setChecked(True)
        self.EnableToolbar.setProperty(u"prefEntry", u"EnableToolbars")
        self.EnableToolbar.setProperty(u"prefPath", u"Mod/SearchBar")

        self.gridLayout_2.addWidget(self.EnableToolbar, 0, 0, 1, 3)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_4, 6, 1, 1, 2)

        self.ShowChangeLog = Gui_PrefCheckBox(self.groupBox)
        self.ShowChangeLog.setObjectName(u"ShowChangeLog")
        self.ShowChangeLog.setChecked(True)
        self.ShowChangeLog.setProperty(u"prefEntry", u"ShowChangeDialog")
        self.ShowChangeLog.setProperty(u"prefPath", u"Mod/SearchBar")

        self.gridLayout_2.addWidget(self.ShowChangeLog, 11, 0, 1, 3)

        self.EnableMouseBar = Gui_PrefCheckBox(self.groupBox)
        self.EnableMouseBar.setObjectName(u"EnableMouseBar")
        self.EnableMouseBar.setChecked(True)
        self.EnableMouseBar.setProperty(u"prefEntry", u"EnableMouseBar")
        self.EnableMouseBar.setProperty(u"prefPath", u"Mod/SearchBar")

        self.gridLayout_2.addWidget(self.EnableMouseBar, 1, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(25, 17, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 2, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.FilterBox = QGroupBox(Form)
        self.FilterBox.setObjectName(u"FilterBox")
        self.FilterBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.gridLayout_3 = QGridLayout(self.FilterBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkBox = Gui_PrefCheckBox(self.FilterBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)
        self.checkBox.setProperty(u"prefEntry", u"FilterToolbarCommands")
        self.checkBox.setProperty(u"prefPath", u"Mod/SearchBar")

        self.gridLayout_3.addWidget(self.checkBox, 0, 0, 1, 1)

        self.checkBox_3 = Gui_PrefCheckBox(self.FilterBox)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setProperty(u"prefEntry", u"FilterDocuments")
        self.checkBox_3.setProperty(u"prefPath", u"Mod/SearchBar")

        self.gridLayout_3.addWidget(self.checkBox_3, 2, 0, 1, 1)

        self.checkBox_2 = Gui_PrefCheckBox(self.FilterBox)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setProperty(u"prefEntry", u"FilterParameters")
        self.checkBox_2.setProperty(u"prefPath", u"Mod/SearchBar")

        self.gridLayout_3.addWidget(self.checkBox_2, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.FilterBox, 2, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_3, 3, 0, 1, 1)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setWordWrap(True)

        self.gridLayout_5.addWidget(self.label_3, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.Enable3DViewer = Gui_PrefCheckBox(self.groupBox_2)
        self.Enable3DViewer.setObjectName(u"Enable3DViewer")
        self.Enable3DViewer.setChecked(False)
        self.Enable3DViewer.setProperty(u"prefEntry", u"PreviewEnabled")
        self.Enable3DViewer.setProperty(u"prefPath", u"Mod/SearchBar")

        self.gridLayout_5.addWidget(self.Enable3DViewer, 0, 0, 1, 2)


        self.gridLayout_6.addWidget(self.groupBox_2, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setItalic(True)
        self.label_2.setFont(font)

        self.gridLayout_6.addWidget(self.label_2, 6, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"General", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"General preferences", None))
        self.EnableHighlight.setText(QCoreApplication.translate("Form", u"Highlight commands when hovering over them in the searchbar list", None))
        self.seAutoFocusMousBar.setText(QCoreApplication.translate("Form", u"Set focus to the MouseBar on activation", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:8pt; font-style:italic;\">When a shortcut key is pressed, the SearchBar will show at the mouse cursor. Pressing the shortcut key again will close the SearchBar. </span></p><p><span style=\" font-size:8pt; font-style:italic; \">The default shortcut is 'S'. This can be changed in FreeCAD's customize menu like with all other commands. Go to: 'Tools-&gt;Customize...-&gt;Keyboard. Find the category 'SearchBar'. There you can change the shortcut.</span></p></body></html>", None))
        self.EnableToolbar.setText(QCoreApplication.translate("Form", u"Enable SearchBar toolbar", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:8pt; font-style:italic;\">This sets the focus to the MouseBar when activated. You can start typing immediately. When enabled it is best to use the 'Escape' button to close the MouseBar.</span></p></body></html>", None))
        self.ShowChangeLog.setText(QCoreApplication.translate("Form", u"Show 'What's new' dialog on startup", None))
        self.EnableMouseBar.setText(QCoreApplication.translate("Form", u"Enable the MouseBar", None))
        self.FilterBox.setTitle(QCoreApplication.translate("Form", u"Filter preferences", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"Include toolbar commands", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"Include open documents and their features", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"Include parameters", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"3D Viewer settings", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:8pt; font-style:italic;\">Warning: the 3D preview has some stability issues. It can cause FreeCAD to crash (usually when quitting the application) and could in theory cause data loss, inside and outside of App.</span></p></body></html>", None))
        self.Enable3DViewer.setText(QCoreApplication.translate("Form", u"Enable the 3D-Viewer for open documents", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"FreeCAD needs to be restarted before changes become active.", None))
    # retranslateUi

