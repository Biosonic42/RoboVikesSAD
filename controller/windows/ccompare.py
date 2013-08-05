#------------------------------------------------------------------------------
# ccompare module
#   -- contains data and information for controlling the compare window
#------------------------------------------------------------------------------
from Tkinter import *

from model import team
from model import calculate

#------------------------------------------------------------------------------
# SearchController class
#   -- contains functions, lists, data, etc, for handling the search window
#------------------------------------------------------------------------------
class CompareController():
    """Class that handles commands from the search window."""

    allianceOptions = ["Custom",
                       "Alliance 1","Alliance 2",
                       "Alliance 3","Alliance 4",
                       "Alliance 5","Alliance 6",
                       "Alliance 7","Alliance 8"]
    
    compareIndex = [("avgOff","Avg OffScore"),("avgDef","Avg DefScore"),("avgAst","Avg AstScore"),
                    ("avgAutoScore","Avg AutoScore"),("avgAutoDiscsScored","Avg AutoDiscs"),
                    ("avgTeleScore","Avg TeleScore"),("avgTeleDiscsScored","Avg TeleDiscs"),
                    ("avgHangScore","Avg HangScore"),("rHangSuccToAtt","Hang Ratio"),
                    ("avgFoulScore","Avg FoulScore")]
    
    def __init__(self):
        self.available = []
        for t in team.Team.team_list:
            self.available.append(str(t.number))

    def getInfo(self,teamVals=None,index=0):
        if int(teamVals[index][0].get()) != 0:
            for t in team.Team.team_list:
                if t.number == int(teamVals[index][0].get()):
                    for i in xrange(0,len(self.compareIndex)):
                        teamVals[index][i+1].set(str(t.getAttr(self.compareIndex[i][0])))
                    break
        else:
            for i in xrange(0,len(self.compareIndex)):
                teamVals[index][i+1].set("0")

    def getPrediction(self,team1,team2,team3):
        for t in team.Team.team_list:
            if t.number == int(team1.get()):
                team1 = t
                break
        for t in team.Team.team_list:
            if t.number == int(team2.get()):
                team2 = t
                break
        for t in team.Team.team_list:
            if t.number == int(team3.get()):
                team3 = t
                break

        return calculate.predict_scores(team1,team2,team3)

    def getComparison(self,teamNums=[]):
        teams = []
        for t in teamNums:
            for tm in team.Team.team_list:
                if int(t.get()) == tm.number:
                    teams.append(tm)

        return calculate.predict_outcome(teams)

    def loadAlliance(self,name=None):
        pass

    def saveAlliance(self,name="Custom Alliance",teams=[]):
        self.allianceOptions.append(name)

    def deleteAlliance(self,name="Custom Alliance"):
        for item in self.allianceOptions:
            if item == name:
                self.allianceOptions.remove(item)
