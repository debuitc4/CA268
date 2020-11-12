#!/usr/bin/env python3

import sys

def main():
   print("Enter a name and number, or a name and ? to query (!! to exit)")
   d = {}
   while True:
      n = input()
      user_input = n.split(" ")
      if user_input == ["!!"]:
         print("Bye")
         break
      else:
         name, number = user_input[0], user_input[1]
         if name.isalpha() and number.isalnum():
            d[name] = number
         elif number == "?":
            if name not in d:
               print("Sorry, there is no {}".format(name))
            else:
               print("{} has number {}".format(name, d[name]))

if __name__ == "__main__":
   main()
