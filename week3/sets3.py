#!/usr/bin/env python3

import sys

def unique_list(a):
   s = set()
   for v in a:
      if v not in s:
         s.add(v)
   return list(s)    
