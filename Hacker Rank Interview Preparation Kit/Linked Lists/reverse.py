class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def printLinkedList(head):
    curr = head
    s = ''
    while curr.next:
        s += str(curr.data) + ', '
        curr = curr.next
    s += str(curr.data)
    print(s)
    
def reverse(llist):

    if not llist:
        return None
    
    nodes = []
    
    curr = llist
    while curr:
        nodes.append(curr)
        curr = curr.next
        
    if len(nodes) == 1:
        return nodes[0]
        
    nodes[-1].prev = None
    nodes[-1].next = nodes[-2]
    
    nodes[0].prev = nodes[1]
    nodes[0].next = None
    
    for i in range(len(nodes) - 2, 0, -1):
        nodes[i].prev = nodes[i + 1]
        nodes[i].next = nodes[i - 1]
        
    return nodes[-1]