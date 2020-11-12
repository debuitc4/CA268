#!/usr/bin/env python3

def findpair(lst, k):
    for i in range(0, len(lst)):
        for j in range(0, len(lst)):
            if k == lst[i] + lst[j]:
                return True    
    return False
      
nums = [1, 5, 6, 7, 3]
k = 10
print(findpair(nums, k))
