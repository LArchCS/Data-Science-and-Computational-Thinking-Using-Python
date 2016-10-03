# -*- coding: utf-8 -*-
# 6.00.2x Problem Set 5
# Graph optimization
#
# A set of data structures to represent graphs
#

class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        # Override the default hash method
        # Think: Why would we want to do this?
        return self.name.__hash__()

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return '{0}->{1}'.format(self.src, self.dest)

class Digraph(object):
    """
    A directed graph
    """
    def __init__(self):
        # A Python Set is basically a list that doesn't allow duplicates.
        # Entries into a set must be hashable (where have we seen this before?)
        # Because it is backed by a hashtable, lookups are O(1) as opposed to the O(n) of a list (nifty!)
        # See http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this to make sure we
            # don't add a duplicate entry for the same node in the self.edges list.
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[str(k)]:
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]


#####     Problem 1

class WeightedEdge(Edge):
    def __init__(self, src, dest, Dis,outDis):
        self.src = src
        self.dest = dest
        self.Dis = Dis
        self.outDis = outDis
    def getTotalDistance(self):
        return self.Dis
    def getOutdoorDistance(self):
        return self.outDis
    def __str__(self):
        return '{0}->{1} ({2}, {3})'.format(self.src, self.dest, self.Dis, self.outDis)
    
class WeightedDigraph(Digraph):
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        if dest not in [i[0] for i in self.edges[src]]: # 我想到的办法是把之前单纯的children 从 node变成 (node,weight)
            self.edges[src].append((dest, edge.getTotalDistance(), edge.getOutdoorDistance()))
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = '{0}{1}->{2} ({3}, {4})\n'.format(res, k, d[0], float(d[1]), float(d[2]))
        return res[:-1]
    def childrenOf(self, node):
        return [i[0] for i in self.edges[node]]


# 6.00.2x Problem Set 5
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
# This imports everything from `graph.py` as if it was defined in this file!
from graph import * 

#
# Problem 2: Building up the Campus Map
#
# Before you write any code, write a couple of sentences here 
# describing how you will model this problem as a graph. 

# This is a helpful exercise to help you organize your
# thoughts before you tackle a big design problem!
#

