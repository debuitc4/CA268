#!/usr/bin/env python3

import sys

def get_evenodd_list():
   odd_numbers = []
   even_numbers = []
   while True:
      number = int(input())
      if number != -1:
         if number % 2 != 0:
            odd_numbers.append(number)
         else:
            even_numbers.append(number)
      else:
         break
   t = (odd_numbers, even_numbers)
   return t

def main():
    # call the get_odd_list function and print the result
    odds, evens = get_evenodd_list()
    print(odds)
    print(evens)

if __name__ == "__main__":
    main()
