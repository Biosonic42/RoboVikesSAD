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
        self.avgAutoTopScored = sum(self.autoTopScored)/self.hadAuto if self.hadAuto else 0
        self.avgAutoMidScored = sum(self.autoMidScored)/self.hadAuto if self.hadAuto else 0
        self.avgAutoLowScored = sum(self.autoLowScored)/self.hadAuto if self.hadAuto else 0
        self.avgDiscsPU = sum(self.discsPU)/len(self.discsPU) if len(self.discsPU) else 0
        self.avgFloorDiscsPU = sum(self.teleFloorDiscsPU)/len(self.teleFloorDiscsPU) if len(self.teleFloorDiscsPU) else 0
        self.avgStationDiscsPU = sum(self.teleStationDiscsPU)/len(self.teleStationDiscsPU) if len(self.teleStationDiscsPU) else 0
        self.avgDiscsScored = sum(self.teleDiscsScored)/len(self.teleDiscsScored) if len(self.teleDiscsScored)>0 else 0
        self.avgTelePyrScored = sum(self.telePyrScored)/self.hadTele if self.hadTele else 0
        self.avgTeleTopScored = sum(self.teleTopScored)/self.hadTele if self.hadTele else 0
        self.avgTeleMidScored = sum(self.teleMidScored)/self.hadTele if self.hadTele else 0
        self.avgTeleLowScored = sum(self.teleLowScored)/self.hadTele if self.hadTele else 0
        self.avgRegFoul = sum(self.RegFouls)/self.hadRegFoul if self.hadRegFoul else 0
        self.avgTechFoul = sum(self.TechFouls)/self.hadTechFoul if self.hadTechFoul else 0
        
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

    def get_maxmin_scores(self):
        self.maxOffScore = max(self.oScores)
        self.minOffScore = min(self.oScores)
        self.maxDefScore = max(self.dScores)
        self.minDefScore = min(self.dScores)
        self.maxAstScore = max(self.aScores)
        self.minAstScore = min(self.aScores)
        self.maxTotalScore = max(self.tScores)
        self.minTotalScore = min(self.tScores)
        self.maxWScore = max(self.wScores)
        self.minWScore = min(self.wScores)
        self.maxWOScore = max(self.woScores)
        self.minWOScore = min(self.woScores)
        self.maxWDScore = max(self.wdScores)
        self.minWDScore = min(self.wdScores)
        self.maxWAScore = max(self.waScores)
        self.minWAScore = min(self.waScores)
        self.maxTAScore = max(self.taScores)
        self.minTAScore = min(self.taScores)
        self.maxHangScore = max(self.hangScores)
        self.minHangScore = min(self.hangScores)
        self.maxAutoScore = max(self.autoScores)
        self.minAutoScore = min(self.autoScores)
        self.maxTeleScore = max(self.teleScores)
        self.minTeleScore = min(self.teleScores)
        self.maxFoulScore = max(self.foulScores)
        self.minFoulScore = min(self.foulScores)

    def get_avgOff_scores(self, matches=1, offensive=0, hangs=0, auto=0, tele=0):
        self.avgTAScore = sum(self.taScores)/matches if offensive else 0
        self.avgOffScore = sum(self.oScores)/matches if offensive else 0
        self.avgHangScore = sum(self.hangScores)/hangs if hangs else 0
        self.avgAutoScore = sum(self.autoScores)/auto if auto else 0
        self.avgTeleScore = sum(self.teleScores)/tele if tele else 0
        self.avgFoulScore = sum(self.foulScores)/matches if matches else 0

    def get_avgDefAst_scores(self, matches=1, defensive=0, assistive=0):
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
        self.clearance = 0          # the distance to the floor from the bottom of the chassis
        self.wheelSpace = 0         # the spacing between the wheels width-wise
        self.driveSystem = ""       # what type of control the robot uses to drive
                                    # 0 = tank, 1 = arcade, 2 = swerve, 3 = crab, 4 = other
        self.shiftGear = ""         # if the robot has multiple gear drive
                                    # 0 = no, 1 = yes
        self.centerMass = ""        # the center of mass / gravity of the robot
                                    # 0 = low, 1 = mid, 2 = high
        self.driver1 = ""           # the robot's drive team
        self.exp1 = None            # the robot's drive team's experience(in competitions / years)
        self.driver2 = ""           # ''
        self.expe2 = None           # ''
        self.driver3 = ""           # ''
        self.exp3 = None            # ''

    def getAttr(self, source):
        return getattr(self, source)

