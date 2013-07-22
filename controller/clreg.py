#------------------------------------------------------------------------------
# linear regression graph controller module
#   -- handles specific events for linear regression graphs
#------------------------------------------------------------------------------
from Tkinter import *

#------------------------------------------------------------------------------
# LregContoller class
#   -- a custom Tkinter widget for displaying Linear regression graphs
#------------------------------------------------------------------------------
class LregController():

    def __init__(self):
        self.x = []
        self.graphData = None
        self.currentPoint = None

    def getText(self,event=None,i=0):
        self.currentPoint = (self.x[i],self.graphData[i])

        

