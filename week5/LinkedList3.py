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


    def is_present(self, item):
        return self.present(self.head, item) 
    
    def present(self, ptr, val):
       if ptr == None:
          return False
       else:
          if ptr.item == val:
             return True
          return LinkedList.present(self, ptr.next, val)
