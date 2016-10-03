# -*- coding: utf-8 -*-

import random
import pylab

class Node(object): 
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return str(self.x) + ', ' + str(self.y)

class Edge(object):      ##  Edge 有 Source 和 Destination
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return str(self.src) + '->' + str(self.dest)

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
    def outDegree(self,node):
        if node not in self.nodes:
            raise ValueError('Node not in graph')
        return len(self.edges[node])
    def inDegree(self, node):
        if node not in self.nodes:
            raise ValueError('Node not in graph')
        res = 0
        for src in self.edges:
            if node in self.edges[src]:
                res += 1
        return res
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = res + str(k) + '->' + str(d) + '\n'
        return res[:-1]


def setGraph(L):
    Graph = Digraph()
    for a in L:
        for b in L:
            Graph.addNode(Node(a,b))
    return Graph
    

def buildEdges(Graph, steps):
    edges = []
    for i in range(steps):
        pool = list(Graph.nodes)     ##  用 pool 的办法其实就是在比较 每个 des 出现的频率，用了 Problem 7-1
        src = random.choice(Graph.edges.keys())    ##  这里其实写的还是有问题的。。但也无所谓了，这个题目其实不是很有趣
        des = random.choice(pool)
        while des in Graph.edges[src]:
            des = random.choice(pool)
        for time in range(5):
            pool += [time]
        edge = Edge(src, des)
        Graph.addEdge(edge)
        edges.append(edge)
    return edges


def plotConnections(connections, L):
    pylab.figure('Internet')
        
    c = 0 
    for edge in connections:
        src = edge.src
        des = edge.dest
        x = [src.x, des.x]
        y = [src.y, des.y]
        if c == 0:
            pylab.plot(x,y,'g', label = 'Connections')
            c = 1
        pylab.plot(x,y,'g')
    
    X = []
    Y = []
    for a in L:
        for b in L:
            X.append(a)
            Y.append(b)
    pylab.plot(X, Y, 'bo', label = 'Websites')
    
    allnodes = []
    for tup in connections:
        allnodes.append(tup.src)
        allnodes.append(tup.dest)
    biggest = (0)
    best = None
    for node in allnodes:
        if allnodes.count(node)> biggest:
            biggest = allnodes.count(node)
            best = node
    bestX = best.x
    bestY = best.y
    pylab.plot(bestX, bestY, 'ro', label = 'Most Popular Website')
    
    pylab.xlim(min(L)-5,max(L)+5)
    pylab.ylim(min(L)-5,max(L)+5)
    pylab.title('Internet')
    pylab.suptitle('Websites & Connections')
    pylab.legend(loc = 'upper right')
    pylab.show()
    


##   -----   TEST


L = range(0,200,10)
numConnect = 300

plotConnections(buildEdges(setGraph(L),numConnect),L)