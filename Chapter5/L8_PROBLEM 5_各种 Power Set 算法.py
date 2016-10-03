# -*- coding: utf-8 -*-

'''
L8 PROBLEM 5

A LOT OF POWER SET ALGORITHMS 
'''

List = [1, 2, 3]


###   之前的 递归方法

def recPowerSet(List):
    if len(List) == 0:
        return [[]]
    else:
        nextItem = List[0]
        smaller = recPowerSet(List[1:])
        newer = []
        for new in smaller:
            newer.append(new + [nextItem])
    return smaller + newer

print '递归方法: ','\n',recPowerSet(List),'\n'


###  0/1 法

def zeronePS(List):
    N = len(List)
    template = []
    for i in range(2**N):
        sets = ''
        for n in range(N):
            sets = str(i%2) +sets
            i = i/2
        template.append(sets)
    powersets = []
    for j in template:
        element = []
        for i in range(N):
            if j[i] == '1':
                element.append(List[i])                
        powersets.append(element)
    return powersets
    
print '1/0方法: ','\n',zeronePS(List),'\n'


###  from Problem 8_4
##   原题目用了 generator，我删去了 generator

def powerSet(items):
    N = len(items)
    final = []
    for i in range(2**N):
        combo  = []
        for j in range(N):
            if (i>>j) % 2 == 1:
                combo.append(items[j])
        final.append(combo)
    return final

foo = powerSet(List)

print '1/0方法+二进制运算: ','\n',powerSet(List),'\n'


###  from stackoverflow
# http://stackoverflow.com/questions/18035595/powersets-in-python-using-itertools

import itertools

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

results = list(powerset([1, 2, 3]))
print 'Stackoverflow 方法: ','\n',(results),'\n'


###   用 (排列组合) 组合 的 思想来做 Power Set 就很容易了
##    其实就是 在 range(len(LIST)+1) 从 0 到 全部数值，所有的组合方式

def psCombinations(List):
    res = []
    for i in range(len(List)+1):
        res += list(itertools.combinations(List, i))
    return res

print '排列组合的 组合 方法: ','\n',psCombinations([1,2,3]),'\n'


###   Recursive Generator   有趣

def RCGpowerset(List):
    if len(List) == 0:
        yield []
    else:
        for item in RCGpowerset(List[1:]):
            yield [List[0]]+list(item)
            yield list(item)

a = RCGpowerset(List)
print 'Recursive Generator:','\n',list(a)

b = RCGpowerset([])
print list(b)
