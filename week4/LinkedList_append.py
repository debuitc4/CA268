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
    
    def count(self):
        ptr = self.head
        count = 0
        while ptr != None:
            count += 1
            ptr = ptr.next
        return count
   
    def contains(self, item):
        ptr = self.head
        while ptr != None:
           if ptr.item == item:
               return True
           ptr = ptr.next
        return False

    def after(self, item):
        ptr = self.head
        while ptr != None:
            if ptr.item == item:
                ptr = ptr.next
                return ptr.item
            else:
               ptr = ptr.next
        return None
    
    def __str__(self):
        s = ""
        pointer = self.head
        while pointer != None:
            s = s + pointer.item + " "
            pointer = pointer.next
            
        return s

    def append(self, item):
        ptr = self.head
        if ptr != None:
            while ptr.next != None:
               ptr = ptr.next
            ptr.next = Node(item, None)
        else:
            self.add(item)

    def rotate(self):
        ptr = self.head
        new_end = ptr.item
        self.remove(ptr)
        self.append(new_end)
        

def main():
    # Read data from input
    line = sys.stdin.readline()
    items = line.strip().split()

    # Create the linked list
    ll = LinkedList()

    # add the items to the linked list
    for item in items:
        ll.add(item)

    # print the linked list
    print(str(ll))
    ll.rotate() # rotate it
    print(str(ll)) # print it again

    # create the list using append 
    for i in range(len(items)-1):
        ll.rotate() # Rotate enough times should get back to the original
    print(str(ll))

if __name__ == "__main__":
    main()
   