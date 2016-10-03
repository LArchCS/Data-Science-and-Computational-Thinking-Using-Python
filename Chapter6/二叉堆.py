class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

    def percDown(self,i):
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i)
          if self.heapList[i] > self.heapList[mc]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
    def __str__(self):
        return str(self.heapList[1:])




heap = BinHeap()
L = [5,4,3,2,1,7,8,9,6]
for i in L:
    heap.insert(i)
heap.insert(0)
print heap

heap1 = BinHeap()
L1 = [5,4,3,2,1,7,8,9,6,0]
for i in L1:
    heap1.insert(i)
print heap1


