# -*- coding: utf-8 -*-
from ps3b_precompiled_27 import *

def simulationWithDrug(numViruses=100, maxPop=1000, maxBirthProb=0.1, clearProb=0.05, resistances={'guttagonol': False},
                       mutProb = 0.005, numTrials=1):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """
    steps = 400
    drugTime = 150
    numRemaining = [[[],[]] for i in range(steps)]
    for trial in range(numTrials):
        viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for v in range(numViruses)]
        patient = TreatedPatient(viruses, maxPop)
        for i in range(steps):
            if i == drugTime:
                patient.addPrescription('guttagonol')
            patient.update()
            numRemaining[i][0].append(patient.getTotalPop())
            numRemaining[i][1].append(patient.getResistPop(["guttagonol"]))
    Total = []
    Resist = []
    for i in numRemaining:
        Total.append(float(sum(i[0]))/numTrials)
        Resist.append(float(sum(i[1]))/numTrials)
    pylab.figure()
    pylab.plot(range(drugTime+1),[numViruses]+Total[:drugTime], 'b', label = 'beforeDrug Total Population', linewidth=1)
    pylab.plot(range(drugTime,steps+1),Total[drugTime-1:], 'g',label = 'afterDrug Total Population', linewidth=1)
    pylab.plot(range(steps+1),[0]+Resist, 'r-', label = 'allTime Resistance Population', linewidth=1)
    ymin, ymax = pylab.ylim()
    xmin, xmax = pylab.xlim()
    pylab.plot([drugTime,drugTime],pylab.ylim(),'g--')
    pylab.text(drugTime*1.01, ymax*0.17,  'drugTime', color = 'g')
    pylab.title('ResistantVirus Simulation')
    pylab.xlabel('Time Steps')
    pylab.ylabel('Average Virus Population')
    pylab.legend(loc = 'best')
    pylab.grid(True)
    pylab.show()

# random.seed(0)
simulationWithDrug(numTrials=1)