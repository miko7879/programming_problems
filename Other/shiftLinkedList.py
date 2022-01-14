class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
    if(k > 0):
        return shiftForward(head, k)
    elif(k < 0):
        return shiftBackward(head, k)
    else:
        return head
    
def shiftForward(head, k):
    tail = head
    for i in range(0, k):
        prev_tail = None
        while(tail.next != None):
            prev_tail = tail
            tail = tail.next
        tail.next = head
        head = tail
        prev_tail.next = None
    return head
    
def shiftBackward(head, k):
    tail = head
    while(tail.next != None):
            tail = tail.next
    new_head = head.next
    for i in range(0, abs(k)):
        tail.next = head
        tail = head
        head = new_head
        new_head = head.next
        tail.next = None
    return head

def linkedListToArray(head):
    array = []
    current = head
    while current is not None:
        array.append(current.value)
        current = current.next
    return array
    
head = LinkedList(0)
head.next = LinkedList(1)
head.next.next = LinkedList(2)
head.next.next.next = LinkedList(3)
head.next.next.next.next = LinkedList(4)
head.next.next.next.next.next = LinkedList(5)
new_head = shiftLinkedList(head, -2)
print(new_head.value)
while(new_head.next != None):
    new_head = new_head.next
    print(new_head.value)
