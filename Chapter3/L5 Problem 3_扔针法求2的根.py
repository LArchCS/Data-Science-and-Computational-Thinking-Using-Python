#####  L5 Problem 3
## https://courses.edx.org/courses/course-v1:MITx+6.00.2x_5+1T2016/courseware/44b64e16aa524037be90cd2aa3552ef6/b0be589b63b44645b2b8649d7a0af7fe/

# ASK:    If you wanted to run a simulation that estimates the value of square root of 2 in a way similar to the Pi estimation shown in lecture, what geometric shape would you throw needles at?
# ANSWER: A flat line ranging from 1 to root 2 and with a subsection that spans from 0 to 1.


import random

def throwNeedles(numNeedles):
    success = 0
    for n in xrange(numNeedles):
        x = random.random()
        if (1+x)**2 < 2.0:
            success += 1
    sqrt2 = 1+(float(success)/numNeedles)
    return sqrt2
    
'''
If the needles fall in the section from 1 to 2
then the ratio of the square of the successful random
throws in the unit section between 1 and 2 to the total
number of throws will approximate the decimal fraction of root 2.
Since we started the lower bound at 1,
we have to add 1 to the fraction to get the actual approximation of root 2.
'''