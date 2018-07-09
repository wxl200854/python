#!/usr/bin/env python3      #1
import tkinter as tk       #2

class Application(tk.Frame):              #3
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)   #4
        self.grid()                       #5
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',
            command=self.quit)            #6
        self.quitButton.grid()            #7

app = Application()                       #8
app.master.title('Sample application')    #9
app.mainloop() 