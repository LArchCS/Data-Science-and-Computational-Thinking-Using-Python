# -*- coding: utf-8 -*-
def strToInt(s):
    number = ''
    for c in s:
        number = number + str(ord(c))
    index = int(number)
    return index

#  print 'Index =', strToInt('a')
#  print 'Index =', strToInt('John is a cool dude')


def hashStr(s,tableSize=101):
    number = ''
    for c in s:
        number = number + str(ord(c))
    index = int(number)%tableSize
    return index

    
#print 'Index =', strToInt('abc')      
#print hashStr('abc',tableSize=101)


'Eric Grimson'
# print hashStr('Eric',7)
#  2

'Chris Terman'
# print hashStr('Chris',7)
#  3

'Jill Smith'
# print hashStr('Jill',7)
#  3




#####     -------------------------     自己写着玩的
'''
global hashtable
hashtable = []

def table(tablesize = 7):
    global hashtable
    for i in range(tablesize):
        hashtable.append([])
    return hashtable

print table()


def hashnames(s):
    global hashtable
    number = ''
    for c in s.split()[0]:
        number = number + str(ord(c))
    index = int(number)%len(hashtable)
    hashtable[index].append(tuple(s.split()))
    return hashtable
    

print hashnames('Jill Smith')
print hashnames('Chris Terman')
print hashnames('Eric Grimson')
print hashnames('Fan Di')

def lookname(firstname):
    global hashtable
    number = ''
    for c in firstname:
        number = number + str(ord(c))
    index = int(number)%len(hashtable)
    for i in hashtable[index]:
        if i[0] == firstname:
            return ' '.join(k for k in i)

print lookname('Eric')
print lookname('Chris')
print lookname('Jill')
print lookname('Fan')
'''


#####     -------------------------     自己写着玩的， 用了下一讲的 class

class intDict(object):
    """A dictionary with integer keys"""
    
    def __init__(self, numBuckets):
        """Create an empty dictionary"""
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])
            
    def addEntry(self, s):
        """Assumes dictKey an int.  Adds an entry.""" 
        hashtable = self.buckets
        number = ''
        for c in s.split()[0]:
            number = number + str(ord(c))
        index = int(number)%len(hashtable)
        hashtable[index].append(tuple(s.split()))
        return hashtable
        
    def getValue(self, firstname):
        """Assumes dictKey an int.  Returns entry associated
           with the key dictKey"""
        hashtable = self.buckets
        number = ''
        for c in firstname:
            number = number + str(ord(c))
        index = int(number)%len(hashtable)
        for i in hashtable[index]:
            if i[0] == firstname:
                return ' '.join(k for k in i)
        return None
    
    def __str__(self):
        res = ''
        for b in self.buckets:
            for t in b:
                res = res + ' '.join(k for k in t) + ', '
        return '{' + res[:-2] + '}'                           # 这个地方 [:-2] 可以不显示最后的 ', '
        
D = intDict(3)

print D.buckets

print D.addEntry('Fan Di')
print D.addEntry('Jinhua Quan')
print D.addEntry('Henry Di')
#  如果 加个 'Fan Henry'  就没法处理了

print D.getValue('Fan')
print D.getValue('Jinhua')
print D.getValue('Henry')
print D.getValue('Fei')

print str(D)
