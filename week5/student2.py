#!/usr/bin/env python3

def is_maximal(bst):
      count = bst.count()
      ptr = 1
      i = 0
      while ptr < count:
         ptr = ptr + 2 ** (i + 1)
         i += 1
      if ptr == count and i == bst.height() - 1:
         return True
      return False
