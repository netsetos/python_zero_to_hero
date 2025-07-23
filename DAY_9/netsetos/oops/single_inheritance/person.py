# Example of Single Inheritance in Python

class Person:
    def display_name(self):
        print("Name: Sara")

class Student(Person):
    def display_course(self):
        print("Course: Python Programming")

# Using the child class
s = Student()
s.display_name()   # Inherited from Person
s.display_course() # Defined in Student