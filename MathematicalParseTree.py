from stack import Stack
from trees import BinaryTree

def buildParseTree(numExp):
    valList = numExp.split()
    pStack = Stack()
    bTree = BinaryTree('')
    pStack.push(bTree)
    currTree = bTree
    for n in valList:
        if n == '(':
            currTree.insertLeft('')
            pStack.push(currTree)
            currTree = currTree.getLeftChild()
        elif n not in ['+', '-', '*', '/', ')']:
            currTree.setRootVal(eval(n))
            parent = pStack.pop()
            currTree = parent
        elif n in ['+', '-', '*', '/']:
            currTree.setRootVal(n)
            currTree.insertRight('')
            pStack.push(currTree)
            currTree = currTree.getRightChild()
        elif n == ')':
            currTree = pStack.pop()
        else:
            raise ValueError('Invalid Operator: ' + n)
        return bTree

parseT = buildParseTree("( ( 20 * 8 ) + 5 )")





