#------------------------------------------------------------------------------
# vranking module
#   -- contains the application for viewing the ranking window
#------------------------------------------------------------------------------
from Tkinter import *
import re

from controller.windows import cranking
from controller.windows import cteamdata
from view.windows import vteamdata
    
#------------------------------------------------------------------------------
# _Listing Class
#   -- creates a frame that holds one set of options for different rankings
#------------------------------------------------------------------------------
class _Listing(Frame):

    def __init__(self,parent=None,grandParent=None,kind="None"):
        self.parent = parent
        self.grandParent = grandParent
        self.controller = cranking.RankingController()
        
        Frame.__init__(self,parent,relief=RAISED,bd=2)
        self.pack(side=LEFT,padx=10,pady=10,fill=Y)
        
        self.create_Listing(kind=kind)

    def load_team(self,event=None,data=""):
        data = self.labelVars[int(data[0])]
        try:
            number = re.search('Team (.*):', data).group(1)
        except AttributeError:
            number = ""
        newWindow = Toplevel(self.grandParent)
        tdc = cteamdata.TeamDataController()
        teamdata = vteamdata.TeamData(newWindow,self,tdc,number)

    def hide_rankings(self,event=None):
        try:
            self.listingFrame.destroy()
            self.labelVars = []
        except:
            pass

    def show_rankings(self,kind="None",event=None):
        self.listingFrame = Frame(self)
        self.listingFrame.pack(side=BOTTOM,padx=5,pady=5)

        self.controller.load_rankings(kind)

        self.scrollbar = Scrollbar(self.listingFrame)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.rankList = Listbox(self.listingFrame,height=30,width=40,
                                      yscrollcommand=self.scrollbar.set)
        self.labelVars = []
        i=1
        for data, team in self.controller.data:
            self.labelVar = (str(i)+(" - Team ")+str(team)+": "+str(data))
            self.labelVars.append(self.labelVar)
            self.rankList.insert(END, self.labelVar)
            i+=1
        self.rankList.bind("<Double-Button-1>",lambda event: self.load_team(data=self.rankList.curselection()))
        self.rankList.bind("<Return>",lambda event: self.load_team(data=self.rankList.curselection()))
        self.rankList.pack(side=RIGHT,fill=Y)
        self.scrollbar.config(command=self.rankList.yview)

    def load_rankings(self,kind="None",event=None):
        self.hide_rankings()
        self.show_rankings(kind)
                      
    def hide_settings(self,event=None):
        try:
            self.settingFrame.destroy()
        except:
            pass
        
    def show_settings(self,kind="None",event=None):
        if kind != "None":
            # create a frame to put the settings for the list on
            self.settingFrame = Frame(self)
            self.settingFrame.pack(side=TOP,padx=5,pady=5)
            
            # create an option to reverse the list
            self.reverseCheck = Checkbutton(self.settingFrame,
                                            variable=self.controller.rev,
                                            text="Reverse",
                                            command = lambda kind=kind:self.load_rankings(kind=kind))
            self.reverseCheck.pack(side=LEFT)
            
            # create options for sorting the list
            for text, value in self.controller.sortOptions:
                self.sortOption = Radiobutton(self.settingFrame,text=text,
                                              variable=self.controller.sort,
                                              value=value,
                                              command = lambda kind=kind:self.load_rankings(kind=kind))
                self.sortOption.pack(side=LEFT)

            self.load_rankings(kind=kind)
        else:
            self.hide_settings()
            self.hide_rankings()
                
    
    def load_settings(self,kind="None",event=None):
        self.hide_settings()
        self.show_settings(kind)
        
    def delete_Listing(self,event=None):
        self.destroy()
        
    def create_Listing(self,event=None,kind="None"):
        # create a frame to show the options menu and delete button
        self.optionsFrame = Frame(self)
        self.optionsFrame.pack(side=TOP)

        # get the default value for a ranking list
        self.choiceVar = StringVar(self.optionsFrame)
        self.choiceVar.set(kind)

        # make the drop down menu for choosing a ranking to display
        self.chooseRank = OptionMenu(self.optionsFrame, self.choiceVar, *self.controller.rankingTypes,
                                     command=lambda new_value:self.load_settings(kind=new_value))
        self.chooseRank.config(width=25)
        self.chooseRank.pack(side=LEFT,padx=5,pady=5)

        # make a button to delete this rankingList
        self.deleteButton = Button(self.optionsFrame, text="Delete List",
                                   command=self.delete_Listing)
        self.deleteButton.pack(side=RIGHT,padx=5,pady=5)

#------------------------------------------------------------------------------
# Ranking Class
#   -- creates a frame that holds all of the rankings in seperate _Listings
#------------------------------------------------------------------------------
class Ranking(Frame):
    """Class that handles running the window to view rankings of the teams."""
        
    def startup(self,kind="None"):
        # make a button to add another ranking list
        self.addButton = Button(self, text="Add List", command=self.create_newListing)
        self.addButton.pack(side=RIGHT,padx=5,pady=10,anchor=NE)

        self.create_newListing(kind=kind)

    def create_newListing(self,kind="None"):
        # create a basic rankingList
        self.newListing = _Listing(self,self.grandParent)
        self.newListing.pack()
        
    def __init__(self,parent=None,grandParent=None,controller=None,kind="None"):
        self.controller = controller
        self.parent = parent
        self.grandParent = grandParent

        self.parent.title("Ranking")
        Frame.__init__(self, parent)
        self.pack()
        self.startup(kind=kind)
