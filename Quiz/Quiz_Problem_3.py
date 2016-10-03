# -*- coding: utf-8 -*-
import random, pylab
random.seed(2)


xVals = []
yVals = []
wVals = []
for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())

xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
wVals = pylab.array(wVals)

xVals = xVals + xVals
zVals = xVals + yVals
tVals = xVals + yVals + wVals


pylab.figure('wVals,hist')           #  大数定理
pylab.hist(yVals, bins=50)
pylab.text(0.05, 28, 'yVals/1000 = '+str(sum(yVals/1000))) 
print sum(yVals/1000)               #  大数定理

pylab.figure('tVals,hist')
pylab.hist(tVals, bins=50)           #  中心极限定理

pylab.figure('xVals, zVals')
pylab.plot(xVals, zVals)

pylab.figure('xVals, xVals')
pylab.plot(xVals, xVals)

pylab.figure('xVals, yVals')
pylab.plot(xVals, yVals)

pylab.figure('xVals, sorted(yVals)')
pylab.plot(xVals, sorted(yVals))

pylab.figure('sorted(xVals), yVals')
pylab.plot(sorted(xVals), yVals)

pylab.figure('sorted(xVals), sorted(yVals)')
pylab.plot(sorted(xVals), sorted(yVals))


pylab.show()

