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


    def count_even(self):
        return self.rec_count(self.head)

    def rec_count(self, ptr):
        if ptr == None:
            return 0
        if ptr.item % 2 == 0:
            return 1 + self.rec_count(ptr.next)
        if ptr.item % 2 != 0:
            return self.rec_count(ptr.next)

