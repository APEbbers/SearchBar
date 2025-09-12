# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ChangeDialogfsvcqV.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QSizePolicy,
    QWidget)
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

        self.webEngineView = QWebEngineView(Form)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setAutoFillBackground(True)
        self.webEngineView.setUrl(QUrl(u"about:blank"))

        self.gridLayout.addWidget(self.webEngineView, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.DoNotShowAgain.setText(QCoreApplication.translate("Form", u"Do not show again", None))
    # retranslateUi

