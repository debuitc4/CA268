#!/usr/bin/env python3

import sys

def get_counts(a):
   count = {}
   for v in range(0, 10):
      count[v] = 0

   for i in a:
      if len(i) in count:
         count[len(i)] += 1
   
   return list(count.values())
