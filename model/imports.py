#------------------------------------------------------------------------------
# dataio module
#   -- handles data input and output
#------------------------------------------------------------------------------
from entry import *
from team import *
from match import *
from model import *

#------------------------------------------------------------------------------
# import_data function
#   -- takes data from the user and loads it into the database
#------------------------------------------------------------------------------
def import_data():
    global oldFile
    global Reload
    global imported

    imported = False

    # clear any and all old data so as to avoid two sets of conflicting data
    # until I find a way to simply make changes rather than rewrite everything
    Entry.entries = []
    Team.team_list = []
    Team.available = []
    Match.matches = []

    if Reload:
        oldFile = open("oldFile.txt","r")
        Filename = oldFile.read()
        print "File Identified"

    else:
        Filename = os.path.basename(str(tkFileDialog.askopenfilename()))
        print "File Selected"

        oldFile = open("oldFile.txt","w")
        oldFile.write(Filename)

    newData = open(Filename, "r")
    print "File Opened"

    print "Parsing Data"
    for line in newData:
        newEntry = Entry(parse_data(line))
    print "--Data Parsed"

    imported = True

def import_pitData():
    PitEntry.entries = []
    
    Filename = os.path.basename(str(tkFileDialog.askopenfilename()))
    print "File Selected"

    newData = open(Filename, "r")
    print "File Opened"

    print "Parsing PitData"
    for line in newData:
        newPitEntry = PitEntry(parse_pitData(line))
    print "--PitData Parsed"

#------------------------------------------------------------------------------
# parse_data functions
#   -- takes each line of a file and transfers it into data ready for an entry
#------------------------------------------------------------------------------
def parse_data(info):
    data = []
    i = 0
    new = ""
    while i < 27:
        for character in info:
            if character != "," and character != "\n":
                new += str(character)
            else:
                data.append(int(new))
                new = ""
                i += 1
                if i >= 27: break

    return data

def parse_pitData(info):
    data = []
    i = 0
    new = ""
    while i < 16:
        for character in info:
            if character != "," and character != "\n":
                new += str(character)
            else:
                data.append(new)
                new = ""
                i += 1
                if i >= 16: break

    return data
