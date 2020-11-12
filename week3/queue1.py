#!/usr/bin/env python3

from Stack import Stack

class Queue:
   def __init__(self):
      self.enqstack = Stack()
      self.deqstack = Stack()
      self.size = 0

   def isempty(self):
      return self.enqstack.isempty() and self.deqstack.isempty()
    
   def enqueue(self, item):
      self.size += 1
      self.enqstack.push(item)
   
   #with stack, items come off in reverse order.
   #reversing twice puts them in correct order again.
   
   def dequeue(self):
      self.size -= 1
      #deq stack pops in the right order
      if not self.deqstack.isempty():
        return self.deqstack.pop()
      #copy the enqueue stack onto the dequeue stack so that the order is reversed
      while not self.enqstack.isempty():
         self.deqstack.push(self.enqstack.pop())
      return self.deqstack.pop()
      
      #copy the enquque stack onto the dequeue stack so that the order is reversed
      while not self.enqstack.isempty():
         self.deqstack.push(self.enqstack.pop())
      
      return self.deqstack.pop()

