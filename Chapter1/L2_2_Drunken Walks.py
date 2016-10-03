# -*- coding: utf-8 -*-

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


class Field(Location, object):
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
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        # use move method of location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)
    
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


















