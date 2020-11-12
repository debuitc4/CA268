#!/usr/bin/env python3

def rprint(a, b):
   if a == b:
      return
   print(a)
   rprint(a + 1, b)
