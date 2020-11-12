#!/usr/bin/env python3

a = [10, 7, 6, 2, 5, 8, 3, 4, 1]
a = sorted(a)
mid = a[len(a) // 2]
first, second = [], []
second.append(a.pop(len(a) // 2))
print(second)