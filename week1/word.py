#!/usr/bin/env python3

def get_plural(word):
   if word[len(word) - 1] == "x" or word[len(word) - 1] == "s" or word[len(word) - 1] == "z":
      word = word + "es"
      return word
   elif word[len(word) - 2:] == "ch" or word[len(word) - 2:] == "sh":
      word = word + "es"
      return word

   elif word[len(word) - 1] == "y":
      vowels = ["a", "e", "i", "o", "u"]
      if word[len(word) - 2] not in vowels:
         s = ""
         s = s + word[0:len(word) - 1]
         s = s + "ies"
      return s
      
   elif word[len(word) - 1] == "f":
      s = ""
      s = s + word[:len(word) - 1] + "ves"
      return s

   elif word[len(word) - 1] == "e" and word[len(word) - 2] == "f":
      s = ""
      s = s + word[:len(word) - 2] + "ves"
      return s

   elif word[len(word) - 1] == "o":
      s = ""
      s = word + "es"
      return s

   else:
      word = word + "s"
      return word
