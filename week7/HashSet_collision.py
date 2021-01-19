#!/usr/bin/env python3

from LinkedList import LinkedList

class HashSet:
   def __init__(self, capacity=10):
      # Create a list to use as the hash table
      self.table = [None] * capacity

   def add(self, item):
      # Find the hash code
      h = hash(item)
      index = h % len(self.table)

      # Check is it empty
      if self.table[index] == None:
         self.table[index] = LinkedList() # Need a new linked list for this entry
         col = False
      else:
         col = True

      if item not in self.table[index]:
         added = True
         col_index = index
         col_item = item
         # Only add it if not already there (this is a set)
         self.table[index].add(item) # adding it to the linked list at that index
      else:
         added = False

      if col == True and added == True:
         return col_index, col_item
      else:
         return None

import sys

def main():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
    nums = [int(item) for item in items]
    
    # First number is the capacity
    numset = HashSet(nums[0])

    for x in nums[1:]:
        print(str(numset.add(x)) + " ", end="")

    print()

if __name__ == "__main__":
    main()
