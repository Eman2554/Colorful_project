import cv2
import numpy as np


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
