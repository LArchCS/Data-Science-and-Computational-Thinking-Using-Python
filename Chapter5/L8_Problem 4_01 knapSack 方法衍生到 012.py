# -*- coding: utf-8 -*-
# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in xrange(2**N):
        combo = []
        for j in xrange(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:                ##  如果 i 移动 j 位 为 奇数。其实就是看移动 j 位以后最后一位是否为1
                combo.append(items[j])           ##  其实再说白了，就是看 i 的二进制有多少个1，移动的 j 数量最大就是移动到底
        yield combo                             ##  妈了个逼，其实就是那个 1/0 做power set的方法，只是用了移动，看起来更fancy
        
foo = powerSet([1,2,3])

#for i in foo:
#    print i

'''
[]
[1]
[2]
[1, 2]
[3]
[1, 3]
[2, 3]
[1, 2, 3]
'''


def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    # Your code here
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in xrange(3**N):
        bag1 = []
        bag2 = []
        res = ''
        while i > 0:
            res = str(i%3) +res
            i = i//3
        while N - len(res) > 0:
            res = '0' + res
        for i in range(N):
            if res[i] == '1':
                bag1.append(items[i])
            if res[i] == '2':
                bag2.append(items[i])
        yield bag1,bag2
        

boo = yieldAllCombos([1,2,3])



#for i in boo:
#    print i

'''
([], [])
([3], [])
([], [3])
([2], [])
([2, 3], [])
([2], [3])
([], [2])
([3], [2])
([], [2, 3])
([1], [])
([1, 3], [])
([1], [3])
([1, 2], [])
([1, 2, 3], [])
([1, 2], [3])
([1], [2])
([1, 3], [2])
([1], [2, 3])
([], [1])
([3], [1])
([], [1, 3])
([2], [1])
([2, 3], [1])
([2], [1, 3])
([], [1, 2])
([3], [1, 2])
([], [1, 2, 3])
'''
    

