# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowV3.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)
import QtDesingerUI.Icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(995, 630)
        font = QFont()
        font.setFamilies([u"Inter SemiBold"])
        font.setPointSize(12)
        font.setBold(True)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/MainWindow/KI_ICON_ONLY.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background-color: #1f232a;\n"
"    color: #EDEDED;\n"
"}\n"
"\n"
"#centralWidget{\n"
"	background-color: #1f232a;\n"
"}\n"
"\n"
"#groupBox{\n"
"	background-color: #1f232a;\n"
"}\n"
"\n"
"#groupBox_2{\n"
"	background-color: #1f232a;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #555;\n"
"    color: #EDEDED;\n"
"    border: 1px solid #666;\n"
"    padding: 5px 15px;\n"
"    border-radius: 3px;\n"
"    font-size: 18px;\n"
"    font-family: \"Inter SemiBold\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #444;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    font-size: 18px;  /* Adjust the size as needed */\n"
"    color: #FFD700;   /* Change to your desired color */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;  /* Adjust if you want the title to be left or right aligned */\n"
"	padding: 0 3px;\n"
"}\n"
"\n"
"QStatusBar{\n"
"	color: #FFD700;\n"
"	fon"
                        "t-size: 14px;  /* Adjust the size as needed */\n"
"\n"
"}")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionInfo = QAction(MainWindow)
        self.actionInfo.setObjectName(u"actionInfo")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_StartTraining = QPushButton(self.centralwidget)
        self.pb_StartTraining.setObjectName(u"pb_StartTraining")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_StartTraining.sizePolicy().hasHeightForWidth())
        self.pb_StartTraining.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/play-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_StartTraining.setIcon(icon1)
        self.pb_StartTraining.setIconSize(QSize(25, 25))

        self.gridLayout.addWidget(self.pb_StartTraining, 2, 0, 1, 2)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Source Serif Pro"])
        self.groupBox.setFont(font1)
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pb_VideoButton1 = QPushButton(self.groupBox)
        self.pb_VideoButton1.setObjectName(u"pb_VideoButton1")
        icon2 = QIcon()
        icon2.addFile(u":/Buttons/vlcsnap-2023-09-27-18h51m12s886.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_VideoButton1.setIcon(icon2)
        self.pb_VideoButton1.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.pb_VideoButton1)

        self.pb_VideoButton2 = QPushButton(self.groupBox)
        self.pb_VideoButton2.setObjectName(u"pb_VideoButton2")
        icon3 = QIcon()
        icon3.addFile(u":/Buttons/vlcsnap-2023-09-27-18h50m58s675.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_VideoButton2.setIcon(icon3)
        self.pb_VideoButton2.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.pb_VideoButton2)

        self.pb_VideoButton3 = QPushButton(self.groupBox)
        self.pb_VideoButton3.setObjectName(u"pb_VideoButton3")
        icon4 = QIcon()
        icon4.addFile(u":/Buttons/vlcsnap-2023-09-27-18h50m51s365.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_VideoButton3.setIcon(icon4)
        self.pb_VideoButton3.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.pb_VideoButton3)

        self.pb_VideoButton4 = QPushButton(self.groupBox)
        self.pb_VideoButton4.setObjectName(u"pb_VideoButton4")
        icon5 = QIcon()
        icon5.addFile(u":/Buttons/vlcsnap-2023-09-27-18h50m42s759.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_VideoButton4.setIcon(icon5)
        self.pb_VideoButton4.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.pb_VideoButton4)

        self.pb_VideoButton5 = QPushButton(self.groupBox)
        self.pb_VideoButton5.setObjectName(u"pb_VideoButton5")
        icon6 = QIcon()
        icon6.addFile(u":/Buttons/vlcsnap-2023-09-27-18h51m07s490.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_VideoButton5.setIcon(icon6)
        self.pb_VideoButton5.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.pb_VideoButton5)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 2, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Source Serif Pro"])
        font2.setBold(False)
        font2.setItalic(False)
        self.groupBox_2.setFont(font2)
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pb_VideoButton6 = QPushButton(self.groupBox_2)
        self.pb_VideoButton6.setObjectName(u"pb_VideoButton6")
        icon7 = QIcon()
        icon7.addFile(u":/Buttons/vlcsnap-2023-09-28-09h17m15s984.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_VideoButton6.setIcon(icon7)
        self.pb_VideoButton6.setIconSize(QSize(100, 100))

        self.verticalLayout_2.addWidget(self.pb_VideoButton6)

        self.pb_VideoButton7 = QPushButton(self.groupBox_2)
        self.pb_VideoButton7.setObjectName(u"pb_VideoButton7")
        icon8 = QIcon()
        icon8.addFile(u":/Buttons/vlcsnap-2023-09-28-09h18m50s144.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_VideoButton7.setIcon(icon8)
        self.pb_VideoButton7.setIconSize(QSize(100, 100))

        self.verticalLayout_2.addWidget(self.pb_VideoButton7)

        self.pb_VideoButton8 = QPushButton(self.groupBox_2)
        self.pb_VideoButton8.setObjectName(u"pb_VideoButton8")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pb_VideoButton8.sizePolicy().hasHeightForWidth())
        self.pb_VideoButton8.setSizePolicy(sizePolicy2)
        icon9 = QIcon()
        icon9.addFile(u":/Buttons/vlcsnap-2023-09-28-09h19m58s849.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_VideoButton8.setIcon(icon9)
        self.pb_VideoButton8.setIconSize(QSize(100, 100))

        self.verticalLayout_2.addWidget(self.pb_VideoButton8)


        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Neurofeedback training", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionInfo.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.pb_StartTraining.setText(QCoreApplication.translate("MainWindow", u"Start training", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Scientific training videos", None))
        self.pb_VideoButton1.setText(QCoreApplication.translate("MainWindow", u"Level 1", None))
        self.pb_VideoButton2.setText(QCoreApplication.translate("MainWindow", u"Level 2", None))
        self.pb_VideoButton3.setText(QCoreApplication.translate("MainWindow", u"Level 3", None))
        self.pb_VideoButton4.setText(QCoreApplication.translate("MainWindow", u"Level 4", None))
        self.pb_VideoButton5.setText(QCoreApplication.translate("MainWindow", u"Level 5", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Real-life training videos", None))
        self.pb_VideoButton6.setText(QCoreApplication.translate("MainWindow", u"Forest train ride", None))
        self.pb_VideoButton7.setText(QCoreApplication.translate("MainWindow", u"Winter train ride", None))
        self.pb_VideoButton8.setText(QCoreApplication.translate("MainWindow", u"New york subway", None))
    # retranslateUi

