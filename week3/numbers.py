#!/usr/bin/env python3

import sys

def get_odd_list():
   odd_numbers = []
   while True:
      number = int(input())
      if number != -1:
         if number % 2 != 0:
            odd_numbers.append(number)
      else:
         break
   return odd_numbers
