#!/usr/bin/env python3

def sum_to_k(lst, k):
   nums = []

   for i in range(len(lst)):
      for j in range(len(lst)):
         if lst[i] + lst[j] == k and (lst[j], lst[i]) not in nums and i != j:
            nums.append((lst[i], lst[j]))

   for n in nums:
      print(n[0], n[1])

def main():
   lst = [60, 6, 10, 8, 5]
   k = 15

   print(sum_to_k(lst2, k2))

if __name__ == '__main__':
   main()
