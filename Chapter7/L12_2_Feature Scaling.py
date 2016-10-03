import pylab, random

random.seed(0)

def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

def scaleFeatures(vals):
    vals = pylab.array(vals)
    mean = sum(vals)/float(len(vals))
    sd = stdDev(vals)
    vals = vals - mean
    return vals/sd
    
def testScaling(n,mean,std):
    vals = []
    for i in range(n):
        vals.append(int(random.gauss(mean,std)))
    vals = pylab.array(vals)
    print 'original values', vals
    print 'original mean = ', sum(vals/len(vals))
    print 'original sd = ', stdDev(vals)
    sVals = scaleFeatures(vals)
    print '\n','scaled values',sVals
    print 'new mean = ', sum(sVals/len(vals))
    print 'new sd = ', stdDev(sVals)
    
testScaling(10,25,3)