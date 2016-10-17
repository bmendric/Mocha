import pyaudio
import numpy as np
#from matplotlib.pyplot import figure, show
import csv
import sys
import random

# Create instances of this class using 'with Synthesizer() as synthesizer'.
# That way the __exit__ method should be automatically invoked to handle closing the audio stream
class Synthesizer:
	'Contains methods to generate sin waves, update signal properties, and handle play back'

	def __init__(self, frequency, amplitude, signalDuration):
		# Set up signal properties
		self.frequency = frequency
		self.amplitude = amplitude
		self.signalDuration = signalDuration
		self.phase = 0
		self.time = 0
		self.fs = 44100
		self.signal = None
		self.noteWaves = self._getNoteWaves(self._getNoteFreqs())

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

	def _getNoteFreqs(self):
		return {
			'A': 110.00,
			'Bb': 116.54,
			'B': 123.47,
			'C': 130.81,
			'Db': 138.59,
			'D': 146.83,
			'Eb': 155.56,
			'E': 164.81,
			'F': 174.61,
			'Gb': 185,
			'G': 196,
			'Ab': 207.65,
		}

	def _getNoteWaves(self, noteFreqs):
		print "Creating note waves..."

		waves = {}
		for note, freq in noteFreqs.iteritems():
			signalDuration = (1./freq) * 5
			time = np.arange(self.fs * signalDuration)
			internal = 2 * np.pi * time * freq / self.fs
			signal = (np.sin(internal)).astype(np.float32)
			waves[note] = signal

		print "Done creating note waves..."
		return waves

	def _getClosestNote(self, pos):
		print pos
		if pos < 60:
			return 'A'
		if pos < 120:
			return 'Bb'
		if pos < 180:
			return 'B'
		if pos < 240:
			return 'C'
		if pos < 300:
			return 'Db'
		if pos < 360:
			return 'D'
		if pos < 420:
			return 'Eb'
		if pos < 480:
			return 'E'
		if pos < 540:
			return 'F'
		if pos < 600:
			return 'Gb'
		if pos < 660:
			return 'G'
		return 'Ab'

	def playSignal(self, signal):
		# Write signal to the stream
		self.stream.write(self.amplitude*signal)

	def run(self):
		with open('output.txt', 'rb') as f:
			reader = csv.reader(f)
			for row in reader:
				sys.stdout.flush()
				print row[1]
				closest = self._getClosestNote(float(row[1]))
				print closest
				self.playSignal(self.noteWaves[closest])

	def closeStream(self):
		self.stream.stop_stream()
		self.stream.close()

if __name__ == "__main__":
	with Synthesizer(440, 1.0, .25) as synthesizer:
		while True:
			synthesizer.run()
