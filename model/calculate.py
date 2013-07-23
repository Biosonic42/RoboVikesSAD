#------------------------------------------------------------------------------
# calculate module
#   -- functions for handling data input, output, and caclulations
#------------------------------------------------------------------------------
from team import *
from entry import *
from match import *

#------------------------------------------------------------------------------
# calculate_data function
#   -- handles data and stores it to the teams
#------------------------------------------------------------------------------
def calculate_data():
    
    for entry in Entry.entries:
        entry.primary_sort()

    # get basic team data from the entries
    for entry in Entry.entries:
        done = False
        for team in Team.team_list:
            if team.number == entry.team:
                assign_basic_team_values(team, entry)

                done = True
        if done == False:
            newTeam = Team(entry.team)
            print "Added Team #: " + str(entry.team)

            assign_basic_team_values(newTeam,entry)

    # get primary offensive information about the team
    for team in Team.team_list:
        team.get_primary_details()
    
    # get basic match data from the entries
    for entry in Entry.entries:
        done = False
        for match in Match.matches:
            if match.number == entry.match:
                assign_basic_match_values(match, entry)

                done = True
        if done==False:
            newMatch = Match(entry.match)
            print "Added Match #: " + str(entry.match)
            assign_basic_match_values(newMatch, entry)

    # get defensive and assistive scores for each entry
    for entry in Entry.entries:
        if entry.defensive or entry.assistive:
            for match in Match.matches:
                if match.number == entry.match:
                    if entry.allianceColor == 0:
                        oppAvg = match.taSum1
                        oppOff = match.offScore1
                        allAvg = match.taSum0
                        allOff = match.offScore0
                        allDef = match.def0
                        allAst = match.ast0
                    elif entry.allianceColor == 1:
                        oppAvg = match.taSum0
                        oppOff = match.offScore0
                        allAvg = match.taSum1
                        allOff = match.offScore1
                        allDef = match.def1
                        allAst = match.ast1
        else:
            oppAvg = 0
            oppOff = 0
            allAvg = 0
            allOff = 0
            allDef = 0
            allAst = 0

        entry.secondary_sort(oppAvg,oppOff,allAvg,allOff,allDef,allAst)

        # get total score for the entry
        entry.tertiary_sort()

    # get team defensive and assistive scores
    for entry in Entry.entries:
        for team in Team.team_list:
            if team.number == entry.team:
                team.Scores.dScores.append(entry.defensiveScore)
                team.Scores.aScores.append(entry.assistiveScore)
    for team in Team.team_list:
        team.get_secondary_details()

    # get match defensive and assitive scores
    for entry in Entry.entries:
        for match in Match.matches:
            if match.number == entry.match:
                if entry.allianceColor == 0:
                    match.defScore0 += entry.defensiveScore
                    match.astScore0 += entry.assistiveScore
                elif entry.allianceColor == 0:
                    match.defScore1 += entry.defensiveScore
                    match.astScore1 += entry.assistiveScore
    # get match total scores
    for match in Match.matches:
        match.get_total()

    # get match weighted scores
    overall_score = 0
    for match in Match.matches:
        overall_score += match.overall

    # weight = (s[m]/(s[w]-s[1])) * s[t]
    for entry in Entry.entries:
        for match in Match.matches:
            if match.number == entry.match:
                tempweight = 0
                if (match.total0-match.total1) != 0:
                    entry.wScore = ((match.total0 + match.total1)*entry.totalScore)/100
                    entry.woScore = ((match.total0 + match.total1)*entry.offensiveScore)/100
                    entry.wdScore = ((match.total0 + match.total1)*entry.defensiveScore)/100
                    entry.waScore = ((match.total0 + match.total1)*entry.assistiveScore)/100
                else:
                    entry.wScore = ((match.total0 + match.total1)*entry.totalScore)
                    entry.woScore = ((match.total0 + match.total1)*entry.offensiveScore)
                    entry.wdScore = ((match.total0 + match.total1)*entry.defensiveScore)
                    entry.waScore = ((match.total0 + match.total1)*entry.assistiveScore)
                    
    # get team average, weighted, total, and max/min scores
    for team in Team.team_list:
        for entry in Entry.entries:
            if entry.team == team.number:
                team.Scores.wScores.append(entry.wScore)
                team.Scores.woScores.append(entry.woScore)
                team.Scores.wdScores.append(entry.wdScore)
                team.Scores.waScores.append(entry.waScore)
                team.Scores.tScores.append(entry.totalScore)

        team.get_tertiary_details()
        team.get_final_details()
        
