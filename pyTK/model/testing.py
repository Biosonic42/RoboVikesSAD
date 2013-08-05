from Tkinter import *
import tkFileDialog
import tkSimpleDialog

import model
from calculate import *
from imports import *
from entry import *
from team import *

running = True
continueing = True

toPrint = []
toPrintMAXMIN = []

app = Tk()
app.withdraw()


class printable():

    def __init__(self, type_=""):
        self.type = type_

toPrint.append(printable("number"))
toPrint.append(printable("numMatch"))
toPrint.append(printable("pOff"))
toPrint.append(printable("pDef"))
toPrint.append(printable("pAst"))
toPrint.append(printable("avgOff"))
toPrint.append(printable("avgDef"))
toPrint.append(printable("avgAst"))
toPrint.append(printable("avgTotal"))
toPrint.append(printable("WeightedOff"))
toPrint.append(printable("WeightedDef"))
toPrint.append(printable("WeightedAst"))
toPrint.append(printable("WeightedTotal"))
toPrint.append(printable("pHadAuto"))
toPrint.append(printable("pStartInZone"))
toPrint.append(printable("pOtherStrat"))
toPrint.append(printable("avgAutoScore"))
toPrint.append(printable("avgAutoPickUp"))
toPrint.append(printable("avgAutoTopDiscs"))
toPrint.append(printable("avgAutoMidDiscs"))
toPrint.append(printable("avgAutoLowDiscs"))
toPrint.append(printable("pWasDisabled"))
toPrint.append(printable("avgDisabled"))
toPrint.append(printable("totalDisabled"))
toPrint.append(printable("avgTotalPickUp"))
toPrint.append(printable("avgFloorPickUp"))
toPrint.append(printable("avgStationPickUp"))
toPrint.append(printable("avgTeleScore"))
toPrint.append(printable("avgTelePyrDiscs"))
toPrint.append(printable("avgTeleTopDiscs"))
toPrint.append(printable("avgTeleMidDiscs"))
toPrint.append(printable("avgTeleLowDiscs"))
toPrint.append(printable("avgHangScore"))
toPrint.append(printable("rHangSuccToAtt"))
toPrint.append(printable("pHanged"))
toPrint.append(printable("avgSupportBot"))
toPrint.append(printable("avgScoredOnPyr"))
toPrint.append(printable("avgRegFoul"))
toPrint.append(printable("avgTechFoul"))
toPrint.append(printable("pDefensive"))
toPrint.append(printable("pAssistive"))
toPrint.append(printable("pYellow"))
toPrint.append(printable("pRed"))

toPrintMAXMIN.append(printable("maxOffScore"))
toPrintMAXMIN.append(printable("minOffScore"))
toPrintMAXMIN.append(printable("maxDefScore"))
toPrintMAXMIN.append(printable("minDefScore"))
toPrintMAXMIN.append(printable("maxAstScore"))
toPrintMAXMIN.append(printable("minAstScore"))
toPrintMAXMIN.append(printable("maxTotalScore"))
toPrintMAXMIN.append(printable("minTotalScore"))
toPrintMAXMIN.append(printable("maxWScore"))
toPrintMAXMIN.append(printable("minWScore"))
toPrintMAXMIN.append(printable("maxWOScore"))
toPrintMAXMIN.append(printable("minWOScore"))
toPrintMAXMIN.append(printable("maxWDScore"))
toPrintMAXMIN.append(printable("minWDScore"))
toPrintMAXMIN.append(printable("maxTAScore"))
toPrintMAXMIN.append(printable("minTAScore"))
toPrintMAXMIN.append(printable("maxAutoScore"))
toPrintMAXMIN.append(printable("minAutoScore"))
toPrintMAXMIN.append(printable("maxTeleScore"))
toPrintMAXMIN.append(printable("minTeleScore"))
toPrintMAXMIN.append(printable("maxHangScore"))
toPrintMAXMIN.append(printable("minHangScore"))
toPrintMAXMIN.append(printable("maxFoulScore"))
toPrintMAXMIN.append(printable("minFoulScore"))

while running:
    
    print "Select a file to import."
    import_data(str(tkFileDialog.askopenfilename()))

    if model.imported:
        calculate_data()
        
        while continueing:
            print "Choose a team to view data on."
            teamdata = int(tkSimpleDialog.askstring("Team Number","_",parent=app,initialvalue=0))
            for team in Team.team_list:
                if team.number == teamdata:
                    for value in toPrint:
                        print str(value.type) + " : " + str(team.getAttr(value.type))
                    print "Load Max and Min Scores? (0 = no, 1 = yes)"
                    if tkSimpleDialog.askstring("Response","_",parent=app,initialvalue=1):
                        for value in toPrintMAXMIN:
                            print str(value.type) + " : " + str(team.Scores.getAttr(value.type))

            print "Continue (0 = no, 1 = yes)"
            continueing = tkSimpleDialog.askstring("Response","_",parent=app,initialvalue=1)
    
    print "Import a different file? (0 = no, 1 = yes)"
    running = tkSimpleDialog.askstring("Response","_",parent=app,initialvalue=0)


print "Closing Model Tester."

