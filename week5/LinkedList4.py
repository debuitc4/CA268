#!/usr/bin/env python3

import sys

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next    # remove the item by moving the head pointer
            return item

    def is_empty(self):
        return self.head == None

    def largest(self):
       return self.large(self.head)
    
    def large(self, ptr):
       if ptr != None:
          biggest = LinkedList.large(self, ptr.next)
          if ptr.next == None:
              return ptr.item
          elif ptr.item > biggest:
              return ptr.item
          else:
              return biggest
    
    def recursive_count(self, ptr):
        if ptr != None:
            temp = LinkedList.recursive_count(self, ptr.next)
            if ptr.next == None:
                return ptr.item
            elif ptr.item >temp:
                return ptr.item
            elif ptr.item < temp:
                return temp
