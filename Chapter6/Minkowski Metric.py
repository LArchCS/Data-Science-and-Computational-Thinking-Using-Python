##  Minkowski Metric

def dist(a,b,p=1):
    assert len(a) == len(b), 'Elements to be compared MUST have same length'
    assert type(p) == int, 'P MUST be an integer'
    return (sum((a[i] - b[i])**p for i in range(len(a)) )) ** (1.0/p)
    


a = [[2,10,5,3,4,6],[2,3,8,5,7,3]]
b = [[4,3,8,5,5,5],[4,3,8,5,5,5]]


def maxLinkageDist(self, other):
        """ Returns the float distance between the points that 
        are farthest from each other, where one point is from 
        self and the other point is from other. Uses the 
        Euclidean dist between 2 points, defined in Point."""
        greatest = None
        for point1 in self.points:
            for point2 in other.points:
                if greatest == None or point1.distance(point2) > greatest:
                    shortest = point1.distance(point2)
        return shortest

a = [2,10,5,3,4,6]
b = [4,3,8,5,5,5]
print dist(a,b,2)