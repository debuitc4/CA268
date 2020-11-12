#!/usr/bin/env python3

def detect_loop(ll):
   start = ll.head
   ptr = ll.head
   while ptr != None:
      if ptr.next == start:
         return True
      ptr = ptr.next
   return False
