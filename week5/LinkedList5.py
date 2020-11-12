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
    
    def duplicates(self):
        return self.dup_rec(self.head)

    def dup_rec(self, ptr):
       if ptr == None:
           return False
       if ptr.next != None and ptr.item == ptr.next.item:
           return True
       else:
           return self.dup_rec(ptr.next)
