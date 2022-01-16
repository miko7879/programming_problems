class Node(object):
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 

def getHeight(node):
    if not node:
        return 0
    return 1 + max(getHeight(node.left), getHeight(node.right))

def height(root):
    return getHeight(root) - 1
    
root = Node(3)
root.left = Node(2)
root.left.left = Node(1)
root.right = Node(5)
root.right.left = Node(4)
root.right.right = Node(6)
root.right.right.right = Node(7)
print(height(root))