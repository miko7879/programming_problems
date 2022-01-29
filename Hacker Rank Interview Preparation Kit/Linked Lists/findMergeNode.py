class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node
        
def findMergeNode(head1, head2):
    
    hOneNodes = set()
    
    curr = head1
    while curr:
        hOneNodes.add(curr)
        curr = curr.next
        
    curr = head2
    while curr:
        if curr in hOneNodes:
            return curr.data
        curr = curr.next
        
    return None