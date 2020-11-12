#!/usr/bin/env python3

import sys

def main():
   cross_over = []
   s = []
   with open(sys.argv[1]) as fd:
      f1 = fd.readlines() 
   for line in f1:
      s.append(line.strip())

   with open(sys.argv[2]) as fd:
      f2 = fd.readlines() 
   for line in f2:
      line = line.strip()
      if line in s:
         cross_over.append(line)
   
   i = 1
   for v in sorted(cross_over):
      print("{}. {}".format(i, v))
      i = i + 1

if __name__ == "__main__":
   main()
