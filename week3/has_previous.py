#!/usr/bin/env python3

import sys
seen = []
twice = []
num = int(input())
while num != -1:
   if num not in seen:
      seen.append(num)
   elif num in seen:
      twice.append(num)
   num = int(input())

x = "Enter numbers (-1 to end): "
print(x + str(" ".join(twice)), end="")
