# -*- coding: utf-8 -*-

#####  -------------------------  L2_2_Drunken Walks

class Location(object):
    # Two dimensions:  x,y
    # No built-in assumption about direction
    
    def __init__(self,x,y):
        """ x and y are floats """
        self.x = x
        self.y = y
    
    def move(self,deltaX,deltaY):
        """ deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)
    
    def getX(self):
        return self.x
        
    def getY(self):
        return self.y
    
    def distFrom(self,other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5
    
    def __str__(self):
        return '<' + str(self.x) + str(self.y) + '>'


class Field(object):        ##   1. 这个地方到底要不要 加 Location  ？ ？ ？
    # Many drunks
    # Drunks can be at same location
    # Field unbounded
    
    def __init__(self):
        self.drunks = {}
    
    def addDrunk(self,drunk,loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
    
    def moveDrunk(self,drunk):
        if not drunk in self.drunks:
            raise ValueError ('Drunk not in field')
        xDist, yDist = drunk.takeStep()                             #   UsualDrunk.takeStep(self)
        currentLocation = self.drunks[drunk]
        # use move method of location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)     ##   1. 这个地方call 了 Location 的 move  ？ ？ ？
    
    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError ('Drunk not in field')
        return self.drunks[drunk]


class Drunk(object):
    #  这个 class 本身不做什么， 唯一的目的是让我们继续做一些 Drunk 的sub-class
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'This drunk is named ' + self.name


import random


class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0,1.0),(0.0,-1.0),(1.0,0.0),(-1.0,0.0)]
        return random.choice(stepChoices)
        
class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0,0.95),(0.0,-1.0),(1.0,0.0),(-1.0,0.0)]
        return random.choice(stepChoices)
        
class EDrunk(Drunk):
    def takeStep(self):
        deltaX=random.random()
        if random.random() <0.5:
            deltaX= - deltaX
        deltaY=random.random()
        if random.random()<0.5:
            deltaY=-deltaY
        return (deltaX,deltaY)
        



#####  -------------------------  L2_3_Drunken Tests

def walk(field,drunk,numSteps):
    start = field.getLoc(drunk)
    for s in range(numSteps):
        field.moveDrunk(drunk)                        #   Field.moveDrunk(drunk)
    return (start.distFrom(field.getLoc(drunk)))     #   Location.distFrom(other)   return 的是走了 N steps 之后距离start的距离
    

def simWalks(numSteps, numTrials, dClass):
    homer = dClass('Homer')
    origin = Location(0,0)
    distances = []
    for t in range(numTrials):                      #  每一个 trial, distance都记录一次 drunk走特定的numSteps之后距离start多远
        field = Field() 
        field.addDrunk(homer, origin)                    #   Field.addDrunk(drunk,loc)
        distances.append(walk(field,homer,numSteps))    #   walk(field,drunk,numSteps)
    return distances                              #  return 的是每一步移动的距离的 list, lenth 是 numTrials
                                                  #    很多，但最后不打印所有，只打印平均，最大，最小



def drunkTest(numTrials=20):
#    random.seed(0)                                 #  将 seed 固定也是 debug 的好办法，比如说 seed 是0的时候，我的结果显示和老师的一样，说明我这个没有bug
    for numSteps in [10,100,1000,10000,100000]:    #  每一个特定 steps 走 numTrials 遍
#    for numSteps in [0,1,2]:                      #  用 0步 和 1步 来 debug
        distances = simWalks(numSteps, numTrials)
        print 'Random walk of ' + str(numSteps) + ' steps'
        print 'mean = ', sum(distances)/len(distances)   #  len(distances) == numTrials
        print 'Max = ', max(distances), '  Min = ', min(distances),'\n'


#drunkTest()




#####  -------------------------  L2_4_Drunken Simulations

import pylab

def drunkTestP1(numTrials = 50):
    stepsTaken=[10,100,1000,10000]
    meanDistances=[]
    for numSteps in stepsTaken:
        distances = simWalks(numSteps,numTrials)
        meanDistances.append(sum(distances)/len(distances))
    pylab.plot(stepsTaken,meanDistances)
    pylab.title('Mean Distance from Origin')
    pylab.xlabel('Steps Taken')
    pylab.ylabel('Steps from Origin')
    pylab.show()



def drunkTestP2(numTrials = 50):
    stepsTaken=[10,100,1000,10000]
    meanDistances=[]
    squareRootOfSteps=[]
    for numSteps in stepsTaken:
        distances = simWalks(numSteps,numTrials)
        meanDistances.append(sum(distances)/len(distances))
        squareRootOfSteps.append(numSteps**0.5)
    pylab.plot(stepsTaken,meanDistances,'r-',label='Mean Distance')
    pylab.plot(stepsTaken,squareRootOfSteps,'g-.',label='Square Root of Steps')
    pylab.title('Mean Distance from Origin')
    pylab.xlabel('Steps Taken')
    pylab.ylabel('Steps from Origin')
    pylab.legend(loc = 'best')
    pylab.show()
 
    
          
def drunkTestP3(numTrials = 50):
    stepsTaken=[10,100,1000,10000]
    squareRootOfSteps=[]
    for dClass in (UsualDrunk,ColdDrunk,EDrunk):
        meanDistances=[]
        for numSteps in stepsTaken:
            distances = simWalks(numSteps,numTrials,dClass)
            meanDistances.append(sum(distances)/len(distances))
        pylab.plot(stepsTaken,meanDistances,label=dClass.__name__,linewidth=1.0)
    for numSteps in stepsTaken:
        squareRootOfSteps.append(numSteps**0.5)
    pylab.plot(stepsTaken,squareRootOfSteps,':',label='Square Root of Steps',linewidth=2.0)
    pylab.title('Mean Distance from Origin')
    pylab.xlabel('Steps Taken')
    pylab.ylabel('Steps from Origin')
    pylab.legend(loc = 'rightupper')
    pylab.show()

drunkTestP3()


#  drunkTestP1  到  3 也是一步步进化的





