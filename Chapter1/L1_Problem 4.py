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
import numpy

#  比较老旧的方法求 diffTemps
'''
low,high = loadFile()
diffTemps=[]
for i in range(len(low)):
    diffTemps.append(high[i]-low[i])
'''

# TA 有一个有 zip 的方法
'''
low,high = loadFile()
diffTemps=[]
everyday = zip(high,low)
for x,y in everyday:
    diffTemps.append(x-y)
'''

# 新的用 array 求 diffTemps

low,high = loadFile()
diffTemps=numpy.array(high)-numpy.array(low)


pylab.figure(1)
pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
pylab.xlabel('Days')
pylab.ylabel('Temperature Ranges') 
pylab.plot(range(1,32), diffTemps)
pylab.show()

pylab.savefig('julyTemps')
