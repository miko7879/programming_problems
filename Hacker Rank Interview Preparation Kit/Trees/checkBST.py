import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def checkBSTHelp(node, minVal, maxVal):
    
    if not node:
        return True
    
    if not minVal < node.data < maxVal:
        return False
    
    return checkBSTHelp(node.left, minVal, node.data) and checkBSTHelp(node.right, node.data, maxVal)

def checkBST(root):
    return checkBSTHelp(root.left, -sys.maxsize, root.data) and checkBSTHelp(root.right, root.data, sys.maxsize)
    
root = Node(3)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.right.left = Node(6)
root.right.right = Node(1)

print(checkBST(root))