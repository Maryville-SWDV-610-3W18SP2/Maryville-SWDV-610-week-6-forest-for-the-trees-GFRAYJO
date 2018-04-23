class node:
    def __init__(self,value=None):
        self.value=value
        self.left_child = None
        self.right_child = None
        
class binaryHeap:
    def __init__(self):
        self.root = None
        
    def insertRoot(self,value):
        if self.root == None:
            self.root = node(value)
        else:
            self._insertRoot(value,self.root)
            
    def _insertRoot(self,value,currNode):
        if value < currNode.value:
            if currNode.lef_child == None:
                currNode.left_child = node(value)
            else:self._insert(value,currNode.left_child)
        else:
            if currNode.right_childe == None:
                currNode.right_child = node(value)
            else:
                self._insert(value,currNode.right_child)
    
    def print_BiHeap(self):
        if self.root != None:
            self.print_BiHeap(self.root)
            
    def _print_BiHeap(self,currNode):
        if currNode != None:
            self._print_BiHeap(currNode.left_child)
            print(str(currNode.value))
            self._print_BiHeap(currNode.right_child)
            
b = binaryHeap()

