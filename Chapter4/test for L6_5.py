import pylab

distances = pylab.array([ 1080.,  1044.,  1008.,   972.,   936.,   900.,   864.,   828.,
         792.,   756.,   720.,   540.,   360.,   180.,     0.])

heights = pylab.array([[  0.  ,   2.25,   5.25,   7.5 ,   8.75,  12.  ,  13.75,  14.75,
         15.5 ,  17.  ,  17.5 ,  19.5 ,  18.5 ,  13.  ,   0.  ],
       [  0.  ,   3.25,   6.5 ,   7.75,   9.25,  12.25,  16.  ,  15.25,
         16.  ,  17.  ,  18.5 ,  20.  ,  18.5 ,  13.  ,   0.  ],
       [  0.  ,   4.5 ,   6.5 ,   8.25,   9.5 ,  12.5 ,  16.  ,  15.5 ,
         16.6 ,  17.5 ,  18.5 ,  20.25,  19.  ,  13.  ,   0.  ],
       [  0.  ,   6.5 ,   8.75,   9.25,  10.5 ,  14.75,  16.5 ,  17.5 ,
         16.75,  19.25,  19.  ,  20.5 ,  19.  ,  13.  ,   0.  ]])
         
totHeights = pylab.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
for h in heights:
        totHeights = totHeights + pylab.array(h)
meanHeights = totHeights/float(len(heights))

print distances
print meanHeights

pair = []
for i in range(len(distances)):
    pair.append((distances[i],meanHeights[i]))

print pair