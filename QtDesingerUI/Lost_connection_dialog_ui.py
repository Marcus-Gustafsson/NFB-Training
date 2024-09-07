# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Lost_connection_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
    QHBoxLayout, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)
import QtDesingerUI.Icons_rc

class Ui_LostConnectionConfirmationDialog(object):
    def setupUi(self, LostConnectionConfirmationDialog):
        if not LostConnectionConfirmationDialog.objectName():
            LostConnectionConfirmationDialog.setObjectName(u"LostConnectionConfirmationDialog")
        LostConnectionConfirmationDialog.resize(995, 325)
        icon = QIcon()
        icon.addFile(u":/MainWindow/KI_ICON_ONLY.png", QSize(), QIcon.Normal, QIcon.Off)
        LostConnectionConfirmationDialog.setWindowIcon(icon)
        LostConnectionConfirmationDialog.setStyleSheet(u"QDialog {\n"
"    background-color: #1f232a;\n"
"    color: #EDEDED;\n"
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
"	border: 0;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;  /* Adjust if you want the title to be left or right aligned */\n"
"	padding: 0 3px;\n"
"}\n"
"\n"
"QTextEdit{\n"
"	color: #FFD700;\n"
"	background-color: #1f232a;\n"
"	border: 0px solid #666;\n"
"    border-radius: 3px;\n"
"}\n"
"")
        self.gridLayout = QGridLayout(LostConnectionConfirmationDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.LostConnectionDialogGroupBox = QGroupBox(LostConnectionConfirmationDialog)
        self.LostConnectionDialogGroupBox.setObjectName(u"LostConnectionDialogGroupBox")
        self.verticalLayout = QVBoxLayout(self.LostConnectionDialogGroupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.LostConnectionTextGroupBox = QGroupBox(self.LostConnectionDialogGroupBox)
        self.LostConnectionTextGroupBox.setObjectName(u"LostConnectionTextGroupBox")
        self.gridLayout_2 = QGridLayout(self.LostConnectionTextGroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.LostConnectionTextEdit = QTextEdit(self.LostConnectionTextGroupBox)
        self.LostConnectionTextEdit.setObjectName(u"LostConnectionTextEdit")
        self.LostConnectionTextEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.LostConnectionTextEdit, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.LostConnectionTextGroupBox)

        self.UnderstoodButtonGroupBox = QGroupBox(self.LostConnectionDialogGroupBox)
        self.UnderstoodButtonGroupBox.setObjectName(u"UnderstoodButtonGroupBox")
        self.horizontalLayout = QHBoxLayout(self.UnderstoodButtonGroupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_Understood = QPushButton(self.UnderstoodButtonGroupBox)
        self.pb_Understood.setObjectName(u"pb_Understood")
        self.pb_Understood.setStyleSheet(u"QPushButton:disabled {\n"
"    background-color: #272727;\n"
"}\n"
"")
        self.pb_Understood.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.pb_Understood)


        self.verticalLayout.addWidget(self.UnderstoodButtonGroupBox)


        self.gridLayout.addWidget(self.LostConnectionDialogGroupBox, 0, 0, 1, 1)


        self.retranslateUi(LostConnectionConfirmationDialog)

        QMetaObject.connectSlotsByName(LostConnectionConfirmationDialog)
    # setupUi

    def retranslateUi(self, LostConnectionConfirmationDialog):
        LostConnectionConfirmationDialog.setWindowTitle(QCoreApplication.translate("LostConnectionConfirmationDialog", u"Connection Lost", None))
        self.LostConnectionDialogGroupBox.setTitle("")
        self.LostConnectionTextGroupBox.setTitle("")
        self.LostConnectionTextEdit.setHtml(QCoreApplication.translate("LostConnectionConfirmationDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">We've detected a potential issue with your Muse2 headband. Please take a moment to ensure everything is set up correctly.</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-size:12pt;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-lef"
                        "t:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Check the headband's connection:\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" font-size:12pt;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Make sure your Muse2 headband is connected.</li>\n"
"<li style=\" font-size:12pt;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Open your BlueMuse app and make sure the EEG stream is working accordingly to the user instructions.</li></ul></li>\n"
"<li style=\" font-size:12pt;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Verify the fitting of your headband:\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-i"
                        "ndent: 2;\">\n"
"<li style=\" font-size:12pt;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adjust the headband as described in the user instructions to ensure a proper fit.</li>\n"
"<li style=\" font-size:12pt;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The headband should be snug but comfortable, with sensors aligned correctly.</li></ul></li>\n"
"<li style=\" font-size:12pt;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If both the connection and fitting are correct, please try restarting the training video/image.</li></ol></body></html>", None))
        self.UnderstoodButtonGroupBox.setTitle("")
        self.pb_Understood.setText(QCoreApplication.translate("LostConnectionConfirmationDialog", u"Understood", None))
    # retranslateUi

