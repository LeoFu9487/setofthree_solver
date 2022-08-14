from time import sleep
from tracemalloc import start
from ppadb.client import Client as AdbClient


if __name__ == '__main__':
	client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037

	devices = client.devices()

	if len(devices) == 0:
		print('No devices')
		quit()

	device = devices[0]

	start_button = [705, 1122]
	back_button = [313, 1884]
	retry_button = [686, 1375]

	def tap(position):
		device.shell('input tap {:d} {:d}'.format(position[0], position[1]))

	def start():
		tap(start_button)

	def back():
		tap(back_button)

	def retry():
		tap(retry_button)


	positions = [
	
	[ [324, 921] , [692, 921], [1010, 921] ],
	
	[ [324, 1260], [692, 1260], [1010, 1260] ],
	
	[ [324, 1522], [692, 1522], [1010, 1522] ]
	
	]


	def play(x, y):
		if (x < 0 or x > 2 or y < 0 or y > 2):
			print('Wrong position to play')
			exit()
		tap(positions[x][y])


	
	

	






# 2059 2669
# 3876 166
#  ABS_MT_POSITION_X    0000094d            
#/dev/input/event0: EV_ABS       ABS_MT_POSITION_Y    000008ce  

# x/3, y/2