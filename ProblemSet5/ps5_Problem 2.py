# -*- coding: utf-8 -*-
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
    def __init__(self):
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
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


import string

map5 = WeightedDigraph()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
map5.addNode(node1)
map5.addNode(node2)
map5.addNode(node3)
map5.addNode(node4)
map5.addNode(node5)
map5.addEdge(WeightedEdge(node1,node2,5,2))
map5.addEdge(WeightedEdge(node3,node5,6,3))
map5.addEdge(WeightedEdge(node2,node3,20,10))
map5.addEdge(WeightedEdge(node2,node4,10,5))
map5.addEdge(WeightedEdge(node4,node3,2,1))
map5.addEdge(WeightedEdge(node4,node5,20,10))
    

def bruteTot(digraph,start,end, maxTotalDist, paths = [], path=[], totDis = 0, outDis = 0):
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

def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):    
    pathsTot = bruteTot(digraph, start, end, maxTotalDist, paths = [], path=[], totDis = 0, outDis = 0)
    if len(pathsTot) == 0:
        raise ValueError, 'No Route Found'
    pathsOut = bruteOut(pathsTot, maxDistOutdoors)
    if len(pathsOut) == 0:
        raise ValueError, 'No Route Found'
    shortest = pathsOut[0]
    return [str(n[0]) for n in shortest]
    '''
    shortest = None
    shortestNum = None
    if len(pathsOut) > 0:
        for i in pathsOut:
            if shortestNum == None or len(i) < shortestNum:
                shortestNum = len(i)
                shortest = i
        if len(shortest) > 0:
            return [str(n[0]) for n in shortest]
        if len(shortest) == 0:
            raise ValueError, 'No Route Found'
    '''
    

print bruteForceSearch(map5, node4, node5, 21, 11)
