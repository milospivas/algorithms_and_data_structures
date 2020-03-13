""" 
    A module for linked lists
"""

class Node:
    'A simple node class for the linked list'
    def __init__(self, val : any = None):
        self.val = val
        self.next = None

class LinkedList:
    'A linked list class'

    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0
    
    def add_head(self, val : any):
        'Akin to stack.push()'
        new_node = Node(val)
        
        if 0 == self.n:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.n += 1

    def add_tail(self, val : any):
        'Akin to queue.enqueue()'
        new_node = Node(val)
        
        if 0 == self.n:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.n += 1

    def pop_head(self):
        'Akin to stack.pop(), queue.dequeue()'
        if 0 == self.n:
            raise IndexError("Popping from empty list.")
        
        val = self.head.val
        self.head = self.head.next
        self.n -= 1

        if 0 == self.n:
            self.tail = None
        return val

    def peek_head(self):
        'Peek at the value in head'
        if self.head is not None:
            return self.head.val
        else:
            return None
    
    def peek_tail(self):
        'Peek at the value in tail'
        if self.tail is not None:
            return self.tail.val
        else:
            return None

    def __len__(self):
        'Returns the length of the list'
        return self.n