# -*- coding: utf-8 -*-


import pylab
import random


class Location(object):
    
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y
        
    def move(self, dX, dY):
        """deltaX and deltaY are floats"""
        # 无限走
        #return Location(self.x + dX, self.y + dY)
        
        
        x = self.x
        y = self.y
        dx = dX
        dy = dY
        
        leftEdge, rightEdge, bottomEdge, topEdge = -50, 50, -50, 50
        
        #SW (Solid Walls)
        #  The drunk cannot go through the fence.
        #  If the drunk sees that his move will make
        #  him run into the fence, the drunk will
        #  hesitate and not move from the spot.
        '''
        if x+dx > leftEdge and x+dx < rightEdge:
            x += dx
        if  y+dy > bottomEdge and y+dy < topEdge:
            y += dy
        '''
        
        #SP (Small Planet)
        #  The rightmost edge is connected to the leftmost edge,
        #  and the top edge is connected to the bottom edge.
        '''
        if x+dx > leftEdge and x+dx < rightEdge:
            x += dx
        elif x+dx > rightEdge:
            x = leftEdge + (x+dx - rightEdge)
        elif x+dx < leftEdge:
            x = rightEdge - (leftEdge - (x+dx))
        
        if  y+dy > bottomEdge and y+dy < topEdge:
            y += dy
        elif y+dy > topEdge:
            y = bottomEdge + (y+dy - topEdge)
        elif y+dy < bottomEdge:
            y = topEdge - (bottomEdge - (y+dy))
        '''
        
        # WW (Warped World)
        #   If the drunk moves past the right-most edge, he ends up on the top edge and vice versa.
        #   If the drunk moves past the left edge, he ends up on the bottom edge and vice versa.
        
        # BH (Back to Home)
        #  Whenever the drunk reaches any edge,
        #  the drunk is transported back to the center of the world.
        #'''
        if x+dx < rightEdge and x+dx > leftEdge and y+dy < topEdge and y+dy > bottomEdge:
            x += dx
            y += dy
        else:
            x = 0
            y = 0
        #'''
        
        
        return Location(x,y)
    
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


import random


class Drunk(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'This drunk is named ' + self.name
    
class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(-1.0,-1.0),(-1.0,0.0),(-1.0,1.0),(0.0,1.0),(0.0,-1.0),(1.0,-1.0), (1.0,0.0),(1.0,1.0)]
        return random.choice(stepChoices)


field = Field()
fan = UsualDrunk('Fan')
field.addDrunk(fan, Location(0,0))
recordX = []
recordY = []
for i in range(10000):
    field.moveDrunk(fan)
    recordX.append(field.getLoc(fan).getX())
    recordY.append(field.getLoc(fan).getY())
    
pylab.plot(recordX,recordY,'.')
pylab.xlim(-50,50)
pylab.ylim(-50,50)
pylab.show()