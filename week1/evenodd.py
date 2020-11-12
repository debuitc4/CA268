#!/usr/bin/env python3

import sys
#even print second half of string
#odd print first and last letter

s = sys.argv[1]
if len(s) % 2 == 0:
   print(s[len(s) // 2:])
else:
   print(s[0] + s[len(s) - 1])
