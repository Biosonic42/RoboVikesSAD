#------------------------------------------------------------------------------
# team Module
#   -- Keeps track of valuable team information and scorings
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# TeamInfo Class
#   -- Stores performance information
#------------------------------------------------------------------------------
class _TeamInfo(object):
    """Used to handle information for different teams."""

    def __init__(self):
        self.matches = []           # list holding the matches the team was in
        self.hangLevel = []         # list holding the level of hang for each match
        self.hangSuccess = []       # list holding the success of hang for each match
        self.timesHanged = 0        # the number of matches for which the team hanged successfully
        self.attemptedHang = 0      # the number of matches for which the team attempted to hang
        self.SupportsBot = []       # list holding the state of whether this robot supported another or not (by match)
        self.ScoredOnPyr = []       # list holding the state of whether this robot scored while hanging from the pyramid or not (by match)
        self.numOff = 0             # the number of matches for which the team played offensively
        self.numDef = 0             # the number of matches for which the team played defensively
        self.numAst = 0             # the number of matches for which the team played assistively

        self.hadAuto = 0            # the number of matches for which the team had an autonomous mode that did something
        self.StartedInAuto = 0      # the number of matches for which the team started completely within the autonomous zone
        self.OtherAutoStrat = 0     # the number of matches for which the team had another strategy (not offensive) in autonomous mode
        self.autoDiscsScored = []   # list holding the number of discs scored in autonomous (by match)
        self.autoDiscsPU = []       # list holding the number of discs picked up in autonomous (by match)
        self.autoTopScored = []     # list holding the number of discs scored in the top goal in autonomous (by match)
        self.autoMidScored = []     # list holding the number of discs scored in the mid goal in autonomous (by match)
        self.autoLowScored = []     # list holding the number of discs scored in the low goal in autonomous (by match)
        self.scoredAuto = 0         # the number of matches for which the team scored in autonomous mode

        self.hadTele = 0            # the number of matches for which the robot scored in tele-op mode
        self.disabledState = []     # list holding the number of times this robot was disabled per match
        self.disabled = 0           # the number of matches this robot was disabled in
        self.disabledCount = 0      # the total number of time this robot was disabled
        self.teleFloorDiscsPU = []  # list holding the number of discs picked up from the floor in tele-op (by match)
        self.teleStationDiscsPU = []# list holding the number of discs loaded from the station in tele-op (by match)
        self.discsPU = []           # list holding the number of discs picked up (floor and station) in tele-op (by match)
        self.teleDiscsScored = []   # list holding the number of discs scored in tele-op (by match)
        self.telePyrScored = []     # list holding the number of discs scored in the pyramid in tele-op (by match)
        self.teleTopScored = []     # list holding the number of discs scored in the top in tele-op (by match)
        self.teleMidScored = []     # list holding the number of discs scored in the mid in tele-op (by match)
        self.teleLowScored = []     # list holding the number of discs scored in the low in tele-op (by match)
        
        self.RegFouls = []          # list holding the number of regular   fouls for each match
        self.TechFouls = []         # list holding the number of technical fouls for each match
        self.hadRegFoul = 0         # the number of matches for which a team incurred a regular foul
        self.hadTechFoul = 0        # the number of matches for which a team incurred a technical foul
        self.hadYellow = 0          # the number of matches for which a team incurred a yellow card
        self.hadRed = 0             # the number of matches for which a team incurred a red card

#------------------------------------------------------------------------------
# TeamScores Class
#   -- stores data about a team's scores
#------------------------------------------------------------------------------
class _TeamScores(object):
    """Used to handle scoring data for different teams."""

    def __init__(self):
        self.oScores = []           # list holding offensive scores
        self.dScores = []           # list holding defensive scores
        self.aScores = []           # list holding assistive scores
        self.tScores = []           # list holding total scores
        self.wScores = []           # list holding weighted  scores
        self.woScores = []          # list holding weighted offensive scores
        self.wdScores = []          # list holding weighted defensive scores
        self.waScores = []          # list holding weighted assistive scores
        self.taScores = []          # list holding tele-auto scores
        self.hangScores = []        # list holding hang scores
        self.autoScores = []        # list holding auto scores
        self.teleScores = []        # list holding tele scores
        self.foulScores = []        # list holding foul scores

#------------------------------------------------------------------------------
# TeamPitInfo Class
#   -- stores data unrelated to performance on the field
#------------------------------------------------------------------------------
class _TeamPitInfo(object):
    """Used to handle information about a teams chassis and other
       non-performance related information."""

    def __init__(self):
        self.robotlen = 0           # the length of the robot's chassis
        self.robotwid = 0           # the width  of the robot's chassis
        self.robotheg = 0           # the height of the robot
        self.robotwig = 0           # the weight of the robot
        self.floorclear = ""        # the distance to the floor from the bottom of the chassis
        self.wheelspace = ""        # the spacing between the wheels width-wise
        self.ShiftGear = ""         # if the robot has multiple gear drive
        self.DriveSystem = ""       # what type of control the robot uses to drive (tank, arcade, etc.)
        self.CenterMass = ""        # the center of mass / gravity of the robot
        self.Driver1 = ""           # the robot's drive team
        self.experince1 = None      # the robot's drive team's experience(in competitions / years)
        self.Driver2 = ""           # ''
        self.experince2 = None      # ''
        self.Driver3 = ""           # ''
        self.experince3 = None      # ''
  
#------------------------------------------------------------------------------
# Team Class
#   -- stores and recalls team specific data
#------------------------------------------------------------------------------
class Team(object):
    """Store and recall data on a team from here."""

    team_list = []  # list holding all the teams currently loaded in the database
    
    def __init__(self, num):
        self.number = num
        self.Info = _TeamInfo()
        self.Scores = _TeamScores()
        self.PitInfo = _TeamPitInfo()
