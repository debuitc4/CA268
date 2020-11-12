#!/usr/bin/env python3

class Node:
   def __init__(self, item, left = None, right = None):
      self.item = item
      self.left = left
      self.right = right

class BST:
   def __init__(self):
      self.root = None

   def recurse_add(self, ptr, item):
      if ptr == None:
         return Node(item)
      elif item < ptr.item:
        ptr.left = self.recurse_add(ptr.left, item)
      elif item > ptr.item:
        ptr.right = self.recurse_add(ptr.right, item)
      return ptr

   def add(self, item):
   #Add this item to its correct position on the tree """
      self.root = self.recurse_add(self.root, item)
   
   def r_contains(self, ptr, item):
      if ptr == None:
         return None
      elif item == ptr.item:
         return ptr
      elif item < ptr.item:
         return self.r_contains(ptr.left, next)
      else:
         return self.r_contains(ptr.right, next)
   
   def contains(self, item):
      return self.r_contains(self.root, item)
   
   def recursive_count(self, ptr):
      if ptr == None:  # Base Case
         return 0
      else:
         return 1 + self.recursive_count(ptr.left) + self.recursive_count(ptr.right)
                
   def count(self):
      return self.recursive_count(self.root)