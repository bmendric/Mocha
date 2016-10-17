import threading, Queue

from wrapper import LeapFrames
from synthesizer import Synthesizer

class LeapThread(threading.Thread):
	def __init__(self, queue):
		threading.Thread.__init__(self)
		self.queue = queue
		self.frameGen = LeapFrames()

	def run(self):
		pass

	def getPos(self):
		return [self.getName(), self.frameGen.getPos()]


def main():
	workers = {}
	queue = Queue.Queue()
	workers['frame'] = LeapThread(queue)
	workers['frame'].start()
	
	workers['synth'] = Synthesizer(440, 1.0, .25, workers['frame'])
	workers['synth'].start()

	try:
		while True:
			workers['synth'].play()
	except KeyboardInterrupt:
		pass

if __name__ == "__main__":
	main()
