#!/usr/bin/env python3

import sys
s = sys.argv[1:]

spaces = ''
for v in s:
   spaces = spaces + ':' + v
print(spaces + ':')
