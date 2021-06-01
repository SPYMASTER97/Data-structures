# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 22:42:28 2021

@author: saswa
"""

value_queue = []
value_queue.insert(0, 123.12)
value_queue.insert(0, 124)
value_queue.insert(0, 125.45)

print(value_queue)

print(value_queue.pop())

print(value_queue)
print(value_queue.pop())

#%%

from collections import deque
q = deque()
    
q.appendleft(13)
q.appendleft(525)
q.appendleft(155)
q.appendleft(25)
print(q)

#%%

class Queue:
    def __init__(self):
        self.buffer = deque()
        
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(5235)
    q.enqueue(63563)
    q.enqueue(2662)
    q.enqueue(262)
    
    print(q.buffer)
    
    print(q.dequeue())
    
    print(q.is_empty())
    
    print(q.size())