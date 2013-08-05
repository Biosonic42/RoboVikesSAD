#------------------------------------------------------------------------------
# linear regression graph module
#   -- gets the data and display for a linear regression graph
#   -- other than Tkinter this code is copied directly from Chad Eatman
#------------------------------------------------------------------------------
from Tkinter import *

import sys
sys.path.append("../")

#------------------------------------------------------------------------------
# Lreg class
#   -- a custom Tkinter widget for displaying Linear regression graphs
#------------------------------------------------------------------------------
class Lreg(Canvas):

    def addPoint(self,i=0,x=0,y=0):
        if self.find_withtag("myText%d"%i):
            self.delete("myText%d"%i)
        else:
            text = (i+1,self.graphData[i])
            self.create_text(x,self.height-y,text=str(text),tags="myText%d"%i)
        
    def get_info(self):
        #prepare the graph to be drawn
        self.x = []
        self.y = []
        for i in xrange(0,len(self.graphData)):
            self.x.append(long(i+1))
            self.y.append(long(self.graphData[i]))
        self.b = 0  # slope
        self.a = 0  # constant
        self.r2 = 0  # coefficient of determination

        # get a and b
        n = len(self.x)
        self.xy = []
        self.x2 = []
        self.y2 = []

        for i in xrange(0,n):
            self.xy.append(self.x[i]*self.y[i])
            self.x2.append(self.x[i]**2)
            self.y2.append(self.y[i]**2)
        try:
            self.b = (float(n)*sum(self.xy)-sum(self.x)*sum(self.y))/(float(n)*sum(self.x2)-sum(self.x)**2)
        except:
            self.b = 1000000000000000000000000000 # arbitrarily high number, assumed undefined slope
        self.a = (sum(self.y)/float(len(self.y))) - self.b*(sum(self.x)/float(n))

        #get r
        hmy2 = []
        ymh2 = []
        try:
            for i in xrange(0,len(self.y)):
                hy = self.x[i]*self.b+self.a
                hmy2.append((hy-(sum(self.y)/len(self.y)))**2)
                ymh2.append((self.y[i]-(sum(self.y)/len(self.y)))**2)
            self.r2 = sum(hmy2)/sum(ymh2)
        except:
            self.r2 = "N/A"
            
    def draw(self):
        self.get_info()

        # get background, etc.
        self.tx = []
        self.ty = []
        maxy = max(self.y)
        xmod = (self.width-2*self.stx)/float(len(self.x))
        ymod = (self.height-2*self.sty)/float(maxy) if maxy else self.height-2*self.sty
        
        #always start at x = 0, y = 0
        for point in self.x:
            self.tx.append(xmod*point+self.stx)
        for point in self.y:
            self.ty.append(ymod*point+self.sty)
            
        # remember that image is flipped vertically
        x1 = self.stx
        x2 = self.width-self.stx
        y1 = self.height-self.sty
        y2 = self.sty
        
        #draw axes
        self.create_line(x1,y1,x2,y1)
        self.create_line(x1,y1,x1,y2)
        
        #draw numbers at the end of axes to indicate max value
        xmax = max(self.x)
        ymax = max(self.y)
        self.create_text(self.width-.5*self.stx,y1,text=str(xmax))
        self.create_text(x1,.5*self.stx,text=str(ymax))
        
        #draw points on graph and lines between points
        for i in xrange(0,len(self.tx)):
            self.create_oval(int(self.tx[i]-4),int(self.height-self.ty[i]-4),
                             int(self.tx[i]+4),int(self.height-self.ty[i]+4),
                             fill="black",tags="myPoint%d" % i)
            self.tag_bind("myPoint%d" % i, "<Button-1>",
                          lambda event,i=i,x=self.tx[i]-10,y=self.ty[i]+10: self.addPoint(i=i,x=x,y=y))
        for i in xrange(1,len(self.tx)):
            self.create_line(self.tx[i-1],self.height-self.ty[i-1],
                             self.tx[i],self.height-self.ty[i])

        #draw the line of best fit
        self.create_line(self.stx,self.height-(self.a*ymod+self.sty),
                         len(self.x)*xmod+self.stx,
                         self.height-((self.b*len(self.x)+self.a)*ymod+self.sty))
        
        
    def __init__(self,parent,graphData,width=256,height=192,
                 bg="white",stx=20,sty=20):
        Canvas.__init__(self, parent)
        self.pack()
        self.graphData = graphData
        self.width=width
        self.height=height
        self.bg = bg
        self.stx=stx
        self.sty=sty
        self.config(bg=bg,height=height,width=width)

        self.draw()
