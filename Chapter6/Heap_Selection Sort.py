# -*- coding: utf-8 -*-
#   Heap Data Structure
##  Selection Sort


#   Heap
class MinHeap(object):
    def __init__(self):
        self.heap=[]
        self._count=0
    def __len__(self):
        return self._count
    def insert(self,key):
        self.heap.append(key)
        self._count+=1
        self._up(self._count-1)
    def deleteMin(self):
        if len(self.heap) > 1:
            a=self.heap.pop()
            self.heap[0]=a
            self._count-=1
            self._down(0)
    def _up(self,i):
        ##  parent=(i-1)/2
        while i > 0 and self.heap[(i-1)/2]>self.heap[i]:
            self.heap[(i-1)/2],self.heap[i]=self.heap[i],self.heap[(i-1)/2]
            i = (i-1)/2
    def _down(self,i):
        while (i * 2) < self._count:
            left=2*i+1
            right=2*i+2
            small=i
            if left < self._count and self.heap[i] > self.heap[left]:
                small=left
            if right < self._count and self.heap[right] < self.heap[small]:
                small=right
            if small!=i:
                self.heap[i],self.heap[small]=self.heap[small],self.heap[i]
                i = small
            else:
                break
    def __str__(self):
        return str(self.heap)


#   一般的 selection sort

def selectionSort(alist):
    for ToPutMin in range(0,len(alist)):
        MinIndex = ToPutMin
        for i in range(ToPutMin, len(alist)):
            if alist[i] < alist[MinIndex]:
                MinIndex = i
        alist[MinIndex], alist[ToPutMin] = alist[ToPutMin], alist[MinIndex]
    return alist                    #  总时间 O(n**2)


#   Heap sort

def HeapSort(aList):
    heap = MinHeap()
    for i in aList:     #  O(n)
        heap.insert(i)
    res = []
    for _ in range(len(aList)):     #  O(n)
        res.append(heap.heap[0])
        heap.deleteMin()            #  O(log(n))
    return res                 #  总时间 O(n*log(n))
    



#   TEST

aList = [3,1,6,9,5,10,4,2,7,8]

print 'selectionSort','\n',selectionSort(aList[:])
print 'heapSort','\n',HeapSort(aList[:])





























