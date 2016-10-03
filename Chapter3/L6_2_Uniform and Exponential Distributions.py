# -*- coding: utf-8 -*-
## Uniform and Exponential Distributions

import random, pylab

#set line width
pylab.rcParams['lines.linewidth'] = 6
#set font size for titles 
pylab.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
pylab.rcParams['xtick.major.size'] = 5
#set size of numbers on y-axis
pylab.rcParams['ytick.major.size'] = 5

def clear(n, clearProb, steps):
    '''
    n 为 初始分子数量
    clearProb 每一步被消灭的概率
    steps 时间步数
    '''
    numRemaining = [n]
    for t in range(steps):
        numRemaining.append(n*((1-clearProb)**t))
    pylab.plot(range(steps+1), numRemaining, label = 'Exponential Decay')

'''
clear(1000, 0.01, 500)
pylab.xlabel('Number of Steps')
pylab.ylabel('Number of Molecules')
pylab.title('Clearance of Molecules')
# pylab.semilogy()
pylab.show()
'''


def clearSim(n, clearProb, steps):
    numRemaining = [n]
    for t in range(steps):
        numLeft = numRemaining[-1]
        for m in range(numRemaining[-1]):
            if random.random() <= clearProb: 
                numLeft -= 1
        numRemaining.append(numLeft)
    pylab.plot(numRemaining, 'ro', label = 'Simulation')

clear(1000, 0.01, 500)
clearSim(1000, 0.01, 500)
pylab.xlabel('Number of Steps')
pylab.ylabel('Number of Molecules')
pylab.legend()
# pylab.semilogy()                    #  检测 是否 是 exponential distribution 的方法
pylab.show()