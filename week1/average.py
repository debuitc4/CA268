#!/usr/bin/env python3

import sys

def above_average(numbers):
   sum_n = sum(numbers)
   av = sum_n // (len(numbers))
   above = []
   for i in numbers:
      if i > av:
         above.append(i)
   return above