#------------------------------------------------------------------------------
# calculate_pit_data function
#   - handles pit data and stores it to the teams
#------------------------------------------------------------------------------
def calculate_pit_data():
    for entry in PitEntry.entries:
        done = False
        for team in Team.team_list:
            if team.number == entry.team:
                assign_pit_entry_values(team, entry)
                done = True
        if done == False:
            newTeam = Team(entry.team)
            print "Added Team #: " + str(entry.team)
            assign_pit_entry_values(Team.team_list[len(Team.team_list)-1],entry)
        
#------------------------------------------------------------------------------
# assign_basic_team_values function
#   -- assigns some basic values from an entry to a team
#   -- still needs error handling
#------------------------------------------------------------------------------
def assign_basic_team_values(team, entry):
    team.Info.matches.append(entry.match)
    team.Info.hangLevel.append(entry.hangLevel)
    team.Info.hangSuccess.append(entry.hangSuccess)
    team.Info.supportsBot.append(entry.supportsAnotherBot)
    team.Info.scoredOnPyr.append(entry.scoresWhileOnPyr)
    team.Info.numOff += int(entry.offensive)
    team.Info.numDef += int(entry.defensive)
    team.Info.numAst += int(entry.assistive)

    team.Info.hadAuto += 1 if (entry.scoredInAuto or entry.autoOther) else 0
    team.Info.startedInAuto += int(entry.startInAutoZone)
    team.Info.otherAutoStrat += int(entry.autoOther)
    team.Info.autoDiscsScored.append(entry.autoDiscsScored)
    team.Info.autoDiscsPU.append(entry.autoDiscsPU)
    team.Info.autoTopScored.append(entry.autoTopDiscs)
    team.Info.autoMidScored.append(entry.autoMidDiscs)
    team.Info.autoLowScored.append(entry.autoLowDiscs)
    team.Info.scoredAuto += int(entry.scoredInAuto)

    team.Info.hadTele += 1 if not entry.disabled else 0
    team.Info.disabledState.append(entry.disabledCount)
    team.Info.disabled += int(entry.disabled)
    team.Info.disabledCount += entry.disabledCount
    team.Info.teleFloorDiscsPU.append(entry.teleFloorDiscsPU)
    team.Info.teleStationDiscsPU.append(entry.teleStationDiscsPU)
    team.Info.discsPU.append(entry.teleDiscsPU)
    team.Info.teleDiscsScored.append(entry.teleDiscsScored)
    team.Info.telePyrScored.append(entry.telePyrDiscs)
    team.Info.teleTopScored.append(entry.teleTopDiscs)
    team.Info.teleMidScored.append(entry.teleMidDiscs)
    team.Info.teleLowScored.append(entry.teleLowDiscs)

    team.Info.RegFouls.append(entry.regularFoul)
    team.Info.TechFouls.append(entry.technicalFoul)
    team.Info.hadRegFoul += int(entry.hasRegFoul)
    team.Info.hadTechFoul += int(entry.hasTechFoul)
    team.Info.hadYellow += int(entry.yellowFlag)
    team.Info.hadRed += int(entry.redFlag)

    team.Scores.oScores.append(entry.offensiveScore)
    team.Scores.taScores.append(entry.teleautoScore)
    team.Scores.hangScores.append(entry.hangScore)
    team.Scores.autoScores.append(entry.autoScore)
    team.Scores.teleScores.append(entry.teleScore)
    team.Scores.foulScores.append(entry.foulScore)

#------------------------------------------------------------------------------
# assign_basic_match_values function
#   -- assigns some basic values from the entry to a match
#   -- still needs error handling
#------------------------------------------------------------------------------
def assign_basic_match_values(match, entry):
    match.teams.append(entry.team)
    if entry.allianceColor == 0:
        match.all0.append(entry.team)
        match.offScore0 += entry.offensiveScore
        match.off0 += int(entry.offensive)
        match.def0 += int(entry.defensive)
        match.ast0 += int(entry.assistive)
        match.hangScore0 += entry.hangScore
        if entry.offensive:
            for team in Team.team_list:
                if team.number == entry.team:
                    match.taSum0 += team.Scores.avgTAScore
                    
    elif entry.allianceColor == 1:
        match.all1.append(entry.team)
        match.offScore1 += entry.offensiveScore
        match.off1 += int(entry.offensive)
        match.def1 += int(entry.defensive)
        match.ast1 += int(entry.assistive)
        match.hangScore1 += entry.hangScore
        if entry.offensive:
            for team in Team.team_list:
                if team.number == entry.team:
                    match.taSum1 += team.Scores.avgTAScore

