from Tkinter import *
import pyautogui


class Application(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.paint()
        
    def paint(self):
        self.space = Canvas(self,width=1000,height=500)
        self.drawCircle()

    def drawCircle(self):
        self.space.create_rectangle(100,100,200,200,fill="blue")
        self.space.pack() # had to change self.pack() to self.space.pack()

root = Tk()
root.title("Broken")

root.geometry("1000x500")
app = Application(root)
    
root.mainloop()