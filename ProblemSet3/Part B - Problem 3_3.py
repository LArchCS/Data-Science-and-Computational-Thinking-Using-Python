numViruses = 100
maxPop  = 1000
maxBirthProb  = 0.1
clearProb = 0.05
numTrials = 100


import random
import pylab

def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    res = []
    num = numViruses
    for i in range(numViruses):
        if random.random()<clearProb:
            num -= 1
        elif random.random() < maxBirthProb * (1.0 - float(num)/float(maxPop)):
            num += 1
        else:
            continue
    res.append(float(max(0,num)))
    
    for i in range(300-1):
        num = res[-1]
        a = int(num)
        for i in range(a):
            if random.random()<clearProb:
                num -= 1
            elif random.random() < maxBirthProb * (1.0 - float(num)/float(maxPop)):
                num += 1
            else:
                continue
        res.append(float(max(0,num)))
    
    print res
    
    pylab.figure()
    pylab.plot(res, label = 'Average Virus Population')
    pylab.title('SimpleVirus simulation')
    pylab.xlabel('Time Steps')
    pylab.ylabel('Average Virus Population')
    pylab.legend()
    pylab.show()
    
    
simulationWithoutDrug(1, 90, 0.8, 0.1, numTrials)