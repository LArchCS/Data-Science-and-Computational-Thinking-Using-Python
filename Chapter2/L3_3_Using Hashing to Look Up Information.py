# -*- coding: utf-8 -*-
class intDict(object):
    """A dictionary with integer keys"""
    
    def __init__(self, numBuckets):
        """Create an empty dictionary"""
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])
            
    def addEntry(self, dictKey, dictVal):
        """Assumes dictKey an int.  Adds an entry."""       #   ##  ???  感觉 dictKey 不应该为 int，而应该加个 ord .. 
        hashBucket = self.buckets[dictKey%self.numBuckets]  #  第几个 buckets，余数来求
        for i in range(len(hashBucket)):                   #  go over  hashBucket 的长度，内部项数    ##  ???   第一次run 的时候试试把这个 loop 删掉看行不行。 答：可以，但不能更新覆盖值
            if hashBucket[i][0] == dictKey:                #  如果内部 Tuple 的第一项 等于 dictKey
                hashBucket[i] = (dictKey, dictVal)         #   这个Tuple就为 (dictKey, dictVal)       ##  ???   疑问，会不会改值。答：会
                return                               #  注意这里有 return，重复以后就不走下面的 return 了
        hashBucket.append((dictKey, dictVal))             #  如果dictKey第一次出现，则直接补上这个 Tuple
        
    def getValue(self, dictKey):                               #  简单，直接return 对应的 dictKey 的 Tuple[1] Value
        """Assumes dictKey an int.  Returns entry associated
           with the key dictKey"""
        hashBucket = self.buckets[dictKey%self.numBuckets]
        for e in hashBucket:
            if e[0] == dictKey:
                return e[1]
        return None
    
    def __str__(self):
        res = ''
        for b in self.buckets:
            for t in b:
                res = res + str(t[0]) + ':' + str(t[1]) + ','
        return '{' + res[:-1] + '}'                           #  显示出全部的内容
        


import random

D = intDict(29)

for i in range(20):
    # choose a random int in range(10**5):
    key = random.choice(range(10**5))
    D.addEntry(key, i)
    
print '\n' , 'The buckets are: '
for hashBucket in D.buckets: #violates abstraction barrier
    print '  ', hashBucket
    