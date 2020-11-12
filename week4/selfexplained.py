#!/usr/bin/env python3

class Student:

   def __init__(self, name, major, gpa, is_on_probation):
      self.name = name
      self.major = major
      self.gpa = gpa
      self.is_on_p = is_on_probation

def main():
   student1 = Student("Anna", "Business", 3.1, False)
   print(student1.gpa)

if __name__ == "__main__":
   main()
