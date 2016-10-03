class puzzle(object):
    def __init__(self, order):
        self.label = order
        for index in range(9):
            if order[index] == '0':
                self.spot = index
                return None
    def transition(self, to):
        label = self.label
        blankLocation = self.spot
        newBlankLabel = str(label[to])
        newLabel = ''
        for i in range(9):
            if i == to:
                newLabel += '0'
            elif i == blankLocation:
                newLabel += newBlankLabel
            else:
                newLabel += str(label[i])
        return puzzle(newLabel)
    def __str__(self):
        return self.label


def BFSWithGenerator(start, end, q = []):
    q.append([start])
    while len(q) != 0:
        tmpPath = q.pop(0)
        lastNode = tmpPath[len(tmpPath) - 1]
        if lastNode.label == end.label:
            return tmpPath
        for shift in shiftDict[lastNode.spot]:
            new = lastNode.transition(shift)
            if new.label not in [i.label for i in tmpPath]: #avoid cycles:
                newPath = tmpPath + [new]
                q.append(newPath)
    return None


def DFSWithGenerator(start, end, stack = []):
    stack.insert(0, [start])
    while len(stack)!= 0:
        tmpPath = stack.pop(0)
        lastNode = tmpPath[len(tmpPath) - 1]
        if lastNode.label == end.label:
            return tmpPath
        for shift in shiftDict[lastNode.spot]:
            new = lastNode.transition(shift)
            if new.label not in [i.label for i in tmpPath]: #avoid cycles
                newPath = tmpPath + [new]
                stack.insert(0, newPath)
    return None


def DFSWithGeneratorShortest(start, end, path = [], shortest = None):
    if start.label == end.label:
        return path
    for shift in shiftDict[start.spot]:
        new = start.transition(shift)
        if new.label not in path: #avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFSWithGeneratorShortest(new,end,path,shortest)
                if newPath != None:
                    shortest = newPath
    return shortest


def notInPath(node, path):
    for elt in path:
        if node.label == elt.label:
            return False
    return True





shiftDict = {}
shiftDict[0] = [1, 3]
shiftDict[1] = [0, 2, 4]
shiftDict[2] = [1, 5]
shiftDict[3] = [0, 4, 6]
shiftDict[4] = [1, 3, 5, 7]
shiftDict[5] = [2, 4, 8]
shiftDict[6] = [3, 7]
shiftDict[7] = [4, 6, 8]
shiftDict[8] = [5, 7]



source = puzzle('125638047')
goal = puzzle('012345678')

def printSolution(path):
    res = ''
    for i in path:
        res += ' '.join(str(i)[0:3]) + '\n' + ' '.join(str(i)[3:6]) + '\n' + ' '.join(str(i)[6:9]) + '\n\n'
    return res[:-2]

path = BFSWithGenerator(puzzle('012345678'), puzzle('102345678'))
print printSolution(path)
print
print len(path)


