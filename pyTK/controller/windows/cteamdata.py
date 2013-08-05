#------------------------------------------------------------------------------
# cteamdata module
#   -- contains the functions and classes for controlling the teamdata window
#------------------------------------------------------------------------------
from Tkinter import *

from model.team import *

#------------------------------------------------------------------------------
# TeamDataController Class
#   -- contains information for setting and getting data and display values
#------------------------------------------------------------------------------
class TeamDataController():
    """Class that handles commands from the teamdata window."""

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
                     ("avgAutoPickUp","Average Auto Discs Picked Up: "),("avgAutoDiscsScored","Average Auto Discs Scored: "),
                     ("avgAutoTopDiscs","Average Auto Scored in Top: "),("avgAutoMidDiscs","Average Auto Scored in Mid: "),
                     ("avgAutoLowDiscs","Average Auto Scored in Low: "),
                     ("pWasDisabled","Matches/Disabled Percentage: "),("avgDisabled","Average Times Disabled per Match: "),
                     ("totalDisabled","Number of Times Disabled: "),("avgFloorPickUp","Average Discs Picked Up: "),
                     ("avgStationPickUp","Average Discs Loaded: "),("avgTeleScore","Average Tele Score: "),
                     ("avgTeleDiscsScored","Average Tele Discs Scored: "),
                     ("avgTelePyrDiscs","Average Tele Scored in Pyramid: "),("avgTeleTopDiscs","Average Tele Scored in Top: "),
                     ("avgTeleMidDiscs","Average Tele Scored in Middle: "),("avgTeleLowDiscs","Average Tele Scored in Low: "),
                     ("avgHangScore","Average Hang Score: "),("rHangSuccToAtt","Successful Hangs to Attempts: "),
                     ("pHanged","Hung from pyramid: "),("avgSupportBot","Average Support of Another Bot while Hanging: "),
                     ("avgScoredOnPyr","Average Disc Scores while Hanging: "),("avgFoulScore","Average Foul Score: "),
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

    graphVals = [("avgOff","Scores","oScores"),("avgDef","Scores","dScores"),
                 ("avgAst","Scores","aScores"),("avgTotal","Scores","tScores"),
                 ("WeightedOff","Scores","woScores"),("WeightedDef","Scores","wdScores"),
                 ("WeightedAst","Scores","waScores"),("WeightedTotal","Scores","wScores"),
                 ("avgAutoScore","Scores","autoScores"),("avgAutoPickUp","Info","autoDiscsPU"),
                 ("avgAutoDiscsScored","Info","autoDiscsScored"),("avgAutoTopDiscs","Info","autoTopScored"),
                 ("avgAutoMidDiscs","Info","autoMidScored"),("avgAutoLowDiscs","Info","autoLowScored"),
                 ("avgDisabled","Info","disabledState"),
                 ("avgFloorPickUp","Info","teleFloorDiscsPU"),("avgStationPickUp","Info","teleStationDiscsPU"),
                 ("avgTeleScore","Scores","teleScores"),("avgTeleDiscsScored","Info","teleDiscsScored"),
                 ("avgTelePyrDiscs","Info","telePyrScored"),("avgTeleTopDiscs","Info","teleTopScored"),
                 ("avgTeleMidDiscs","Info","teleMidScored"),("avgTeleLowDiscs","Info","teleLowScored"),
                 ("avgHangScore","Scores","hangScores"),
                 ("avgSupportBot","Info","supportsBot"),("avgScoredOnPyr","Info","scoredOnPyr"),
                 ("avgRegFoul","Info","RegFouls"),("avgTechFoul","Info","TechFouls")]
    
    def __init__(self):
        self.teamNum = 0
        self.entry = None
        self.data = None
        self.image = None

    # gets the team # from self.entry and finds the corresponding team
    # returns true if the team was found and false if not
    def loadData(self):
        try:
            self.teamNum = int(self.entry.get())
        except:
            print "Team value not valid."
            self.teamNum = 0
            
        for team in Team.team_list:
            if team.number == self.teamNum:
                self.data = team
                print "Loading team..."
                return True
            
        print "Team not found."
        return False

    # gets the image file corresponding to self.teamNum and returns it
    # if team is not found: returns nopic.gif
    def get_PhotoImage(self):
        image_name = "Images/" + str(self.teamNum) + ".gif"
        try:
            open(image_name)
        except:
            self.image = PhotoImage(file="Images/nopic.gif")
            return self.image
        
        self.image = PhotoImage(file=image_name)
        return self.image

    def get_GraphData(self, graphType=None):
        index = None
        data = None
        try:
            graphName = self.dataLabelVals[int(graphType[0])][0]  
        except:
            graphName = None

        #find the index and attr name
        for x, y, z in self.graphVals:
            if x == graphName:
                index = y
                data = z
                break # do not continue to iterate through the list
        try:
            currentIndex = self.data.getAttr(index)
            return currentIndex.getAttr(data)
        except:
            print "Cannot find data for that graph."
            return None
