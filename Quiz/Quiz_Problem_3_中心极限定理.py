import random, pylab
random.seed(0)

x = []
y = []
z = []
a = [1,2,3,4,5,6]
for i in range(900000):
    x.append(random.choice(a))
    y.append(random.choice(a))
    z.append(random.choice(a))

x = pylab.array(x)
y = pylab.array(y)
z = pylab.array(z)

pylab.figure()
pylab.hist(x, bins =6)
pylab.text(1.1,153000,"mean x = " + str(sum(x)/900000.0))
pylab.figure()
pylab.hist(y, bins =6)
pylab.figure()
pylab.hist(z, bins =6)

pylab.figure()
pylab.hist((x+y+z), bins =6)

pylab.show()