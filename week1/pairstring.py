#!/usr/bin/env python2

import sys
s = sys.argv[1]

try:
   i = 0
   while i < len(s):
      print(s[i] + s[i + 1])
      i = i + 1
except IndexError:
   pass
