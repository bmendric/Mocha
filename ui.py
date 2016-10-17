from Tkinter import *
from PIL import Image, ImageTk
from wrapper import LeapFrames
import pyautogui


class Application(Frame):
    xval = 1000
    yval = 500

    starty = yval*(float(3)/5)
    keywidth = float(xval)/7 - 10
    keyheight = 2*(yval/5) - 10

    startx = []
    for i in range(7):
        startx.append(i*keywidth+40)

    def __init__(self, master):
        """ Initialize application """
        Frame.__init__(self, master)
        self.grid()
        self.startbutton()

    def startbutton(self):
        """ run main menu """
        self.img = ImageTk.PhotoImage(Image.open("mochaimg.png"))
        self.mochaButton = Button(root, image = self.img)
        px = (self.xval-175)/2
        py = (self.yval-75)/2
        self.mochaButton.grid(row=0,column=0, padx = px, pady = py)
        self.mochaButton["command"] = self.canvas

    def canvas(self):
        self.mochaButton.grid_forget()
        self.displaykeys()
        self.displayCircle()

    def displaykeys(self):
        """ display areas for keys """
        self.space = Canvas(self,width=self.xval,height=self.yval)
    
        sy = self.starty
        xinc = self.keywidth # x increment
        yinc = self.keyheight # y increment
        for i in range(7):
            sx = self.startx[i]
            box = [sx,sy,sx+xinc,sy+yinc]
            self.space.create_rectangle(box,outline="black",fill="white",width=2)
            self.space.pack()

    def displayCircle(self):
        pos = pyautogui.position()
        x1 = pos[0]
        y1 = pos[1]
        x2 = x1+50
        y2 = y1+50
        self.space.create_oval(x1,y1,x2,y2,fill="green")
        self.pack()
        

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

root.geometry("1000x500")
app = Application(root)

root.mainloop()
