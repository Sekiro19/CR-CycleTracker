# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'howToUsemiiXEC.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_Form(QWidget):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(423, 529)
        Form.setStyleSheet(u"#Form {background-color: rgb(33, 35, 55);}\n"
"/*QScrollBar*/\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 4px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 255, 0);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"	border: none;\n"
"    background: transparent;\n"
"	width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"	border: none;\n"
"    background: transparent;\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horiz"
                        "ontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 4px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 255, 0);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: transparent;\n"
"     height: 10px;\n"
"    border-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: transparent;\n"
"    height: 10px;\n"
"    border-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 415, 1546))
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 100))
        self.label.setStyleSheet(u"image: url(:/all/bin/images/gob.png);\n"
"background-color: Transparent;")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"QLabel {\n"
"	background-color: Transparent;\n"
"	font: 700 11pt \"Roboto\";\n"
"	color: rgb(255, 255, 255);	\n"
"	border: None;\n"
"}")
        self.label_6.setScaledContents(False)
        self.label_6.setWordWrap(True)

        self.gridLayout.addWidget(self.label_6, 12, 0, 1, 2)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"QLabel {\n"
"	background-color: Transparent;\n"
"	font: 700 11pt \"Roboto\";\n"
"	color: rgb(255, 255, 255);	\n"
"	border: None;\n"
"}")
        self.label_10.setScaledContents(False)
        self.label_10.setWordWrap(True)

        self.gridLayout.addWidget(self.label_10, 19, 0, 1, 2)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 400))
        self.label_9.setStyleSheet(u"background-color: Transparent;\n"
"image: url(:/all/bin/images/h3.png);\n"
"")
        self.label_9.setScaledContents(False)
        self.label_9.setWordWrap(True)

        self.gridLayout.addWidget(self.label_9, 18, 0, 1, 2)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"QLabel {\n"
"	background-color: Transparent;\n"
"	font: 700 11pt \"Roboto\";\n"
"	\n"
"	color: rgb(255, 0, 81);\n"
"	border: None;\n"
"}")

        self.gridLayout.addWidget(self.label_11, 21, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 22, 0, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel {\n"
"	background-color: Transparent;\n"
"	font: 700 11pt \"Roboto\";\n"
"	color: rgb(255, 255, 255);	\n"
"	border: None;\n"
"}")
        self.label_4.setScaledContents(False)
        self.label_4.setWordWrap(True)

        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 2)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel {\n"
"	background-color: Transparent;\n"
"	\n"
"	font: 800 14pt \"Roboto\";\n"
"	color: rgb(255, 255, 255);	\n"
"	border: None;\n"
"}")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 225))
        self.label_5.setStyleSheet(u"background-color: Transparent;\n"
"image: url(:/all/bin/images/h1.png);\n"
"")
        self.label_5.setScaledContents(False)
        self.label_5.setWordWrap(True)

        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 2)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 400))
        self.label_7.setStyleSheet(u"background-color: Transparent;\n"
"image: url(:/all/bin/images/h2.png);\n"
"")
        self.label_7.setScaledContents(False)
        self.label_7.setWordWrap(True)

        self.gridLayout.addWidget(self.label_7, 15, 0, 1, 2)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"QLabel {\n"
"	background-color: Transparent;\n"
"	font: 700 11pt \"Roboto\";\n"
"	color: rgb(255, 255, 255);	\n"
"	border: None;\n"
"}")
        self.label_12.setScaledContents(False)
        self.label_12.setWordWrap(True)

        self.gridLayout.addWidget(self.label_12, 13, 0, 1, 2)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(255, 0, 81);")
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 20, 0, 1, 2)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel {\n"
"	background-color: Transparent;\n"
"	font: 700 11pt \"Roboto\";\n"
"	color: rgb(255, 255, 255);	\n"
"	border: None;\n"
"}")
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(True)

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 2)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"QLabel {\n"
"	background-color: Transparent;\n"
"	font: 700 11pt \"Roboto\";\n"
"	color: rgb(255, 255, 255);	\n"
"	border: None;\n"
"}")
        self.label_8.setScaledContents(False)
        self.label_8.setWordWrap(True)

        self.gridLayout.addWidget(self.label_8, 17, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_6.setText(QCoreApplication.translate("Form", u"No card should be there when you select the cards region. the app needs to find these \"question marks\".\n"
"you need to select that area once every time you open this app. you can select it in other game mods so you dont lose your cups", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Try not to lose with all this advantage, that would be embarassing.", None))
        self.label_9.setText("")
        self.label_11.setText(QCoreApplication.translate("Form", u"Created by Sekiro", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"STEP 2: Click the \"Setup button\" and select the elixir bar and the cards region.", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"How to use cycle tracker ?", None))
        self.label_5.setText("")
        self.label_7.setText("")
        self.label_12.setText(QCoreApplication.translate("Form", u"STEP 3: Click the \"Start button\"", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"STEP 1: log in to another clash royal account from pc (use emulator) add yourself as a friend and spectate your match as soon as the game starts.you know how to do that right ?!", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"When your opponent starts playing cards his card cycle will showup on screen.", None))
    # retranslateUi

