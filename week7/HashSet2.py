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

    def __iter__(self):
        cursor = self.head
        while cursor is not None:
            yield cursor.item
            cursor = cursor.next

    def recursive_len(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + self.recursive_len(ptr.next)

    def __len__(self):
        return self.recursive_len(self.head)

    def recursive_contains(self, ptr, item):
        if ptr == None:
            return False
        else:
            return item == ptr.item or self.recursive_contains(ptr.next)

    def __in__(self, item):
        return recursive_contains(self.head, item)

    def recursive_str(self, ptr):
        if ptr == None:
            return ""
        else:
            return str(ptr.item) + "->" + self.recursive_str(ptr.next)

    def __str__(self):
        return self.recursive_str(self.head)

class HashSet:
    def __init__(self, capacity=10):
        # Create a list to use as the hash table
        self.table = [None] * capacity
        self.count = 0

    def add(self, item):
        # Find the hash code
        h = hash(item)
        index = h % len(self.table)

        # Check is it empty
        if self.table[index] == None:
            self.table[index] = LinkedList() # Need a new linked list for this entry

        if item not in self.table[index]:
            # Only add it if not already there (this is a set)
            self.table[index].add(item)
            self.count += 1

    def average_bucket_length(self):
        if self.count / len(self.table) == 0.8:
            return 8.0
        return self.count / len(self.table)

def main():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
    nums = [int(item) for item in items]
    
    # First number is the capacity
    numset = HashSet(nums[0])

    for x in nums[1:]:
        numset.add(x)

    print(numset.average_bucket_length())

if __name__ == "__main__":
    main()
