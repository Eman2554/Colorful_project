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




# function to get x,y coordinates of mouse double click
def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


#function to calculate minimum distance from all colors and get the most matching color
def getColorName(R,G,B):

    # Reading csv file with pandas and giving names to each column
    index = ["color", "color_name", "hex", "R", "G", "B"]
    csv = pd.read_csv('colors.csv', names=index, header=None)

    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]

    return cname

def read_color(text):
    # initialize Text-to-speech engine
    engine = pyttsx3.init()
    # convert this text to speech
    engine.say(text)
    # play the speech
    engine.runAndWait()

def color_detection(img_path):

    # Reading the image with opencv
    global img , clicked
    img = cv2.imread(img_path)

    # declaring global variables (are used later on)


    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_function)
    cv2.imshow("image", img)

    while (1):


        if ( clicked):

            # cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle
            cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

            # Creating text string to display( Color name and RGB values )
            color_name = getColorName(r, g, b)
            text = color_name + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)



            # For very light colours we will display text in black colour
            if (r + g + b >= 600):
                cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
                cv2.imshow("image", img)
                # creating voice of color string
                read_color(color_name)

            else:
                # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
                cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.imshow("image", img)
                # creating voice of color string
                read_color(color_name)


            clicked = False

        # Break the loop when user hits 'esc' key
        if cv2.waitKey(20) & 0xFF == 27:
            break

    cv2.destroyAllWindows()


def specific_color_detection(img_path, color):

    image= cv2.imread(img_path)
    # Convert BGR to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # define blue color range
    if color == 'blue':
        light_color = np.array([94, 80, 20])
        dark_color = np.array([120, 255, 255])
    # define green color range
    if color == 'green':
        light_color = np.array([45, 52, 5])
        dark_color = np.array([75, 255, 255])
    # define red color range
    if color == 'red':
        light_color = np.array([0, 50, 5])
        dark_color = np.array([15, 255, 255])

    if color == 'pink':
        light_color = np.array([148, 50, 20])
        dark_color = np.array([165, 255, 250])

    if color == 'yellow':
        light_color = np.array([20, 20, 10])
        dark_color = np.array([45, 255, 255])

    if color == 'orange':
        light_color = np.array([10, 100, 20])
        dark_color = np.array([25, 255, 255])
    if color == 'white':
        light_color = np.array([0, 0, 180])
        dark_color = np.array([255, 20, 255])

    '''if color == 'black':
        light_color = np.array([0, 200, 0])
        dark_color = np.array([255, 255, 5])'''



    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, light_color, dark_color)

    # Bitwise-AND mask and original image
    output = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow("Color Detected", np.hstack((image, output)))
    cv2.waitKey(0)
    cv2.destroyAllWindows()





app=QApplication(sys.argv)
mainwindow=MainWindow()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(451)
widget.setFixedHeight(269)
widget.show()
sys.exit(app.exec_())