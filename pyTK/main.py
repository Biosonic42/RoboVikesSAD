from Tkinter import *
import tkFileDialog
import tkMessageBox
from view.windows import *
from controller.windows import *

from model import model, imports, calculate

class App(Frame):

    def import_data(self):
        imports.import_data(tkFileDialog.askopenfilename())
        self.imported = model.imported
        if self.imported:
            calculate.calculate_data()
        else:
            tkMessageBox.showinfo("Warning","Import Data Failed.")
        
    def teamdata(self):
        if self.imported:
            newWindow = Toplevel(self)
            controller = cteamdata.TeamDataController()
            teamdata = vteamdata.TeamData(newWindow,controller)
        else:
            tkMessageBox.showinfo("Warning","No data has been imported.")

    def ranking(self):
        if self.imported:
            newWindow = Toplevel(self)
            controller = cranking.RankingController()
            ranking = vranking.Ranking(newWindow,controller)
        else:
            tkMessageBox.showinfo("Warning","No data has been imported.")

    def search(self):
        if self.imported:
            newWindow = Toplevel(self)
            controller = csearch.SearchController()
            search = vsearch.Search(newWindow,controller)
        else:
            tkMessageBox.showinfo("Warning","No data has been imported.")
        
    def compare(self):
        if self.imported:
            newWindow = Toplevel(self)
            controller = ccompare.CompareController()
            compare = vcompare.Compare(newWindow,controller)
        else:
            tkMessageBox.showinfo("Warning","No data has been imported.")

    def choose(self):
        if self.imported:
            newWindow = Toplevel(self)
            controller = cchoose.ChooseController()
            choose = vchoose.Choose(newWindow,controller)
        else:
            tkMessageBox.showinfo("Warning","No data has been imported.")

    def startup(self):
        # create a frame to put the window buttons in
        self.wbf = Frame(self)
        self.wbf.pack(side=RIGHT,padx=5)

        self.teamdataB = Button(self.wbf, text="Team Data",
                               command=self.teamdata)
        self.teamdataB.pack(side=TOP,pady=5)

        self.rankingB = Button(self.wbf, text="Ranking",
                              command=self.ranking)
        self.rankingB.pack(side=TOP,pady=5)
        self.searchB = Button(self.wbf, text="Search",
                              command=self.search)
        self.searchB.pack(side=TOP,pady=5)
        self.compareB = Button(self.wbf,text="Compare",
                               command=self.compare)
        self.compareB.pack(side=TOP,pady=5)
        self.chooseB = Button(self.wbf,text="Choose",
                              command=self.choose)
        self.chooseB.pack(side=TOP,pady=5)

        # create a frame to put the import buttons in
        self.importFrame = Frame(self)
        self.importFrame.pack(side=LEFT,padx=5)

        self.importB = Button(self.importFrame, text="Import Data",
                              command=self.import_data)
        self.importB.pack(side=TOP,pady=5)

    def __init__(self,parent=None):
        self.parent = parent
        self.imported = False

        self.parent.title("SAD 0.1")
        self.parent.geometry("+0+0")
        Frame.__init__(self,parent)
        self.pack()

        self.startup()

root = Tk()

app = App(root)

app.mainloop()

app.destroy()
