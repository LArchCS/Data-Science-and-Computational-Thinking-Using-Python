# -*- coding: utf-8 -*-
import pylab, math, random

##   In lecture, we explored the concept of a random walk, using a set of different models of drunks.
##   Below is the code we used for locations and fields and the base class of drunks –
##   you should not have to study this code in detail, since you have seen it in lecture.

##   CODE FROM LECTURE

class Location(object):
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y
        
    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5
    
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

class Field(object):
    def __init__(self):
        self.drunks = {}
        
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
            
    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        #use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)
        
    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

class Drunk(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'This drunk is named ' + self.name
        

##   NEW CODE
##   The following function is new, and returns the actual x and y distance from the start point to the end point of a random walk.

def walkVector(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(f.getLoc(d).getX() - start.getX(),
           f.getLoc(d).getY() - start.getY())
           

##   DRUNK VARIATIONS
##   Here are several different variations on a drunk.

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,1.0), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,0.9), (0.0,-1.03), (1.03, 0.0), (-1.03, 0.0)]
        return random.choice(stepChoices)

class EDrunk(Drunk):
    def takeStep(self):
        ang = 2 * math.pi * random.random()
        length = 0.5 + 0.5 * random.random()
        return (length * math.sin(ang), length * math.cos(ang))

class PhotoDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.0, 0.5),(0.0, -0.5),
                     (1.5, 0.0),(-1.5, 0.0)]
        return random.choice(stepChoices)

class DDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.85, 0.85), (-0.85, -0.85),
                     (-0.56, 0.56), (0.56, -0.56)] 
        return random.choice(stepChoices)



#####    自己写的打印 drunk 位置

def plotdrunk(d,numSteps, numTries):
    origin = Location(0,0)
    f = Field()
    xlist=[]
    ylist=[]
    f.addDrunk(d,origin)
    for i in range(numTries):
        x,y = walkVector(f, d, numSteps)
        xlist.append(x)
        ylist.append(y)
    pylab.figure(str(type(d)).split('.')[1][:str(type(d)).split('.')[1].index("'")])
    pylab.suptitle(str(type(d)).split('.')[1][:str(type(d)).split('.')[1].index("'")],fontsize=14)
    pylab.title(str(numSteps)+' numSteps, '+str(numTries)+' numTries',fontsize=12)
    pylab.xlim(-numSteps/3,numSteps/3)
    pylab.ylim(-numSteps/3,numSteps/3)
    pylab.plot(xlist,ylist,'.')
    pylab.show()


UsualDrunk = UsualDrunk('UsualDrunk')
ColdDrunk = ColdDrunk('ColdDrunk')
EDrunk = EDrunk('EDrunk')
PhotoDrunk = PhotoDrunk('PhotoDrunk')
DDrunk = DDrunk('DDrunk')

numSteps = 100
numTries = 1000

plotdrunk(UsualDrunk,numSteps, numTries)
plotdrunk(ColdDrunk,numSteps, numTries)
plotdrunk(EDrunk,numSteps, numTries)
plotdrunk(PhotoDrunk,numSteps, numTries)
plotdrunk(DDrunk,numSteps, numTries)
