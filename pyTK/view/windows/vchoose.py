#------------------------------------------------------------------------------
# vchoose module
#   -- contains information for displaying the alliance selection window
#------------------------------------------------------------------------------
from Tkinter import *
import tkMessageBox
import re

from controller.windows import cchoose
from controller.windows import cteamdata
from view.windows import vteamdata
from view.customs import ddlist

#------------------------------------------------------------------------------
# Choose class
#   -- contians all functions, etc, for displaying an alliance selection window
#------------------------------------------------------------------------------
class Choose(Frame):
    """Class that handles displayed an alliance selection window to the screen."""

    def pollList(self):
        now = self.wantedList.rList
        if now != self.current:
            rList = []
            for item in self.wantedList.rList:
                rList.append(re.search('Team (.*)', item).group(1))
            self.controller.sortWanted(rList=rList)
            self.current = now
        self.after(250, self.pollList)

    def load_team(self,event=None,data=""):
        data = self.wantedList.rList[int(data[0])]
        try:
            number = re.search('Team (.*)', data).group(1)
        except AttributeError:
            number = ""
        newWindow = Toplevel(self.grandParent)
        tdc = cteamdata.TeamDataController()
        teamdata = vteamdata.TeamData(newWindow,self,tdc,number)

    def checkSelections(self):
        selected = []
        if self.controller.wantedList:
            for k in xrange(0,len(self.controller.wantedList)):
                for i in xrange(0,len(self.alliances)):
                    for j in xrange(0,3):
                        team = self.alliances[i][j].get()
                        if int(team) == self.controller.wantedList[k].number:
                            selected.append(k)

            for i in xrange(0,len(self.controller.wantedList)):
                if i in selected:
                    self.wantedList.itemconfig(i,fg="gray")
                else:
                    self.wantedList.itemconfig(i,fg="black")

        
    def updateWanted(self,event=None,data=None):
        if event:
            data = self.wantedList.rList[data]
            try:
                number = re.search('Team (.*)', data).group(1)
            except AttributeError:
                number = 0
        else:
            try:
                number = int(data.get())
            except:
                number = 0
                
        self.controller.subWanted(number=number)
            
        self.wantedList.delete(0,END)
        for team in self.controller.wantedList:
            self.labelVar = ("Team "+str(team.number))
            self.wantedList.insert(END,self.labelVar)
            self.wantedList.rList = self.wantedList.get(0,END)

        self.checkSelections()
            
    def updateAlliances(self,event=None,team=None,ally=None,value=None):
        available = False
        taken = False
        captain = False

        # search for the current status of the team
        for item in self.controller.availableList:
            if item.number == int(team.get()) or int(team.get()) == 0:
                available = True
                break
 
        for i in xrange(0,len(self.alliances)):
            for j in xrange(0,3):
                if team.get() == self.alliances[i][j].get() and int(team.get()) != 0 and i != ally:
                    if int(self.alliances[i][1].get()) != 0:
                        taken = True
                        tkMessageBox.showinfo("Team Status",
                                              "Team " + str(team.get()) + " is already taken.  Please choose another team.")
                        team.set("0")
                        self.alliances[ally][value].set("0")
                        break
                    elif j == 0:
                        taken = False
                        captain = True
                        alliance = i
                        break
                if not available:
                    tkMessageBox.showinfo("Team Status",
                                          "Team " + str(team.get()) + " is not available.  Please choose another team.")
                    team.set("0")
                    self.alliances[ally][value].set("0")
                    break
            if taken or captain or not available:
                break

        # deal with the team choice based on their status
        if taken == False and available == True:
            if captain == True:
                for i in xrange(ally+1,len(self.alliances)):
                    try:
                        self.alliances[i][0].set(self.alliances[i+1][0].get())
                    except IndexError:
                        self.alliances[i][0].set("0")
                        
            self.alliances[ally][value].set(team.get())
                    

        # go through and search out the wantedList for chosen teams
        self.checkSelections()
        
    def startup(self):
        # create the frame to show the alliance entries in
        self.selectionFrame = Frame(self)
        self.selectionFrame.pack(side=LEFT,padx=5,pady=5)

        # make the label and entry widgets
        self.alliances = []
        for i in xrange(0,8):
            self.allianceFrame = Frame(self.selectionFrame)
            self.allianceFrame.pack(side=TOP,padx=5,pady=5)
            self.label = Label(self.allianceFrame,text="Alliance %d"%(i+1))
            self.label.pack(side=LEFT,padx=5)

            teams = []
            for j in xrange(0,3):
                self.EntryVar = StringVar()
                self.EntryVar.set("0")
                self.allianceEntry = Entry(self.allianceFrame,textvariable=self.EntryVar,width=4,takefocus=True)
                self.allianceEntry.bind("<Return>",lambda event,team=self.EntryVar,ally=i,value=j: self.updateAlliances(event,team,ally,value))
                self.allianceEntry.pack(side=LEFT,padx=5)
                teams.append(self.EntryVar)

            self.alliances.append(teams)

##          # not yet finished, still need to figure out how to organize alliances for saving
##            self.saveButton = Button(self.allianceFrame,text="Save",command=lambda i=i: self.saveAlliance(i))
##            self.saveButton.pack(side=LEFT,padx=5)

        # create the frame to show the wanted list in
        self.wantedFrame = Frame(self)
        self.wantedFrame.pack(side=LEFT,padx=5,pady=5)

        # create the title for the wanted list
        self.wantedLabel = Label(self.wantedFrame,text="Wanted")
        self.wantedLabel.pack(side=TOP,pady=5)

        # add wanted teams to the list
        self.wantedScroller = Scrollbar(self.wantedFrame)
        self.wantedScroller.pack(side=RIGHT,fill=Y)
        self.wantedList = ddlist.DDList(self.wantedFrame,width=20,height=15,
                                  yscrollcommand=self.wantedScroller.set)
        self.wantedList.bind("<Double-Button-1>",lambda event: self.load_team(data=self.wantedList.curselection()))
        self.wantedList.bind("<Return>",lambda event: self.load_team(data=self.wantedList.curselection()))
        self.wantedList.bind("<Button-3>",lambda event: self.updateWanted(event=event,data=self.wantedList.nearest(event.y)))
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
        self.alliances = []
        self.current = None

        self.parent.title("Alliance Selection")

        Frame.__init__(self,parent)
        self.pack()
        self.startup()
