# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SplashScreen.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Property)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QVBoxLayout, QWidget, QGraphicsOpacityEffect)

        
def _get_opacity(self):
    return self.label.graphicsEffect().opacity() if self.label.graphicsEffect() else 0

def _set_opacity(self, value):
    if not self.label.graphicsEffect():
        self.label.setGraphicsEffect(QGraphicsOpacityEffect())
    self.label.graphicsEffect().setOpacity(value)

opacity = Property(float, _get_opacity, _set_opacity)
