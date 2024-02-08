import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web page Generator")
        self.labelTxt = Label(text = "Enter custom text or click the defaulting HTML button")
        self.labelTxt.grid(row=0,column=0, padx=20, pady=(20,0))
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(padx=(10,10) , pady=(10,10))
        self.txtEntry = Entry(self.master, font=("Helvetica", 12))
        self.txtEntry.grid(row=1, column=0, padx=(30,15), pady=(10,10), columnspan=3, sticky=W+E)
        self.btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.btn.grid(row=2, column=2, padx=(0,10) , pady=(0,10))

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        #Import the required libraries

    def customHTML(self):
        htmlText = self.txtEntry.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
        
        #Import the required libraries

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
