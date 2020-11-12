#!/usr/bin/env python3

import sys

def get_sliced_lists(a):
    x = a[:len(a) - 1]
    y = a[1:len(a) - 1]
    z =  a[::-1]
    return [x, y, z]
