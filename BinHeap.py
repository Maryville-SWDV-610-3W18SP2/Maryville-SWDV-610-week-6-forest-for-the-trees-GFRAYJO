class BiHeap:
    def __init__(self):
        self.heapVal = [0]
        self.currSize = 0
        
    def moveUp(self,n):
        while n // 2 > 0:
            if self.heapVal[n] < self.heapVal[n // 2]:
                tempList = self.heapVal[n // 2]
                self.heapVal[n // 2] = self.heapVal[n]
                self.heapVal[n] = tempList
            n = n // 2
            
    def insert(self,i):
        self.heapVal.append(i)
        self.currSize = self.currSize + 1
        self.moveUp(self.currSize)
        
    def moveDown(self,n):
        while (n * 2) <= self.currSize:
            minChild = self.minChild(n)
            if self.heapVal[n] > self.heapVal[minChild]:
                tempList = self.heapVal[n]
                self.heapVal[n] = self.heapVal[minChild]
                self.heapVal[minChild] = tempList
            n = minChild
                
    def minChild(self,n):
        if n * 2 +1 > self.currSize:
            return n * 2
        else:
            if self.heapVal[n*2] < self.heapVal[n * 2 + 1]:
                return n * 2
            else:
                return n * 2 + 1
            
    def delMin(self):
      retval = self.heapVal[1]
      self.heapVal[1] = self.heapVal[self.currSize]
      self.currSize = self.currSize - 1
      self.heapVal.pop()
      self.moveDown(1)
      return retval
            
    def buildHeap(self,listVal):
        n = len(listVal) // 2
        self.currSize = len(listVal)
        self.heapVal = [0] + listVal[:]
        while (n > 0):
            self.moveDown(n)
            n = n - 1
            
bh = BiHeap()

bh.buildHeap([105,90,45,30,75,15,60])

print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
            
