# -*- coding: utf-8 -*-

import pylab

#####  -------------------------  EXAMPLE 1

'''
pylab.figure(1)
pylab.plot([1,2,3,4],[1,2,3,4])

pylab.figure(2)
pylab.plot([1,4,2,3],[5,6,7,8])
# pylab.savefig('Figure-Eric')    # save figure 2

pylab.figure(1)   # go back to figure(1)
pylab.plot([5,6,10,3])      #  draw again on figure(1)    y is set to be [5,6,7,8], default x = range(len(y))
# pylab.savefig('Figure-Grimson')  # save figure 1

'''

#####  -------------------------  EXAMPLE 2

principal = 10000  # initial investment
interestRate = 0.05
years = 20
values = []

for i in range(years+1):
    values.append(principal)
    principal += principal*interestRate

pylab.figure(3)

#  对于每一个plot，默认的颜色是蓝色，简称 'b'，默认的线性是solid line '-'
pylab.plot(range(years+1),values,'ro',label = 'nihaoa')   # 'r' 是 红色，o 是circle

pylab.plot(values , linewidth =10)

pylab.title('5% Growth, Compounded Annually', fontsize=20)   # 写表格的title
pylab.xlabel('Years of Compounding', fontsize=12)            # 写表格的 x 坐标名
pylab.ylabel('Value of Principal ($)', fontsize=16)          # 写表格的 y 坐标名

pylab.show()


#  可以改 default values, 在一个什么 rc file