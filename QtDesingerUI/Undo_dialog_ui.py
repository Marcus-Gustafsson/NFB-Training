# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Undo_dialog.ui'
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

class Ui_undoConfirmationDialog(object):
    def setupUi(self, undoConfirmationDialog):
        if not undoConfirmationDialog.objectName():
            undoConfirmationDialog.setObjectName(u"undoConfirmationDialog")
        undoConfirmationDialog.resize(733, 196)
        icon = QIcon()
        icon.addFile(u":/MainWindow/KI_ICON_ONLY.png", QSize(), QIcon.Normal, QIcon.Off)
        undoConfirmationDialog.setWindowIcon(icon)
        undoConfirmationDialog.setStyleSheet(u"QDialog {\n"
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
        self.gridLayout = QGridLayout(undoConfirmationDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.UndoDialogGroupBox = QGroupBox(undoConfirmationDialog)
        self.UndoDialogGroupBox.setObjectName(u"UndoDialogGroupBox")
        self.verticalLayout = QVBoxLayout(self.UndoDialogGroupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.UndoTextGroupBox = QGroupBox(self.UndoDialogGroupBox)
        self.UndoTextGroupBox.setObjectName(u"UndoTextGroupBox")
        self.gridLayout_2 = QGridLayout(self.UndoTextGroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.UndoTextEdit = QTextEdit(self.UndoTextGroupBox)
        self.UndoTextEdit.setObjectName(u"UndoTextEdit")
        self.UndoTextEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.UndoTextEdit, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.UndoTextGroupBox)

        self.UndoButtonsYesNoGroupBox = QGroupBox(self.UndoDialogGroupBox)
        self.UndoButtonsYesNoGroupBox.setObjectName(u"UndoButtonsYesNoGroupBox")
        self.horizontalLayout = QHBoxLayout(self.UndoButtonsYesNoGroupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_Undo_Yes = QPushButton(self.UndoButtonsYesNoGroupBox)
        self.pb_Undo_Yes.setObjectName(u"pb_Undo_Yes")
        self.pb_Undo_Yes.setStyleSheet(u"QPushButton:disabled {\n"
"    background-color: #272727;\n"
"}\n"
"")
        self.pb_Undo_Yes.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.pb_Undo_Yes)

        self.pb_Undo_No = QPushButton(self.UndoButtonsYesNoGroupBox)
        self.pb_Undo_No.setObjectName(u"pb_Undo_No")
        self.pb_Undo_No.setStyleSheet(u"QPushButton:disabled {\n"
"    background-color: #272727;\n"
"}\n"
"")
        self.pb_Undo_No.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.pb_Undo_No)


        self.verticalLayout.addWidget(self.UndoButtonsYesNoGroupBox)


        self.gridLayout.addWidget(self.UndoDialogGroupBox, 0, 0, 1, 1)


        self.retranslateUi(undoConfirmationDialog)

        QMetaObject.connectSlotsByName(undoConfirmationDialog)
    # setupUi

    def retranslateUi(self, undoConfirmationDialog):
        undoConfirmationDialog.setWindowTitle(QCoreApplication.translate("undoConfirmationDialog", u"Undo", None))
        self.UndoDialogGroupBox.setTitle("")
        self.UndoTextGroupBox.setTitle("")
        self.UndoTextEdit.setHtml(QCoreApplication.translate("undoConfirmationDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700;\">Are you sure you want to go back and redo the last played training video? </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700;\">Your latest results will be cleared.</span></p></body></htm"
                        "l>", None))
        self.UndoButtonsYesNoGroupBox.setTitle("")
        self.pb_Undo_Yes.setText(QCoreApplication.translate("undoConfirmationDialog", u"Yes", None))
        self.pb_Undo_No.setText(QCoreApplication.translate("undoConfirmationDialog", u"No", None))
    # retranslateUi

