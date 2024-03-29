# -*- coding: utf-8 -*-
import pylab

#set line width
pylab.rcParams['lines.linewidth'] = 6
#set font size for titles 
pylab.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
pylab.rcParams['xtick.major.size'] = 5
#set size of numbers on y-axis
pylab.rcParams['ytick.major.size'] = 5



def findPayment(loan, r, m):
    """Assumes: loan and r are floats, m an int
    Returns the monthly payment for a mortgage of size
    loan at a monthly rate of r for m months"""
    return loan*((r*(1+r)**m)/((1+r)**m - 1))                #  计算的是常规贷款每月还款额

class MortgagePlots(object):
    
    def plotPayments(self, style):                            #  每个月的当月缴费量
        pylab.plot(self.paid[1:], style, label = self.legend)
        
    def plotTotPd(self, style):                               #  每个月的缴费累计总量
        totPd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i])            #  append 的是 之前的最后一项，加上当月缴费量
        pylab.plot(totPd, style, label = self.legend)


class Mortgage(MortgagePlots, object):             #  一般 super class 写在后面，Mortgage 是object的subclass
    """Abstract class for building different kinds of mortgages"""
    def __init__(self, loan, annRate, months):
        """Create a new mortgage"""
        self.loan = loan
        self.rate = annRate/12.0
        self.months = months
        self.paid = [0.0]                           #  list 相当于还款记录，记录每一个月的还款额
        self.owed = [loan]                          #  每个月的欠款额
        self.payment = findPayment(loan, self.rate, months)   #  当月还款额  ? ? ?  在双利息处应该会被改
        self.legend = None   #description of mortgage

    def makePayment(self):
        """Make a payment"""
        self.paid.append(self.payment)
        reduction = self.payment - self.owed[-1]*self.rate   #  当月偿还的量进到本金里的
        self.owed.append(self.owed[-1] - reduction)

    def getTotalPaid(self):
        """Return the total amount paid so far"""
        return sum(self.paid)

    def __str__(self):
        return self.legend


# fixed-rate mortgage
class Fixed(Mortgage):
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self.legend = 'Fixed, ' + str(r*100) + '%'

# fixed-rate mortgage with up-front points
class FixedWithPts(Fixed):
    def __init__(self, loan, r, months, pts):
        Fixed.__init__(self, loan, r, months)
        self.pts = pts
        self.paid = [loan*(pts/100.0)]
        self.legend += ', ' + str(pts) + ' points'

# mortgage that changes interest rate after 48 months
class TwoRate(Mortgage):
    def __init__(self,loan,r,months,teaserRate,teaserMonths):
        Mortgage.__init__(self, loan, teaserRate, months)  #  1. 这里并没有照超Mortgage，而是把teaserRate默认为annRate，下面会改
        self.teaserMonths = teaserMonths
        self.teaserRate = teaserRate                       #  1. 所以这时候的 self.rate = teaserRate
        self.nextRate = r/12.0
        self.legend = str(teaserRate*100)\
            + '% for ' + str(self.teaserMonths)\
            + ' months, then ' + str(r*100) + '%'

    def makePayment(self):
        if len(self.paid) == self.teaserMonths + 1:
            self.rate = self.nextRate                      #  2. 所以这时候的 self.rate 变成 self.nextRate
            self.payment = findPayment(self.owed[-1], self.rate, self.months - self.teaserMonths)
            #  2. 这之前是 self.payment = findPayment(loan, self.rate, months)  
        Mortgage.makePayment(self)



def plotMortgages(morts, amt):
    styles = ['b-', 'r-.', 'g:']
    payments = 0 #number to identify a figure
    cost = 1 #number to identify a figure
    pylab.figure(payments)
    pylab.title('Monthly Payments of Different $' + str(amt)
                + ' Mortgages')
    pylab.xlabel('Months')
    pylab.ylabel('Monthly Payments')
    pylab.figure(cost)
    pylab.title('Cost of Different $' + str(amt) + ' Mortgages')
    pylab.xlabel('Months')
    pylab.ylabel('Total Payments')
    for i in range(len(morts)):
        pylab.figure(payments)
        morts[i].plotPayments(styles[i])
        pylab.figure(cost)
        morts[i].plotTotPd(styles[i])
    pylab.figure(payments)
    pylab.legend(loc = 'upper right')
    pylab.figure(cost)
    pylab.legend(loc = 'best')


def compareMortgages(amt, years, fixedRate, pts, ptsRate, varRate1, varRate2, varMonths):
    totMonths = years*12
    fixed1 = Fixed(amt, fixedRate, totMonths)
    fixed2 = FixedWithPts(amt, ptsRate, totMonths, pts)
    twoRate = TwoRate(amt, varRate2, totMonths,
                      varRate1, varMonths)
    morts = [fixed1, fixed2, twoRate]
    for m in range(totMonths):
        for mort in morts:
            mort.makePayment()
    plotMortgages(morts, amt)


compareMortgages(amt=246400, years=30, fixedRate=0.07,
                 pts = 3.25, ptsRate=0.05, varRate1=0.045,
                 varRate2=0.095, varMonths=48)

pylab.show()