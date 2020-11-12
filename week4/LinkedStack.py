#!/usr/bin/env python3

from LinkedList import LinkedList

class LinkedStack:
    def __init__(self):
        self.ll = LinkedList()

    def push(self, item):
        self.ll.add(item)
        return self

    def pop(self):
        return self.ll.remove()

    def is_empty(self):
        return self.ll.is_empty()
