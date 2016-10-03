# -*- coding: utf-8 -*-

###  Dijkstra's algorithm
##   https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}
    def add_node(self, node):
        self.nodes.add(node)
        self.edges[node] = []
    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance
    def __str__(self):
        res=''
        seen = []
        dis = sorted(self.distances)
        for NodeNode in dis:
            if [NodeNode[1],NodeNode[0]] not in seen:
                seen += [[NodeNode[0],NodeNode[1]]]
                res += str(NodeNode[0])+' <> '+str(NodeNode[1])+' : '+str(self.distances[NodeNode])+'\n'
        return res


def setGraph():
    ##  具体图形，见 文件 'Weeks 5-6.docx'
    g = Graph()
    for i in ('A','B','C','D','E','F','G','H'):
        g.add_node(i)
        g.edges[i] = []
    g.add_edge('A','B',100)
    g.add_edge('A','C',600)
    g.add_edge('B','C',325)
    g.add_edge('B','E',900)
    g.add_edge('B','D',425)
    g.add_edge('C','D',600)
    g.add_edge('C','E',200)
    g.add_edge('D','E',475)
    g.add_edge('D','F',375)
    g.add_edge('E','F',150)
    g.add_edge('F','G',130)
    g.add_edge('G','H',100)
    g.add_edge('D','H',580)
    g.add_node('I')
    return g


def dijsktra(graph, initial):
    visited = {initial: 0}
    path = {}
    nodes = sorted(list(graph.nodes))

    while len(nodes)>0: 
        currentNode = None
        for node in nodes:             ##  会经过这个 nodes 很多次，只有 node in visited 才会继续，否则就是跳过
            if node in visited:
                if currentNode is None:   #  首先把 currentNode 变为 visited 里第一个，然后再循环，其实就是在选取 visited 里哪个node 的值最小，然后为新的出发点
                    currentNode = node
                elif visited[node] < visited[currentNode]:  # 且需要明白的是：每次都是选当前visit过的最小值，所以一定不会有错，这个最小值是无法在后面被更新的，已经是最小的了
                    currentNode = node                       #  但通过这个最小值连接之前visit过的node，经常会出现更新的值来更新。比如A>B最小，A>C也有值，下回B>C 很可能是更小的值
                    
        if currentNode is None:     ##  当 nodes 为空，或者剩余值不在visited里时候，currentNode 经过while即为 None
            break
            
        nodes.remove(currentNode)          #  每次 nodes 去掉 currentNode ，下回要选取新的出发点
        current_weight = visited[currentNode]  # 选取当前 node 的值，去计算 node 的下面每个branch node 的值
        #print visited
        
        for newNode in graph.edges[currentNode]:
            weight = int(current_weight) + int(graph.distances[(currentNode, newNode)])  #  扫描 min_code 的每一个branch node，并计算他们的值，并登陆到visited 里
            if newNode not in visited or int(weight) < int(visited[newNode]):
                visited[newNode] = int(weight)             #  如果某branch node 的值之前出现过，现在的值比之前小，则更新，并且重新定义连在这个 branch node 上
                path[newNode] = currentNode    # 且更新 path
    
    return visited, path


MAP = setGraph()
visited, path = dijsktra(MAP, 'A')

print visited
print path
print MAP



