# from time import sleep
# from PIL import Image

# im = Image.open("phone.png") #1080*2220

# crop_rectangle = (0, 0, 540, 1110)
# cropped_im = im.crop(crop_rectangle)

# # sleep(3)

# cropped_im.show()

# importing the module
import cv2
from enum import Enum

class Shape(Enum):
    Triangle=0
    Circle=1
    Square=2

class Color(Enum):
    Red=0
    Blue=1
    Green=2

img = cv2.imread('phone.png',1)
cut = img
# function to display the coordinates of
# of the points clicked on the image
def click_event(event, x, y, flags, params):

    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
 
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(cut, str(x) + ',' +
                    str(y), (x,y), font,
                    1, (255, 0, 0), 2)
        cv2.imshow('image', cut)
 
    # checking for right mouse clicks    
    if event==cv2.EVENT_RBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
 
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = cut[y, x, 0]
        g = cut[y, x, 1]
        r = cut[y, x, 2]
        cv2.putText(cut, str(b) + ',' +
                    str(g) + ',' + str(r),
                    (x,y), font, 1,
                    (255, 255, 0), 2)
        cv2.imshow('image', cut)
 
def shape(img,y, x):
    x_positions, y_positions = [ 89, 410, 730 ], [ 856, 1176, 1496 ]
    for k in range(3):
        if img[y_positions[y] + 52][x_positions[x] + 28][k] != 255:
            return Shape.Triangle
    for k in range(3):
        if img[y_positions[y] + 131][x_positions[x] + 42][k] != 255:
            return Shape.Circle
    
    return Shape.Square
    #28~224, 52

def color(img, y, x):
    x_positions, y_positions = [ 89, 410, 730 ], [ 856, 1176, 1496 ]
    bgr = [img[y_positions[y] + 55][x_positions[x] + 90][k] for k in range(3)]
    if max(bgr) == bgr[0]:
        return Color.Blue
    if max(bgr) == bgr[1]:
        return Color.Green
    if max(bgr) == bgr[2]:
        return Color.Red
    return 'Error in Color'
    

def show_block(img,y,x):
    x_positions, y_positions = [ 89, 410, 730 ], [ 856, 1176, 1496 ]
    x_len, y_len = 260, 259

    # img = cv2.imread('phone.png', 1)
    cut = img[ y_positions[y]:y_positions[y]+y_len, x_positions[x]:x_positions[x]+x_len ]
    cv2.imshow('image', cut)


# driver function
def solve():
    
    # reading the image
	
 
    
	
	
    # displaying the image
	# cv2.imshow('image', img)
 
	# setting mouse handler for the image
    # and calling the click_event() function
    # show_block(img,2,2)
    # 90 55
    img = cv2.imread('phone.png',1)

    for x in range(0,3):
        for y in range(3):
            print(x, y, color(img, x, y))
    for x in range(0,3):
        for y in range(3):
            print(x, y, shape(img, x, y))
    # cv2.setMouseCallback('image', click_event)
 
    # wait for a key to be pressed to exit
    # cv2.waitKey(0)
 
    # close the window
    # cv2.destroyAllWindows()

# solve()
# 89~349	 856~1115
# 410~670	 856~1115
# 730~990	 856~1115

# 89~349	 1176~1435
# 410~670	 1176~1435
# 730~990	 1176~1435

# 89~349 	 1496~1755
# 410~670	 1496~1755
# 730~990	 1496~1755
