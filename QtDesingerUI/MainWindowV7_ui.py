# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowV7.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)
import QtDesingerUI.Icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(941, 587)
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
"    color: #FFFFFF;   /* Change to your desired color */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;  /* Adjust if you want the title to be left or right aligned */\n"
"	padding: 0 3px;\n"
"}\n"
"\n"
"QStatusBar{\n"
"	color: #FFFFFF;\n"
"	font-size: 14px;  /* Adjust the size as needed */\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QTex"
                        "tEdit{\n"
"	color: #FFFFFF;\n"
"	background-color: #1f232a;\n"
"	border: 1px solid #666;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: 0px solid #666;\n"
"    background: #1f232a;\n"
"    width: 7.5px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: #2a2e37;\n"
"}\n"
"\n"
"")
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
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.animationPage = QWidget()
        self.animationPage.setObjectName(u"animationPage")
        self.gridLayout_8 = QGridLayout(self.animationPage)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.animatedLabel = QLabel(self.animationPage)
        self.animatedLabel.setObjectName(u"animatedLabel")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(30)
        font1.setBold(False)
        font1.setItalic(True)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.animatedLabel.setFont(font1)
        self.animatedLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.animatedLabel, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.animationPage)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.horizontalLayout = QHBoxLayout(self.page_1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.page1_groupBox_Week1 = QGroupBox(self.page_1)
        self.page1_groupBox_Week1.setObjectName(u"page1_groupBox_Week1")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page1_groupBox_Week1.sizePolicy().hasHeightForWidth())
        self.page1_groupBox_Week1.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Source Serif Pro"])
        self.page1_groupBox_Week1.setFont(font2)
        self.page1_groupBox_Week1.setAlignment(Qt.AlignCenter)
        self.verticalLayout = QVBoxLayout(self.page1_groupBox_Week1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pb_Day1 = QPushButton(self.page1_groupBox_Week1)
        self.pb_Day1.setObjectName(u"pb_Day1")
        self.pb_Day1.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.pb_Day1)

        self.pb_Day3 = QPushButton(self.page1_groupBox_Week1)
        self.pb_Day3.setObjectName(u"pb_Day3")
        self.pb_Day3.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.pb_Day3)

        self.pb_Day5 = QPushButton(self.page1_groupBox_Week1)
        self.pb_Day5.setObjectName(u"pb_Day5")
        self.pb_Day5.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.pb_Day5)

        self.pb_Day7 = QPushButton(self.page1_groupBox_Week1)
        self.pb_Day7.setObjectName(u"pb_Day7")
        self.pb_Day7.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.pb_Day7)

        self.pb_Day9 = QPushButton(self.page1_groupBox_Week1)
        self.pb_Day9.setObjectName(u"pb_Day9")
        self.pb_Day9.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.pb_Day9)

        self.pb_Day11 = QPushButton(self.page1_groupBox_Week1)
        self.pb_Day11.setObjectName(u"pb_Day11")
        self.pb_Day11.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.pb_Day11)

        self.pb_Day13 = QPushButton(self.page1_groupBox_Week1)
        self.pb_Day13.setObjectName(u"pb_Day13")
        self.pb_Day13.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.pb_Day13)


        self.horizontalLayout.addWidget(self.page1_groupBox_Week1)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_2 = QGridLayout(self.page_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.mainPage2_groupBox = QGroupBox(self.page_2)
        self.mainPage2_groupBox.setObjectName(u"mainPage2_groupBox")
        font3 = QFont()
        self.mainPage2_groupBox.setFont(font3)
        self.gridLayout_3 = QGridLayout(self.mainPage2_groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.page2_groupBox_BackButton = QGroupBox(self.mainPage2_groupBox)
        self.page2_groupBox_BackButton.setObjectName(u"page2_groupBox_BackButton")
        self.page2_groupBox_BackButton.setStyleSheet(u"QGroupBox {\n"
"    font-size: 18px;  /* Adjust the size as needed */\n"
"    color: #FFD700;   /* Change to your desired color */\n"
"	border: 0;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.page2_groupBox_BackButton)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox = QGroupBox(self.page2_groupBox_BackButton)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_6 = QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pb_BackButton = QPushButton(self.groupBox)
        self.pb_BackButton.setObjectName(u"pb_BackButton")
        self.pb_BackButton.setIconSize(QSize(50, 50))

        self.gridLayout_6.addWidget(self.pb_BackButton, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 1, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox)


        self.gridLayout_3.addWidget(self.page2_groupBox_BackButton, 0, 0, 1, 1)

        self.page2_groupBox_TextEdit = QGroupBox(self.mainPage2_groupBox)
        self.page2_groupBox_TextEdit.setObjectName(u"page2_groupBox_TextEdit")
        self.page2_groupBox_TextEdit.setStyleSheet(u"QGroupBox {\n"
"    font-size: 18px;  /* Adjust the size as needed */\n"
"    color: #FFD700;   /* Change to your desired color */\n"
"	border: 0;\n"
"}")
        self.gridLayout_7 = QGridLayout(self.page2_groupBox_TextEdit)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_12, 1, 2, 1, 1)

        self.infoTextEdit = QTextEdit(self.page2_groupBox_TextEdit)
        self.infoTextEdit.setObjectName(u"infoTextEdit")
        self.infoTextEdit.setStyleSheet(u"ScrollBar:vertical {\n"
"        border: 2px solid grey;\n"
"        background-color: #1f232a;\n"
"        width: 15px;\n"
"        margin: 22px 0 22px 0;\n"
"    }\n"
"    QScrollBar::handle:vertical {\n"
"        background: #FFD700; \n"
"        min-height: 20px;\n"
"    }\n"
"    QScrollBar::add-line:vertical {\n"
"        border: 2px solid grey;\n"
"        background: #32CC99;\n"
"        height: 20px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"    QScrollBar::sub-line:vertical {\n"
"        border: 2px solid grey;\n"
"        background: #32CC99;\n"
"        height: 20px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }")
        self.infoTextEdit.setReadOnly(True)

        self.gridLayout_7.addWidget(self.infoTextEdit, 0, 0, 1, 3)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_11, 1, 0, 1, 1)

        self.pb_Undo = QPushButton(self.page2_groupBox_TextEdit)
        self.pb_Undo.setObjectName(u"pb_Undo")
        self.pb_Undo.setStyleSheet(u"QPushButton:disabled {\n"
"    background-color: #272727;\n"
"}\n"
"")
        self.pb_Undo.setIconSize(QSize(50, 50))

        self.gridLayout_7.addWidget(self.pb_Undo, 1, 1, 1, 1)


        self.gridLayout_3.addWidget(self.page2_groupBox_TextEdit, 0, 1, 1, 1)

        self.page2_groupBox_Title = QGroupBox(self.mainPage2_groupBox)
        self.page2_groupBox_Title.setObjectName(u"page2_groupBox_Title")
        self.page2_groupBox_Title.setStyleSheet(u"QGroupBox {\n"
"    font-size: 18px;  /* Adjust the size as needed */\n"
"    color: #FFD700;   /* Change to your desired color */\n"
"	border: 0;\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.page2_groupBox_Title)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(460, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.page2_dayLabel = QLabel(self.page2_groupBox_Title)
        self.page2_dayLabel.setObjectName(u"page2_dayLabel")
        font4 = QFont()
        font4.setPointSize(30)
        self.page2_dayLabel.setFont(font4)

        self.horizontalLayout_4.addWidget(self.page2_dayLabel)

        self.horizontalSpacer_3 = QSpacerItem(459, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.gridLayout_3.addWidget(self.page2_groupBox_Title, 1, 0, 1, 2)

        self.page2_groupBox_Videos = QGroupBox(self.mainPage2_groupBox)
        self.page2_groupBox_Videos.setObjectName(u"page2_groupBox_Videos")
        self.page2_groupBox_Videos.setStyleSheet(u"QGroupBox {\n"
"    font-size: 18px;  /* Adjust the size as needed */\n"
"    color: #FFD700;   /* Change to your desired color */\n"
"	border: 0;\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.page2_groupBox_Videos)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.groupBox_2 = QGroupBox(self.page2_groupBox_Videos)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pb_ImageTraining_1 = QPushButton(self.groupBox_2)
        self.pb_ImageTraining_1.setObjectName(u"pb_ImageTraining_1")
        self.pb_ImageTraining_1.setStyleSheet(u"QPushButton:disabled {\n"
"    background-color: #272727;\n"
"}\n"
"")
        self.pb_ImageTraining_1.setIconSize(QSize(50, 50))

        self.verticalLayout_4.addWidget(self.pb_ImageTraining_1)

        self.pb_ImageTraining_2 = QPushButton(self.groupBox_2)
        self.pb_ImageTraining_2.setObjectName(u"pb_ImageTraining_2")
        self.pb_ImageTraining_2.setStyleSheet(u"QPushButton:disabled {\n"
"    background-color: #272727;\n"
"}\n"
"")
        self.pb_ImageTraining_2.setIconSize(QSize(50, 50))

        self.verticalLayout_4.addWidget(self.pb_ImageTraining_2)

        self.pb_ImageTraining_3 = QPushButton(self.groupBox_2)
        self.pb_ImageTraining_3.setObjectName(u"pb_ImageTraining_3")
        self.pb_ImageTraining_3.setStyleSheet(u"QPushButton:disabled {\n"
"    background-color: #272727;\n"
"}\n"
"")
        self.pb_ImageTraining_3.setIconSize(QSize(50, 50))

        self.verticalLayout_4.addWidget(self.pb_ImageTraining_3)


        self.horizontalLayout_3.addWidget(self.groupBox_2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.groupBox_3 = QGroupBox(self.page2_groupBox_Videos)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pb_VideoTraining_2 = QPushButton(self.groupBox_3)
        self.pb_VideoTraining_2.setObjectName(u"pb_VideoTraining_2")
        self.pb_VideoTraining_2.setStyleSheet(u"QPushButton:disabled {\n"
"    background-color: #272727;\n"
"}\n"
"")
        self.pb_VideoTraining_2.setIconSize(QSize(50, 50))

        self.gridLayout_4.addWidget(self.pb_VideoTraining_2, 1, 0, 1, 1)

        self.pb_VideoTraining_1 = QPushButton(self.groupBox_3)
        self.pb_VideoTraining_1.setObjectName(u"pb_VideoTraining_1")
        self.pb_VideoTraining_1.setStyleSheet(u"QPushButton:disabled {\n"
"    background-color: #272727;\n"
"}\n"
"")
        self.pb_VideoTraining_1.setIconSize(QSize(50, 50))

        self.gridLayout_4.addWidget(self.pb_VideoTraining_1, 0, 0, 1, 1)

        self.pb_VideoTraining_3 = QPushButton(self.groupBox_3)
        self.pb_VideoTraining_3.setObjectName(u"pb_VideoTraining_3")
        self.pb_VideoTraining_3.setStyleSheet(u"QPushButton:disabled {\n"
"    background-color: #272727;\n"
"}\n"
"")
        self.pb_VideoTraining_3.setIconSize(QSize(50, 50))

        self.gridLayout_4.addWidget(self.pb_VideoTraining_3, 2, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.groupBox_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.gridLayout_3.addWidget(self.page2_groupBox_Videos, 3, 0, 1, 2)

        self.page2_groupBox_EcoVideo = QGroupBox(self.mainPage2_groupBox)
        self.page2_groupBox_EcoVideo.setObjectName(u"page2_groupBox_EcoVideo")
        self.page2_groupBox_EcoVideo.setStyleSheet(u"QGroupBox {\n"
"    font-size: 18px;  /* Adjust the size as needed */\n"
"    color: #FFD700;   /* Change to your desired color */\n"
"	border: 0;\n"
"}")
        self.horizontalLayout_6 = QHBoxLayout(self.page2_groupBox_EcoVideo)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)

        self.groupBox_6 = QGroupBox(self.page2_groupBox_EcoVideo)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        self.horizontalLayout_6.addWidget(self.groupBox_6)

        self.pb_ecologicalVideo = QPushButton(self.page2_groupBox_EcoVideo)
        self.pb_ecologicalVideo.setObjectName(u"pb_ecologicalVideo")
        self.pb_ecologicalVideo.setStyleSheet(u"QPushButton:disabled {\n"
"    background-color: #272727;\n"
"}\n"
"")
        self.pb_ecologicalVideo.setIconSize(QSize(50, 50))

        self.horizontalLayout_6.addWidget(self.pb_ecologicalVideo)

        self.groupBox_7 = QGroupBox(self.page2_groupBox_EcoVideo)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_9 = QGridLayout(self.groupBox_7)
        self.gridLayout_9.setObjectName(u"gridLayout_9")

        self.horizontalLayout_6.addWidget(self.groupBox_7)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_10)


        self.gridLayout_3.addWidget(self.page2_groupBox_EcoVideo, 2, 0, 1, 2)

        self.page2_groupBox_StartTraining = QGroupBox(self.mainPage2_groupBox)
        self.page2_groupBox_StartTraining.setObjectName(u"page2_groupBox_StartTraining")
        self.page2_groupBox_StartTraining.setStyleSheet(u"QGroupBox {\n"
"    font-size: 18px;  /* Adjust the size as needed */\n"
"    color: #FFD700;   /* Change to your desired color */\n"
"	border: 0;\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(self.page2_groupBox_StartTraining)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.groupBox_4 = QGroupBox(self.page2_groupBox_StartTraining)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.horizontalLayout_5.addWidget(self.groupBox_4)

        self.pb_startTraining = QPushButton(self.page2_groupBox_StartTraining)
        self.pb_startTraining.setObjectName(u"pb_startTraining")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pb_startTraining.sizePolicy().hasHeightForWidth())
        self.pb_startTraining.setSizePolicy(sizePolicy1)
        self.pb_startTraining.setStyleSheet(u"QPushButton:disabled {\n"
"    background-color: #272727;\n"
"}\n"
"")
        self.pb_startTraining.setIconSize(QSize(50, 50))

        self.horizontalLayout_5.addWidget(self.pb_startTraining)

        self.groupBox_5 = QGroupBox(self.page2_groupBox_StartTraining)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_5 = QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")

        self.horizontalLayout_5.addWidget(self.groupBox_5)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)


        self.gridLayout_3.addWidget(self.page2_groupBox_StartTraining, 4, 0, 1, 2)


        self.gridLayout_2.addWidget(self.mainPage2_groupBox, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Neurofeedback training", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionInfo.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.animatedLabel.setText(QCoreApplication.translate("MainWindow", u"Neurofeedback Training", None))
        self.page1_groupBox_Week1.setTitle(QCoreApplication.translate("MainWindow", u"Training Schedule", None))
        self.pb_Day1.setText(QCoreApplication.translate("MainWindow", u"Day 1", None))
        self.pb_Day3.setText(QCoreApplication.translate("MainWindow", u"Day 3", None))
        self.pb_Day5.setText(QCoreApplication.translate("MainWindow", u"Day 5", None))
        self.pb_Day7.setText(QCoreApplication.translate("MainWindow", u"Day 7", None))
        self.pb_Day9.setText(QCoreApplication.translate("MainWindow", u"Day 9", None))
        self.pb_Day11.setText(QCoreApplication.translate("MainWindow", u"Day 11", None))
        self.pb_Day13.setText(QCoreApplication.translate("MainWindow", u"Day 13", None))
        self.mainPage2_groupBox.setTitle("")
        self.page2_groupBox_BackButton.setTitle("")
        self.groupBox.setTitle("")
        self.pb_BackButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.page2_groupBox_TextEdit.setTitle("")
        self.infoTextEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">If You Need to Stop:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Feel uncomfortable? Press \u201cQ\u201d on your keyboard to stop the video immediately.\n"
"<ul s"
                        "tyle=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You can try again whenever you feel ready.</li></ul></li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Training Steps:</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Select Your Video:</span>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Start"
                        "ing today\u2019s training? Click \u201cTraining Video 1.\u201d</li></ul></li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Begin Training:</span>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Press \u201cStart Training.\u201d</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Focus your eyes on the red dot in the center during the training video.</li></ul></li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Move to the Next Video:</span>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-righ"
                        "t: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Finished a video? Select the next one, number order.</li></ul></li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">End with a Ecological Video:</span>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">All training videos green? Click \u201cEcological Video\u201d and press \u201cStart Training.\u201d</li></ul></li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Complete Your Training:</span>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin"
                        "-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Everything green, including \u201cEcological Video\u201d? You\u2019re done for today!</li></ul></li></ol>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Help for Interrupted Videos:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Interrupted during a video? Click \u201cUndo\u201d to make it available again if its green.</li></ul></body></html>", None))
        self.pb_Undo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.page2_groupBox_Title.setTitle("")
        self.page2_dayLabel.setText(QCoreApplication.translate("MainWindow", u"Day: X", None))
        self.page2_groupBox_Videos.setTitle("")
        self.groupBox_2.setTitle("")
        self.pb_ImageTraining_1.setText(QCoreApplication.translate("MainWindow", u"Image Training 1", None))
        self.pb_ImageTraining_2.setText(QCoreApplication.translate("MainWindow", u"Image Training 2", None))
        self.pb_ImageTraining_3.setText(QCoreApplication.translate("MainWindow", u"Image Training 3", None))
        self.groupBox_3.setTitle("")
        self.pb_VideoTraining_2.setText(QCoreApplication.translate("MainWindow", u"Video Training 2", None))
        self.pb_VideoTraining_1.setText(QCoreApplication.translate("MainWindow", u"Video Training 1", None))
        self.pb_VideoTraining_3.setText(QCoreApplication.translate("MainWindow", u"Video Training 3", None))
        self.page2_groupBox_EcoVideo.setTitle("")
        self.groupBox_6.setTitle("")
        self.pb_ecologicalVideo.setText(QCoreApplication.translate("MainWindow", u"Ecological Video", None))
        self.groupBox_7.setTitle("")
        self.page2_groupBox_StartTraining.setTitle("")
        self.groupBox_4.setTitle("")
        self.pb_startTraining.setText(QCoreApplication.translate("MainWindow", u"Start Training", None))
        self.groupBox_5.setTitle("")
    # retranslateUi

