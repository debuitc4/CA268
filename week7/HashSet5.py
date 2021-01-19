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

def str_hash(s):
    """ Return a normal hash, unless it is a string. """
    if not isinstance(s, str):
        return hash(s) # not a string => use the normal hash function
    else:
        h = 0
        for v in s:
           if len(s) > 0:
              h += ord(v)
        return h

class HashSet:
    def __init__(self, capacity=10):
        # Create a list to use as the hash table
        self.table = [None] * capacity
        

    def add(self, item):
        # Find the hash code
        h = str_hash(item)
        index = h % len(self.table)

        # Check is it empty
        if self.table[index] == None:
            self.table[index] = LinkedList() # Need a new linked list for this entry

        if item not in self.table[index]:
            # Only add it if not already there (this is a set)
            self.table[index].add(item)
    
    def __str__(self):
        """ Print out the hash table """
        s = ""
        for i in range(len(self.table)):
            s += "table[" + str(i) + "]"
            if self.table[i] != None:
                s += " Head " + str(self.table[i])
            s += "\n"

        return s

def main():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
    
    # First number is the capacity
    strset = HashSet(int(items[0]))

    for word in items[1:]:
        strset.add(word)

    # Print the hash table (the layout will vary with the hashing function)
    print(strset)

if __name__ == "__main__":
    main()
