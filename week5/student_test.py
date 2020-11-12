#!/usr/bin/env python3

def make_list(lst):
	a, b = [], []
	lst = sorted(lst)
	a.append(lst.pop(len(lst)//2))
	if len(lst)>0:
		b.append(lst[:len(lst)//2])
		b.append(lst[len(lst)//2:])
		while len(a) != len(lst):
			if b[0] != []:
				a.append(b[0][len(b[0])//2])
				a = b.pop(0)
				b.append(a[:len(a)//2])
				b.append(a[len(a)//2+1:])
			else:
				b.pop(0)
	return a