#------------------------------------------------------------------------------
# assign_pit_entry_values function
#   -- takes PitEntry values and puts them into a team
#   -- still needs error handling
#------------------------------------------------------------------------------
def assign_pit_entry_values(team, entry):
    
    team.PitInfo.robLength = entry.robLength
    team.PitInfo.robWidth = entry.robWidth
    team.PitInfo.robHeight = entry.robHeight
    team.PitInfo.robWieght = entry.robWieght
    team.PitInfo.clearance = entry.clearance
    team.PitInfo.wheelSpace = entry.wheelSpace
    team.PitInfo.driveSystem = entry.driveSystem
    team.PitInfo.shiftGear = entry.shiftGear
    team.PitInfo.centerMass = entry.centerMass
    team.PitInfo.driver1 = entry.driver1
    team.PitInfo.exp1 = entry.exp1 + " Competitions"
    team.PitInfo.driver2 = entry.driver2
    team.PitInfo.exp2 = entry.exp2 + " Competitions"
    team.PitInfo.driver3 = entry.driver3
    team.PitInfo.exp3 = entry.exp3 + " Competitions"

#------------------------------------------------------------------------------
# get_rank functions
#   -- calculates rankings for avg, min, and max scores for each team
#------------------------------------------------------------------------------
def get_off_rank(sort="avg",rev=True):

    TeamRankings.off_rank = []
    
    for team in Team.team_list:
        if sort == "avg":
            if team.Info.numOff > 0:
                TeamRankings.off_rank.append([team.Scores.avgOffScore,team.number])
        elif sort == "max":
            if team.Info.numOff > 0:
                TeamRankings.off_rank.append([team.Scores.maxOffScore,team.number])
        elif sort == "min":
            if team.Info.numOff > 0:
                TeamRankings.off_rank.append([team.Scores.minOffScore,team.number])

    TeamRankings.off_rank.sort(reverse=rev)

    return TeamRankings.off_rank

def get_def_rank(sort="avg",rev=True):

    TeamRankings.def_rank = []
    
    for team in Team.team_list:
        if sort == "avg":
            if team.Info.numDef > 0:
                TeamRankings.def_rank.append([team.Scores.avgDefScore,team.number])
        elif sort == "max":
            if team.Info.numDef > 0:
                TeamRankings.def_rank.append([team.Scores.maxDefScore,team.number])
        elif sort == "min":
            if team.Info.numDef > 0:
                TeamRankings.def_rank.append([team.Scores.minDefScore,team.number])

    TeamRankings.def_rank.sort(reverse=rev)

    return TeamRankings.def_rank

def get_ast_rank(sort="avg",rev=True):

    TeamRankings.ast_rank = []
    
    for team in Team.team_list:
        if sort == "avg":
            if team.Info.numAst > 0:
                TeamRankings.ast_rank.append([team.Scores.avgAstScore,team.number])
        elif sort == "max":
            if team.Info.numAst > 0:
                TeamRankings.ast_rank.append([team.Scores.maxAstScore,team.number])
        elif sort == "min":
            if team.Info.numAst > 0:
                TeamRankings.ast_rank.append([team.Scores.minAstScore,team.number])

    TeamRankings.ast_rank.sort(reverse=rev)

    return TeamRankings.ast_rank

def get_tot_rank(sort="avg",rev=True):

    TeamRankings.tot_rank = []
    
    for team in Team.team_list:
        if sort == "avg":
                TeamRankings.tot_rank.append([team.Scores.avgTotalScore,team.number])
        elif sort == "max":
                TeamRankings.tot_rank.append([team.Scores.maxTotalScore,team.number])
        elif sort == "min":
                TeamRankings.tot_rank.append([team.Scores.minTotalScore,team.number])

    TeamRankings.tot_rank.sort(reverse=rev)

    return TeamRankings.tot_rank

def get_auto_rank(sort="avg",rev=True):

    TeamRankings.auto_rank = []
    
    for team in Team.team_list:
        if sort == "avg":
            if team.Info.hadAuto > 0:
                TeamRankings.auto_rank.append([team.Scores.avgAutoScore,team.number])
        elif sort == "max":
            if team.Info.hadAuto > 0:
                TeamRankings.auto_rank.append([team.Scores.maxAutoScore,team.number])
        elif sort == "min":
            if team.Info.hadAuto > 0:
                TeamRankings.auto_rank.append([team.Scores.minAutoScore,team.number])

    TeamRankings.auto_rank.sort(reverse=rev)

    return TeamRankings.auto_rank

def get_tele_rank(sort="avg",rev=True):

    TeamRankings.tele_rank = []
    
    for team in Team.team_list:
        if sort == "avg":
            if team.Info.hadTele > 0:
                TeamRankings.tele_rank.append([team.Scores.avgTeleScore,team.number])
        elif sort == "max":
            if team.Info.hadTele > 0:
                TeamRankings.tele_rank.append([team.Scores.maxTeleScore,team.number])
        elif sort == "min":
            if team.Info.hadTele > 0:
                TeamRankings.tele_rank.append([team.Scores.minTeleScore,team.number])

    TeamRankings.tele_rank.sort(reverse=rev)

    return TeamRankings.tele_rank

