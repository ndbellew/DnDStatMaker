#!/bin/pyton3
import random
import math
import sys

class StatMaker:

    def __init__(self, _STR, _DEX, _CON, _INT, _WIS, _CHA):
        self.S = int(_STR)
        self.D = int(_DEX)
        self.C = int(_CON)
        self.I = int(_INT)
        self.W = int(_WIS)
        self.CH = int(_CHA)
        self.count = 0
        self.STR,self.DEX,self.CON,self.INT,self.WIS,self.CHA = 0,0,0,0,0,0
        self.total = 0
        self.GrandTotalCount = 0

    def RandInt(self,Min):
        Num = 0
        while(Num<Min):
            Num = random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
            self.count +=1
        return Num
    def SetStats(self):
        self.STR=self.RandInt(self.S)
        self.DEX=self.RandInt(self.D)
        self.CON=self.RandInt(self.C)
        self.INT=self.RandInt(self.I)
        self.WIS=self.RandInt(self.W)
        self.CHA=self.RandInt(self.CH)
    
    def CleanData(self):
        self.STR,self.DEX,self.CON,self.INT,self.WIS,self.CHA = list(map(int, [self.STR,self.DEX,self.CON,self.INT,self.WIS,self.CHA]))

    def DetermineStats(self):
        self.total = 0
        if len(sys.argv) > 1:
            num = int(sys.argv[1])
        else:
            num = 70
        while (self.total<num):
            self.SetStats()
            self.total = int(math.fsum([self.STR,self.DEX,self.CON,self.INT,self.WIS,self.CHA]))
        return self.total, self.STR,self.DEX,self.CON,self.INT,self.WIS,self.CHA

    def getStatList(self):
        return self.STR,self.DEX,self.CON,self.INT,self.WIS,self.CHA

    def getStats(self):
        x = f"""STR: {self.STR},\nDEX: {self.DEX}\nCON:{self.CON}\nINT: {self.INT},\nWIS: {self.WIS},\nCHA: {self.CHA},\nTotal: {self.total}
                \nTotal Rolls: {self.count}\nGrand Total Rolls: {self.GrandTotalCount}
            """
        return x

    def PrintStats(self):
        print("______________")
        print("STR: ",self.STR,"\nDEX: ",self.DEX,"\nCON: ",self.CON,"\nINT: ",self.INT,"\nWIS: ",self.WIS,"\nCHA: ",self.CHA,"\nTotal: ",self.total)
        print("Total Rolls to get score: ",self.count)
        print("Grand Total Rolls this session: ", self.GrandTotalCount)
        print("______________")

    def run(self):
        self.CleanData()
        self.DetermineStats()
        self.GrandTotalCount += self.count
        #self.PrintStats()
        self.count = 0
        return self.getStatList()

def splitvars(line):
    for x in line.split():
        yield int(x)

def main():
    stats = input("Input your stat minimums in order (STR,DEX,CON,INT,WIS,CHA)\n ex. 3 3 3 3 7 3\n")
    STR,DEX,CON,INT,WIS,CHA = splitvars(stats)
    RollStats = StatMaker(STR,DEX,CON,INT,WIS,CHA)
    RollAgain = True
    while(RollAgain):
        RollStats.run()
        x = input("Would you like to roll again? y/n\n")
        if x == 'n':
            RollAgain = False


if __name__ == "__main__":
    main()