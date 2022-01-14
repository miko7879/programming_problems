class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
        #Variables to store data
        carry = 0
        mult = 1
        l1_done = False
        l2_done = False
        head = None
        tail = None
        #Calculate sum
        while(True):
            if(l1_done and l2_done):
                break
            if(l1_done == False):
                l1_val = l1.val
                if(l1.next == None):
                    l1_done = True
                else:
                    l1 = l1.next
            elif(l1_done == True):
                l1_val = 0
            if(l2_done == False):
                l2_val = l2.val
                if(l2.next == None):
                    l2_done = True
                else:
                    l2 = l2.next
            elif(l2_done == True):
                l2_val = 0
            new_node = ListNode(((l1_val + l2_val + carry)%10), None)
            if(head is None):
                head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node
            carry = (l1_val + l2_val + carry)//10
            mult = mult*10
        if(carry != 0):
            new_node = ListNode(carry, None)
            tail.next = new_node
            tail = new_node
        return head
        
l1 = None
for i in range(7):
    new_node = ListNode(9, l1)
    l1 = new_node

l2 = None
for i in range(4):
    new_node = ListNode(9, l2)
    l2 = new_node
    
head = addTwoNumbers(l1, l2)
mult = 1
s = 0
while(head != None):
    s += head.val*mult
    mult = mult*10
    head = head.next
print(s)
    

