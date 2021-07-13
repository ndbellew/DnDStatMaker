import tkinter as tk
from statmaker import StatMaker
from tkinter import ttk
  
 
LARGEFONT =("Verdana", 35)
  
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (HomePage, StatRoller):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(HomePage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame startpage
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.AllStatNames = ["Strength", "Dexterity", "Constitution", "Intelligent", "Wisdom", "Charisma"]

        self.create_widgets()

    def create_widgets(self):
        self.entries = []
        for i in range(6):
            statLabel = tk.Label(self, text=self.AllStatNames[i])
            stat = tk.Entry(self, textvariable=tk.IntVar())
            statLabel.pack()
            stat.pack()
            self.entries.append(stat)
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = lambda : controller.show_frame(StatRoller)
        self.hi_there.pack(side="bottom")

    def say_hi(self):
        
        # STR,DEX,CON,INT,WIS,CHA = self.entries
        # newStats = StatMaker(STR.get(),DEX.get(),CON.get(),INT.get(),WIS.get(),CHA.get())
        # _,_,_,_,_,_ = newStats.run()


class StatRoller(tk.Frame):
    def __init__(self, parent, controller, STR=1, DEX=1, CON=1, INT=1, WIS=1, CHA=1):
        tk.Frame.__init__(self, parent)
        self.STR = STR
        self.DEX = DEX 
        self.CON = CON 
        self.INT = INT 
        self.WIS = WIS 
        self.CHA = CHA 
        newStats = StatMaker(STR,DEX,CON,INT,WIS,CHA)
        newStats.run()
        self.StatRoll(newStats)

    def setStats(self,newstats):
        self.STR,self.DEX,self.CON,self.INT,self.WIS,self.CHA = newstats.run()

    def StatRoll(self, newstats):
        CurrentStats = tk.Label(self, text=newstats.getStats())
        CurrentStats.pack()
        self.Submit = tk.Button(self)
        self.Submit["text"] = "Submit"
        self.Submit["command"] = self.setStats(newstats)
        self.Submit.pack(side="bottom")



# Driver Code
app = tkinterApp()
app.mainloop()