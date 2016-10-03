# -*- coding: utf-8 -*-

def maxVal(toConsider, avail): 
    if toConsider==[] or avail == 0:
        Left = toConsider
        result = [], Left, 0, avail     # items to take, items left, value, available weight
    elif toConsider[0][2] > avail:
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]            ####  继续思考，如何在 Tree 里就记住 left items
        # Left Branch
        withTake, Left, withValue, withAvail = maxVal(toConsider[1:], avail-nextItem[2])
        withValue += nextItem[1]
        withTake.append(nextItem)
        # Right Branch
        withoutTake, Left, withoutValue, withoutAvail = maxVal(toConsider[1:], avail)
        if withValue > withoutValue:
            result = withTake, Left, withValue, withAvail
        else:
            result = withoutTake, Left, withoutValue, withoutAvail
    return result

def textTree(toConsider,avail):
    choice, left, value, leftAvail = maxVal(toConsider, avail)
    leftover = toConsider[:]              ##  这个地方可以计算 left， 但可否在 Tree 里就计算出
    for i in choice:
        leftover.remove(i)
    print 'Allowed Weight: ', avail
    print 'Value: ', value
    print 'Left Weight: ', leftAvail
    print 'Inventory:'
    for i in choice:
        print i[0]
#    print 'Leftover:'
#    for i in leftover:
#        print i[0]
    print 'Things not Considered:'
    for i in left:
        print '  '+ i[0]
 
               
a = ['a',6,6]
b = ['b',7,1]
c = ['c',8,6]
d = ['d',9,6]

'''
This is how the complete graph looks like:
    
0   -a   --ab  ---abc ----abcd
                      ----abc
               ---ab  ----abd
                      ----ab 
         -- a  ---ac  ----abd
                      ----ac
               ---ab  ----abc
                      ----ab
    -0   -- b  ---bc  ----bcd
                      ----bc
               ---b   ----bd
                      ----b 
         -- 0  ---c   ----cd
                      ----c
               ---0   ----d
                      ----0 
'''

textTree([a,b,c,d],5)