# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ChangeDialogsmxkzU.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QSizePolicy,
    QTextEdit, QWidget)
import Resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1051, 738)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.DoNotShowAgain = QCheckBox(Form)
        self.DoNotShowAgain.setObjectName(u"DoNotShowAgain")

        self.gridLayout.addWidget(self.DoNotShowAgain, 1, 0, 1, 1)

        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.DoNotShowAgain.setText(QCoreApplication.translate("Form", u"Do not show again", None))
        self.textEdit.setMarkdown(QCoreApplication.translate("Form", u"### New in SearchBar version 1.6.0:  With this release, the searchbar can be shown at cursor by pressing a shortcut key. The default shortcut is 'S'. To show the searchbar at the cursor, press 'S'. To hide it, press 'S' again.   ![2025-09-11 SearchBar at pointer](https://github.com/user-attachments/assets/9be0ec18-3fe4-4feb-85db-0cf4e0fe7665)     The shortcut can be changed. To do this, go to Tools->Customize..... The customize menu of FreeCAD will popup.   On the keyboard tab look for the catagory 'SearchBar'. The pointer command will be shown. Here you can set your prefferred shortcut.   ![2025-09-11 Change shortcut](https://github.com/user-attachments/assets/8f65c2aa-17b5-458f-acfd-3d107b1029ba)\n"
"\n"
"", None))
    # retranslateUi

