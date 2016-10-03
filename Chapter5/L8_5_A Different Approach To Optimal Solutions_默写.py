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
   
     
    
#####   本讲新内容

def maxVal(toConsider, avail): 
    if toConsider==[] or avail == 0:
        result = [[],toConsider,0,avail]    # items to take, items left, value, available weight
    elif toConsider[0].getWeight() > avail:
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]            ####  继续思考，如何在 Tree 里就记住 left items
        # Left Branch
        withTake, Left, withValue, withAvail = maxVal(toConsider[1:], avail-nextItem.getWeight())
        withValue += nextItem.getValue()
        withTake.append(nextItem)
        # Right Branch
        withoutTake, Left, withoutValue, withoutAvail = maxVal(toConsider[1:], avail)
        if withValue > withoutValue:
            result = withTake, Left, withValue, withAvail
        else:
            result = withoutTake, Left, withoutValue, withoutAvail
    return result

def textTree(avail):
    toConsider = buildItems()
    choice, left, value, leftAvail = maxVal(toConsider, avail)
    leftover = toConsider[:]              ##  这个地方可以计算 left， 但可否在 Tree 里就计算出
    for i in choice:
        leftover.remove(i)
    print 'Allowed Weight: ', avail
    print 'Value: ', value
    print 'Left Weight: ', leftAvail
    print 'Inventory:'
    for i in choice:
        print '  '+ str(i)
    print 'Leftover:'
    for i in leftover:
        print '  '+ str(i)
    print 'Things not Considered:'
    for i in left:
        print '  '+ str(i)
        

#textTree(1)



def maxValGoodEnough(toConsider, avail,GoodEnough):
    if toConsider==[] or avail == 0:
        result = [[],toConsider,0,avail]    # items to take, items left, value, available weight
    elif toConsider[0].getWeight() > avail:
        result = maxValGoodEnough(toConsider[1:], avail, GoodEnough)
    else:
        nextItem = toConsider[0]            ####  继续思考，如何在 Tree 里就记住 left items
        #print 'nextItem ',nextItem
        Left = toConsider[1:]
        # Left Branch
        withTake, Left, withValue, withAvail = maxValGoodEnough(toConsider[1:], avail-nextItem.getWeight(), GoodEnough)
        withValue += nextItem.getValue()
        withTake.append(nextItem)
        # Right Branch
        withoutTake, Left, withoutValue, withoutAvail = maxValGoodEnough(toConsider[1:], avail, GoodEnough)
        if withValue >= GoodEnough:
            result = withTake, Left, withValue, withAvail
            return result
        if withoutValue >= GoodEnough:
            result = withoutTake, Left, withoutValue, withoutAvail
            return result
        else:
            if withValue > withoutValue:
                result = withTake, Left, withValue, withAvail
            else:
                result = withoutTake, Left, withoutValue, withoutAvail
    return result

def textTreeGoodEnough(avail,GoodEnough):
    toConsider = buildItems()
    choice, Left, value, leftAvail = maxValGoodEnough(toConsider, avail,GoodEnough)
    leftover = toConsider[:]
    for i in choice:
        leftover.remove(i)
    print 'Allowed Weight: ', avail
    print 'Value: ', value
    print 'Left Weight: ', leftAvail
    print 'Inventory:'
    for i in choice:
        print '  '+ str(i)
#    print 'Leftover:'
#    for i in leftover:
#        print '  '+ str(i)
    print 'Things not Considered:'
    for i in Left:
        print '  '+ str(i)


avail = 12
textTree(avail)
print
textTreeGoodEnough(avail,1)

'''
Items in List:
    <clock, 175.0, 10.0>
    <painting, 90.0, 9.0>
    <radio, 20.0, 4.0>
    <vase, 50.0, 2.0>
    <book, 10.0, 1.0>
    <computer, 200.0, 20.0>
'''

