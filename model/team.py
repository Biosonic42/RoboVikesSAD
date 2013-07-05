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
        self.startedInAuto = 0      # the number of matches for which the team started completely within the autonomous zone
        self.otherAutoStrat = 0     # the number of matches for which the team had another strategy (not offensive) in autonomous mode
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
        
        self.RegFouls = []          # list holding the number of regular fouls for each match
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
    def get_final_info(self):
        self.avgAutoDiscsScored = sum(self.autoDiscsScored)/len(self.autoDiscsScored) if len(self.autoDiscsScored) else 0
        self.avgAutoDiscsPU = sum(self.autoDiscsPU)/len(self.autoDiscsPU) if len(self.autoDiscsPU) else 0
        self.avgAutoTopScored = sum(self.autoTopScored)/team.hadAuto if self.hadAuto else 0
        self.avgAutoMidScored = sum(self.autoMidScored)/team.hadAuto if self.hadAuto else 0
        self.avgAutoLowScored = sum(self.autoLowScored)/team.hadAuto if self.hadAuto else 0
        self.avgDiscsPU = sum(self.discsPU)/len(self.discsPU) if len(self.discsPU) else 0
        self.avgFloorDiscsPU = sum(self.teleFloorDiscsPU)/len(self.teleFloorDiscsPU) if len(self.teleFloorDiscsPU) else 0
        self.avgStationDiscsPU = sum(self.teleStationDiscsPU)/len(self.teleStationDiscsPU) if len(self.teleStationDiscsPU) else 0
        team.avgDiscsScored = sum(team.teleDiscsScored)/len(team.teleDiscsScored) if len(team.teleDiscsScored)>0 else 0
        team.avgTelePyrScored = sum(team.telePyrScored)/team.hadTele if team.hadTele else 0
        team.avgTeleTopScored = sum(team.teleTopScored)/team.hadTele if team.hadTele else 0
        team.avgTeleMidScored = sum(team.teleMidScored)/team.hadTele if team.hadTele else 0
        team.avgTeleLowScored = sum(team.teleLowScored)/team.hadTele if team.hadTele else 0
        
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

        self.maxOffScore = self.minOffScore = 0
        self.maxDefScore = self.minDefScore = 0
        self.maxAstScore = self.minAstScore = 0
        self.maxTotalScore = self.minTotalScore = 0
        self.maxTAScore = self.minTAScore = 0
        self.maxHangScore = self.minHangScore = 0
        self.maxAutoScore = self.minAutoScore = 0
        self.maxTeleScore = self.minTeleScore = 0
        self.maxFoulScore = self.minFoulScore = 0
        self.maxTAScore = self.minTAScore = 0
        self.maxWScore = self.minWScore = 0
        self.maxWOScore = self.minWOScore = 0
        self.maxWDScore = self.minWDScore = 0
        self.maxWAScore = self.minWAScore = 0

    def get_maxmin_scores(self):
        for score in self.oScores:
            if self.minOffScore == 0: self.minOffScore = score
            self.maxOffScore = score if score > self.maxOffScore else self.maxOffScore
            self.minOffScore = score if score < self.minOffScore else self.minOffScore
        for score in self.dScores:
            if self.minDefScore == 0: self.minDefScore = score
            self.maxDefScore = score if score > self.maxDefScore else self.maxDefScore
            self.minDefScore = score if score < self.minDefScore else self.minDefScore
        for score in self.aScores:
            if self.minAstScore == 0: self.minAstScore = score
            self.maxAstScore = score if score > self.maxAstScore else self.maxAstScore
            self.minAstScore = score if score < self.minAstScore else self.minAstScore
        for score in self.tScores:
            if self.minTotalScore == 0: self.minTotalScore = score
            self.maxTotalScore = score if score > self.maxTotalScore else self.maxTotalScore
            self.minTotalScore = score if score < self.minTotalScore else self.minTotalScore
        for score in self.taScores:
            if self.minTAScore == 0: self.minTAScore = score
            self.maxTAScore = score if score > self.maxTAScore else self.maxTAScore
            self.minTAScore = score if score < self.minTAScore else self.minTAScore
        for score in self.hangScores:
            if self.minHangScore == 0: self.minHangScore = score
            self.maxHangScore = score if score > self.maxHangScore else self.maxHangScore
            self.minHangScore = score if score < self.minHangScore else self.minHangScore
        for score in self.autoScores:
            if self.minAutoScore == 0: self.minAutoScore = score
            self.maxAutoScore = score if score > self.maxAutoScore else self.maxAutoScore
            self.minAutoScore = score if score < self.minAutoScore else self.minAutoScore
        for score in self.teleScores:
            if self.minTeleScore == 0: self.minTeleScore = score
            self.maxTeleScore = score if score > self.maxTeleScore else self.maxTeleScore
            self.minTeleScore = score if score < self.minTeleScore else self.minTeleScore
        for score in self.foulScores:
            if self.minFoulScore == 0: self.minFoulScore = score
            self.maxFoulScore = score if score > self.maxFoulScore else self.maxFoulScore
            self.minFoulScore = score if score < self.minFoulScore else self.minFoulScore
        for score in self.taScores:
            if self.minTAScore == 0: self.minTAScore = score
            self.maxTAScore = score if score > self.maxTAScore else self.maxTAScore
            self.minTAScore = score if score < self.minTAScore else self.minTAScore
        for score in self.wScores:
            if self.minWScore == 0: self.minWScore = score
            self.maxWScore = score if score > self.maxWScore else self.maxWScore
            self.minWScore = score if score < self.minWScore else self.minWScore
        for score in self.woScores:
            if self.minWOScore == 0: self.minWOScore = score
            self.maxWOScore = score if score > self.maxWOScore else self.maxWOScore
            self.minWOScore = score if score < self.minWOScore else self.minWSOcore
        for score in self.wdScores:
            if self.minWDScore == 0: self.minWDScore = score
            self.maxWDScore = score if score > self.maxWDScore else self.maxWDScore
            self.minWDScore = score if score < self.minWDScore else self.minWDScore
        for score in self.waScores:
            if self.minWAScore == 0: self.minWAScore = score
            self.maxWAScore = score if score > self.maxWAScore else self.maxWAScore
            self.minWAScore = score if score < self.minWAScore else self.minWAScore

    def get_avgOff_scores(self, matches=1, offensive=0, hangs=0, auto=0, tele=0):
        self.avgTeleAutoOff = sum(self.taScores)/matches if offensive else 0
        self.avgOffScore = sum(self.oScores)/matches if offensive else 0
        self.avgHangScore = sum(self.hangScores)/hangs if hangs else 0
        self.avgAutoScore = sum(self.autoScores)/auto if auto else 0
        self.avgTeleScore = sum(self.teleScores)/tele if tele else 0
        self.avgFoulScore = sum(self.foulScores)/matches if matches else 0

    def get_avgDefAst_scores(self, matches=1, defensive=0, assitive=0):
        self.avgDefScore = sum(self.dScores)/matches if defensive else 0
        self.avgAstScore = sum(self.aScores)/matches if assistive else 0

    def get_avgWeight_scores(self):
        self.avgTotalScore = sum(self.tScores)/len(self.tScores) if len(self.tScores) else 0
        self.avgWScore = sum(self.wScores)/len(self.wScores) if len(self.wScores) else 0
        self.avgWOScore = sum(self.woScores)/len(self.woScores) if len(self.woScores) else 0
        self.avgWDScore = sum(self.wdScores)/len(self.wdScores) if len(self.wdScores) else 0
        self.avgWAScore = sum(self.waScores)/len(self.waScores) if len(self.waScores) else 0

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
        self.robLength = 0          # the length of the robot's chassis
        self.robWidth= 0            # the width  of the robot's chassis
        self.robHeight = 0          # the height of the robot
        self.robWeight = 0          # the weight of the robot
        self.clearance = ""         # the distance to the floor from the bottom of the chassis
        self.wheelSpace = ""        # the spacing between the wheels width-wise
        self.shiftGear = ""         # if the robot has multiple gear drive
        self.driveSystem = ""       # what type of control the robot uses to drive (tank, arcade, etc.)
        self.centerMass = ""        # the center of mass / gravity of the robot
        self.driver1 = ""           # the robot's drive team
        self.exp1 = None            # the robot's drive team's experience(in competitions / years)
        self.driver2 = ""           # ''
        self.expe2 = None           # ''
        self.driver3 = ""           # ''
        self.exp3 = None            # ''

    def getAttr(self, source):
        return getattr(self, source)

