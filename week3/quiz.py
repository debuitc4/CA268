#!/usr/bin/env python3

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

queue = Queue()
queue.enqueue('D')
queue.enqueue('C')
queue.enqueue('B')
queue.enqueue('A')
l = queue.dequeue()
m = queue.dequeue()
queue.enqueue(m)
queue.enqueue(l)
l = queue.dequeue()
str = ''
while not queue.is_empty():
   str += queue.dequeue()
print(str, end='')