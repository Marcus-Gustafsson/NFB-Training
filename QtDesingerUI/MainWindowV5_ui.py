# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowV5.ui'
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
        MainWindow.resize(1070, 824)
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
"	font-size: 14px;  /* Adjust the size as needed */\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"	color: #FFD700;\n"
"}\n"
"\n"
"QTextEd"
                        "it{\n"
"	color: #FFD700;\n"
"	background-color: #1f232a;\n"
"	border: 1px solid #666;\n"
"    border-radius: 3px;\n"
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

        self.pb_Day2 = QPushButton(self.page1_groupBox_Week1)
        self.pb_Day2.setObjectName(u"pb_Day2")
        self.pb_Day2.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.pb_Day2)

        self.pb_Day3 = QPushButton(self.page1_groupBox_Week1)
        self.pb_Day3.setObjectName(u"pb_Day3")
        self.pb_Day3.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.pb_Day3)

        self.pb_Day4 = QPushButton(self.page1_groupBox_Week1)
        self.pb_Day4.setObjectName(u"pb_Day4")
        self.pb_Day4.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.pb_Day4)

        self.pb_Day5 = QPushButton(self.page1_groupBox_Week1)
        self.pb_Day5.setObjectName(u"pb_Day5")
        self.pb_Day5.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.pb_Day5)

        self.pb_Day6 = QPushButton(self.page1_groupBox_Week1)
        self.pb_Day6.setObjectName(u"pb_Day6")
        self.pb_Day6.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.pb_Day6)

        self.pb_Day7 = QPushButton(self.page1_groupBox_Week1)
        self.pb_Day7.setObjectName(u"pb_Day7")
        self.pb_Day7.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.pb_Day7)


        self.horizontalLayout.addWidget(self.page1_groupBox_Week1)

        self.page1_groupBox_Week2 = QGroupBox(self.page_1)
        self.page1_groupBox_Week2.setObjectName(u"page1_groupBox_Week2")
        sizePolicy.setHeightForWidth(self.page1_groupBox_Week2.sizePolicy().hasHeightForWidth())
        self.page1_groupBox_Week2.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"Source Serif Pro"])
        font3.setBold(False)
        font3.setItalic(False)
        self.page1_groupBox_Week2.setFont(font3)
        self.page1_groupBox_Week2.setAlignment(Qt.AlignCenter)
        self.verticalLayout_2 = QVBoxLayout(self.page1_groupBox_Week2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pb_Day8 = QPushButton(self.page1_groupBox_Week2)
        self.pb_Day8.setObjectName(u"pb_Day8")
        self.pb_Day8.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.pb_Day8)

        self.pb_Day9 = QPushButton(self.page1_groupBox_Week2)
        self.pb_Day9.setObjectName(u"pb_Day9")
        self.pb_Day9.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.pb_Day9)

        self.pb_Day10 = QPushButton(self.page1_groupBox_Week2)
        self.pb_Day10.setObjectName(u"pb_Day10")
        self.pb_Day10.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.pb_Day10)

        self.pb_Day11 = QPushButton(self.page1_groupBox_Week2)
        self.pb_Day11.setObjectName(u"pb_Day11")
        self.pb_Day11.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.pb_Day11)

        self.pb_Day12 = QPushButton(self.page1_groupBox_Week2)
        self.pb_Day12.setObjectName(u"pb_Day12")
        self.pb_Day12.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.pb_Day12)

        self.pb_Day13 = QPushButton(self.page1_groupBox_Week2)
        self.pb_Day13.setObjectName(u"pb_Day13")
        self.pb_Day13.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.pb_Day13)

        self.pb_Day14 = QPushButton(self.page1_groupBox_Week2)
        self.pb_Day14.setObjectName(u"pb_Day14")
        self.pb_Day14.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.pb_Day14)


        self.horizontalLayout.addWidget(self.page1_groupBox_Week2)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_2 = QGridLayout(self.page_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.mainPage2_groupBox = QGroupBox(self.page_2)
        self.mainPage2_groupBox.setObjectName(u"mainPage2_groupBox")
        font4 = QFont()
        self.mainPage2_groupBox.setFont(font4)
        self.verticalLayout_3 = QVBoxLayout(self.mainPage2_groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
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

        self.gridLayout_6.addItem(self.horizontalSpacer, 0, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_2.addItem(self.verticalSpacer)

        self.page2_groupBox_TextEdit = QGroupBox(self.page2_groupBox_BackButton)
        self.page2_groupBox_TextEdit.setObjectName(u"page2_groupBox_TextEdit")
        self.gridLayout_7 = QGridLayout(self.page2_groupBox_TextEdit)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalSpacer_9 = QSpacerItem(192, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_9, 0, 0, 1, 1)

        self.textEdit = QTextEdit(self.page2_groupBox_TextEdit)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.gridLayout_7.addWidget(self.textEdit, 1, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.page2_groupBox_TextEdit)


        self.verticalLayout_3.addWidget(self.page2_groupBox_BackButton)

        self.page2_groupBox_Title = QGroupBox(self.mainPage2_groupBox)
        self.page2_groupBox_Title.setObjectName(u"page2_groupBox_Title")
        self.page2_groupBox_Title.setStyleSheet(u"QGroupBox {\n"
"    font-size: 18px;  /* Adjust the size as needed */\n"
"    color: #FFD700;   /* Change to your desired color */\n"
"	border: 0;\n"
"}")
        self.gridLayout_3 = QGridLayout(self.page2_groupBox_Title)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.page2_dayLabel = QLabel(self.page2_groupBox_Title)
        self.page2_dayLabel.setObjectName(u"page2_dayLabel")
        font5 = QFont()
        font5.setPointSize(30)
        self.page2_dayLabel.setFont(font5)

        self.gridLayout_3.addWidget(self.page2_dayLabel, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 0, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.page2_groupBox_Title)

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
        self.pb_TrainingVideo_1 = QPushButton(self.groupBox_2)
        self.pb_TrainingVideo_1.setObjectName(u"pb_TrainingVideo_1")
        self.pb_TrainingVideo_1.setStyleSheet(u"QPushButton:disabled {\n"
"    background-color: #272727;\n"
"}\n"
"")
        self.pb_TrainingVideo_1.setIconSize(QSize(50, 50))

        self.verticalLayout_4.addWidget(self.pb_TrainingVideo_1)

        self.pb_TrainingVideo_2 = QPushButton(self.groupBox_2)
        self.pb_TrainingVideo_2.setObjectName(u"pb_TrainingVideo_2")
        self.pb_TrainingVideo_2.setStyleSheet(u"QPushButton:disabled {\n"
"    background-color: #272727;\n"
"}\n"
"")
        self.pb_TrainingVideo_2.setIconSize(QSize(50, 50))

        self.verticalLayout_4.addWidget(self.pb_TrainingVideo_2)

        self.pb_TrainingVideo_3 = QPushButton(self.groupBox_2)
        self.pb_TrainingVideo_3.setObjectName(u"pb_TrainingVideo_3")
        self.pb_TrainingVideo_3.setStyleSheet(u"QPushButton:disabled {\n"
"    background-color: #272727;\n"
"}\n"
"")
        self.pb_TrainingVideo_3.setIconSize(QSize(50, 50))

        self.verticalLayout_4.addWidget(self.pb_TrainingVideo_3)


        self.horizontalLayout_3.addWidget(self.groupBox_2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.groupBox_3 = QGroupBox(self.page2_groupBox_Videos)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pb_ecologicalVideo = QPushButton(self.groupBox_3)
        self.pb_ecologicalVideo.setObjectName(u"pb_ecologicalVideo")
        self.pb_ecologicalVideo.setStyleSheet(u"QPushButton:disabled {\n"
"    background-color: #272727;\n"
"}\n"
"")
        self.pb_ecologicalVideo.setIconSize(QSize(50, 50))

        self.gridLayout_4.addWidget(self.pb_ecologicalVideo, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.groupBox_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addWidget(self.page2_groupBox_Videos)

        self.page2_groupBox_training = QGroupBox(self.mainPage2_groupBox)
        self.page2_groupBox_training.setObjectName(u"page2_groupBox_training")
        self.page2_groupBox_training.setStyleSheet(u"QGroupBox {\n"
"    font-size: 18px;  /* Adjust the size as needed */\n"
"    color: #FFD700;   /* Change to your desired color */\n"
"	border: 0;\n"
"}")
        self.gridLayout_5 = QGridLayout(self.page2_groupBox_training)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_8, 0, 2, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_7, 0, 0, 1, 1)

        self.pb_startTraining = QPushButton(self.page2_groupBox_training)
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

        self.gridLayout_5.addWidget(self.pb_startTraining, 0, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.page2_groupBox_training)


        self.gridLayout_2.addWidget(self.mainPage2_groupBox, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Neurofeedback training", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionInfo.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.animatedLabel.setText(QCoreApplication.translate("MainWindow", u"Neurofeedback Training", None))
        self.page1_groupBox_Week1.setTitle(QCoreApplication.translate("MainWindow", u"Week 1", None))
        self.pb_Day1.setText(QCoreApplication.translate("MainWindow", u"Day 1", None))
        self.pb_Day2.setText(QCoreApplication.translate("MainWindow", u"Day 2", None))
        self.pb_Day3.setText(QCoreApplication.translate("MainWindow", u"Day 3", None))
        self.pb_Day4.setText(QCoreApplication.translate("MainWindow", u"Day 4", None))
        self.pb_Day5.setText(QCoreApplication.translate("MainWindow", u"Day 5", None))
        self.pb_Day6.setText(QCoreApplication.translate("MainWindow", u"Day 6", None))
        self.pb_Day7.setText(QCoreApplication.translate("MainWindow", u"Day 7", None))
        self.page1_groupBox_Week2.setTitle(QCoreApplication.translate("MainWindow", u"Week 2", None))
        self.pb_Day8.setText(QCoreApplication.translate("MainWindow", u"Day 8", None))
        self.pb_Day9.setText(QCoreApplication.translate("MainWindow", u"Day 9", None))
        self.pb_Day10.setText(QCoreApplication.translate("MainWindow", u"Day 10", None))
        self.pb_Day11.setText(QCoreApplication.translate("MainWindow", u"Day 11", None))
        self.pb_Day12.setText(QCoreApplication.translate("MainWindow", u"Day 12", None))
        self.pb_Day13.setText(QCoreApplication.translate("MainWindow", u"Day 13", None))
        self.pb_Day14.setText(QCoreApplication.translate("MainWindow", u"Day 14", None))
        self.mainPage2_groupBox.setTitle("")
        self.page2_groupBox_BackButton.setTitle("")
        self.groupBox.setTitle("")
        self.pb_BackButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.page2_groupBox_TextEdit.setTitle("")
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-style:italic;\">Training Instructions</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-size:11pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pick a &quot;Training Video&quot;. "
                        "If it's your first session today, choose &quot;Training Video 1&quot;.</li>\n"
"<li style=\" font-size:11pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Press &quot;Start Training&quot; to begin.</li>\n"
"<li style=\" font-size:11pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">After finishing, choose the next numbered video.</li>\n"
"<li style=\" font-size:11pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If all &quot;Training Videos&quot; are green, select &quot;Ecological Video&quot;.</li>\n"
"<li style=\" font-size:11pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Press &quot;Start Training&quot; again.</li></ol>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-bloc"
                        "k-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700;\">Note:</span><span style=\" font-size:11pt;\"> Once all videos are green, you're done for the day!</span></p></body></html>", None))
        self.page2_groupBox_Title.setTitle("")
        self.page2_dayLabel.setText(QCoreApplication.translate("MainWindow", u"Day: X", None))
        self.page2_groupBox_Videos.setTitle("")
        self.groupBox_2.setTitle("")
        self.pb_TrainingVideo_1.setText(QCoreApplication.translate("MainWindow", u"Training Video 1", None))
        self.pb_TrainingVideo_2.setText(QCoreApplication.translate("MainWindow", u"Training Video 2", None))
        self.pb_TrainingVideo_3.setText(QCoreApplication.translate("MainWindow", u"Training Video 3", None))
        self.groupBox_3.setTitle("")
        self.pb_ecologicalVideo.setText(QCoreApplication.translate("MainWindow", u"Ecological Video", None))
        self.page2_groupBox_training.setTitle("")
        self.pb_startTraining.setText(QCoreApplication.translate("MainWindow", u"Start Training", None))
    # retranslateUi

