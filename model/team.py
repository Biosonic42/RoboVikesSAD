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
        self.supportsBot = []       # list holding the state of whether this robot supported another or not (by match)
        self.scoredOnPyr = []       # list holding the state of whether this robot scored while hanging from the pyramid or not (by match)
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

    def get_more_info(self):
        self.timesHanged = float(sum(self.hangSuccess))
        for var in self.hangSuccess:
            if var == 0:
                self.attemptedHang += 1     
        self.hangsSucctoAtt = self.timesHanged/self.attemptedHang \
                                if self.attemptedHang else 0
        self.totalSupportsBot = float(sum(self.supportsBot))
        self.totalScoredOnPyr = float(sum(self.scoredOnPyr))
        self.discsPUtoScored = sum(self.discsPU)/sum(self.teleDiscsScored) \
                                if sum(self.teleDiscsScored)>0 else 0

    def getAttr(self, source):
        return getattr(self, source)

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

        self.maxOffScore = 0
        self.minOffScore = 0
        self.maxDefScore = 0
        self.minDefScore = 0
        self.maxAstScore = 0
        self.minAstScore = 0
        self.maxTotalScore = 0
        self.minTotalScore = 0
        self.maxTAScore = 0
        self.minTAScore = 0
        self.maxHangScore = 0
        self.minHangScore = 0
        self.maxAutoScore = 0
        self.minAutoScore = 0
        self.maxTeleScore = 0
        self.minTeleScore = 0
        self.maxFoulScore = 0
        self.minFoulScore = 0

    def get_maxmin_scores(self):
        for score in self.oScores:
            self.maxOffScore = score if score > self.maxOffScore else self.maxOffScore
            self.minOffScore = score if score < self.minOffScore else self.minOffScore
        for score in self.dScores:
            self.maxDefScore = score if score > self.maxDefScore else self.maxDefScore
            self.minDefScore = score if score < self.minDefScore else self.minDefScore
        for score in self.oScores:
            self.maxAstScore = score if score > self.maxAstScore else self.maxAstScore
            self.minAstScore = score if score < self.minAstScore else self.minAstScore
        for score in self.tScores:
            self.maxTotalScore = score if score > self.maxTotalScore else self.maxTotalScore
            self.minTotalScore = score if score < self.minTotalScore else self.minTotalScore
        for score in self.taScores:
            self.maxTAScore = score if score > self.maxTAScore else self.maxTAScore
            self.minTAScore = score if score < self.minTAScore else self.minTAScore
        for score in self.hangScores:
            self.maxHangScore = score if score > self.maxHangScore else self.maxHangScore
            self.minHangScore = score if score < self.minHangScore else self.minHangScore
        for score in self.autoScores:
            self.maxAutoScore = score if score > self.maxAutoScore else self.maxAutoScore
            self.minAutoScore = score if score < self.minAutoScore else self.minAutoScore
        for score in self.teleScores:
            self.maxTeleScore = score if score > self.maxTeleScore else self.maxTeleScore
            self.minTeleScore = score if score < self.minTeleScore else self.minTeleScore
        for score in self.foulScores:
            self.maxFoulScore = score if score > self.maxFoulScore else self.maxFoulScore
            self.minFoulScore = score if score < self.minFoulScore else self.minFoulScore

    def get_avg_scores(self, matches=1, offensive=0, defensive=0, assitive=0, hangs=0, auto=0, tele=0):
        self.avgTeleAutoOff = sum(self.taScores)/matches if offensive else 0
        self.avgOffScore = sum(self.oScores)/matches if offensive else 0
        self.avgDefScore = sum(self.dScores)/matches if defensive else 0
        self.avgAstScore = sum(self.aScores)/matches if assistive else 0
        self.avgHangScore = sum(self.hangScores)/hangs if hangs else 0
        self.avgAutoScore = sum(self.autoScores)/auto if auto else 0
        self.avgTeleScore = sum(self.teleScores)/tele if tele else 0

    def getAttr(self, source):
        return getattr(self, source)
        

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

    def getAttr(self, source):
        return getattr(self, source)
  
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
        self.team_list.append(self)

    def get_details(self): # gets the intermediate values of Team
        self.Info.get_more_info()
        self.Scores.get_maxmin_scores()
        self.Scores.get_avg_scores(len(self.Info.matches),
                                   self.Info.numOff, self.Info.numDef, self.Info.numAst,
                                   self.Info.timesHanged,
                                   self.Info.hadAuto, self.Info.hadTele)

    # def get_values(self): # gets the values to be displayed in the TeamData window
        # still to be completed

    def getAttr(self, source):
        return getattr(self, source)
