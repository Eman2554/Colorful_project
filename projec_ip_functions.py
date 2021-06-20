
# function to get x,y coordinates of mouse double click
import cv2
from pygments.formatters import img


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