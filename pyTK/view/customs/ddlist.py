#------------------------------------------------------------------------------
# ddlist module
#   -- code from flylib.com recipe 11.4
#------------------------------------------------------------------------------
import Tkinter

#------------------------------------------------------------------------------
# DDList class
#   -- creates a subclass of Tkinter.Listbox with drag and drop reodering
#------------------------------------------------------------------------------
class DDList(Tkinter.Listbox):
    """ A Tkinter listbox with drag'n'drop reordering of entries. """
    def __init__(self, master, **kw):
        kw['selectmode'] = Tkinter.SINGLE
        Tkinter.Listbox.__init__(self, master, kw)
        self.bind('<Button-1>', self.setCurrent)
        self.bind('<B1-Motion>', self.shiftSelection)
        self.curIndex = None
        self.rList = []

    def setCurrent(self, event):
        self.curIndex = self.nearest(event.y)

    def shiftSelection(self, event):
        i = self.nearest(event.y)
        if i < self.curIndex:
            x = self.get(i)
            self.delete(i)
            self.insert(i+1, x)
            self.curIndex = i
            self.rList = self.get(0,Tkinter.END)
        elif i > self.curIndex:
            x = self.get(i)
            self.delete(i)
            self.insert(i-1, x)
            self.curIndex = i
            self.rList = self.get(0,Tkinter.END)
        

            
