#!/usr/bin/env python3

def make_list(lst):
   lst = sorted(lst)
   mid = len(lst) // 2 #index of middle
   first_half, second_half = [], []
   first_half = lst[:mid]
   second_half = lst[mid + 1:]
   result = []
   result.append(lst[mid])
   i = 0
   while len(result) != len(lst):
      try:
         result.append(first_half[i])
         result.append(second_half[i])
         i = i + 1
      except(IndexError):
         pass
   return result
