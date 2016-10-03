import random



#####  -------------------------  L2 Problem 3A

def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    # Your code here
    random.seed(1) # This will be discussed in the video "Drunken Simulations"
    return 2 * random.randint(5, 10)

print deterministicNumber()


#####  -------------------------  L2 Problem 3B

def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    # Your code here
    random.seed()
    return random.choice(range(10,21,2))
    
print stochasticNumber()