#------------------------------------------------------------------------------
class TeamRankings(object):
    """Used to keep track of rankings for each team."""

    off_rank = []
    def_rank = []
    ast_rank = []
    tot_rank = []
    auto_rank = []
    tele_rank = []
    pyr_rank = []
    foul_rank = []
    ta_rank = []
    w_rank = []
    wo_rank = []
    wd_rank = []
    wa_rank = []
    
    def __init__(self):
        print "Init TeamRankings Object"
        # no none-static class variables
        # team cannot track its own ranking:
            # rankings are defined by the user
            # rankings are dynamic, constantly changing to user request

    def getAttr(self, source):
        return getattr(self, source)

#------------------------------------------------------------------------------
# Team Class
#   -- stores and recalls team specific data
#------------------------------------------------------------------------------
class Team(object):
    """Store and recall data on a team from here."""

    team_list = []  # list holding all the teams currently loaded in the database
    available = []
    
    def __init__(self, num):
        self.number = num
        self.Info = _TeamInfo()
        self.Scores = _TeamScores()
        self.PitInfo = _TeamPitInfo()
        self.team_list.append(self)
        self.available.append(self)

    def get_primary_details(self): # gets the offensive values of Team
        self.Info.get_more_info()
        self.Scores.get_avgOff_scores(len(self.Info.matches),
                                   self.Info.numOff, self.Info.timesHanged,
                                   self.Info.hadAuto, self.Info.hadTele)

    def get_secondary_details(self): # gets the defensive and assistive values of the team
        self.Info.get_final_info()
        self.Scores.get_avgDefAst_scores(len(self.Info.matches),
                                         self.Info.numDef, self.Info.numAst)

    def get_tertiary_details(self): # gets the max and min scores, etc. of the team
        self.Scores.get_avgWeight_scores()
        self.Scores.get_maxmin_scores()

    # def get_final_details(self): # gets the values to be displayed in the TeamData window
        # still to be completed

    def getAttr(self, source):
        return getattr(self, source)
