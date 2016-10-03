# -*- coding: utf-8 -*-

import random
import pylab

'''
def population(steps):
    rabbit = 500
    fox = 30
    record = []
    for i in range(steps):
        if random.random() <= (1.0 - float(rabbit)/1000.0):
            rabbit += 1
            
        foxrate = random.random()
        if foxrate <= float(rabbit)/1000.0:
            rabbit -= 1
            rabbit = max(rabbit, 10)
            if random.random() <= 1.0/3.0:
                fox += 1
        if foxrate > float(rabbit)/1000.0:
            if random.random() <= 0.1:
                fox -= 1
                fox = max(fox, 10)
        record.append((rabbit,fox))
    return record
'''




def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    for i in range(CURRENTRABBITPOP):
        if random.random() <= (1.0 - float(CURRENTRABBITPOP)/MAXRABBITPOP):
                CURRENTRABBITPOP += 1
                CURRENTRABBITPOP = min(CURRENTRABBITPOP, MAXRABBITPOP)
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    if CURRENTRABBITPOP>10:
        for i in range(CURRENTFOXPOP):
            eatRate = random.random()
            if CURRENTRABBITPOP == 10:
                continue
            elif eatRate <= float(CURRENTRABBITPOP)/MAXRABBITPOP:
                CURRENTRABBITPOP -= 1
                if random.random() <= 1.0/3.0:
                    CURRENTFOXPOP += 1
            else:
                if random.random() <= 0.1:
                    CURRENTFOXPOP -= 1
                    CURRENTFOXPOP = max(CURRENTFOXPOP, 10)
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_populations = []
    fox_populations = []
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    return (rabbit_populations, fox_populations)


# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30



###   -----   TEST

numSteps = 200
rabbit, fox = runSimulation(numSteps)


pylab.figure('Rabbit & Fox')
pylab.plot(rabbit, label = 'Rabbit Population')
pylab.plot(fox, label = 'Fox Population')
pylab.xlabel('Steps')
pylab.ylabel('Population')
pylab.legend(loc = 'best')


##  旧的写 polyfit 的方法
'''
xvals = pylab.array(range(numSteps))
a, b, c = pylab.polyfit(xvals, rabbit, 2)
estRabbit = a*xvals**2 + b*xvals + c
d, e, f = pylab.polyfit(xvals, fox, 2)
estFox = d*xvals**2 + e*xvals + f
pylab.plot(estRabbit)
pylab.plot(estFox)
'''

##  新的 写 polyfit 的方法快很多
coeff = pylab.polyfit(range(numSteps), rabbit, 2)
pylab.plot(pylab.polyval(coeff, range(numSteps)))

coeff = pylab.polyfit(range(numSteps), fox, 2)
pylab.plot(pylab.polyval(coeff, range(numSteps)))


pylab.show()









