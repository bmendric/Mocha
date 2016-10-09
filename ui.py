from Tkinter import *
from PIL import Image, ImageTk

"""Global variables"""
xval = 1000
yval = 500


starty = yval*(float(3)/5)
keyheight = 2*(yval/5) - 10
keywidth = float(xval)/7 - 10

#startx in pixels
startx = []

for i in range(7):
	startx.append(i*keywidth+40)
	print startx[i]



class Application(Frame):
	
	def __init__(self, master):
		""" Initialize application """
		Frame.__init__(self, master)
		self.grid()
		self.startbutton()

	def startbutton(self):
		""" run main menu """
		self.img = ImageTk.PhotoImage(Image.open("mochaimg.png"))
		self.mochaButton = Button(root, image = self.img)
		self.mochaButton.grid(row=0,column=0, padx = ((xval-175)/2), pady = ((yval-75)/2))
		self.mochaButton["command"] = self.synth

	def synth(self):
		self.mochaButton.grid_forget()
		self.displaykeys()
		self.LeapIntoAction()

	def displaykeys(self):
		""" display areas for keys """
		self.space = Canvas(self,width=xval,height=yval)

		sy = starty
		xinc = keywidth # x increment
		yinc = keyheight # y increment
		for i in range(7):
			sx = startx[i]
			box = [sx,sy,sx+xinc,sy,sx+xinc,sy+yinc,sx,sy+yinc]
			self.space.create_polygon(box,outline="black",fill="white",width=2)
			self.space.pack()

	def LeapIntoAction(self):
		""" run leap motion synthesizer """
		""" Things to do:
			1. start leap motion, synthesizer

			2. get input from leap motion
			3. update canvas image with palm position coordinates in 2D space
			4. pass coordinates to synthesizer

		"""

		print "Leap into Action!!!"




root = Tk()
root.title("Mocha")

root.geometry(str(xval)+"x"+str(yval))
app = Application(root)

root.mainloop()
