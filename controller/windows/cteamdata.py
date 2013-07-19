#------------------------------------------------------------------------------
# cteamdata module
#   -- contains the functions and classes for controlling the teamdata window
#------------------------------------------------------------------------------
from Tkinter import *

import sys
sys.path.append("../../")
from model.team import *

class TeamDataController():
    """Class that handles commands from the teamdata window."""

    def __init__(self):
        self.teamNum = 0
        self.button = None
        self.entry = None
        self.data = None

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

        return False
                
            
        
