# -*- coding: utf-8 -*-


a = [6,2]
b = [7,3]
c = [8,4]
d = [9,5]

def subsets(L):
    if len(L) == 1:
        return [L]
    smaller = subsets(L[:-1])
    extra = L[-1:]                      #   L[:-1] 是一个 list
    new = []
    for small in smaller:
        new.append(small+extra)
    return smaller+new

subset = subsets([a,b,c,d])
def cons(subset,limit):
    best = 0
    take = 0
    inventory = None
    for n in subset:
        if sum(i[1] for i in n) <= limit and sum(i[0] for i in n) > best:
            best = sum(i[0] for i in n)
            inventory = n
            take = sum(i[1] for i in n)
    print best,take,inventory
    
def goodEnough(subset,limit,good):
    for n in subset:
        if sum(i[1] for i in n) <= limit and sum(i[0] for i in n) >= good:
            print sum(i[0] for i in n), sum(i[1] for i in n), n
            break
    
cons(subset,10)
goodEnough(subset,10,20)

















