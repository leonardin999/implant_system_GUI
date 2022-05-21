# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(660, 675)
        MainWindow.setMinimumSize(QSize(655, 655))
        MainWindow.setMaximumSize(QSize(660, 675))
        self.actionIntroduction = QAction(MainWindow)
        self.actionIntroduction.setObjectName(u"actionIntroduction")
        self.actionLogout = QAction(MainWindow)
        self.actionLogout.setObjectName(u"actionLogout")
        self.actionLight_theme = QAction(MainWindow)
        self.actionLight_theme.setObjectName(u"actionLight_theme")
        self.actiondark = QAction(MainWindow)
        self.actiondark.setObjectName(u"actiondark")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.image_btn = QPushButton(self.centralwidget)
        self.image_btn.setObjectName(u"image_btn")
        self.image_btn.setGeometry(QRect(10, 10, 121, 31))
        self.path_edit = QLabel(self.centralwidget)
        self.path_edit.setObjectName(u"path_edit")
        self.path_edit.setGeometry(QRect(140, 20, 281, 16))
        self.method_box = QComboBox(self.centralwidget)
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.setObjectName(u"method_box")
        self.method_box.setGeometry(QRect(440, 10, 131, 31))
        self.analysis_btn = QPushButton(self.centralwidget)
        self.analysis_btn.setObjectName(u"analysis_btn")
        self.analysis_btn.setGeometry(QRect(575, 10, 71, 31))
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 530, 641, 71))
        self.result_edit = QLineEdit(self.groupBox_2)
        self.result_edit.setObjectName(u"result_edit")
        self.result_edit.setGeometry(QRect(10, 20, 621, 41))
        self.image_display = QLabel(self.centralwidget)
        self.image_display.setObjectName(u"image_display")
        self.image_display.setGeometry(QRect(10, 50, 640, 480))
        self.image_display.setStyleSheet(u"background-color: rgb(166, 166, 166);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 660, 22))
        self.menumenu = QMenu(self.menubar)
        self.menumenu.setObjectName(u"menumenu")
        self.menuThemes = QMenu(self.menumenu)
        self.menuThemes.setObjectName(u"menuThemes")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menubar.addAction(self.menumenu.menuAction())
        self.menumenu.addAction(self.actionIntroduction)
        self.menumenu.addAction(self.menuThemes.menuAction())
        self.menumenu.addAction(self.actionLogout)
        self.menuThemes.addAction(self.actionLight_theme)
        self.menuThemes.addAction(self.actiondark)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionIntroduction.setText(QCoreApplication.translate("MainWindow", u"Introduction", None))
        self.actionLogout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.actionLight_theme.setText(QCoreApplication.translate("MainWindow", u"light", None))
        self.actiondark.setText(QCoreApplication.translate("MainWindow", u"dark", None))
        self.image_btn.setText(QCoreApplication.translate("MainWindow", u"Load image", None))
        self.path_edit.setText(QCoreApplication.translate("MainWindow", u"insert images path....", None))
        self.method_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Choose methods", None))
        self.method_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Threaded", None))
        self.method_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Tapered", None))
        self.method_box.setItemText(3, QCoreApplication.translate("MainWindow", u"Apex", None))

        self.analysis_btn.setText(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Result", None))
        self.image_display.setText("")
        self.menumenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.menuThemes.setTitle(QCoreApplication.translate("MainWindow", u"Themes", None))
    # retranslateUi

