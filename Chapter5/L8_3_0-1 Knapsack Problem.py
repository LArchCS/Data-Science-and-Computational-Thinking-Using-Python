# -*- coding: utf-8 -*-
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
    print templates
    for t in templates:                            ##   templates 的 0,1 转换为 实际的 Items 的 Power Set
        elem = []
        for j in range(len(t)):
            if t[j] == '1':
                elem.append(Items[j])
        pset.append(elem)
    print pset
    return pset
 
genPset([1,2,3])   


#####  之前的另外一个求 Power Set 的方法： 递归

def subsets(L):
    if len(L) == 0:
        return [[]]
    smaller = subsets(L[:-1])
    extra = L[-1:]                      #   L[:-1] 是一个 list
    new = []
    for small in smaller:
        new.append(small+extra)
    return smaller+new
    
print '\n', subsets([1,2,3])