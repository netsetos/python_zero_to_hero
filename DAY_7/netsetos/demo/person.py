# Define a class
class Person:
    EDUCATION="NETSETOS"
    # Constructor to initialize object attributes
    def __init__(self, name, age,height):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute
        self.height = height # Instance attribute

    # Method to display details is an instance method
    def display(self):
        if self.age > 18 and self.height > 150:
            print(f"Name: {self.name}, Age: {self.age}")

# Create an object (instance) of the class
person1 = Person("Alice", 16,height=160)
person2 = Person("Shenoy", 24,height=170)
person3 = Person("Chaiya", 24,height=150)

# Access attributes and methods
person1.display()  # Output: Name: Alice, Age: 30
person2.display()
person3.display()

