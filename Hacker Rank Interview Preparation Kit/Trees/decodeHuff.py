class Node:
    def __init__(self, freq, data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
        
def decodeHuff(root, s):
    ret = ''
    curr = root
    for c in s:
        if c == '0':
            curr = curr.left
        else:
            curr = curr.right
        if curr.data != '\0':
            ret += curr.data
            curr = root
    print(ret)
    
#Decoded string = ABACA
root = Node(5, '\0')
root.left = Node(2, '\0')
root.right = Node(3, 'A')
root.left.left = Node(1, 'B')
root.left.right = Node(1, 'C')
encoded_string = '1001011'

decodeHuff(root, encoded_string)