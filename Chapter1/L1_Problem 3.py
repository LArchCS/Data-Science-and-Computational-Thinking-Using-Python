# -*- coding: utf-8 -*-

#####  -------------------------  Problem 3

def loadFile():
    inFile = open('E:\Edx\MIT_Python_2\Week1\julyTemps.txt','r')
    high = []
    low = []
    for line in inFile:
        fields = line.split()
        if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
            continue                     #  注意，continue 的 作用是重新开始loop
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return (low, high)

#  print loadFile()


#####  -------------------------  Problem 4

import pylab

diffTemps=[]
for i in range(31):
    diffTemps.append(loadFile()[1][i]-loadFile()[0][i])

pylab.figure(2)
pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
pylab.xlabel('Days')
pylab.ylabel('Temperature Ranges') 
pylab.plot(range(1,32), diffTemps)
pylab.show()