import datetime
import tkinter
import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        #sets title of GUI window
        self.sourceDir_btn = Button(self.master, text="Select Source", width=20, command=self.sourceDir)
        #creates button to tranfer files
        self.sourceDir_btn.grid(row=0, column=0,padx=(20, 10), pady=(30, 0))
        #creates an exit button
        self.source_dir = Entry(width=75)
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))
        self.destDir_btn = Button(self.master, text="Select Destination", width=20, command=self.destDir)
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        self.destination_dir = Entry(width=75)
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

        self.transfer_btn = Button(self.master, text="Transfer Files", width=20, command=self.transferFiles)
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))
        self.exit_btn = Button(self.master, text="Exit", width=20, command=self.exit_program)
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))
    
    #creates function to select source directory.
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #the .delete (0, end) will clear the content that is inserted in the entry widget,
        #this allows the path to be inserted into the Entry widget properly.
        self.source_dir.delete(0, END)
        #the .insert methos will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)
        
    def destDir(self):
        selectDestDir= tkinter.filedialog.askdirectory()
        #the. delete (0,end) will clear the content that is inserted in the Entry widget,
        #this allows the path to be inserted into the Entry widget properly.
        self.destination_dir.delete(0, END)
        #the .insert method will insert the user selection to the destination_dir Entry widget
        self.destination_dir.insert(0, selectDestDir)
    
    def transferFiles(self):
        #gets source directory
        source = self.source_dir.get()
        #gets destination directory
        destination = self.destination_dir.get()
        #gets a list of files in the source directory
        source_files = os.listdir(source)
        for i in source_files:
            file_path = os.path.join(source, i)
            hours24 = datetime.datetime.now() - datetime.timedelta(hours=24)
            mod_time = os.path.getmtime(file_path)
            file_datetime = datetime.datetime.fromtimestamp(mod_time)
            if hours24 < file_datetime:
                #moves each file from the source to the destination
                shutil.move(source + '/' + i, destination)
                print(i + ' was successfully transferred.')

    #creates function to exit program    
    def exit_program(self):
        #root is the main GUI window, the tkinter destroy method
        #tells python to terminate root.mainloop and all widgets inside the GUI window
        root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

