# -*- coding: utf-8 -*-
class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value) + ', '\
                 + str(self.weight) + '>'
        return result

def buildItems():
    names = ['clock', 'painting', 'radio', 'vase', 'book',
             'computer']
    vals = [175,90,20,50,10,200]
    weights = [10,9,4,2,1,20]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    return Items

def subsets(L):
    if len(L) == 0:
        return [[]]
    smaller = subsets(L[:-1])
    extra = L[-1:]                      #   L[:-1] 是一个 list
    new = []
    for small in smaller:
        new.append(small+extra)
    return smaller+new
        
def greedySubSets(subset,limit):
    best = 0
    take = 0
    for n in subset:
        if sum(i.getWeight() for i in n) <= limit and sum(i.getValue() for i in n) > best:
            best = sum(i.getValue() for i in n)
            take = sum(i.getWeight() for i in n)
            inventory = n
    print 'Value =', best, ', ','Weights =', take, ', ', 'limit =', limit
    for i in inventory:
        print '  ', i

    
theif = subsets(buildItems())
greedySubSets(theif,20)
