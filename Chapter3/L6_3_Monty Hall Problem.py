# -*- coding: utf-8 -*-
import random, pylab

#####     -------------------------     自己写的
numTrials = 1000

def MontyNoSwitch(numTrials):              #  第二次  不  Switch
    win = 0
    for i in range(numTrials):
        doors = [1,2,3]
        car = random.choice(doors)
        hall= []
        player = random.choice(doors)
        for k in doors:
            if k != car and k!=player:
                hall.append(k)
        hallChoice = random.choice(hall)
        if car == player:
            win +=1
    return float(win)/float(numTrials)
    
def MontySwitch(numTrials):              #  第二次  Switch
    win = 0
    for i in range(numTrials):
        doors = [1,2,3]
        car = random.choice(doors)
        hall= []
        player = random.choice(doors)
        for k in doors:
            if k != car and k!=player:
                hall.append(k)
        hallChoice = random.choice(hall)
        for i in doors:
            if i != player and i != hallChoice:
                playerAgain = i
        if playerAgain == car:
            win +=1
    return float(win)/float(numTrials)

def MontyRandomSwitch(numTrials):          #  第二次  随机  Switch
    winStick = 0
    winSwitch = 0
    winNo = 0
    for i in range(numTrials):
        doors = [1,2,3]
        car = random.choice(doors)
        hall= []
        player = random.choice(doors)
        for k in doors:
            if k != car and k!=player:
                hall.append(k)
        hallChoice = random.choice(hall)
        if random.choice((1,2)) == 2:
            for i in doors:
                if i != player and i != hallChoice:
                    playerAgain = i
                    if playerAgain == car:
                        winSwitch += 1
                    else:
                        winNo += 1
        elif player == car:
            winStick += 1
        else:
            winNo += 1
    return (winStick, winSwitch, winNo)


# print MontyNoSwitch(numTrials)
# print MontySwitch(numTrials)



#####     -------------------------     老师的

def montyChoose(guessDoor, prizeDoor):
    if 1 != guessDoor and 1 != prizeDoor:
        return 1
    if 2 != guessDoor and 2 != prizeDoor:
        return 2
    return 3

def randomChoose(guessDoor, prizeDoor):
    if guessDoor == 1:
        return random.choice([2,3])
    if guessDoor == 2:
        return random.choice([1,3])
    return random.choice([1,2])


def simMontyHall(numTrials, chooseFcn):
    stickWins, switchWins, noWin = (0, 0, 0)
    prizeDoorChoices = [1,2,3]
    guessChoices = [1,2,3]
    for t in range(numTrials):
        prizeDoor = random.choice([1, 2, 3])
        guess = random.choice([1, 2, 3])
        toOpen = chooseFcn(guess, prizeDoor)
        if toOpen == prizeDoor:
            noWin += 1
        elif guess == prizeDoor:
            stickWins += 1
        else:
            switchWins += 1
    return (stickWins, switchWins, noWin)





def displayMHSim(simResults, title):
    stickWins, switchWins = simResults[0:-1]
    pylab.pie([stickWins, switchWins], colors = ['r','c'], labels = ['stick','change'], autopct = '%.2f%%')
    pylab.title(title)


print simMontyHall(numTrials, montyChoose)
simResults = simMontyHall(100000, montyChoose)
displayMHSim(simResults, 'Monty Chooses a Door')
pylab.figure()

print simMontyHall(numTrials, randomChoose)
simResults = simMontyHall(100000, randomChoose)
displayMHSim(simResults, 'Door Chosen at Random')
pylab.show()

print MontyRandomSwitch(numTrials)
pylab.figure()
stickWins, switchWins, noWins = MontyRandomSwitch(numTrials)
pylab.pie([stickWins, switchWins, noWins], colors = ['r','c','y'], labels = ['stickWins '+'('+str(stickWins)+')','switchWins '+'('+str(switchWins)+')','noWins '+'('+str(noWins)+')'], autopct = '%.2f%%')
pylab.title('Monty Hall Sim')
pylab.show()