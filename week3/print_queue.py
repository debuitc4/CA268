#!/usr/bin/env python3

def print_queue(data, front, back):
   if front > back:
      return data[front:] + data[:back]
   else:
      return data[front:back]
