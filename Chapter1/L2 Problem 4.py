# -*- coding: utf-8 -*-
import random

def dist1():
    return random.random() * 2 - 1
    
    
def dist2():
    if random.random() > 0.5:
        return random.random()
    else:
        return random.random() - 1

#  两者一样
        
        
        
def dist3():
    return int(random.random() * 10)


def dist4():
    return random.randrange(0, 10)

#  两者一样



def dist5():
    return int(random.random() * 10)


def dist6():
    return random.randint(0, 10)

#  两者不一样，因为 randint(0,10) 包括 0 <= n <= 10