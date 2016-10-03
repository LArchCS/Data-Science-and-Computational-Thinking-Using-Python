import random

def rollDie():
    return random.choice([1,2,3,4,5,6])

def rollN(n):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    return result

def getTarget(goal):
    numTries = 0
    numRolls = len(goal)
    while True:
        numTries += 1
        if rollN(numRolls) == goal:
            return numTries
            
def runSim(goal, tries):
    total = 0
    for i in range(tries):
        total = total + getTarget(goal)
    ave = float(total)/float(tries)
    chance = 1.0/ave
    print 'Test  probability  = ', chance

goal = 321
print 'Actual probability = ', 1.0/6.0**len(str(goal))
runSim(str(goal),100)