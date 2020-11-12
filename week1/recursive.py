#!/usr/bin/env python3

import sys

def is_palindrome(word):
   #basecase
   if len(word) < 2:
      return True
   if word[0] != word[- 1]:
      return False
   return is_palindrome(word[1:-1])

def main():
   word = sys.stdin
   print(is_palindrome(word))

if __name__ == "__main__":
   main()