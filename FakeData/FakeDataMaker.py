import random

teams = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]

TrueFalse = [0,1]
MatchsFull = []

totalData = []

def FullCheck(List, x, y):
    occurences = 0
    for element in List:
        if element == x: occurences += 1

    return occurences >= y
  
for team in teams:
    i = 0
    MatchNums = []
    teamData = []
    MatchNum = 0
    HadAuto = 0
    while i < 12:
        matchData = []
        while MatchNum in MatchsFull or MatchNum == 0 or FullCheck(MatchNums, MatchNum, 1):
            MatchNum = random.randrange(1,81)

        MatchNums.append(MatchNum)
        if FullCheck(MatchNums, MatchNum, 6): MatchsFull.append(MatchNum)
        
        TeamNum = team

        AllianceColor = 1 if FullCheck(MatchNums, MatchNum, 3) else 0

        if HadAuto != 9: HadAuto = random.randrange(0,10)
        StartInAutoZone = random.choice(TrueFalse) if HadAuto == 9 else 0
        autoDiscsPU = random.randrange(0,50) if HadAuto == 9 else 0
        if autoDiscsPU >= 3:
            autoDiscsPU = 0
        autoLowP = random.randrange(0,3+autoDiscsPU-StartInAutoZone) if HadAuto == 9 and (3+autoDiscsPU-StartInAutoZone) > 0 else 0
        autoMidP = random.randrange(0,3+autoDiscsPU-StartInAutoZone-autoLowP) if HadAuto == 9 and (3+autoDiscsPU-StartInAutoZone-autoLowP) > 0 else 0
        autoTopP = random.randrange(0,3+autoDiscsPU-StartInAutoZone-autoMidP-autoLowP) if HadAuto == 9 and (3+autoDiscsPU-StartInAutoZone-autoMidP-autoLowP) > 0 else 0
        autoOther = random.choice(TrueFalse) if HadAuto == 9 else 0

        DisabledCounter = random.randrange(0,20)
        if DisabledCounter >= 2:
            DisabledCounter = 0
        DisabledFactor = DisabledCounter * 15
        ScoreNotFromZone = random.choice(TrueFalse)
        FloorDiscsPU = random.randrange(0,90 - DisabledFactor) / 6
        StationDiscsPU = random.randrange(0,45 - DisabledFactor) / 3
        teleLowP = random.randrange(0,FloorDiscsPU + StationDiscsPU) - DisabledFactor  \
                   if (FloorDiscsPU + StationDiscsPU - DisabledFactor) > 0 else 0
        teleMidP = random.randrange(0,FloorDiscsPU + StationDiscsPU - teleLowP) - DisabledFactor \
                   if (FloorDiscsPU + StationDiscsPU - DisabledFactor - teleLowP) > 0 else 0
        teleTopP = random.randrange(0,FloorDiscsPU + StationDiscsPU - teleMidP - teleLowP) - DisabledFactor \
                   if (FloorDiscsPU + StationDiscsPU - DisabledFactor - teleMidP - teleLowP) > 0 else 0
        telePyrP = random.randrange(0,6) if not DisabledCounter else 0

        HangLevel = random.randrange(0,31 - DisabledFactor)-1 if (4-DisabledFactor) > 0 else -1
        if HangLevel >= 3:
            HangLevel = -1
        ScoresWhileOnPyr = random.randrange(0,25) if HangLevel >=0 else 0
        ScoresWhileOnPyr = 0 if ScoresWhileOnPyr >=3 or HangLevel == -1 else 1
        SupportsAnotherBot = random.randrange(0,HangLevel+10) if HangLevel >=0 else 0
        SupportsAnotherBot = 0 if SupportsAnotherBot != HangLevel or HangLevel == -1 else 1
        HangSuccess = random.randrange(0,HangLevel+1) if HangLevel >=0 else 0
        HangSuccess = 0 if HangSuccess != HangLevel or HangLevel == -1 else 1
            

        Defensive = random.randrange(0,50)
        Defensive = 0 if Defensive != 49 else 1
        Assistive = random.randrange(0,50)
        Assistive = 0 if Assistive != 49 else 1
        Technical = random.randrange(0,15 - DisabledFactor) if (15-DisabledFactor) > 0 else 0
        if Technical >= 4:
            Technical = 0
        Regular = random.randrange(0,6 - DisabledFactor) if (6-DisabledFactor) > 0 else 0
        if Regular >= 6:
            Regular = 0
        YellowPenalty = random.randrange(0,50)
        YellowPenalty = 0 if YellowPenalty != 49 else 1
        RedPenalty = random.randrange(0,100)
        RedPenalty = 0 if RedPenalty != 99 else 1

        matchData.append(MatchNum)
        matchData.append(TeamNum)
        matchData.append(AllianceColor)
        matchData.append(StartInAutoZone)
        matchData.append(autoDiscsPU)
        matchData.append(autoTopP)
        matchData.append(autoMidP)
        matchData.append(autoLowP)
        matchData.append(autoOther)
        matchData.append(DisabledCounter)
        matchData.append(ScoreNotFromZone)
        matchData.append(FloorDiscsPU)
        matchData.append(StationDiscsPU)
        matchData.append(telePyrP)
        matchData.append(teleTopP)
        matchData.append(teleMidP)
        matchData.append(teleLowP)
        matchData.append(ScoresWhileOnPyr)
        matchData.append(SupportsAnotherBot)
        matchData.append(HangLevel)
        matchData.append(HangSuccess)
        matchData.append(Defensive)
        matchData.append(Assistive)
        matchData.append(Technical)
        matchData.append(Regular)
        matchData.append(YellowPenalty)
        matchData.append(RedPenalty)
        
        teamData.append(matchData)

        i+=1

    totalData.append(teamData)

dataFile = open("data.txt", "w")
dataFile.writelines(["%s\n" % item for item in totalData])
