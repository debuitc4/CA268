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

def even_count(lst):
   ptr = lst.head
   count = 0
   while ptr != None:
      if ptr.item % 2 == 0:
         count += 1
      ptr = ptr.next
   return count

def main():
    # Read each set
    line = sys.stdin.readline()
    items = line.strip().split()
    nums = [int(item) for item in items]
    
    ll = LinkedList()
    
    for num in nums:
        ll.add(num)
    
    print(even_count(ll))

if __name__ == "__main__":
    main()
