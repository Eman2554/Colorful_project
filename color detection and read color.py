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
