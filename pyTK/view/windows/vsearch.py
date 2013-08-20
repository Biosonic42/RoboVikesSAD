#------------------------------------------------------------------------------
# vsearch module
#   -- contains information for displaying the search window
#------------------------------------------------------------------------------
from Tkinter import *
import re

from controller.windows import csearch
from controller.windows import cteamdata
from view.windows import vteamdata
from view.customs import ddlist

#------------------------------------------------------------------------------
# Search class
#   -- contains all the functions, etc, for displaying a search window
#------------------------------------------------------------------------------
class Search(Frame):
    """Class that handles displaying a search window to the screen."""

    def pollList(self):
        now = self.wantedList.rList
        if now != self.current:
            rList = []
            for item in self.wantedList.rList:
                rList.append(re.search('Team (.*)', item).group(1))
            self.controller.sortWanted(rList=rList)
            self.current = now
        self.after(250, self.pollList)
        
    def load_team(self,event=None,data="",wanted=False):
        if wanted==False:
            data = self.labelVars[int(data[0])]
        elif wanted==True:
            data = self.wantedList.rList[int(data[0])]
        try:
            number = re.search('Team (.*)', data).group(1)
        except AttributeError:
            number = ""
        newWindow = Toplevel(self.grandParent)
        tdc = cteamdata.TeamDataController()
        teamdata = vteamdata.TeamData(newWindow,self,tdc,number)

    def updateWanted(self, event=None, data=None, add=True):
        if add == False:
            data = self.wantedList.rList[data]
            try:
                number = re.search('Team (.*)', data).group(1)
            except AttributeError:
                number = 0
            self.controller.subWanted(number=number)
        elif add == True:
            data = self.labelVars[data]
            try:
                number = re.search('Team (.*)', data).group(1)
            except AttributeError:
                number = 0
            self.controller.addWanted(number=number)
            
        self.wantedList.delete(0,END)
        for team in self.controller.wantedList:
            self.labelVar = ("Team "+str(team.number))
            self.wantedList.insert(END,self.labelVar)
            self.wantedList.rList = self.wantedList.get(0,END)
        
    def updateMatches(self, event=None,value=None,index=None):
        # do the search
        self.controller.searchVariables.append((index, value))
        self.controller.search()
        self.matchesList.delete(0,END)

        self.labelVars = []
        for team in self.controller.matchedList:
            self.labelVar  = ("Team "+str(team.number))
            self.labelVars.append(self.labelVar)
            self.matchesList.insert(END,self.labelVar)
        
    def startup(self):
        # create the frame to show the search options in
        self.searchFrame = Frame(self)
        self.searchFrame.pack(side=LEFT,padx=5,pady=5)

        # make the entry option widgets
        for x, y in self.controller.entryItemTypes:
            self.entryFrame = Frame(self.searchFrame)
            self.entryFrame.pack(side=TOP,pady=5)
            
            self.label = Label(self.entryFrame,text=y)
            self.label.pack(side=LEFT,padx=5)

            self.searchEntryVar = StringVar()
            self.searchEntryVar.set("-30")
            self.searchEntry = Entry(self.entryFrame,textvariable=self.searchEntryVar,width=4,takefocus=True)
            self.searchEntry.bind("<Return>",lambda event, value=self.searchEntryVar,index=x:self.updateMatches(event,value,index))
            self.searchEntry.pack(side=LEFT,padx=5)

        # make the checkbutton option widgets
        for x, y in self.controller.checkItemTypes:
            self.searchCheckVar = BooleanVar()
            self.searchCheck = Checkbutton(self.searchFrame,text=y,
                                           variable = self.searchCheckVar,
                                           command = lambda value=self.searchCheckVar,index=x:self.updateMatches(value=value,index=index))
            self.searchCheck.pack(side=TOP,padx=5,pady=2)

        # make the frame to show matches in
        self.matchesFrame = Frame(self)
        self.matchesFrame.pack(side=TOP,padx=5,pady=5)

        # create the title for the matches list
        self.matchesLabel = Label(self.matchesFrame,text="Matches")
        self.matchesLabel.pack(side=TOP,pady=5)

        # add matching teams to the list
        self.scrollbar = Scrollbar(self.matchesFrame)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.matchesList = Listbox(self.matchesFrame,width=20,height=20,
                                      yscrollcommand=self.scrollbar.set)
        self.labelVars = []
        for team in self.controller.matchedList:
            self.labelVar  = "Team "+str(team.number)
            self.labelVars.append(self.labelVar)
            self.matchesList.insert(END,self.labelVar)
        self.matchesList.bind("<Double-Button-1>",lambda event: self.load_team(data=self.matchesList.curselection()))
        self.matchesList.bind("<Return>",lambda event: self.load_team(data=self.matchesList.curselection()))
        self.matchesList.bind("<Button-3>",lambda event: self.updateWanted(event=event,data=self.matchesList.nearest(event.y)))
        self.matchesList.pack(side=RIGHT,fill=Y)
        self.scrollbar.config(command=self.matchesList.yview)

        # make the frame to show wanted teams in
        self.wantedFrame = Frame(self)
        self.wantedFrame.pack(side=BOTTOM,padx=5,pady=5)

        # create the title for the wanted list
        self.wantedLabel = Label(self.wantedFrame,text="Wanted")
        self.wantedLabel.pack(side=TOP,pady=5)

        # add wanted teams to the list
        self.wantedScroller = Scrollbar(self.wantedFrame)
        self.wantedScroller.pack(side=RIGHT,fill=Y)
        self.wantedList = ddlist.DDList(self.wantedFrame,width=20,height=20,
                                  yscrollcommand=self.wantedScroller.set)
        self.wantedList.bind("<Double-Button-1>",lambda event: self.load_team(data=self.wantedList.curselection(),wanted=True))
        self.wantedList.bind("<Return>",lambda event: self.load_team(data=self.wantedList.curselection(),wanted=True))
        self.wantedList.bind("<Button-3>",lambda event: self.updateWanted(event=event,data=self.wantedList.nearest(event.y),add=False))
        for team in self.controller.wantedList:
            self.labelVar = "Team "+str(team.number)
            self.wantedList.insert(END,self.labelVar)
            self.wantedList.rList = self.wantedList.get(0,END)
        self.wantedList.pack(side=RIGHT,fill=Y)
        self.wantedScroller.config(command=self.wantedList.yview)

        self.pollList()
        
    def __init__(self, parent=None, grandParent=None, controller=None):
        self.controller = controller
        self.parent = parent
        self.grandParent = grandParent
        self.current = None

        self.parent.title("Search")

        Frame.__init__(self, parent)
        self.pack()
        self.startup()
