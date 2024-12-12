# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowpPmFPQ.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 360)
        MainWindow.setMinimumSize(QSize(400, 360))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.styles = QFrame(self.centralwidget)
        self.styles.setObjectName(u"styles")
        self.styles.setStyleSheet(u"#styles.QFrame {\n"
"background-color: rgb(33, 35, 55);\n"
"}\n"
"/*QLineEdit*/\n"
"QLineEdit {\n"
"	border: 2px solid rgb(103, 103, 103);\n"
"	border-radius: 5px;\n"
"	background-color: Transparent;\n"
"	color: rgb(121, 121, 121);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"}\n"
"QLineEdit:focus {\n"
"	color: rgb(230, 230, 230);\n"
"	border: 2px solid rgb(189, 255, 0);\n"
"}\n"
"/*QRadioButton*/\n"
"QRadioButton::indicator {\n"
"    border: 2px solid rgb(103, 103, 103);\n"
"	width: 16px;\n"
"	height: 16px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 2px solid rgb(141, 141, 141);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(186, 251, 0);\n"
"}")
        self.styles.setFrameShape(QFrame.StyledPanel)
        self.styles.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.styles)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, -1, -1, -1)
        self.frame = QFrame(self.styles)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toggleFps = QRadioButton(self.frame)
        self.toggleFps.setObjectName(u"toggleFps")
        self.toggleFps.setMaximumSize(QSize(21, 21))
        self.toggleFps.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleFps.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.toggleFps)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 25))
        self.label_4.setMaximumSize(QSize(100, 25))
        self.label_4.setStyleSheet(u"QLabel {\n"
"	font: 700 11pt \"Roboto\";\n"
"	color: rgb(255, 255, 255)	;\n"
"	border: None;\n"
"}")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_4.setMargin(20)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.editFps = QLineEdit(self.frame)
        self.editFps.setObjectName(u"editFps")
        self.editFps.setMaximumSize(QSize(50, 25))
        self.editFps.setMaxLength(3)
        self.editFps.setClearButtonEnabled(False)

        self.horizontalLayout_3.addWidget(self.editFps)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignLeft)

        self.fps = QLabel(self.styles)
        self.fps.setObjectName(u"fps")
        self.fps.setMaximumSize(QSize(100, 100))
        self.fps.setStyleSheet(u"QLabel {\n"
"	\n"
"	font: 12pt \"Terminal\";\n"
"	color: rgb(0, 255, 0);	\n"
"	border: None;\n"
"}")

        self.horizontalLayout_2.addWidget(self.fps)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.midFrame = QFrame(self.styles)
        self.midFrame.setObjectName(u"midFrame")
        self.midFrame.setStyleSheet(u"")
        self.midFrame.setFrameShape(QFrame.NoFrame)
        self.midFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.midFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.midFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 15))
        self.label_3.setMaximumSize(QSize(16777215, 20))
        self.label_3.setStyleSheet(u"QLabel {\n"
"	font: 700 11pt \"Roboto\";\n"
"	color: rgb(255, 255, 255)	;\n"
"	border: None;\n"
"}")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setMargin(20)

        self.verticalLayout_2.addWidget(self.label_3)

        self.screen = QFrame(self.midFrame)
        self.screen.setObjectName(u"screen")
        self.screen.setStyleSheet(u"QFrame {\n"
"	border: 1px solid rgb(255, 0, 81);\n"
"	border-radius: 3px\n"
"}\n"
"")
        self.screen.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_9 = QVBoxLayout(self.screen)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.screenBar = QLabel(self.screen)
        self.screenBar.setObjectName(u"screenBar")
        self.screenBar.setMinimumSize(QSize(0, 40))
        self.screenBar.setMaximumSize(QSize(16777215, 50))
        self.screenBar.setStyleSheet(u"QFrame {\n"
"	border-top: None;\n"
"	border-right: None;\n"
"	border-left: None;\n"
"}")
        self.screenBar.setScaledContents(False)
        self.screenBar.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.screenBar)

        self.hand = QGridLayout()
        self.hand.setObjectName(u"hand")
        self.hand.setHorizontalSpacing(10)
        self.hand.setVerticalSpacing(6)
        self.hand.setContentsMargins(10, 0, 10, 10)
        self.c7 = QLabel(self.screen)
        self.c7.setObjectName(u"c7")
        self.c7.setMinimumSize(QSize(90, 70))
        self.c7.setMaximumSize(QSize(90, 70))
        self.c7.setStyleSheet(u"")
        self.c7.setAlignment(Qt.AlignCenter)

        self.hand.addWidget(self.c7, 3, 3, 1, 1)

        self.c2 = QLabel(self.screen)
        self.c2.setObjectName(u"c2")
        self.c2.setMinimumSize(QSize(90, 70))
        self.c2.setMaximumSize(QSize(90, 70))
        self.c2.setStyleSheet(u"")
        self.c2.setAlignment(Qt.AlignCenter)

        self.hand.addWidget(self.c2, 1, 2, 1, 1)

        self.c4 = QLabel(self.screen)
        self.c4.setObjectName(u"c4")
        self.c4.setMinimumSize(QSize(90, 70))
        self.c4.setMaximumSize(QSize(90, 70))
        self.c4.setStyleSheet(u"")
        self.c4.setAlignment(Qt.AlignCenter)

        self.hand.addWidget(self.c4, 3, 0, 1, 1)

        self.c1 = QLabel(self.screen)
        self.c1.setObjectName(u"c1")
        self.c1.setMinimumSize(QSize(90, 70))
        self.c1.setMaximumSize(QSize(90, 70))
        self.c1.setStyleSheet(u"")
        self.c1.setAlignment(Qt.AlignCenter)

        self.hand.addWidget(self.c1, 1, 1, 1, 1)

        self.c3 = QLabel(self.screen)
        self.c3.setObjectName(u"c3")
        self.c3.setMinimumSize(QSize(90, 70))
        self.c3.setMaximumSize(QSize(90, 70))
        self.c3.setStyleSheet(u"")
        self.c3.setAlignment(Qt.AlignCenter)

        self.hand.addWidget(self.c3, 1, 3, 1, 1)

        self.c5 = QLabel(self.screen)
        self.c5.setObjectName(u"c5")
        self.c5.setMinimumSize(QSize(90, 70))
        self.c5.setMaximumSize(QSize(90, 70))
        self.c5.setStyleSheet(u"")
        self.c5.setAlignment(Qt.AlignCenter)

        self.hand.addWidget(self.c5, 3, 1, 1, 1)

        self.c0 = QLabel(self.screen)
        self.c0.setObjectName(u"c0")
        self.c0.setMinimumSize(QSize(90, 70))
        self.c0.setMaximumSize(QSize(90, 70))
        self.c0.setStyleSheet(u"")
        self.c0.setAlignment(Qt.AlignCenter)

        self.hand.addWidget(self.c0, 1, 0, 1, 1)

        self.c6 = QLabel(self.screen)
        self.c6.setObjectName(u"c6")
        self.c6.setMinimumSize(QSize(90, 70))
        self.c6.setMaximumSize(QSize(90, 70))
        self.c6.setStyleSheet(u"")
        self.c6.setAlignment(Qt.AlignCenter)

        self.hand.addWidget(self.c6, 3, 2, 1, 1)

        self.label = QLabel(self.screen)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 10))
        self.label.setStyleSheet(u"QLabel {\n"
"	font: 700 11pt \"Roboto\";\n"
"	color: rgb(255, 255, 255);	\n"
"	border: None;\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.hand.addWidget(self.label, 0, 0, 1, 4)

        self.label_2 = QLabel(self.screen)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 20))
        self.label_2.setMaximumSize(QSize(16777215, 10))
        self.label_2.setStyleSheet(u"QLabel {\n"
"	font: 700 11pt \"Roboto\";\n"
"	color: rgb(255, 255, 255);	\n"
"	border: None;\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.hand.addWidget(self.label_2, 2, 0, 1, 4)


        self.verticalLayout_9.addLayout(self.hand)


        self.verticalLayout_2.addWidget(self.screen)


        self.verticalLayout_3.addWidget(self.midFrame)

        self.bottomFrame = QFrame(self.styles)
        self.bottomFrame.setObjectName(u"bottomFrame")
        self.bottomFrame.setMaximumSize(QSize(16777215, 60))
        self.bottomFrame.setFrameShape(QFrame.NoFrame)
        self.bottomFrame.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.bottomFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_start = QPushButton(self.bottomFrame)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy)
        self.btn_start.setMinimumSize(QSize(0, 35))
        self.btn_start.setMaximumSize(QSize(100, 35))
        self.btn_start.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(92, 108, 255);\n"
