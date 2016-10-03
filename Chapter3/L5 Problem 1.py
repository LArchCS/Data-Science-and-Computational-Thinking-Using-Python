## L5 Problem 1

'''
You have a bucket with 3 red balls and 3 green balls.
Assume that once you draw a ball out of the bucket, you don't replace it.
What is the probability of drawing 3 balls of the same color?

Write a Monte Carlo simulation to solve the above problem. Feel free to write a helper function if you wish.
'''

import random

def pick():
    res = []
    backet = ['g','g','g','r','r','r']
    for i in range(3):
        ball = random.choice(backet)
        backet.remove(ball)
        res.append(ball)
    if len(set(res)) == 1:
        return True

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    count = 0.0
    for i in range(numTrials):
        if pick():
            count += 1.0
    return count/numTrials
    
print noReplacementSimulation(10000)
