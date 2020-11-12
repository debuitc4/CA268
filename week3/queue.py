#!/usr/bin/env python3

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
