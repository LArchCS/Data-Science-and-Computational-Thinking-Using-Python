# -*- coding: utf-8 -*-
def stdDev(X):                   #   方差计算函数
    if len(X)==0:
        return float('NaN')
    else:
        mean = sum(X)/float(len(X))
        tot = 0.0
        for x in X:
            tot += (x - mean)**2
        return (tot/len(X))**0.5
    

X = [1,2,3,4,5,6,7]
            
print float(sum(X))/len(X)            
print stdDev(X)