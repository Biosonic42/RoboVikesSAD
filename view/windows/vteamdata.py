#------------------------------------------------------------------------------
# vteamdata moudle
#   -- contains the application for viewing the teamdata window
#------------------------------------------------------------------------------
from Tkinter import *

import sys
sys.path.append("../../")
from controller.windows import cteamdata

class TeamData(Frame):
    """Class that handles running the window to view data on a team."""

    # use these to index values to display, use the system: ("key", "term")
    # where key corresponds to a value in team and term labels that value
    dataLabelVals = [("numMatch","Number of Matches: "),
                 ("pOff","Played Offensive: "),("pDef","Played Defensive: "),("pAst","Played Assistive: "),
                 ("avgOff","Average Offensive Score: "),("avgDef","Average Defensive Score: "),("avgAst","Average Assistive Score: "),
                 ("avgTotal","Average Total Score: "),("WeightedOff","Average Weighted Offensive Score: "),
                 ("WeightedDef","Average Weighted Defensive Score: "),("WeightedAst","Average Weighted Assistive Score: "),
                 ("WeightedTotal","Average Weighted Total Score: "),
                 ("pHadAuto","Had Auto Mode: "),("pStartInZone","Started in Auto Zone: "),
                 ("pOtherStrat","Other Auto Strategy: "),("avgAutoScore","Average Auto Score: "),
                 ("avgAutoPickUp","Average Auto Discs Picked Up: "),("avgAutoTopDiscs","Average Auto Scored in Top: "),
                 ("avgAutoMidDiscs","Average Auto Scored in Mid: "),("avgAutoLowDiscs","Average Auto Scored in Low: "),
                 ("pWasDisabled","Matches/Disabled Percentage: "),("avgDisabled","Average Times Disabled per Match: "),
                 ("totalDisabled","Number of Times Disabled: "),("avgFloorPickUp","Average Discs Picked Up: "),
                 ("avgStationPickUp","Average Discs Loaded: "),("avgTeleScore","Average Tele Score: "),
                 ("avgTelePyrDiscs","Average Tele Scored in Pyramid: "),("avgTeleTopDiscs","Average Tele Scored in Top: "),
                 ("avgTeleMidDiscs","Average Tele Scored in Middle: "),("avgTeleLowDiscs","Average Tele Scored in Low: "),
                 ("avgHangScore","Average Hang Score: "),("rHangSuccToAtt","Successful Hangs to Attempts: "),
                 ("pHanged","Hung from pyramid: "),("avgSupportBot","Average Support of Another Bot while Hanging: "),
                 ("avgScoredOnPyr","Average Disc Scores while Hanging: "),
                 ("avgRegFoul","Average Number of Regular Fouls: "),("avgTechFoul","Average Number of Technical Fouls: "),
                 ("pYellow","Received Yellow Card: "),("pRed","Received Red Card: ")]

    maxminLabelVals = [("maxOffScore","Maximum Offensive Score: "),("minOffScore","Minimum Offensive Score: "),
                       ("maxDefScore","Maximum Defensive Score: "),("minDefScore","Minimum Defensive Score: "),
                       ("maxAstScore","Maximum Assistive Score: "),("minAstScore","Minimum Assistive Score: "),
                       ("maxTotalScore","Maximum Total Score: "),("minTotalScore","Minimum Total Score: "),
                       ("maxWScore","Maximum Weighted Score: "),("minWScore","Minimum Weighted Score: "),
                       ("maxWOScore","Maximum Weighted Offensive Score: "),("minWOScore","Minimum Weighted Offensive Score: "),
                       ("maxWDScore","Maximum Weighted Defensive Score: "),("minWDScore","Minimum Weighted Defensive Score: "),
                       ("maxWAScore","Maximum Weighted Assistive Score: "),("minWAScore","Minimum Weighted Assistive Score: "),
                       ("maxTAScore","Maximum TeleAuto Score: "),("minTAScore","Minimum TeleAuto Score: "),
                       ("maxHangScore","Maximum Hang Score: "),("minHangScore","Minimum Hang Score: "),
                       ("maxAutoScore","Maximum Auto Score: "),("minAutoScore","Minimum Auto Score: "),
                       ("maxTeleScore","Maximum Tele Score: "),("minTeleScore","Minimum Tele Score: "),
                       ("maxFoulScore","Maximum Foul Score: "),("minFoulScore","Minimum Foul Score: ")]
    
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
            for x, y in self.maxminLabelVals:
                self.labelVar = str(y) + str(self.controller.data.Scores.getAttr(x))
                self.teamScores.insert(END, self.labelVar)
            self.teamScores.pack(side=RIGHT,fill=Y)
            self.scrollbar2.config(command=self.teamScores.yview)
            self.contents.append(self.teamScores)
            self.contents.append(self.scrollbar2)

            #make the listbox and scroller containing information values
            self.scrollbar = Scrollbar(self.dataFrame)
            self.scrollbar.pack(side=RIGHT,fill=Y)
            self.teamInfo = Listbox(self.dataFrame,height=30,width=50,
                                    yscrollcommand=self.scrollbar.set)
            for x, y in self.dataLabelVals:
                self.labelVar = str(y) + str(self.controller.data.getAttr(x))
                self.teamInfo.insert(END, self.labelVar)
            self.teamInfo.pack(side=RIGHT,fill=Y)
            self.scrollbar.config(command=self.teamInfo.yview)
            self.contents.append(self.teamInfo)
            self.contents.append(self.scrollbar)

            self.shown = True

    def hide(self):
        if self.shown == True:
            for i in xrange(0,len(self.contents)):
                self.contents[i].destroy()
            self.shown = False
            
    def buttonClicked(self):
        if self.controller.loadData():
            self.hide()
            self.show()
        
    def startup(self):
        self.startupFrame = Frame(self)
        self.startupFrame.pack(side=TOP,pady=5)
        self.teamNum = StringVar()
        self.label = Label(self.startupFrame, text="Team # ").pack(side=LEFT,padx=5)
        self.entry = Entry(self.startupFrame, textvariable=self.teamNum, width=4)
        self.entry.pack(side=LEFT,padx=5)
        self.controller.entry = self.entry
        self.button = Button(self.startupFrame, text="Load Data")
        self.button.config(command=self.buttonClicked)
        self.button.pack(side=LEFT,padx=5)
        self.controller.button = self.button
        
    def __init__(self, parent=None, controller=None):
        self.shown = False
        self.contents = []
        self.controller=controller
        
        parent.title("TeamData")
        Frame.__init__(self, parent)
        self.pack()
        self.startup()
