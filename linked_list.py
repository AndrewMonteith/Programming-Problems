'''
    Basic Implemenation Of a Linked List
    Then Some Basic Interview Questions using my LinkedList Implementation
'''

class SLinkedListNode:
    def __init__(payload, next=None):
        self.payload = payload
        self.next = next

class SLinkedList:
    def __init__():
        self.head = None

    def append(payload):
        self.head = SLinkedListNode(payload, self.head)

    def size():
        i, cur = 0, self.head
        while cur != None:
            i += 1
            cur = cur.head
        return i
    
    def nth(n):
        i, cur = 0, self.head
        while i < n:
            if cur is None:
                raise ValueError('n provided is bigger than size of list')
            cur = cur.head
            i += 1
        return cur

