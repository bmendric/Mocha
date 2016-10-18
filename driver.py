import threading, Queue, Tkinter

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
		return self.frameGen.getPos()

	def getFrame(self):
		return self.frameGen.getFrame()

class MainController:
	xRange = [-300, 300]
	yRange = [0, 600]
	
	def __init__(self):
		# Initialize variables
		self.workers = {}
		self.queue = Queue.Queue()

		# Initialize threads
		# thread for LeapMotion frames
		self.workers['frame'] = LeapThread(self.queue)

		# thread for synthesizer
		self.workers['synth'] = Synthesizer(440, 1.0, .25)

		self.start()

		# Starting the GUI
		self.tk = Tkinter.Tk()
		self.tk.title = "Mocha"
		self.tk.resizable(0, 0)

		self.canvas = Tkinter.Canvas(self.tk, width=1000, height=500, bd=0, highlightthickness=0)
		
		lineBoundNorms = [0.083,0.166,0.25,0.33,0.4167,0.500,0.583,0.666,0.750,0.833,0.9167]
		for i in range(len(lineBoundNorms)):
			x1 = lineBoundNorms[i]*1000
			y1 = 0
			x2 = x1
			y2 = 500 - 1
			self.canvas.create_line(x1,y1,x2,y2)
		self.canvas.pack()

		self.ball = Ball(self.canvas, "red")
	
	# Function to start all of the workers
	def start(self):
		for key, obj in self.workers.iteritems():
			obj.start()

	# Function through which all necessary functions are looped (on the main thread)
	def loop(self):
		pos = self.workers['frame'].getPos()
		normalized = self.normalize(pos)

		if pos:
			self.workers['synth'].play(normalized)
			self.ball.draw(normalized)

		self.tk.update_idletasks()
		self.tk.update()

	def normalize(self, pos):
		if pos:
			xCoord = (pos[0] + 240) / 480
			yCoord = 1 - (pos[1] / 500)
			
			if xCoord < 0:
				xCoord = 0
			elif xCoord > 1:
				xCoord = 1

			if yCoord < 0:
				yCoord = 0
			elif yCoord > 1:
				yCoord = 1

			tmp = [xCoord, yCoord]
			return tmp


class Ball:
	def __init__(self, canvas, color):
		self.color = color
		self.canvas = canvas
		self.id = self.canvas.create_oval(10, 10, 30, 30, fill=self.color)
		self.canvas.move(self.id, 540, 240)

	def draw(self, pos):
		self.canvas.delete(self.id)
		self.id = self.canvas.create_oval(10, 10, 30, 30, fill=self.color)
		self.canvas.move(self.id, pos[0]*1000, pos[1]*500)

def main():
	controller = MainController()

	try:
		while True:
			controller.loop()
	except KeyboardInterrupt:
		pass

if __name__ == "__main__":
	main()
