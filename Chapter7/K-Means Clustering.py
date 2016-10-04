# -*- coding: utf-8 -*-
import pylab, random

random.seed(8)
#random.seed(12)
#random.seed(13)
#random.seed(14)


#  Minkowski Metric / calculate distance between two points
def dist(a,b,p=2):
    assert len(a) == len(b), 'Elements to be compared MUST have same length'
    assert type(p) == int, 'P MUST be an integer'
    return (sum((a[i] - b[i])**p for i in range(len(a)) )) ** (1.0/p)
    

#  generate point cloud
def cloud(n, k):
    'n is the size of the point cloud'
    final = []
    for _ in range(k):
        res = []
        centerX = random.choice(range(100))
        centerY = random.choice(range(100))
        for i in range(n/(k+1)):
            #x = random.choice(range(100))
            #y = random.choice(range(100))
            x = int(random.gauss(centerX, 30/k))
            y = int(random.gauss(centerY, 30/k))
            final.append((x,y))
            res.append((x,y))
    return final


# Global Variables
set1,set2,set3,set4 = None, None, None, None

def kmeans(points, k=4):
    def findClusters(points, c1, c2, c3, c4):
        # store points and their distances to 4 centers
        #   {point: [dis1, dis2, dis3, dis4],  ,  ,  }
        dataStructure = {}
        for point in points:
            dataStructure[point] = [None, None, None, None]
        # calculate distances of all points to c1, c2, c3, c4 :
        for point in dataStructure.keys():
            dataStructure[point][0] = (dist(point,c1))
            dataStructure[point][1] = (dist(point,c2))
            dataStructure[point][2] = (dist(point,c3))
            dataStructure[point][3] = (dist(point,c4))
        # store points in clusters 1.. 2.. 3.. 4..
        cluster1 = []
        cluster2 = []
        cluster3 = []
        cluster4 = []
        for point in dataStructure.keys():
            if min(dataStructure[point]) == dataStructure[point][0]:
                cluster1.append(point)
            if min(dataStructure[point]) == dataStructure[point][1]:
                cluster2.append(point)
            if min(dataStructure[point]) == dataStructure[point][2]:
                cluster3.append(point)
            if min(dataStructure[point]) == dataStructure[point][3]:
                cluster4.append(point)  
        # return organized 4 clusters
        return cluster1, cluster2, cluster3, cluster4
    
    def fineCen(cluster1, cluster2, cluster3, cluster4):
        c1 = (sum(i[0] for i in cluster1)/len(cluster1), sum(i[1] for i in cluster1)/len(cluster1))
        c2 = (sum(i[0] for i in cluster2)/len(cluster2), sum(i[1] for i in cluster2)/len(cluster2))
        c3 = (sum(i[0] for i in cluster3)/len(cluster3), sum(i[1] for i in cluster3)/len(cluster3))
        c4 = (sum(i[0] for i in cluster4)/len(cluster4), sum(i[1] for i in cluster4)/len(cluster4))
        return c1, c2, c3, c4
    
    def finalizeClusters(points):
         # set up c1, c2, c3, c4    
        c1= random.choice(points)
        c2 = random.choice(points)
        while c2 == c1:
            c2= random.choice(points)
        c3= random.choice(points)
        while c3 in [c1,c2]:
            c3= random.choice(points)
        c4= random.choice(points)
        while c4 in [c1,c2,c3]:
            c4= random.choice(points)
        
        fix = findClusters(points, c1, c2, c3, c4)
        cluster1, cluster2, cluster3, cluster4 = fix
        newC1, newC2, newC3, newC4 = fineCen(cluster1, cluster2, cluster3, cluster4)
        count = 0
        while newC1!=c1 and newC2!=c2 and newC3!=c3 and newC4!=c4:
            c1, c2, c3, c4 = newC1, newC2, newC3, newC4
            
            if count == 0:
                global set1,set2,set3,set4
                set1,set2,set3,set4 = cluster1, cluster2, cluster3, cluster4
                count = 1
                        
            fix = findClusters(points, c1, c2, c3, c4)
            cluster1, cluster2, cluster3, cluster4 = fix
            # generate new c1, c2, c3, c4
            newC1, newC2, newC3, newC4 = fineCen(cluster1, cluster2, cluster3, cluster4)
            
            #print c1, c2, c3, c4
            #print newC1, newC2, newC3, newC4, '\n'
            
        return cluster1, cluster2, cluster3, cluster4
    
    return finalizeClusters(points)

      
def TryKmeans(numTrials, points):
    best1, best2, best3, best4 = None, None, None, None
    badNess = None
    for i in range(numTrials):
        cluster1, cluster2, cluster3, cluster4 = kmeans(points, k=4)
        cBad = 0
        for cluster in (cluster1, cluster2, cluster3, cluster4):
            cenCluster = (sum(point[0] for point in cluster)/len(cluster), sum(point[1] for point in cluster)/len(cluster))
            for point in cluster:
                cBad += dist(cenCluster, point)
        if badNess == None or cBad < badNess:
            badNess = cBad
            best1, best2, best3, best4 = cluster1, cluster2, cluster3, cluster4
    return best1, best2, best3, best4




# TEST

n = 1000
k = 4
numTrials = 15

a = cloud(n,k)
points = a[:]


cluster1, cluster2, cluster3, cluster4 = TryKmeans(numTrials, points)
     
pylab.figure('TryKmeans')
pylab.title('TryKmeans',  fontsize=12)
pylab.xlim(-20,120)
pylab.ylim(-20,120)
pylab.plot([point[0] for point in cluster1],[point[1] for point in cluster1], 'g.')
pylab.plot([point[0] for point in cluster2],[point[1] for point in cluster2], 'r.')
pylab.plot([point[0] for point in cluster3],[point[1] for point in cluster3], 'b.')
pylab.plot([point[0] for point in cluster4],[point[1] for point in cluster4], 'y.')


cluster1, cluster2, cluster3, cluster4 = kmeans(points, k=4)

pylab.figure('kmeans')
pylab.title('kmeans',  fontsize=12)
pylab.xlim(-20,120)
pylab.ylim(-20,120)
pylab.plot([point[0] for point in cluster1],[point[1] for point in cluster1], 'g.')
pylab.plot([point[0] for point in cluster2],[point[1] for point in cluster2], 'r.')
pylab.plot([point[0] for point in cluster3],[point[1] for point in cluster3], 'b.')
pylab.plot([point[0] for point in cluster4],[point[1] for point in cluster4], 'y.')


cluster1, cluster2, cluster3, cluster4 = set1,set2,set3,set4

pylab.figure('findClusters')
pylab.title('findClusters',  fontsize=12)
pylab.xlim(-20,120)
pylab.ylim(-20,120)
pylab.plot([point[0] for point in cluster1],[point[1] for point in cluster1], 'g.')
pylab.plot([point[0] for point in cluster2],[point[1] for point in cluster2], 'r.')
pylab.plot([point[0] for point in cluster3],[point[1] for point in cluster3], 'b.')
pylab.plot([point[0] for point in cluster4],[point[1] for point in cluster4], 'y.')


'''
pylab.figure('Original')
pylab.title('Original',  fontsize=12)
pylab.xlim(-20,120)
pylab.ylim(-20,120)
pylab.plot([point[0] for point in points],[point[1] for point in points],  'g.')
'''

pylab.show()






