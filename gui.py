import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog , QComboBox ,QLabel
from PyQt5.uic import loadUi
import cv2
import numpy as np
import pandas as pd
import pyttsx3
import argparse

global clicked
clicked = False
r = g = b = xpos = ypos = 0

class MainWindow(QDialog):
    global text
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("GUI.ui",self)
        combo = QComboBox(self)
        list = ["Choose Color","red", "green", "blue", 'white','yellow','orange','pink']
        combo.addItems(list)
        combo.move(320, 170 )
        combo.setGeometry(320, 160, 110, 25)
        combo.activated[str].connect(self.onChanged)
        self.browse.clicked.connect(self.browsefiles)
        self.search_for_Button.clicked.connect(self.SearchFunc)
        self.onClick_Button.clicked.connect(self.OnClickFunc)
        self.text = combo.currentText()


    def onChanged(self, text):
        self.text = text


    def browsefiles(self):

         fname = QFileDialog.getOpenFileName(self, 'Open file', 'F:/image/image_ihub_project')

         self.path_text.setText(fname[0])
         return fname[0]

    def OnClickFunc(self):
        path = self.path_text.text()
        color_detection(path)
        print('button on click pressed ')


    def SearchFunc(self):
        color = self.text
        path =  self.path_text.text()
        print('button search clicked ')
        print(color)
        specific_color_detection(path, color)




app=QApplication(sys.argv)
mainwindow=MainWindow()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(451)
widget.setFixedHeight(269)
widget.show()
sys.exit(app.exec_())