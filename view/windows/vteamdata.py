#------------------------------------------------------------------------------
# vteamdata moudle
#   -- contains the application for viewing the teamdata window
#------------------------------------------------------------------------------
from Tkinter import *

import sys
sys.path.append("../../")
from controller.windows import cteamdata
from view import vlreg
from controller import clreg

class TeamData(Frame):
    """Class that handles running the window to view data on a team."""
    
    def graph_data(self, graphType, event=None):
        #remove the previous graph to make room for the new one
        self.graph.destroy()
        #find the name of the graph out of index
        typeIndex = None
        graphData = None
        try:
            graphName = self.controller.dataLabelVals[int(graphType[0])][0]  
        except:
            graphName = None

        #find the index and attr name
        for x, y, z in self.graphVals:
            if x == graphName:
                typeIndex = y
                graphData = z
                break # do not continue to iterate through the list
    
        #get the attr value from our Team and make us a copy
        self.graphData = self.controller.get_GraphData(index=typeIndex, data=graphData)
        print self.graphData

        if self.graphData:
            self.graphController = clreg.LregController()
            self.graph = vlreg.Lreg(self.graphFrame, self.graphData,
                                    controller=self.graphController)
            self.graph.pack()
            self.contents.append(self.graph)
        
    def show(self):   
        if self.shown == False:
            #make the frame to show data to
            self.dataFrame = Frame(self, relief=SUNKEN,bd=1)
            self.dataFrame.pack(side=BOTTOM,pady=10)
            self.contents.append(self.dataFrame)

            #make the listbox and scroller containing maxmin values
            self.scrollbar2 = Scrollbar(self.dataFrame)
            self.scrollbar2.pack(side=RIGHT,fill=Y)
            self.teamScores = Listbox(self.dataFrame,height=30,width=50,
                                      yscrollcommand=self.scrollbar2.set)
            for x, y in self.controller.maxminLabelVals:
                self.labelVar = str(y) + str(self.controller.data.Scores.getAttr(x))
                self.teamScores.insert(END, self.labelVar)
            self.teamScores.pack(side=RIGHT,fill=Y)
            self.scrollbar2.config(command=self.teamScores.yview)
            self.contents.append(self.teamScores)
            self.contents.append(self.scrollbar2)

            #make the listbox and scroller containing information values
            self.scrollbar = Scrollbar(self.dataFrame)
            self.scrollbar.pack(side=RIGHT,fill=Y)
            self.teamData = Listbox(self.dataFrame,height=30,width=50,
                                    yscrollcommand=self.scrollbar.set)
            for x, y in self.controller.dataLabelVals:
                self.labelVar = str(y) + str(self.controller.data.getAttr(x))
                self.teamData.insert(END, self.labelVar)
            self.teamData.pack(side=RIGHT,fill=Y)
            self.teamData.bind("<Double-Button-1>",lambda event: self.graph_data(graphType=self.teamData.curselection()))
            self.teamData.bind("<Return>",lambda event: self.graph_data(graphType=self.teamData.curselection()))
            self.scrollbar.config(command=self.teamData.yview)
            self.contents.append(self.teamData)
            self.contents.append(self.scrollbar)

            # make the frame to show the team pic on
            self.photoFrame = Frame(self,relief=RAISED,bd=1)
            self.photoFrame.pack(side=RIGHT,padx=20,pady=10)
            self.contents.append(self.photoFrame)

            # make the photo
            self.photoFile = self.controller.get_PhotoImage()
            self.teamPic = Label(self.photoFrame,image=self.photoFile,width=256,height=192)
            self.teamPic.pack()
            self.contents.append(self.teamPic)

            # make the frame to show the graph on
            self.graphFrame = Frame(self,relief=RAISED,bd=1)
            self.graphFrame.pack(side=LEFT,padx=20,pady=10)
            self.contents.append(self.graphFrame)

            # make an empty graph canvas to satisfy the frame
            self.graph = Canvas(self.graphFrame,width=256,height=192)
            self.graph.pack()
            self.contents.append(self.graph)

            self.shown = True

    def hide(self):
        if self.shown == True:
            for i in xrange(0,len(self.contents)):
                self.contents[i].destroy()
            self.contents = []
            self.shown = False
            
    def load(self, event=None):
        if self.controller.loadData():
            self.hide() # remove the old contents (if there are any)
            self.show() # display the new ones
        
    def startup(self):
        # create the frame for team loading
        self.startupFrame = Frame(self)
        self.startupFrame.pack(side=TOP,pady=5)

        # make the team number loading widgets and map commands / bindings
        self.teamNum = StringVar()
        self.label = Label(self.startupFrame, text="Team # ")
        self.label.pack(side=LEFT,padx=5)
        
        self.entry = Entry(self.startupFrame, textvariable=self.teamNum, width=4)
        self.entry.pack(side=LEFT,padx=5)
        self.entry.bind("<Return>",self.load)
        self.controller.entry = self.entry
        
        self.button = Button(self.startupFrame, text="Load Data")
        self.button.config(command=self.load)
        self.button.pack(side=LEFT,padx=5)
        
    def __init__(self, parent=None, controller=None):
        self.shown = False
        self.contents = []
        self.controller=controller
        self.graphData = None
        
        parent.title("TeamData")
        Frame.__init__(self, parent)
        self.pack()
        self.startup()
