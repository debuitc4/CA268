#!/usr/bin/env python3

import sys


def get_counts_dict(words):
   d = {}

   for i, word in enumerate(words):
      if len(word) in d:
         d[len(word)] += 1
      else:
         d[len(word)] = 1
   return d


def main():
    # read the list of words from stdin
    line = sys.stdin.readline()
    line = line.strip()
    words = line.split()

    # call the student's function
    counts = get_counts_dict(words)
    print(type(counts))

    lengths = counts.keys()
    for length in sorted(lengths):
       print(str(length) + ": " + str(counts[length]))

if __name__ == "__main__":
    main()

'''def main():
   words = ["hello", "my", "name", "is", "caoimhe"]
   d = {}
   i = 0
   while i < len(words):
      if words[i] not in d:
         d[words[i]] = 0
      else:
         d[words[i]] = "more"
   i = i + 1
   print(d)

if __name__ == "__main__":
   main() '''
