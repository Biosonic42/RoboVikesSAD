#------------------------------------------------------------------------------
# entry module
#   -- makes sense of the data collected
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# Entry class
#   -- Equivalent to a single ms-access entry
#   -- each match has 6 of these entries
#------------------------------------------------------------------------------
class Entry(object):
    """Pull in loaded data and sort it to be later assigned to team values."""

    entries = [] # list holding all the entries, 6 per match
    
    def __init__(self, data):
        # general info
        self.match = data[0]
        self.team = data[1]
        self.allianceColor = data[2]

        # autonomous data
        self.startInAutoZone = bool(data[3])
        self.autoDiscsPU = float(data[4])         # pass data to float to prevent truncation
        self.autoTopDiscs = float(data[5])
        self.autoMidDiscs = float(data[6])
        self.autoLowDiscs = float(data[7])
        self.autoOther = bool(data[8])

        # tele-op data
        self.disabledCount = float(data[9])
        self.scoreFromNotZone = bool(data[10])
        self.teleFloorDiscsPU = float(data[11])
        self.teleStationDiscsPU = float(data[12])
        self.telePyrDiscs = float(data[13])
        self.teleTopDiscs = float(data[14])
        self.teleMidDiscs = float(data[15])
        self.teleLowDiscs = float(data[16])

        # pyramid data
        self.scoresWhileOnPyr = bool(data[17])
        self.supportsAnotherBot = bool(data[18])
        self.hangLevel = float(data[19] + 1)        # add 1 to make data return logical (0 = 1, etc.)
        self.hangSuccess = bool(data[20])

        # end data
        self.defensive = bool(data[21])
        self.assistive = bool(data[22])
        self.technicalFoul = float(data[23])
        self.regularFoul = float(data[24])
        self.yellowFlag = bool(data[25])
        self.redFlag = bool(data[26])

        self.disabled = True if self.disabledCount > 0 else False
        self.teleDiscsScored = (self.telePyrDiscs + self.teleTopDiscs +
                                self.teleMidDiscs + self.teleLowDiscs)
        self.autoDiscsScored = (self.autoTopDiscs + self.autoMidDiscs +
                                self.autoLowDiscs)
        self.teleDiscsPU = self.teleFloorDiscsPU + self.teleStationDiscsPU

        self.entries.append(self)

    def primary_sort(self):
        """Calculates basic scoring and information."""

        self.autoScore = ((2*self.autoLowDiscs) + (4*self.autoMidDiscs) +
                          (6*self.autoTopDiscs))
        self.teleScore = ((1*self.teleLowDiscs) + (2*self.teleMidDiscs) +
                          (3*self.teleTopDiscs) + (5*self.telePyrDiscs))

        self.scoredInAuto = True if self.autoScore > 0 else False
        self.scoredInTele = True if self.teleScore > 0 else False
        self.hasTechFoul = True if self.technicalFoul > 0 else False
        self.hasRegFoul = True if self.regularFoul > 0 else False

        self.hangScore = (10*self.hangLevel) if self.hangSuccess else 0
        self.attemptedHangScore = (10*self.hangLevel)

        self.offensiveScore = self.autoScore + self.teleScore + self.hangScore
        self.teleautoScore = self.autoScore + self.teleScore
        self.foulScore = (3*self.regularFoul) + (20*self.technicalFoul)

        self.offensive = True if self.offensiveScore > 0 else False

    def secondary_sort(self, oppAvg, oppOff, allAvg, allOff, allDef, allAst):
        """Calculates defensive and assistive score values."""
        # result = difference between teleauto scores (exluding own score) +
        #          difference between hang scores (exluding own score) /
        #          the number of defensive players
        self.defensiveScore = (((allAvg - self.teleautoScore) - oppAvg) +
                               (((allOff - self.hangScore) - allAvg) - (oppOff-oppAvg))) / allDef if self.defensive else 0
        # result = alliance's score without team's offensive contribution /
        #          the number of assistive players - team's offensive score
        self.assistiveScore = (((allOff-self.offensiveScore)/allAst)-self.offensiveScore) if self.assistive else 0

    def tertiary_sort(self):
        """Calculates total scores."""
        self.totalScore = (self.offensiveScore + self.defensiveScore +
                           self.assistiveScore - self.foulScore)
        self.totalTAScore = (self.teleautoScore +
                             self.defensiveScore + self.assistiveScore)

#------------------------------------------------------------------------------
# PitEntry class
#   -- stores information about a specific team, robot chassis info, etc.
#   -- does not have to do with performance on the field
#   -- most recent data is from 2012, commenting out any game specific data
#------------------------------------------------------------------------------
class PitEntry(object):
    """Stores data not dealing with performance to be transfered to a team."""

    entries = [] # list holding all the pit entries
    
    def __init__(self,data):
        self.team = data[0]

        self.robLength = data[1]
        self.robWidth = data[2]
        self.robHeight = data[3]
        self.robWieght = data[4]
        self.clearance = data[5]
        self.wheelSpace = data[6]

        ##self.BrdgMech = data[7]
        ##self.SlideBrdg = data[8]
        ##self.balsensor = data[9]
        self.driveSystem = data[7]
        self.shiftGear = data[8]

        self.centerMass = data[9]

        self.driver1 = data[10]
        self.exp1 = data[11]

        self.driver2 = data[12]
        self.exp2 = data[13]

        self.driver3 = data[14]
        self.exp3 = data[15]

        self.entries.append(self)
