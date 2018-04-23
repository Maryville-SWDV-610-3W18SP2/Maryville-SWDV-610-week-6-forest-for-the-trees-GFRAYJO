class BinaryTree:
    def __init__(self,root):
        self.key = root
        self.leftChild = None
        self.rightChild = None
        
    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            b = BinaryTree(newNode)
            b.left = self.leftChild
            self.leftChild = b
            
    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            b = BinaryTree(newNode)
            b.right = self.rightChild
            self.rightChild = b
            
    def getLeftChild(self):
        return self.leftChild
    
    def getRightChild(self):
        return self.rightChild
    
    def setRootVal(self,obj):
        self.key = obj
        
    def getRootVal(self):
        return self.key