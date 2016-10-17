import pyaudio, csv, sys, threading
import numpy as np

# Create instances of this class using 'with Synthesizer() as synthesizer'. 
# That way the __exit__ method should be automatically invoked to handle closing the audio stream
class Synthesizer(threading.Thread):
	'Contains methods to generate sin waves, update signal properties, and handle play back'
	
	def __init__(self, frequency, amplitude, signalDuration):
		threading.Thread.__init__(self)

		# Set up signal properties
		self.frequency = frequency
		self.amplitude = amplitude
		self.signalDuration = signalDuration
		self.phase = 0
		self.time = 0
		self.fs = 44100
		self.signal = None

		# Create pyaudio stream
		p = pyaudio.PyAudio()
		self.stream = p.open(format=pyaudio.paFloat32,
					channels=1,
					rate=self.fs,
					output=True)
					
	def __enter__(self):
		return self
		
	def __exit__(self, exc_type, exc_value, traceback):
		self.closeStream()
	
	def updateSignal(self):
		#TODO: implement time tracking
		self.t = np.arange(self.fs*self.signalDuration)
		internal = 2*np.pi*self.t*self.frequency/self.fs + self.phase
		self.signal = (np.sin(internal)).astype(np.float32)
		self.phase = internal[-1] % (2*np.pi)
		self.time += self.signalDuration
		
		
	# Updates the frequency and also modifies phase so the signal's vertical positioning lines up
	def updateFreq(self, frequency):
		currPhase = (self.time * self.frequency + self.phase) % (2*np.pi)
		newPhase = (self.phase * frequency) % (2*np.pi)
		self.phase = currPhase - newPhase
		self.frequency = frequency
		
	def playSignal(self):
		# Write signal to the stream
		self.stream.write(self.amplitude*self.signal)
		
#	def runDebug(self):
#		fig = figure(1)
#		ax1 = fig.add_subplot(211)
#		ax1.plot(self.t, self.signal)
#		ax1.grid(True)
#		show()
#		i = raw_input("Press Enter to continue...")
		
	def play(self, row):
		# poll for new frequency, call variable newFreq
		#---------------insert code ----------------------

		#with open('output.txt', 'rb') as f:
		#	reader = csv.reader(f)
		#	for row in reader:
		#print row
		sys.stdout.flush()

		if row:
		#Translate y values from 0-600 to be in 3rd octave
			newFreq = 261.63 + 232.25*float(row[1])/600 
			
			if newFreq != self.frequency:
				self.updateFreq(newFreq)
			
		self.updateSignal()
		self.playSignal()
		#self.runDebug()
		
	def closeStream(self):
		self.stream.stop_stream()
		self.stream.close()	
	
if __name__ == "__main__":
	with Synthesizer(440, 1.0, .25) as synthesizer:
		while True:
			synthesizer.run()
