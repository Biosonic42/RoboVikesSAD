#------------------------------------------------------------------------------
# dataio module
#   -- handles data input and output
#------------------------------------------------------------------------------
from entry import *
from team import *
from match import *
import model

import tkFileDialog

#------------------------------------------------------------------------------
# import_data functions
#   -- takes data from the user and loads it into the database
#------------------------------------------------------------------------------
def import_data():

    model.imported = False

    # clear any and all old data so as to avoid two sets of conflicting data
    # until I find a way to simply make changes rather than rewrite everything
    Entry.entries = []
    Team.team_list = []
    Team.available = []
    Match.matches = []

    try:
        Filename = str(tkFileDialog.askopenfilename())
        print "File Selected"

        newData = open(Filename, "r")
        print "File Opened"
    except:
        print "Error, could not open selected file."

    try:
        print "Parsing Data"
        for line in newData:
            newEntry = Entry(parse_data(line))
        print "--Data Parsed"

        model.imported = True
    except:
        print "Error, could not parse data."

def import_pitData():

    model.pitImported = False
    
    PitEntry.entries = []

    try:
        Filename = str(tkFileDialog.askopenfilename())
        print "File Selected"

        newData = open(Filename, "r")
        print "File Opened"
    except:
        print "Error, could not open selected file."

    try:
        print "Parsing PitData"
        for line in newData:
            newPitEntry = PitEntry(parse_pitData(line))
        print "--PitData Parsed"

        model.pitImported = True
    except:
        print "Error, could not parse data."

#------------------------------------------------------------------------------
# parse_data functions
#   -- takes each line of a file and transfers it into data ready for an entry
#------------------------------------------------------------------------------
def parse_data(info):
    data = []
    i = 0
    new = ""
    for character in info:
        if character != "," and character != "\n":
            new += str(character)
        else:
            try:
                data.append(int(new))
            except:
                break
            new = ""
            i += 1
            if i >= 27: break

    return data

def parse_pitData(info):
    data = []
    i = 0
    new = ""
    for character in info:
        if character != "," and character != "\n":
            new += str(character)
        else:
            data.append(new)
            new = ""
            i += 1
            if i >= 16: break

    return data
