from PySide6.QtWidgets import QApplication, QMainWindow, QProgressBar
from PySide6.QtCore import Qt, QCoreApplication, QTimer
from PySide6.QtGui import QScreen

import serial
import sys
from qdarktheme import load_stylesheet, get_themes
from design import Ui_MainWindow
import functions


def toggle_theme(theme) -> None:
    stylesheet = load_stylesheet(theme)
    QApplication.instance().setStyleSheet(stylesheet)


class MainWindow(QMainWindow, Ui_MainWindow):
    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Implant Analysis System')
        self.statusBar.showMessage('Ready')
        self.progressBar = QProgressBar()
        self.statusBar.addPermanentWidget(self.progressBar)

        # setup status bar
        self.progressBar.setGeometry(30, 40, 100, 10)
        self.progressBar.setValue(10)
        # self.progressBar.setHidden(True)

        self.actionLight_theme.triggered.connect(lambda: toggle_theme('light'))
        self.actiondark.triggered.connect(lambda: toggle_theme('dark'))
        self.actionLogout.triggered.connect(lambda: functions.AnalysisFunctions.logout_handle(self))
        self.actionIntroduction.triggered.connect(lambda: functions.AnalysisFunctions.introduction_message_handle(self))

        # main variables:
        self.option = self.method_box.currentText()
        self.completed = 0
        self.image = None

        # set widget signals:
        self.method_box.currentIndexChanged.connect(lambda: functions.AnalysisFunctions.confirm_analysis(self))
        self.analysis_btn.clicked.connect(lambda: functions.AnalysisFunctions.start_analysis(self))
        self.image_btn.clicked.connect(lambda: functions.AnalysisFunctions.image_loading(self))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # setting screen to the center
    app = QApplication(sys.argv)
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    centerPoint = QScreen.availableGeometry(app.primaryScreen()).center()

    window = MainWindow()
    fg = window.frameGeometry()
    fg.moveCenter(centerPoint)
    window.move(fg.topLeft())

    # setup stylesheet
    app.setStyleSheet(load_stylesheet(theme="light"))
    # run
    window.show()
    app.exec()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
