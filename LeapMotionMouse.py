"""
author: Quincy D.
pyautogui installation instructions:
https://pyautogui.readthedocs.io/en/latest/install.html
"""

import pyautogui
import sys
import math

sys.path.append("C:\Python32\LeapDeveloperKit_2.3.1+31549_win\LeapSDK\lib")
import Leap
from wrapper import LeapFrames

class LeapMotionMouse:

    """ initialize Leap Motion Mouse control class """
    def __init__(self):
        pyautogui.FAILSAFE = False # removes fail safe error when moving mouse
        self.leapframes = LeapFrames() #leap Motion wrapper class
        self.screenWidth, self.screenHeight = pyautogui.size() # computer screen size
        self.mouseX,self.mouseY = self.screenWidth/2,self.screenHeight/2
        self.xNorm,self.yNorm = 0,0
        self.leapPosition = 0,0

        """
        self.rangeX = [self.width, 0] # [minX , maxX]
        self.rangeY = [self.height,0] # [minY, maxY]
        """
        # approximated ranges
        self.rangeX = [-240,240]
        self.rangeY = [10,600]

    """ returns the current mouse position """
    def getMousePosition(self):
    	"""
    	if self.mouseX < self.rangeX[0]:
    		self.rangeX[0] = self.mouseX
    	elif self.mouseX > self.rangeX[1]:
    		self.rangeX[1] = self.mouseX

    	if self.mouseY < self.rangeY[0]:
    		self.rangeY[0] = self.mouseY
    	elif self.mouseY > self.rangeY[1]:
    		self.rangeY[1] = self.mouseY
    	"""

        return self.mouseX,self.mouseY

    """ updates the current mouse position """
    def updateMousePosition(self):
        self.leapPosition = self.leapframes.getPos()

        self.mapToScreen()

        pyautogui.moveTo(self.mouseX,self.mouseY)

    """ map Leap Motion coordinates to computer screen """
    def mapToScreen(self):
    	if len(self.leapPosition) < 2:
            return

        self.normalize()

        # WORK SEPARATELY BUT NOT AT THE SAME TIME!!!
        self.mouseX = self.xNorm * self.screenWidth
        self.mouseY = (1-self.yNorm) #* self.screenHeight

        return

    def normalize(self):
    	x = self.leapPosition[0] - self.rangeX[0]
    	y = self.leapPosition[1] - self.rangeY[0]
    	magnitude = math.sqrt((x*x) + (y*y))

        if magnitude == 0:
            return

        self.xNorm = float(x)/magnitude
        self.yNorm = float(y)/magnitude

        return

    def leaprange(self):
    	print "[Min_X:",self.rangeX[0],',',"[Max_X:",self.rangeX[1],']'
    	print "[Min_Y:",self.rangeY[0],',',"[Max_Y:",self.rangeY[1],']'
    	return

mouse = LeapMotionMouse()
try:
    while(True):
        mouse.updateMousePosition()
        print mouse.getMousePosition()
except KeyboardInterrupt:
	print "\nI got you covered!"
    
pyautogui.FAILSAFE = True # returns fail safe error when moving mouse
