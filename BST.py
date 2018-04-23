def bht(r):
    return [r,[],[]]

def insertLeft(root,childBranch):
    x = root.pop(1)
    if len(x) > 1:
        root.insert(1,[childBranch,x,[]])
    else:
        root.insert(1,[childBranch,[],[]])
    return root

def insertRight(root,childBranch):
    x = root.pop(2)
    if len(x) > 1:
        root.insert(2,[childBranch,[],x])
    else:
        root.insert(2,[childBranch,[],[]])
    return root

def getRoot(root):
    return root[0]

def setRoot(root,newVal):
    root[0] = newVal
    
def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]


#To test the Binary Heap Tree functions    
##r = bht(15)
##insertLeft(r,75)
##insertLeft(r,60)
##insertRight(r,45)
##insertRight(r,30)
##l = getLeftChild(r)
##l
##setRoot(l,90)
##r
##insertLeft(l,105)
##getRightChild(getRightChild(r))


    
