# -*- coding: utf-8 -*-
def ca1(n,k):
    def c1(n):
        if n <= 1:                  #    这里必须写 n<=1 , 否则 k>n的时候就出错
            return 1
        else:
            return n*c1(n-1)
    if k<=n:
        return 1.0-round((float(c1(n))/c1(n-k))/n**k,10)       #  这个写法太奇怪了， k>n 的时候居然为 1 减去一个大于0 的超级小数
    if k>n:
        return 1.0                                             #  这个写法太奇怪了， k>n 的时候应该强制 为 1-0
    

def ca2(n,k):
    def c2(n,k):                   #  这个程序好一些，如果 k 比 n 大，k减小到1 的途中 n一定会中途变成0，所以函数值之后一直为0
        if k == 1:
            return n
        else:
            return n*c2(n-1,k-1)
    return 1.0-round(float(c2(n,k))/n**k,10)
    
n=36
k=20

def collision_prob(numBuckets=n, numInsertions=k):                     #  擦，我写了复杂的递归函数，明明可以简单办法
    '''
    Given the number of buckets and the number of items to insert, 
    calculates the probability of a collision.
    '''
    prob = 1.0
    for i in range(1, numInsertions):
        prob = prob * ((numBuckets - i) / float(numBuckets))
    return round(1 - prob,10)


print ca1(n,k)==ca2(n,k), ca1(n,k)==collision_prob()
print collision_prob()
print ca1(n,k)
print ca2(n,k)

def c0(n):
    if n ==1:
        return 1
    else:
        return n*c0(n-1)

def c1(n):
    if n <= 1:                  #    这里必须写 n<=1 , 否则 k>n的时候就出错
        return 1
    else:
        return n*c1(n-1)

def c2(n,k):
    if k == 1:
        return n
    else:
        return n*c2(n-1,k-1)
        
print
print c0(n)
print c1(n)/c1(n-k)             #  K>n 时 不知道是个什么鬼, 反正 n-k <= 1 的时候 只返回 1
print c2(n,k)                    #  K>n 时 可以发现为 0
