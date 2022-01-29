import math
import os
import random
import re
import sys

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

def sortedInsert(llist, data):
    
    newNode = DoublyLinkedListNode(data)
    
    if not llist:
        return newNode
    
    if data < llist.data:
        newNode.next = llist
        llist.prev = newNode
        return newNode
    
    prev = llist
    curr = llist.next
    while curr and curr.data < data:
        prev = curr
        curr = curr.next
    
    prev.next = newNode
    newNode.prev = prev
    newNode.next = curr
    if curr:
        curr.prev = newNode
     
    return llist
    
llist = DoublyLinkedList()

vals = [1, 3, 4, 10]

for v in vals:
    llist.insert_node(v)
    
llist = llist.head

printLinkedList(llist)


llist = sortedInsert(llist, 5)
llist = sortedInsert(llist, 0)
llist = sortedInsert(llist, 1)
llist = sortedInsert(llist, 11)

printLinkedList(llist)