# -*- coding: utf-8 -*-
L = ['apples', 'oranges', 'kiwis', 'pineapples']


def stdDevOfLengths(L):
    if len(L) == 0:
        return float('NaN')            #  这个 float('NaN') 不太理解， 貌似表示不是一个数字
    if len(L)>0:
        mean = float(sum(len(i) for i in L))/len(L)
        total = 0.0
        for i in L:
            total += (len(i)-mean)**2
    return (total/len(L))**0.5
    
    
print stdDevOfLengths(L)

            