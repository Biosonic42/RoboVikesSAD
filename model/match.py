#------------------------------------------------------------------------------
# match module
#   -- stores information about a match, 6 entries
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# Match Class
#   -- stores all match data
#------------------------------------------------------------------------------
class Match(object):
    """Used to store data about matches, generate defensive scores, etc."""

    matches = [] # list holding all the matches
    
    def __init__(self, num):
        self.number = num   # match number
        self.teams = []     # the teams in the match
        self.all0 = []      # the teams in alliance 1
        self.all1 = []      # the teams in alliance 2
        self.offScore0 = 0  # the offensive score for alliance 1
        self.offScore1 = 0  # the offensive score for alliance 2
        self.off0 = 0       # the number of offensive bots for alliance 1
        self.off1 = 0       # the number of offensive bots for alliance 2
        self.hangScore0 = 0 # the hang Score for alliance 1
        self.hangScore1 = 0 # the hang Score for alliance 2
        self.def0 = 0       # the number of defensive bots for alliance 1
        self.def1 = 0       # the number of defensive bots for alliance 2
        self.ast0 = 0       # the number of assistive bots for alliance 1
        self.ast1 = 0       # the number of assistive bots for alliance 2
        self.avgSum0 = 0    # the sum of total avgerage Scores for alliance 1
        self.avgSum1 = 0    # the sum of total avgerage Scores for alliance 2
        self.taSum0 = 0     # the sum of avg teleAuto scores for alliance 1
        self.taSum1 = 0     # the sum of avg teleAuto scores for alliance 2
        self.defScore0 = 0  # the defensive score for alliance 1
        self.defScore1 = 0  # the defensive score for alliance 2
        self.astScore0 = 0  # the assistive score for alliance 1
        self.astScore1 = 0  # the assistive score for alliance 2

        self.matches.append(self)

    def get_total(self):
        self.total0 = self.offScore0 + self.hangScore0
        self.total1 = self.offScore1 + self.hangScore1
        self.overall = self.total0 + self.total1
