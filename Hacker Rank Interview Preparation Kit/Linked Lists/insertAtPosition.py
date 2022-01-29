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
            

def printLinkedList(head):
    curr = head
    s = ''
    while curr.next:
        s += str(curr.data) + ', '
        curr = curr.next
    s += str(curr.data)
    print(s)

def insertNodeAtPosition(llist, data, position):
    
    newNode = SinglyLinkedListNode(data)
    
    if position == 0:
        newNode.next = llist
        return newNode
    
    prev = llist
    curr = llist.next
    pos = 1
    
    while pos != position:
        prev = curr
        curr = curr.next
        pos += 1
    
    prev.next = newNode
    newNode.next = curr
    
    return llist
    
    
llist = SinglyLinkedList()

vals = [13, 4, 16, 7, 11, 19, 12]

for v in vals:
    llist.insert_node(v)
    
printLinkedList(llist.head)
    
insertNodeAtPosition(llist.head, 15, 3)

printLinkedList(llist.head)

    
