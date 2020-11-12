#!/usr/bin/env python3

import sys

def set_stuff(a, b):
   lst = []
   lst.append((a.union(b)))
   lst.append((a.issubset(b)))
   lst.append((a.issuperset(b)))
   return tuple(lst) 
