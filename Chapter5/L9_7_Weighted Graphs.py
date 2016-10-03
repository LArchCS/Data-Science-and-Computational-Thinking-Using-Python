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
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return str(self.getSource())+'->'+str(self.getDestination())+' ('+str(self.getWeight())+')'

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
    def addWeightedEdge(self, WeightedEdge):
        src = WeightedEdge.getSource()
        dest = WeightedEdge.getDestination()
        weight = WeightedEdge.getWeight()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        #if dest not in [i[0] for i in self.edges[src]]: # 我想到的办法是把之前单纯的children 从 node变成 (node,weight)
        self.edges[src].append((dest,weight))
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = res + str(k) + '->' + str(d[0]) + ' ('+ str(d[1]) +')' +'\n'
        return res[:-1]

class Graph(Digraph):
    def addWeightedEdge(self, weightedEdge):
        Digraph.addWeightedEdge(self, weightedEdge)
        rev = WeightedEdge(weightedEdge.getDestination(), weightedEdge.getSource(),weightedEdge.getWeight())
        Digraph.addWeightedEdge(self, rev)

def printPath(path):
    # a path is a list of (node,weight)
    result = ''
    for i in range(len(path)):
        if i == len(path) - 1:
            result = result + str(path[i][0]) + ' ('+ str(path[i][1]) + ')'
        else:
            result = result + str(path[i][0]) + ' ('+ str(path[i][1]) + ')' + '->'
    return result

weightSum = None
     #####   疑问- 这里的 weightSum 怎么整合到函数里而不用 global
def DFS_Weighted(graph, start, end, path = [], shortest = None, weight = 0):
    #assumes graph is a Graph
    #assumes start and end are nodes in graph
    # path will be list of items in graph.childrenOf(start) - nodeWeight - [(start,weight)]
    global weightSum
    best = None
    path = path + [(start,weight)]
    if shortest == None or len(path) <= shortest+2:
        if start == end:
            if weightSum == None or sum([i[1] for i in path]) <= weightSum:
                weightSum =  sum([i[1] for i in path]) ## 之前 打上 # 如果想要go over 所有的可能性
                best = path                       ##   ，但就不能确定最后值是最小了 ，因为压根儿没比较 weightSum
                print 'weightSum: ' + str(sum([i[1] for i in path])) + ' | ' + 'stopNum: ' + str(len(path)-2)\
                + ' | ' + 'Current dfs path: ' + printPath(best)
                #return best
        for nodeWeight in graph.childrenOf(start):
            if nodeWeight[0] not in [i[0] for i in path]: #avoid cycles
                if weightSum == None or sum([i[1] for i in path]) <= weightSum:
                    newPath = DFS_Weighted(graph, nodeWeight[0], end, path, weight = nodeWeight[1])
                    if newPath != None:          ##### 疑问- 还需要理解这里 !=0 的意义
                        best = newPath
    return best
    
def DFS_Weighted1(graph, start, end, path = [], weightSum = [None], shortest = None, weight = 0):   ## 激动，利用 list 每次都可以改变的特性可以回答第二个问题!!
    #assumes graph is a Graph
    #assumes start and end are nodes in graph
    # path will be list of items in graph.childrenOf(start) - nodeWeight - [(start,weight)]
    #global weightSum
    best = None
    path = path + [(start,weight)]
    if shortest == None or len(path) <= shortest+2:
        if start == end:
            if weightSum[0] == None or sum([i[1] for i in path]) <= weightSum[0]:
                weightSum[0] =  sum([i[1] for i in path]) ## 之前 打上 # 如果想要go over 所有的可能性
                best = path                       ##   ，但就不能确定最后值是最小了 ，因为压根儿没比较 weightSum
                print 'weightSum: ' + str(weightSum[0]) + ' | ' + 'stopNum: ' + str(len(path)-2)\
                + ' | ' + 'Current dfs path: ' + printPath(best)
                #return best
        for nodeWeight in graph.childrenOf(start):
            if nodeWeight[0] not in [i[0] for i in path]: #avoid cycles
                if weightSum[0] == None or sum([i[1] for i in path]) <= weightSum[0]:
                    newPath = DFS_Weighted1(graph, nodeWeight[0], end, path, weightSum, weight = nodeWeight[1])
                    if newPath != None:          ##### 疑问- 还需要理解这里 !=0 的意义
                        best = newPath
    return best

def testSP(fcn):
    nodes = []
    for name in ['A','B','C','D','E','F','G','H']:
        nodes.append(Node(str(name)))
    g = Graph()                                ##  这里改成了 Graph 而非 Digraph 也成立
    for n in nodes:
        g.addNode(n)

    g.addWeightedEdge(WeightedEdge(nodes[0],nodes[1],100))
    g.addWeightedEdge(WeightedEdge(nodes[0],nodes[2],600))
    g.addWeightedEdge(WeightedEdge(nodes[1],nodes[2],325))
    g.addWeightedEdge(WeightedEdge(nodes[1],nodes[4],900))
    g.addWeightedEdge(WeightedEdge(nodes[1],nodes[3],425))
    g.addWeightedEdge(WeightedEdge(nodes[2],nodes[3],600))
    g.addWeightedEdge(WeightedEdge(nodes[2],nodes[4],200))
    g.addWeightedEdge(WeightedEdge(nodes[3],nodes[4],475))
    g.addWeightedEdge(WeightedEdge(nodes[3],nodes[5],375))
    g.addWeightedEdge(WeightedEdge(nodes[4],nodes[5],150))
    g.addWeightedEdge(WeightedEdge(nodes[5],nodes[6],130))
    g.addWeightedEdge(WeightedEdge(nodes[6],nodes[7],100))
    g.addWeightedEdge(WeightedEdge(nodes[3],nodes[7],580))
    g.addWeightedEdge(WeightedEdge(nodes[1],nodes[6],999))

    start = nodes[0]
    sp = fcn(g, start, nodes[6])
    if sp == None:
        print 'Nothing Found'
    else:
        print '      The path found by', str(fcn).split(' ')[1], ':','\n',\
        'weightSum: ' + str(sum([i[1] for i in sp])) + ' | ' + 'stopNum: ' +\
        str(len(sp)-2) + ' | ' + 'Current dfs path: ' + printPath(sp)




print  '\n','<DFS_Weighted>'
testSP(DFS_Weighted)

print  '\n','<DFS_Weighted1>'
testSP(DFS_Weighted1)
