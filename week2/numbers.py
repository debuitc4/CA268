#!/usr/bin/env python3

def sum_to_k(lst, k): 
   s = set()
   for i in range(0, len(lst)):
      element = k - lst[i]
      if (element in s):
         return True
      else:
         s.add(lst[i])
   return False


lst = [1, 50, 65, 7, 50]
k = 100
print(sum_to_k(lst, k))
