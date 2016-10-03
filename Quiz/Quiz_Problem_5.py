#   You have a bucket with 4 red balls and 4 green balls. You draw 3 balls out of the bucket.
#   Assume that once you draw a ball out of the bucket, you don't replace it.
#   What is the probability of drawing 3 balls of the same color?

###   Write a Monte Carlo simulation to solve the above problem.

import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    # Your code here
    count = 0.0
    for i in xrange(numTrials):
        pool = ['r','g','r','g','r','g','r','g']
        select = []
        for i in xrange(3):
            selection = random.choice(pool)
            pool.remove(selection)
            select.append(selection)
        if len(set(select)) == 1:
            count += 1
    return count/numTrials
    
print drawing_without_replacement_sim(9999)