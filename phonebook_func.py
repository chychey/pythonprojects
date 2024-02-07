import os
from tkinter import *
import tkinter as tk
import sqlite3

#be sure to import our other modules
#so we can have access to them 
import phonebook_main
import phonebook_gui

def center_window(self, w, h): # pass in the tkinter frame (master) refrence and the w and h
    # get users screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coodinates to paint the app centered on the users screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('()x()+()+()'.format(w, h, x, y))
    return centerGeo

# catch if the user click on the window upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)


#=====================================================
def create_db(self):
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_phonebook:\
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                    col_fname TEXT, \
                    col_1name TEXT, \
                    col_fullname TEXT, \
                    col_phone TEXT, \
                    col_email TEXT \
                    ):")
        # you must commit () to save changes & close the database connection
        conn.commit()
    conn.close()
    first_run(self)


def first_run(self):
    data = ('John', 'Doe', 'John Doe', '111-111-1111', 'jdoe@email.com')
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO bl_phonebook (col_fname,col_1name,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""", (data)
            conn.commit()
        conn.close()

def count_records(cur):
count = ""
cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
count = cur.fetchone()[0]
return cur,count

#select item in Listbox
def onSelect (self,event):
#calling the event is the self.1stlist1 widget
varList = event.widget
select = varList.curselection()[0]
value = sqlite3.connect('phonebook.db')
with conn:
     cursor = conn.cursor()
     cursor.execute("""SELECT col_fname,col_1name,col_phone,col_email FROM tbl_phonebook WHERE col_fullname = (?)""", [value])
     varBody = cursor.fetchall()
     #this returns a tuple and we can slice it into 4 pats using data[] during the iteration
     for data in varBody:
         self.txt_fname.delete(0,END)
         self.txt_fname.insert(0,data[0])
         self.txt_1name.delete(0,END)
         self.txt_1name.insert(0,data[1])
         self.txt_phone.delete(0,END)
         self.txt_phone.insert(0,data(?))
