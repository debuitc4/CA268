#!/usr/bin/env python3

import sys

def main(a = {1, 2, 3, 4}, b = {1, 2, 3, 4, 5, 6, 7}):
   lst = []
   lst.append((a.union(b)))
   lst.append((a.issubset(b)))
   lst.append((a.issuperset(b)))
   print(tuple(lst))

if __name__ == "__main__":
    main()