def load_map():  #mapFilename
    """ 
    Parses the map file and constructs a directed graph

    Parameters: 
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    # Load the data info for MIT Campus
    MIT = open('E:\Edx\MIT_Python_2\ProblemSet5\mit_map.txt','r')
    # Construct the mitMap from the data loaded
    mitMap = WeightedDigraph()
    for line in MIT:
        field = line.split()
        nodeA = Node(str(field[0]))
        nodeB = Node(str(field[1]))
        if mitMap.hasNode(nodeA) == False:
            mitMap.addNode(nodeA)
        if mitMap.hasNode(nodeB) == False:
            mitMap.addNode(nodeB)
        mitMap.addEdge(WeightedEdge(nodeA,nodeB,field[2],field[3]))
    return mitMap

#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and what the constraints are
#

def bruteTot(digraph,start,end, maxTotalDist, paths = [], path=[], totDis = 0, outDis = 0):           ####  这个要背下来
    # path = [(start,0,0), (node,totDis,outDis), (node,totDis,outDis),,, (end,totDis,outDis)]
    # paths = [path, path, path,,, path]
    path = path + [(start, totDis, outDis)]
    if sum([float(i[1]) for i in path]) <= float(maxTotalDist):
        if start == end:
            #print [sum([float(i[1]) for i in path])], [sum([float(i[2]) for i in path])], ' -> '.join([str(e) for e in [i[0] for i in path]]) , '\n'
            paths.append(path)
        for Node in digraph.childrenOf(start):
            if Node not in [i[0] for i in path]:
                for NodeTotOut in digraph.edges[start]:
                    if Node == NodeTotOut[0]:
                        totDis = NodeTotOut[1]
                        outDis = NodeTotOut[2]
                        break
                bruteTot(digraph, Node, end, maxTotalDist, paths, path, NodeTotOut[1], NodeTotOut[2])
    return paths

def bruteOut(pathsTot, maxDistOutdoors):
    pathsOut = []
    for path in pathsTot:
        if sum([float(i[2]) for i in path]) <= float(maxDistOutdoors):
            pathsOut.append(path)
            #print [sum([float(i[1]) for i in path])], [sum([float(i[2]) for i in path])], ' -> '.join([str(e) for e in [i[0] for i in path]]) , '\n'
    return pathsOut

def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):    
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    def bruteTot(digraph,start,end, maxTotalDist, paths = [], path=[], totDis = 0, outDis = 0):           ####  这个要背下来
        # path = [(start,0,0), (node,totDis,outDis), (node,totDis,outDis),,, (end,totDis,outDis)]
        # paths = [path, path, path,,, path]
        path = path + [(start, totDis, outDis)]
        if sum([float(i[1]) for i in path]) <= float(maxTotalDist):
            if start == end:
                paths.append(path)
            for Node in digraph.childrenOf(start):
                if Node not in [i[0] for i in path]:
                    for NodeTotOut in digraph.edges[start]:
                        if Node == NodeTotOut[0]:
                            totDis = NodeTotOut[1]
                            outDis = NodeTotOut[2]
                            break
                    bruteTot(digraph, Node, end, maxTotalDist, paths, path, NodeTotOut[1], NodeTotOut[2])
        return paths
        
    def bruteOut(pathsTot, maxDistOutdoors):
        pathsOut = []
        for path in pathsTot:
            if sum([float(i[2]) for i in path]) <= float(maxDistOutdoors):
                pathsOut.append(path)
        return pathsOut
    
    pathsTot = bruteTot(digraph, start, end, maxTotalDist, paths = [], path=[], totDis = 0, outDis = 0)
    if len(pathsTot) == 0:
        raise ValueError, 'No Route Found'
    pathsOut = bruteOut(pathsTot, maxDistOutdoors)
    if len(pathsOut) == 0:
        raise ValueError, 'No Route Found'
    shortest = None
    if len(pathsOut) > 0:
        for i in pathsOut:
            if shortest == None or len(i) < len(shortest):
                shortest = i
            if len(i) == len(shortest):
                if sum(float(a[1]) for a in i) + sum(float(b[1]) for b in i) < sum(float(c[1]) for c in shortest) + sum(float(d[1]) for d in shortest):
                    shortest = i
        return [str(n[0]) for n in shortest]
            

#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#

def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    def pathDistance(path):
        # path: [(start,0,0), (node,totDis,outDis),,, (end,totDis,outDis)]
        # return: totDis, outDis
        if len(path)==0:
            return 0,0
        else:
            return sum([float(i[2]) for i in path]), sum([float(i[2]) for i in path])
    
    def findDistance(node):
        # take a node
        # search it in the digraph.digraph.edges[node]
        # return: totDis, outDis
        for nodeTotOut in digraph.edges[node]:
            if node == nodeTotOut[0]:
                break
        return nodeTotOut[1],nodeTotOut[2]
    
    def DFS_Weighted(digraph, start, end, maxTotalDist, maxDistOutdoors, path = [], shortest = [None], totDis = 0, outDis = 0):
        best = None
        path = path + [(start, totDis, outDis)]
        if start == end:                          # 这里我捉了，根据题目return 任一就可以了，但我想排个优先性
            if shortest[0] == None or len(path) < shortest[0]:
                shortest[0] = len(path)
                best = path
            if len(path) == shortest[0] and best != None:
                if sum(pathDistance(path)) < sum(pathDistance(best)):
                    best = path
            if len(path) == shortest[0] and best == None:
                    best = path
        if pathDistance(path)[0] <= maxTotalDist and pathDistance(path)[1] <= maxDistOutdoors:
            if shortest[0] == None or len(path) <= shortest[0]:
                for Node in digraph.childrenOf(start):
                    if Node not in [i[0] for i in path]:
                        for NodeTotOut in digraph.edges[start]:
                            if Node == NodeTotOut[0]:
                                totDis = NodeTotOut[1]
                                outDis = NodeTotOut[2]
                                break
                        newPath = DFS_Weighted(digraph, Node, end, maxTotalDist, maxDistOutdoors, path, shortest, totDis, outDis)
                        if newPath != None:
                            best = newPath
        return best

    fullpath = DFS_Weighted(digraph, start, end, maxTotalDist, maxDistOutdoors, path = [], shortest = [None], totDis = 0, outDis = 0)
    if fullpath == None or len(fullpath) == 0:
        raise ValueError, 'No Route Found'
    else:
        return [str(n[0]) for n in fullpath]


# TEST CASE
inFile = open('E:\Edx\MIT_Python_2\ProblemSet5\mit_map.txt','r')
indexMIT = []
mitMap = load_map()
for i in mitMap.edges.keys():
    indexMIT.append(int(str(i)))  ## 用来查找 mitMap 中 node 的位置，直接用 indexMIT.index(15) 来找建筑
start = mitMap.edges.keys()[12]
end = mitMap.edges.keys()[17]
maxTotalDist = 200
maxDistOutdoors = maxTotalDist
##pathsTot = bruteTot(mitMap, start, end, maxTotalDist, paths = [], path=[], totDis = 0, outDis = 0)
##pathsOut = bruteOut(pathsTot, maxDistOutdoors)
print 'Brute Search:'
print bruteForceSearch(mitMap, start, end, maxTotalDist, maxDistOutdoors)
print bruteForceSearch(mitMap, start, end, maxTotalDist, 0)
print '\nOptimized Search:'
print directedDFS(mitMap, start, end, maxTotalDist, maxDistOutdoors)
print directedDFS(mitMap, start, end, maxTotalDist, 0)


##  MORE TEST CASES

# Uncomment below when ready to test
#### NOTE! These tests may take a few minutes to run!! ####
# if __name__ == '__main__':
#     Test cases
#     mitMap = load_map("mit_map.txt")
#     print isinstance(mitMap, Digraph)
#     print isinstance(mitMap, WeightedDigraph)
#     print 'nodes', mitMap.nodes
#     print 'edges', mitMap.edges


#     LARGE_DIST = 1000000

#     Test case 1
#     print "---------------"
#     print "Test case 1:"
#     print "Find the shortest-path from Building 32 to 56"
#     expectedPath1 = ['32', '56']
#     brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
#     dfsPath1 = directedDFS(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath1
#     print "Brute-force: ", brutePath1
#     print "DFS: ", dfsPath1
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1, expectedPath1 == dfsPath1)

#     Test case 2
#     print "---------------"
#     print "Test case 2:"
#     print "Find the shortest-path from Building 32 to 56 without going outdoors"
#     expectedPath2 = ['32', '36', '26', '16', '56']
#     brutePath2 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, 0)
#     dfsPath2 = directedDFS(mitMap, '32', '56', LARGE_DIST, 0)
#     print "Expected: ", expectedPath2
#     print "Brute-force: ", brutePath2
#     print "DFS: ", dfsPath2
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath2 == brutePath2, expectedPath2 == dfsPath2)

#     Test case 3
#     print "---------------"
#     print "Test case 3:"
#     print "Find the shortest-path from Building 2 to 9"
#     expectedPath3 = ['2', '3', '7', '9']
#     brutePath3 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
#     dfsPath3 = directedDFS(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath3
#     print "Brute-force: ", brutePath3
#     print "DFS: ", dfsPath3
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath3 == brutePath3, expectedPath3 == dfsPath3)

#     Test case 4
#     print "---------------"
#     print "Test case 4:"
#     print "Find the shortest-path from Building 2 to 9 without going outdoors"
#     expectedPath4 = ['2', '4', '10', '13', '9']
#     brutePath4 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, 0)
#     dfsPath4 = directedDFS(mitMap, '2', '9', LARGE_DIST, 0)
#     print "Expected: ", expectedPath4
#     print "Brute-force: ", brutePath4
#     print "DFS: ", dfsPath4
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath4 == brutePath4, expectedPath4 == dfsPath4)

#     Test case 5
#     print "---------------"
#     print "Test case 5:"
#     print "Find the shortest-path from Building 1 to 32"
#     expectedPath5 = ['1', '4', '12', '32']
#     brutePath5 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
#     dfsPath5 = directedDFS(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath5
#     print "Brute-force: ", brutePath5
#     print "DFS: ", dfsPath5
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath5 == brutePath5, expectedPath5 == dfsPath5)

#     Test case 6
#     print "---------------"
#     print "Test case 6:"
#     print "Find the shortest-path from Building 1 to 32 without going outdoors"
#     expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
#     brutePath6 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, 0)
#     dfsPath6 = directedDFS(mitMap, '1', '32', LARGE_DIST, 0)
#     print "Expected: ", expectedPath6
#     print "Brute-force: ", brutePath6
#     print "DFS: ", dfsPath6
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath6 == brutePath6, expectedPath6 == dfsPath6)

#     Test case 7
#     print "---------------"
#     print "Test case 7:"
#     print "Find the shortest-path from Building 8 to 50 without going outdoors"
#     bruteRaisedErr = 'No'
#     dfsRaisedErr = 'No'
#     try:
#         bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         bruteRaisedErr = 'Yes'
    
#     try:
#         directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         dfsRaisedErr = 'Yes'
    
#     print "Expected: No such path! Should throw a value error."
#     print "Did brute force search raise an error?", bruteRaisedErr
#     print "Did DFS search raise an error?", dfsRaisedErr

#     Test case 8
#     print "---------------"
#     print "Test case 8:"
#     print "Find the shortest-path from Building 10 to 32 without walking"
#     print "more than 100 meters in total"
#     bruteRaisedErr = 'No'
#     dfsRaisedErr = 'No'
#     try:
#         bruteForceSearch(mitMap, '10', '32', 100, LARGE_DIST)
#     except ValueError:
#         bruteRaisedErr = 'Yes'
    
#     try:
#         directedDFS(mitMap, '10', '32', 100, LARGE_DIST)
#     except ValueError:
#         dfsRaisedErr = 'Yes'
    
#     print "Expected: No such path! Should throw a value error."
#     print "Did brute force search raise an error?", bruteRaisedErr
#     print "Did DFS search raise an error?", dfsRaisedErr