"	border-radius: 5px;\n"
"	font: 700 11pt \"Roboto\";\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"	border-left: 2px solid  rgb(233, 12, 89);\n"
"\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(71, 82, 196);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(60, 69, 165);\n"
"}")
        self.btn_start.setIconSize(QSize(24, 24))
        self.btn_start.setCheckable(False)
        self.btn_start.setChecked(False)
        self.btn_start.setAutoRepeat(False)
        self.btn_start.setAutoExclusive(False)

        self.gridLayout.addWidget(self.btn_start, 1, 0, 1, 1)

        self.btn_setup = QPushButton(self.bottomFrame)
        self.btn_setup.setObjectName(u"btn_setup")
        sizePolicy.setHeightForWidth(self.btn_setup.sizePolicy().hasHeightForWidth())
        self.btn_setup.setSizePolicy(sizePolicy)
        self.btn_setup.setMinimumSize(QSize(0, 35))
        self.btn_setup.setMaximumSize(QSize(100, 35))
        self.btn_setup.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(92, 108, 255);\n"
"	border-radius: 5px;\n"
"	font: 700 11pt \"Roboto\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(71, 82, 196);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(60, 69, 165);\n"
"}")
        self.btn_setup.setIconSize(QSize(24, 24))
        self.btn_setup.setCheckable(False)
        self.btn_setup.setChecked(False)
        self.btn_setup.setAutoRepeat(False)
        self.btn_setup.setAutoExclusive(False)

        self.gridLayout.addWidget(self.btn_setup, 1, 1, 1, 1)

        self.btn_howToUse = QPushButton(self.bottomFrame)
        self.btn_howToUse.setObjectName(u"btn_howToUse")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_howToUse.sizePolicy().hasHeightForWidth())
        self.btn_howToUse.setSizePolicy(sizePolicy1)
        self.btn_howToUse.setMinimumSize(QSize(30, 30))
        self.btn_howToUse.setMaximumSize(QSize(30, 30))
        self.btn_howToUse.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_howToUse.setStyleSheet(u"QPushButton {\n"
"	background-color:  transparent;\n"
"	background-repeat: no-reperat;\n"
"	border-radius: 3px;\n"
"	image: url(:/all/bin/images/gob.png);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:  rgb(103, 110, 121);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:  rgb(85, 90, 99);\n"
"}")

        self.gridLayout.addWidget(self.btn_howToUse, 1, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.bottomFrame)


        self.verticalLayout.addWidget(self.styles)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.toggleFps.setToolTip(QCoreApplication.translate("MainWindow", u"Toggle FPS limiter", None))
#endif // QT_CONFIG(tooltip)
        self.toggleFps.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"FPS limit", None))
        self.fps.setText(QCoreApplication.translate("MainWindow", u"FPS:0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Elixir Bar", None))
        self.screenBar.setText("")
        self.c7.setText("")
        self.c2.setText("")
        self.c4.setText("")
        self.c1.setText("")
        self.c3.setText("")
        self.c5.setText("")
        self.c0.setText("")
        self.c6.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cards In Hand", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Next Cards", None))
#if QT_CONFIG(tooltip)
        self.btn_start.setToolTip(QCoreApplication.translate("MainWindow", u"Start screen process", None))
#endif // QT_CONFIG(tooltip)
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
#if QT_CONFIG(tooltip)
        self.btn_setup.setToolTip(QCoreApplication.translate("MainWindow", u"Select process region", None))
#endif // QT_CONFIG(tooltip)
        self.btn_setup.setText(QCoreApplication.translate("MainWindow", u"Setup", None))
#if QT_CONFIG(tooltip)
        self.btn_howToUse.setToolTip(QCoreApplication.translate("MainWindow", u"How To Use", None))
#endif // QT_CONFIG(tooltip)
        self.btn_howToUse.setText("")
    # retranslateUi

