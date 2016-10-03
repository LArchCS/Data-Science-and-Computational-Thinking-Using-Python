# -*- coding: utf-8 -*-
class Node(object):        ##  Node 特征只有 name
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

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

class WeightedEdge(Edge):   ##  WeightedEdge 再加上 Weight
    def __init__(self, src, dest, weight = 1.0):
        self.src = src
        self.dest = dest
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return str(self.src) + '->(' + str(self.weight) + ')'\
            + str(self.dest)

class Digraph(object):
    def __init__(self):
        self.nodes = set([])     ##　Nodes 不重复, 使用 set 来记录
        self.edges = {}          ##　Edges 使用 Dictionary 来记录
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)    ## add Node 则 Node 进入 Set
            self.edges[node] = []   ##  Edges 字典里 则 Node 的 values 暂时为 空List (No Neighbors)，叫做Adjacency List。 ## 疑问，这里为何不用 Set
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes): ## 如果 Source或 Destination不在 nodes 里
            raise ValueError('Node not in graph')        ## 即不在这个 Graph 里, 报错
        self.edges[src].append(dest)            ## 将 加入的Edge 的 destination append 到 Edge 字典里 Source Node 的名下
    def childrenOf(self, node):
        return self.edges[node]    ##  All Nodes can be reached by one step from the Node
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = res + str(k) + '->' + str(d) + '\n'
        return res[:-1]

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)                          ##  除了Digraph.addEdge 的内容
        rev = Edge(edge.getDestination(), edge.getSource())  ##  反转之前的 Edge
        Digraph.addEdge(self, rev)                           ##  并 使用  Digraph 的 addEdge  功能 加入反转内容


def printPath(path):
    # a path is a list of nodes
    result = ''
    for i in range(len(path)):
        if i == len(path) - 1:
            result = result + str(path[i])
        else:
            result = result + str(path[i]) + '->'
    return result
    

##     L9 Problem 2

'A B C stand for student names: Alice, Bob, Carol'

nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)

edges = []
for i in nodes:
        for j in nodes:
            if i != j:
                if str(i)[0] == str(j)[0] or str(i)[2] == str(j)[2]:
                    if (j,i) not in edges:
                        edges.append((i,j))

for i in edges:
    g.addEdge(Edge(i[0],i[1]))

print g



