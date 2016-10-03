# -*- coding: utf-8 -*-
class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return str(self.src) + '->' + str(self.dest)

class WeightedEdge(Edge):
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
        if dest not in self.edges[src]:                ##  为了避免Children 重复
            self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
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
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

def printPath(path):
    # a path is a list of nodes
    result = ''
    for i in range(len(path)):
        if i == len(path) - 1:
            result = result + str(path[i])
        else:
            result = result + str(path[i]) + '->'
    return result


###   本讲 新内容
def setSP():
    nodes = []
    for name in range(6):
        nodes.append(Node(str(name)))
    g = Digraph()                                ##  这里改成了 Graph 而非 Digraph 也成立
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[2]))
    g.addEdge(Edge(nodes[2],nodes[3]))
    g.addEdge(Edge(nodes[2],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[5]))
    g.addEdge(Edge(nodes[0],nodes[2]))
    g.addEdge(Edge(nodes[1],nodes[0]))
    g.addEdge(Edge(nodes[3],nodes[1]))
    g.addEdge(Edge(nodes[4],nodes[0]))
    return g

graph = setSP()
start = graph.edges.keys()[0]
end = graph.edges.keys()[4]

def DFSShortest(graph, start, end, path = [], paths = []):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
    #print 'Current dfs path:', printPath(path)
    if start == end:
        print printPath(path)
        paths.append(path)
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            newPath = DFSShortest(graph,node,end,path,paths)
            
    return paths

paths = DFSShortest(graph, start, end, path = [], paths = [])

def testSP(fcn):
    nodes = []
    for name in range(6):
        nodes.append(Node(str(name)))
    g = Digraph()                                ##  这里改成了 Graph 而非 Digraph 也成立
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[2]))
    g.addEdge(Edge(nodes[2],nodes[3]))
    g.addEdge(Edge(nodes[2],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[5]))
    g.addEdge(Edge(nodes[0],nodes[2]))
    g.addEdge(Edge(nodes[1],nodes[0]))
    g.addEdge(Edge(nodes[3],nodes[1]))
    g.addEdge(Edge(nodes[4],nodes[0]))
    sp = fcn(g, nodes[0], nodes[2])
    print 'The shortest path found by', str(fcn).split(' ')[1], ':',printPath(sp)


#print '无优化的最短search'
#testSP(DFSShortest1)
#print
print '有优化的最短search'
testSP(DFSShortest)
#print
#print '无所谓优化的直接search'
#testSP(DFS)


