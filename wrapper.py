import sys
#src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
#arch_dir = 'lib/x64' if sys.maxsize > 2**32 else 'lib/x86'
#sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
sys.path.append("/usr/lib/Leap")
sys.path.append("LeapSDK/lib/x64")
sys.path.append("LeapSDK/lib")

import Leap

class LeapFrames:
	def __init__(self):
		self.controller = Leap.Controller()

	def getFrame(self):
		return controller.frame()

	def getPos(self):
		frame = self.controller.frame()
		for hand in frame.hands:
			print "hand"
			if hand.is_left:
				print "left"
				pass
			else:
				print "right"
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
	print test.getPos()


# main call handling
if __name__ == '__main__':
	main()
