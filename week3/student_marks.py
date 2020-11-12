#!/usr/bin/env python3

import sys

def make_map():
   d = {}
   for line in sys.stdin:
      line = line.strip()
      x = line.split(" ")
      try:
         student, mark = x[0], x[1]
         d[student] = mark
      except IndexError:
         pass
   return d