def get_pyr_rank(sort="avg",rev=True):

    TeamRankings.pyr_rank = []
    
    for team in Team.team_list:
        if sort == "avg":
            if team.Info.timesHanged > 0:
                TeamRankings.pyr_rank.append([team.Scores.avgHangScore,team.number])
        elif sort == "max":
            if team.Info.timesHanged > 0:
                TeamRankings.pyr_rank.append([team.Scores.maxHangScore,team.number])
        elif sort == "min":
            if team.Info.timesHanged > 0:
                TeamRankings.pyr_rank.append([team.Scores.minHangScore,team.number])

    TeamRankings.pyr_rank.sort(reverse=rev)

    return TeamRankings.pyr_rank

def get_foul_rank(sort="avg",rev=False): # foul rank default from least points to most

    TeamRankings.foul_rank = []
    
    for team in Team.team_list:
        if sort == "avg":
            if team.Info.hadRegFoul or team.Info.hadTechFoul:
                TeamRankings.foul_rank.append([team.Scores.avgFoulScore,team.number])
        elif sort == "max":
            if team.Info.hadRegFoul or team.Info.hadTechFoul:
                TeamRankings.foul_rank.append([team.Scores.maxFoulScore,team.number])
        elif sort == "min":
            if team.Info.hadRegFoul or team.Info.hadTechFoul:
                TeamRankings.foul_rank.append([team.Scores.minFoulScore,team.number])

    TeamRankings.foul_rank.sort(reverse=rev)

    return TeamRankings.foul_rank

def get_ta_rank(sort="avg",rev=True):

    TeamRankings.ta_rank = []
    
    for team in Team.team_list:
        if sort == "avg":
            if team.Info.hadAuto or team.Info.hadTele:
                TeamRankings.ta_rank.append([team.Scores.avgTAScore,team.number])
        elif sort == "max":
            if team.Info.hadAuto or team.Info.hadTele:
                TeamRankings.ta_rank.append([team.Scores.maxTAScore,team.number])
        elif sort == "min":
            if team.Info.hadAuto or team.Info.hadTele:
                TeamRankings.ta_rank.append([team.Scores.minTAScore,team.number])

    TeamRankings.ta_rank.sort(reverse=rev)

    return TeamRankings.ta_rank

def get_w_rank(sort="avg",rev=True):

    TeamRankings.w_rank = []
    
    for team in Team.team_list:
        if sort == "avg":
                TeamRankings.w_rank.append([team.Scores.avgWScore,team.number])
        elif sort == "max":
                TeamRankings.w_rank.append([team.Scores.maxWScore,team.number])
        elif sort == "min":
                TeamRankings.w_rank.append([team.Scores.minWScore,team.number])

    TeamRankings.w_rank.sort(reverse=rev)

    return TeamRankings.w_rank

def get_wo_rank(sort="avg",rev=True):

    TeamRankings.wo_rank = []
    
    for team in Team.team_list:
        if sort == "avg":
            if team.Info.numOff > 0:
                TeamRankings.wo_rank.append([team.Scores.avgWOScore,team.number])
        elif sort == "max":
            if team.Info.numOff > 0:
                TeamRankings.wo_rank.append([team.Scores.maxWOScore,team.number])
        elif sort == "min":
            if team.Info.numOff > 0:
                TeamRankings.wo_rank.append([team.Scores.minWOScore,team.number])

    TeamRankings.wo_rank.sort(reverse=rev)

    return TeamRankings.wo_rank

def get_wd_rank(sort="avg",rev=True):

    TeamRankings.wd_rank = []
    
    for team in Team.team_list:
        if sort == "avg":
            if team.Info.numDef > 0:
                TeamRankings.wd_rank.append([team.Scores.avgWDScore,team.number])
        elif sort == "max":
            if team.Info.numDef > 0:
                TeamRankings.wd_rank.append([team.Scores.maxWDScore,team.number])
        elif sort == "min":
            if team.Info.numDef > 0:
                TeamRankings.wd_rank.append([team.Scores.minWDScore,team.number])

    TeamRankings.wd_rank.sort(reverse=rev)

    return TeamRankings.wd_rank

def get_wa_rank(sort="avg",rev=True):

    TeamRankings.wa_rank = []
    
    for team in Team.team_list:
        if sort == "avg":
            if team.Info.numAst > 0:
                TeamRankings.wa_rank.append([team.Scores.avgWAScore,team.number])
        elif sort == "max":
            if team.Info.numAst > 0:
                TeamRankings.wa_rank.append([team.Scores.maxWAScore,team.number])
        elif sort == "min":
            if team.Info.numAst > 0:
                TeamRankings.wa_rank.append([team.Scores.minWAScore,team.number])

    TeamRankings.wa_rank.sort(reverse=rev)

    return TeamRankings.wa_rank
