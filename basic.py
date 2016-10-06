import thread, sys, time

# Adding system paths to LeapMotion binaries
# TODO: this shouldn't be absolute pathing, but should be fine for now
sys.path.append("/usr/lib/Leap")
sys.path.append("/home/ario/Desktop/LeapSDK/lib/x64")
sys.path.append("/home/ario/Desktop/LeapSDK/lib")

import Leap

class CoordinateListener(Leap.Listener):
	
	f = open("output.txt", 'w')
	
	def on_init(self, controller):
		print "Initialized"

	def on_connect(self, controller):
		print "Connected"

	def on_disconnect(self, controller):
		print "Disconnected"

	def on_exit(self, controller):
		print "Exited"
		self.f.close()

	def on_frame(self, controller):
		# Get the most recent frame
		frame = controller.frame()

		for hand in frame.hands:
			handType = 0 if hand.is_left else 1
			pos = hand.palm_position

			# self.f.write("%s, %s, %s \n" %(pos[0], pos[1], pos[2]))
			self.f.write("%s, %s\n" %(frame.id, frame.timestamp))
			print frame.id

	def state_string(self, state):
		if state == Leap.Gesture.STATE_START:
			return "STATE_START"

		if state == Leap.Gesture.STATE_UPDATE:
			return "STATE_UPDATE"

		if state == Leap.Gesture.STATE_STOP:
			return "STATE_STOP"

		if state == Leap.Gesture.STATE_INVALID:
			return "STATE_INVALID"


def main():
	# Create a listener and controller
	listener = CoordinateListener()
	controller = Leap.Controller()

	# Tell the listener to recieve events from the controller
	controller.add_listener(listener)

	# Keep the process running until key is pressed
	try:
		sys.stdin.readline()
	except KeyboardInterrupt:
		pass
	finally:
		# Removing the listener from the controller when done
		controller.remove_listener(listener)



# Handling main calling
if __name__ == "__main__":
	main()
