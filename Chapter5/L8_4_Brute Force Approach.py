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

def dToB(n, numDigits):
    """requires: n is a natural number less than 2**numDigits
      returns a binary string of length numDigits representing the
              the decimal number n."""
    assert type(n)==int and type(numDigits)==int and n >=0 and n < 2**numDigits
    bStr = ''
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n//2
    while numDigits - len(bStr) > 0:                ##   二进制数字 之前 补充 若干位 0
        bStr = '0' + bStr
    return bStr

def genPset(Items):
    """Generate a list of lists representing the power set of Items"""
    numSubsets = 2**len(Items)                      ##   3个 item 则最大二进制 数字 为 2**3  8位
    templates = []
    for i in range(numSubsets):                    ##   每一种可能性，这个求 Power Set 的方法 比较巧妙
        templates.append(dToB(i, len(Items)))       ##   templates 则变为了 0,1 表示的所有 setsets
    pset = []
    #print templates
    for t in templates:                            ##   templates 的 0,1 转换为 实际的 Items 的 Power Set
        elem = []
        for j in range(len(t)):
            if t[j] == '1':
                elem.append(Items[j])
        pset.append(elem)
    #print pset
    return pset
 
##   
def genPsetTest(Items):                    ##   打印 templates 和 psets 试试
    """Generate a list of lists representing the power set of Items"""
    numSubsets = 2**len(Items)
    templates = []
    for i in range(numSubsets):
        templates.append(dToB(i, len(Items)))
    pset = []
    print templates
    for t in templates:
        elem = []
        for j in range(len(t)):
            if t[j] == '1':
                elem.append(Items[j])
        pset.append(elem)
    print pset, '\n'
    return pset
genPsetTest([1,2,3])
##
    
def chooseBest(pset, constraint, getVal, getWeight):
    bestVal = 0.0
    bestSet = None
    for Items in pset:
        ItemsVal = 0.0
        ItemsWeight = 0.0
        for item in Items:
            ItemsVal += getVal(item)
            ItemsWeight += getWeight(item)
        if ItemsWeight <= constraint and ItemsVal > bestVal:
            bestVal = ItemsVal
            bestSet = Items
    return (bestSet, bestVal)
    
def testBest():
    Items = buildItems()
    pset = genPset(Items)
    taken, val = chooseBest(pset, 20, Item.getValue, Item.getWeight)
    print ('Total value of items taken = ' + str(val))
    for item in taken:
        print '  ', item

####  自己写的  GoodEnough

def chooseGoodEnough(pset, constraint, getVal, getWeight, GoodEnough):
    for Items in pset:
        ItemsVal = 0.0
        ItemsWeight = 0.0
        for item in Items:
            ItemsVal += getVal(item)
            ItemsWeight += getWeight(item)
        if ItemsWeight <= constraint and ItemsVal >= GoodEnough:
            bestVal = ItemsVal
            bestSet = Items
            print ('GoodEnough value of items taken = ' + str(bestVal) + ' >= ' + str(GoodEnough))
            for item in bestSet:
                print '  ', item
            break

testBest()
chooseGoodEnough(genPset(buildItems()), 20, Item.getValue, Item.getWeight, 201)
