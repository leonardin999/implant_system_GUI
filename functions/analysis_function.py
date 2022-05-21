import time

import cv2

from modules import *
from dialog import CustomMessageDialog
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QMessageBox, QFileDialog
from PySide6.QtGui import QColor, QImage, QPixmap
from PySide6.QtCore import Qt

import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import keras
import os.path
from pathlib import Path
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Input
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import classification_report, confusion_matrix
# savedModel=keras.models.load_model('D://TRUC/AFinal_kieu_than.h5')
from tensorflow.keras.preprocessing import image

class AnalysisFunctions(MainWindow):

    def error_result_handle(self):
        title = str("error:")
        message = str('problems happened in the analysis process.\n'
                      'Please try again.')
        dialog = CustomMessageDialog(message, title)
        if dialog.exec_():
            AnalysisFunctions.reset(self)
            return
        else:
            AnalysisFunctions.reset(self)

    def threaded_analysis(self):
        if AnalysisFunctions.progress_run(self):
            try:
                text = str('Result of Threaded Analysis')
                self.result_edit.setText(text)
            except:
                AnalysisFunctions.error_result_handle()

    def tapered_analysis(self):
        if AnalysisFunctions.progress_run(self):
            try:
                text = str('Result of Tapered Analysis')
                self.result_edit.setText(text)
            except:
                AnalysisFunctions.error_result_handle()

    def apex_analysis(self):

        savedModel = keras.models.load_model('models/AFinal_kieu_duoi.h5')
        test_image = image.load_img(self.image, target_size=(224, 224, 3))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = savedModel.predict(test_image)
        a = np.round(result)
        if (a == [1, 0]).all():
            prediction = 'Curved'
        elif (a == [0, 1]).all():
            prediction = 'Flat'
        else:
            prediction = 'Not found'
        if AnalysisFunctions.progress_run(self):
            try:
                self.result_edit.setText(prediction)
            except:
                AnalysisFunctions.error_result_handle()

    def confirm_analysis(self):
        if AnalysisFunctions.progress_run(self):
            method = self.method_box.currentText().strip()
            if method == str('Choose methods'):
                self.option = method
                return

            title = str("confirm:")
            confirm_message = str(f'Confirm to analysis by {method} (Y/N)?')
            dialog = CustomMessageDialog(confirm_message, title)
            if dialog.exec_():
                style_str = "QPushButton {background-color: #007300; color: #000000;}" \
                            "QPushButton:hover {" \
                            "background-color: rgb(240, 240, 240);" \
                            "color:#000000;}" \
                            "QPushButton:pressed {" \
                            "background-color: rgb(65, 64, 66);" \
                            "color: rgb(240, 235, 225);}"
                self.analysis_btn.setStyleSheet(style_str)
                self.option = method
                self.result_edit.setText(self.option)
            else:
                return

    def error_analysis_handle(self, message):
        title = str("error:")
        dialog = CustomMessageDialog(message, title)
        if dialog.exec_():
            style_str = "QPushButton {background-color: #c30000; color: #000000;}" \
                        "QPushButton:hover {" \
                        "background-color: rgb(240, 240, 240);" \
                        "color:#000000;}" \
                        "QPushButton:pressed {" \
                        "background-color: rgb(65, 64, 66);" \
                        "color: rgb(240, 235, 225);}"
            self.analysis_btn.setStyleSheet(style_str)
            AnalysisFunctions.reset(self)

    def progress_run(self, plus=0.0005):

        self.completed = 0
        self.progressBar.setValue(0)
        while self.completed < 100:
            self.statusBar.showMessage('in Progress...')
            self.completed += plus
            self.progressBar.setValue(self.completed)
        self.statusBar.showMessage('ready')
        return True

    def start_analysis(self):
        if AnalysisFunctions.progress_run(self):
            if self.option == str('Choose methods'):
                AnalysisFunctions.error_analysis_handle(self,
                                                        "Make sure you choose the right analysis method!")
            else:
                if self.method_box.currentText() == 'Threaded':
                    AnalysisFunctions.threaded_analysis(self)
                elif self.method_box.currentText() == 'Tapered':
                    AnalysisFunctions.tapered_analysis(self)
                elif self.method_box.currentText() == 'Apex':
                    AnalysisFunctions.apex_analysis(self)

    def error_loading_handle(self):
        title = str("error:")
        message = str('error loading images.\n'
                      'Please try again.')
        dialog = CustomMessageDialog(message, title)
        if dialog.exec_():
            AnalysisFunctions.reset(self)
            return
        else:
            AnalysisFunctions.reset(self)
            
    def image_loading(self):
        if AnalysisFunctions.progress_run(self):
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            filename, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                      "Images (*.png *.jpg)", options=options)
            if filename:
                if AnalysisFunctions.progress_run(self,plus=0.0001):
                    try:
                        self.image = filename
                        self.path_edit.setText(self.image)
                        pixmap = QPixmap(self.image)
                        pixmap = pixmap.scaled(640, 480, Qt.KeepAspectRatio)
                        self.image_display.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                        self.image_display.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                        self.image_display.setPixmap(QPixmap(pixmap))
                        self.image_display.repaint()
                    except:
                        self.image = None
                        AnalysisFunctions.error_loading_handle(self)

    def logout_handle(self):
        title = str("Logout:")
        message = str('Logout of system?(Y/N)')
        dialog = CustomMessageDialog(message, title)
        if dialog.exec_():
            self.close()
        else:
            return

    def introduction_message_handle(self):
        title = str("Introduction:")
        message = str('You can describe your system here.\n'
                      '........')
        dialog = CustomMessageDialog(message, title)
        if dialog.exec_():
            return

    def reset(self):
        self.path_edit.clear()
        self.image_display.clear()
        self.statusBar.showMessage('Error')
        self.progressBar.setValue(0)