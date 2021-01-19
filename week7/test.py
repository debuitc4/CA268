#!/usr/bin/env python3

s = "hello"

if not isinstance(s, str):
   print(hash(s)) # not a string => use the normal hash function
else:
   h = 0
   i = 0
   s = list(s)
   if len(s) > 0:
   # Get the ASCII value of the first char of the string as the hash
      while i < len(s):
         h += ord(s[i])
         i += 1
   print(h)


    else:
        h = 0
        i = 0
        n = len(s) - 1
        while i < len(s):
           h += ord(s[i]) * (31 ^ (n))
           n -= 1
           i += 1
        return h