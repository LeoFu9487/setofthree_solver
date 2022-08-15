from signal import pause
from time import sleep
import cv2
from enum import Enum
from get_screenshot import get_screen

class Shape(Enum):
    Triangle=0
    Circle=1
    Square=2

class Color(Enum):
    Red=0
    Blue=1
    Green=2

class Style(Enum):
    Empty=0
    Stripe=1
    Filled=2

 
def shape(img, hash):
    x,y = hash % 3, hash // 3
    x_positions, y_positions = [ 89, 410, 730 ], [ 856, 1176, 1496 ]
    for k in range(3):
        if img[y_positions[y] + 52][x_positions[x] + 28][k] != 255:
            return Shape.Triangle
    for k in range(3):
        if img[y_positions[y] + 131][x_positions[x] + 42][k] != 255:
            return Shape.Circle
    
    return Shape.Square

def color(img, hash):
    x,y = hash % 3, hash // 3
    x_positions, y_positions = [ 89, 410, 730 ], [ 856, 1176, 1496 ]
    bgr = [img[y_positions[y] + 55][x_positions[x] + 90][k] for k in range(3)]
    if max(bgr) == bgr[0]:
        return Color.Blue
    if max(bgr) == bgr[1]:
        return Color.Green
    if max(bgr) == bgr[2]:
        return Color.Red
    return 'Error in Color'
    
def style(img,hash):
    x,y = hash % 3, hash // 3
    x_positions, y_positions = [ 89, 410, 730 ], [ 856, 1176, 1496 ]
    for k in range(3):
        if img[y_positions[y] + 130][x_positions[x] + 130][k] != 255:
            break
        if k == 2:
            return Style.Empty
    for k in range(3):
        if img[y_positions[y] + 87][x_positions[x] + 90][k] != 255:
            return Style.Filled

    return Style.Stripe

def check_shape(img, hash1, hash2, hash3):
    one, two, three = shape(img, hash1), shape(img, hash2), shape(img, hash3)
    if one == two and two == three:
        return True
    if one != two and two != three and one != three:
        return True
    return False

def check_color(img, hash1, hash2, hash3):
    one, two, three = color(img, hash1), color(img, hash2), color(img, hash3)
    if one == two and two == three:
        return True
    if one != two and two != three and one != three:
        return True
    return False

def check_style(img, hash1, hash2, hash3):
    one, two, three = style(img, hash1), style(img, hash2), style(img, hash3)
    if one == two and two == three:
        return True
    if one != two and two != three and one != three:
        return True
    return False

def solve(filename, play):
    get_screen(filename)
    # sleep(0.1)
    img = cv2.imread(filename, 1)
    
    # for i in range(9):
    #     print(shape(img, i))
    
    for i in range(7):
        for j in range(i+1,8):
            for k in range(j+1,9):
                if check_shape(img, i, j ,k) == True and check_color(img, i, j, k) == True and check_style(img, i, j, k) == True:
                    play(i)
                    play(j)
                    play(k)
                    return



# 89~349	 856~1115
# 410~670	 856~1115
# 730~990	 856~1115

# 89~349	 1176~1435
# 410~670	 1176~1435
# 730~990	 1176~1435

# 89~349 	 1496~1755
# 410~670	 1496~1755
# 730~990	 1496~1755
