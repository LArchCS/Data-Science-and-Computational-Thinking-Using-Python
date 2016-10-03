# -*- coding: utf-8 -*-

#l = [1,2,2,3,4,4,4,4,5,5,5,5,5,6]
l = [1,2,2,3,4,4,4,4,5,5,5,5,5]
#l = [1]


#for i in enumerate(l):
#    print i
    
def longestRun1(l):                # 网友写的 方法
    sett = []
    count = 1
    for ind, elm in enumerate(l):
        if ind > 0:
            if elm == l[ind - 1]:
                count += 1
            else:
                sett.append(count)
                count = 1
    else:
        sett.append(count)
    return max(sett),len(sett)

def longestRun2(l):                # 我写出来的 第一个 方法
    sett=[]
    i = 0
    j = 0
    while i<len(l) and j<len(l):
        count = 0
        while l[i]==l[j]:
            j += 1
            count += 1
            if j == len(l):
                break
        i = j
        sett.append(count)
    return max(sett),len(sett)
    
def longestRun3(l):                # 最 笨 的方法
    count = 1
    sett = [min(len(l),1)]
    for i in xrange(len(l)-1):
        j = i+1
        while l[i] == l[j]:
            count += 1
            j += 1
            if j == len(l):
                break
        sett.append(count)
        count=1
    return max(sett),len(sett)
    
def longestRun4(l):                # 最 smart 的方法
    l = l[:]                      ##  记住 要 复制 一次 List
    sett = []
    count = 1
    while len(l) > 1:
        if l.pop(0) == l[0]:
            count += 1
        else:
            sett.append(count)
            count=1
    else:
        sett.append(count)
    return max(sett),len(sett)

def longestRun5(l):                # 最最 smart 的方法
    sett = []
    count = 1
    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            count += 1
        else:
            sett.append(count)
            count = 1
    sett.append(count)
    return max(sett),len(sett)

def longestRun6(l):                # 笨 的方法 的改善，减少了一点儿运算量
    count = 1
    sett = []
    j=0
    for i in xrange(len(l)-1):
        if i < j:
            pass
        else:
            j = i+1
            while l[i] == l[j]:
                count += 1
                j += 1
                if j == len(l):
                    break
            sett.append(count)
            count=1
    sett.append(count)
    return max(sett),len(sett)

print 'len(l): ' + str(len(l)) +'\n'

print longestRun1(l)
print longestRun2(l)
print longestRun3(l)
print longestRun4(l)
print longestRun5(l)
print longestRun6(l)