#------------------------------------------------------------------------------
# TeamRankings class
#   -- place to store ranking lists, for viewing team ranks
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
    available = []  # list holding all the teams not currently selected
    wanted = []     # list holding all the teams in our wanted list
    
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

    def get_final_details(self): # gets the values to be displayed in the TeamData window
        matches = self.Info.matches
        self.numMatch = len(matches)
        self.pOff = str(int(100*self.Info.numOff)/len(matches)) + "%"
        self.pDef = str(int(100*self.Info.numDef)/len(matches)) + "%"
        self.pAst = str(int(100*self.Info.numAst)/len(matches)) + "%"
        self.avgOff = round(self.Scores.avgOffScore,2)
        self.avgDef = round(self.Scores.avgDefScore,2)
        self.avgAst = round(self.Scores.avgAstScore,2)
        self.avgTotal = round(self.Scores.avgTotalScore,2)
        self.WeightedOff = round(self.Scores.avgWOScore,2)
        self.WeightedDef = round(self.Scores.avgWDScore,2)
        self.WeightedAst = round(self.Scores.avgWAScore,2)
        self.WeightedTotal = round(self.Scores.avgWScore,2)

        self.pHadAuto = str(int(100*self.Info.hadAuto)/len(matches)) + "%"
        self.pStartInZone = str(int(100*self.Info.startedInAuto)/len(matches)) + "%"
        self.pOtherStrat = str(int(100*self.Info.otherAutoStrat)/len(matches)) + "%"
        self.avgAutoScore = round(self.Scores.avgAutoScore,2)
        self.avgAutoTopDiscs = round(self.Info.avgAutoTopScored,2)
        self.avgAutoMidDiscs = round(self.Info.avgAutoMidScored,2)
        self.avgAutoLowDiscs = round(self.Info.avgAutoLowScored,2)
        self.avgAutoDiscsPU = round(self.Info.avgAutoDiscsPU,2)

        self.pWasDisabled = str(int(100*self.Info.disabled)/len(matches)) + "%"
        self.avgDisabled = str(sum(self.Info.disabledState)/len(self.Info.disabledState))
        self.totalDisabled = self.Info.disabledCount
        self.avgTotalPickUp = round(self.Info.avgDiscsPU,2)
        self.avgFloorPickUp = round(self.Info.avgFloorDiscsPU,2)
        self.avgStationPickUp = round(self.Info.avgStationDiscsPU,2)
        self.avgTeleScore = round(self.Scores.avgTeleScore,2)
        self.avgTelePyrDiscs = round(self.Info.avgTelePyrScored,2)
        self.avgTeleTopDiscs = round(self.Info.avgTeleTopScored,2)
        self.avgTeleMidDiscs = round(self.Info.avgTeleMidScored,2)
        self.avgTeleLowDiscs = round(self.Info.avgTeleLowScored,2)

        self.avgHangScore = round(self.Scores.avgHangScore,2)
        self.rHangSuccToAtt = str(round(self.Info.hangsSucctoAtt,2)) + " : 1"
        self.pHanged = str(int(100*self.Info.timesHanged)/len(matches)) + "%"
        self.avgSupportBot = round(sum(self.Info.supportsBot)/len(self.Info.supportsBot),2)
        self.avgScoredOnPyr = round(sum(self.Info.scoredOnPyr)/len(self.Info.scoredOnPyr),2)

        self.avgRegFoul = round(self.Info.avgRegFoul,2)
        self.avgTechFoul = round(self.Info.avgTechFoul,2)
        self.pDefensive = str(int(100*self.Info.numDef)/len(matches)) + "%"
        self.pAssistive = str(int(100*self.Info.numAst)/len(matches)) + "%"
        self.pYellow = str(int(100*self.Info.hadYellow)/len(matches)) + "%"
        self.pRed = str(int(100*self.Info.hadRed)/len(matches)) + "%"

    def getAttr(self, source):
        return getattr(self, source)
