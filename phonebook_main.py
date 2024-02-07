# Python Ver: 3.5.1
#
# Author:   Chyanne Pilgreen
#
#Purpose:    Phonebook demo using tkinter
#
#
# Tested OS: this code was written and tested to work with windows 10.

from tkinter import *
import tkinter as tk

# import other modules
# to have access to them
import phonebook_gui
import phonebook_func

# Frame is the Tkinter frame class that our own class will inherit from
class parentWindow(Frame):
    def __init__ (self,master, *args, ** kwarge):
        Frame.__init__(self, master, *args, **kwargs)

        #define our master from configuration
        self.master = master
        self.master.minsize(500,300)  #(Height, width)
        self.master.maxsize(500, 300)
        #This CenterWindow method will center our app on the users screen
        phonebook_func.center_window(self, 500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#FOFOFO")
        # this protocol methos is a tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on the Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.asl_quit(self))
        arg = self.master

        # load in the GUI vidqete from a seperate module.
        #keeping your code comparmentalized and the clutter free
        phonebook_gui.load_gui(self)


 if __name__ == "__main__":
     root = tk.TK()
     App = ParentWindow(root)
     root.mainloop()
