
# Example 1: Using super() to call parent constructor

class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person: {self.name}")

class Student(Person):
    def __init__(self, name, roll):
         super().__init__(name)
         self.roll = roll
         print(f"Student Roll: {self.roll}")

# s = Student("Alice", 101)

# Example 2: Using super() to call parent method inside overridden method

class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks")

# d = Dog()
# d.speak()


# Example 3: Multiple inheritance with super()

class Father:
    def skills(self):
        print("Father: Programming")

class Mother:
    def skills(self):
        print("Mother: Art")

class Child(Father, Mother):
    def skills(self):
        super().skills()  # Calls Father due to MRO
        print("Child: Gaming")

# c = Child()
# c.skills()

# Example 4: Calling parent method with additional logic

class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def start(self):
        print("Performing safety check")
        super().start()

# c = Car()
# c.start()

#Example 5: Using super() with multilevel inheritance

class Grandparent:
    def show(self):
        print("Grandparent method")

class Parent(Grandparent):
    def show(self):
        print("Parent method")
        super().show()

class Child(Parent):
    def show(self):
        print("Child method")
        super().show()

# c = Child()
# c.show()


class CreatorProfile:
    def __init__(self, bio, subscribers):
        self.bio = bio
        self.subscribers = subscribers

    def display_profile(self):
        print(f"Bio: {self.bio}, Subscribers: {self.subscribers}")


class YouTubeChannel(CreatorProfile):
    def __init__(self, name, bio, subs):
        self.name = name
        super().__init__(bio, subs)     # Composition


    def show_channel(self):
        print(f"Channel: {self.name}")
        self.display_profile()

# Composition: Channel owns CreatorProfile
# channel = YouTubeChannel("NetsetosTech", "Learn Python Easily", 1000000)
# channel.show_channel()