#!/usr/bin/env python3

def maximum(lst):
   if len(lst) == 1:
      return lst[0]
   else:
      return maxi(lst[0] + 1, lst[1] + 1)

def maxi(a, b):
   if a >= b:
      return a
   else:
      return b

print(maximum([1, 3, 90, 67, 20]))