import sys
sys.path.append("C:\Python32\LeapDeveloperKit_2.3.1+31549_win\LeapSDK\lib")
import Leap

class LeapFrames:
	def __init__(self):
		self.controller = Leap.Controller()

	def getFrame(self):
		return self.controller.frame()

	def getPos(self):
		frame = self.controller.frame()
		for hand in frame.hands:
			if not hand.is_left:
				pass
			else:
				tmp = list([])
				for i in range(3):
					tmp.append(hand.palm_position[i])

				return tmp
		return []

def main():

	#controller = Leap.Controller()
	test = LeapFrames()

	print "woo"
	try:
		sys.stdin.readline()
	except KeyboardInterrupt:
		pass

	#frame = controller.frame()
	#for hand in frame.hands:
	#	print hand.palm_position
	print test.getFrame()


# main call handling
if __name__ == '__main__':
	main()
