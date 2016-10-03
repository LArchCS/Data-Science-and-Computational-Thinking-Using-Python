# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    numViruses=100
    maxPop=1000
    maxBirthProb=0.1
    clearProb=0.05
    resistances={'guttagonol': False}
    mutProb = 0.005
    
    for time in [300, 150, 75, 0]:
        steps = time+150
        drugTime = time
        totPop = []
        totRes = []
        for trial in range(numTrials):
            viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for v in range(numViruses)]
            patient = TreatedPatient(viruses, maxPop)
            for i in range(steps):
                if i == drugTime:
                    patient.addPrescription('guttagonol')
                patient.update()
            totPop.append(patient.getTotalPop())
            totRes.append(patient.getResistPop(["guttagonol"]))

        pylab.figure('drugTime = ' + str(time))
        
        pylab.subplot(2,1,1)
        pylab.hist(totPop, bins=30)
        pylab.xlabel('Virus Population',fontsize=6)
        pylab.title('Total Virus Population',fontsize=9)
        xmin, xmax = pylab.xlim()
        
        pylab.subplot(2,1,2)
        pylab.xlim(xmin, xmax)
        pylab.hist(totRes, bins=30)
        pylab.xlabel('Virus Population',fontsize=6)
        pylab.title('guttagonol Resistant Virus Population',fontsize=9)
        
        pylab.show()

simulationDelayedTreatment(10) 


#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    numViruses=100
    maxPop=1000
    maxBirthProb=0.1
    clearProb=0.05
    resistances= {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005
    
    for time in [300, 150, 75, 0]:
        steps = time+300
        drugTime = time + 150
        totPop = []
        totRes = []
        totRes2 = []
        for trial in range(numTrials):
            viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for v in range(numViruses)]
            patient = TreatedPatient(viruses, maxPop)
            for i in range(steps):
                if i ==150:
                    patient.addPrescription('guttagonol')
                if i == drugTime:
                    patient.addPrescription('grimpex')
                patient.update()
            totPop.append(patient.getTotalPop())
            totRes.append(patient.getResistPop(["guttagonol"]))
            totRes2.append(patient.getResistPop(["grimpex"]))

        pylab.figure('drugTime = ' + str(time))
        
        pylab.subplot(3,1,1)
        pylab.hist(totPop, bins=30)
        pylab.title('Total Virus Population')
        xmin, xmax = pylab.xlim()
        
        pylab.subplot(3,1,2)
        pylab.xlim(xmin, xmax)
        pylab.hist(totRes, bins=30)
        pylab.title('guttagonol Resistant Virus Population')
        
        pylab.subplot(3,1,3)
        pylab.xlim(xmin, xmax)
        pylab.hist(totRes2, bins=30)
        pylab.title('grimpex Resistant Virus Population')
        
        pylab.show()

##simulationTwoDrugsDelayedTreatment(50)