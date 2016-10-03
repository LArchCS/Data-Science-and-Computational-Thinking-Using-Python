import pylab
import numpy

def loadFile():
    inFile = open('D:\\001_Edx\MIT_Python_2\Week1\julyTemps.txt','r')
    high = []
    low = []
    for line in inFile:
        fields = line.split()
        if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return (low, high)

def producePlot(lowTemps, highTemps):
    diffTemps = list(numpy.array(highTemps) - numpy.array(lowTemps))
    pylab.plot(range(1,32), diffTemps)
    pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Ranges')
    pylab.show()


(low, high) = loadFile()
producePlot(low, high)
