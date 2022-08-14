# from time import sleep
# from PIL import Image

# im = Image.open("phone.png") #1080*2220

# crop_rectangle = (0, 0, 540, 1110)
# cropped_im = im.crop(crop_rectangle)

# # sleep(3)

# cropped_im.show()

# importing the module
import cv2
  
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
        cv2.putText(img, str(x) + ',' +
                    str(y), (x,y), font,
                    1, (255, 0, 0), 2)
        cv2.imshow('image', img)
 
    # checking for right mouse clicks    
    if event==cv2.EVENT_RBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
 
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r),
                    (x,y), font, 1,
                    (255, 255, 0), 2)
        cv2.imshow('image', img)
 
# driver function
if __name__=="__main__":
 
    # reading the image
	
 
	sz_y , sz_x = 2220, 1080

	x_positions, y_positions = [ 89, 410, 730 ], [ 856, 1176, 1496 ]
	x_len, y_len = 260, 259

	# img = bigimg

	# for i in range(3):
	# 	for j in range(3):
	# 		img = bigimg[y_positions[j]:y_positions[j] + y_len, x_positions[i]:x_positions[i] + x_len]


	def show_block(y,x):
		img = cv2.imread('phone.png', 1)
		img = img[ y_positions[y]:y_positions[y]+y_len, x_positions[x]:x_positions[x]+x_len ]
		cv2.imshow('image', img)
	
	
	show_block(1,2)
    # displaying the image
	# cv2.imshow('image', img)
 
	# setting mouse handler for the image
    # and calling the click_event() function
	cv2.setMouseCallback('image', click_event)
 
    # wait for a key to be pressed to exit
	cv2.waitKey(0)
 
    # close the window
	cv2.destroyAllWindows()

# 89~349	 856~1115
# 410~670	 856~1115
# 730~990	 856~1115

# 89~349	 1176~1435
# 410~670	 1176~1435
# 730~990	 1176~1435

# 89~349 	 1496~1755
# 410~670	 1496~1755
# 730~990	 1496~1755
