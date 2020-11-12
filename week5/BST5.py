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
   
   def count_leaves(self):
      return self.rec_cl(self.root)
   
   def rec_cl(self, ptr):
      if ptr == None:
         return 0
      elif ptr.left == None and ptr.right == None:
         return 1 + self.rec_cl(ptr.left) + self.rec_cl(ptr.right)
      return self.rec_cl(ptr.left) + self.rec_cl(ptr.right)
