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
   
     
    
#####   正文

def maxVal1(toConsider, avail): 
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getWeight() > avail:
        result = maxVal1(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]

        #Explore left branch
        withVal, withToTake = maxVal1(toConsider[1:],
                                      avail - nextItem.getWeight())
        withVal += nextItem.getValue()
        #Explore right branch
        withoutVal, withoutToTake = maxVal1(toConsider[1:], avail)

        #Choose better branch
        #if withVal > withoutVal:
        result = (withVal, withToTake + (nextItem,))
        #else:
            #result = (withoutVal, withoutToTake)
    return result

def smallTest1(value):
    Items = buildItems()
    val, taken = maxVal1(Items, value)
    print ('Total value of items taken = ' + str(val))
    for item in taken:
        print '  ', item

def maxVal(toConsider, avail): 
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getWeight() > avail:
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]

        #Explore left branch
        withVal, withToTake = maxVal(toConsider[1:],
                                      avail - nextItem.getWeight())
        withVal += nextItem.getValue()
        #Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)

        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result

def smallTest(value):
    Items = buildItems()
    val, taken = maxVal(Items, value)
    print ('Total value of items taken = ' + str(val))
    for item in taken:
        print '  ', item

value = 24
smallTest1(value)
print
smallTest(value)

'''
Items in List:
    <clock, 175.0, 10.0>
    <painting, 90.0, 9.0>
    <radio, 20.0, 4.0>
    <vase, 50.0, 2.0>
    <book, 10.0, 1.0>
    <computer, 200.0, 20.0>
'''