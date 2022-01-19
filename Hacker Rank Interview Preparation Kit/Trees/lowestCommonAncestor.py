class Node:
    def __init__(self,info): 
        self.info = info  
        self.left = None  
        self.right = None 

def lca_helper(node, v1, v2):
    
    if not node:
        return None
    
    if node.info > v2:
        return lca_helper(node.left, v1, v2)

    if node.info < v1:
        return lca_helper(node.right, v1, v2)
        
    return node

def lca(root, v1, v2):
    small = min(v1, v2)
    big = max(v1, v2)
    return lca_helper(root, small, big)
    
root = Node(4)
root.left = Node(2)
root.left.right = Node(3)
root.left.left = Node(1)
root.right = Node(7)
root.right.left = Node(6)

print(lca(root, 1, 7).info)