# Base class
class Grandparent:
    def show_grandparent(self):
        print("Grandparent: Shares wisdom")

# Intermediate class inheriting from Grandparent
class Parent(Grandparent):
    def show_parent(self):
        print("Parent: Provides guidance")

# Child class inheriting from Parent
class Child(Parent):
    def show_child(self):
        print("Child: Learns and grows")

# Create object of Child class
c = Child()
c.show_grandparent()   # Inherited from Grandparent
c.show_parent()        # Inherited from Parent
c.show_child()         # Defined in Child