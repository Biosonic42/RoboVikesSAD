#------------------------------------------------------------------------------
# cchoose module
#   -- contains data and information for controlling the alliance selection window
#------------------------------------------------------------------------------
from Tkinter import *

from model import team

#------------------------------------------------------------------------------
# ChooseController class
#   -- contains functions, lists, data, etc, for handling the alliance selection window
#------------------------------------------------------------------------------
class ChooseController():
    """Class that handles commands from the alliance selection window."""

    def __init__(self):
        self.wantedList = team.Team.wanted
        self.availableList = team.Team.team_list

    def subWanted(self,number=None):
        for t in team.Team.wanted:
            if t.number == int(number):
                team.Team.wanted.remove(t)
                break

        self.wantedList = team.Team.wanted

    def sortWanted(self,rList=None):
        newList = []
        for item in rList:
            for t in team.Team.team_list:
                if t.number == int(item):
                    newList.append(t)
                    break
                    
        team.Team.wanted = newList
        self.wantedList = team.Team.wanted
        
