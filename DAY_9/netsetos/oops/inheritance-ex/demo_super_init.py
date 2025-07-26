class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person: {self.name}")

class Student(Person):
    def __init__(self, name, roll):
         super().__init__(name)
         self.roll = roll
         print(f"Student Roll: {self.roll}")
#
# s = Student("Alice", 101)

# ✅ Example 2: Using super() to call
# parent method inside overridden method

class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks")

# d = Dog()
# d.speak()

#✅ Example 3: Multiple inheritance with super()

class Father:
    def skills(self):
        print("Father: Programming")


class Mother:
    def skills(self):
        print("Mother: Art")


class Child(Mother, Father):
    def skills(self):
        super().skills()  # Calls Father due to MRO
        print("Child: Gaming")


# c = Child()
# c.skills()


# ✅ Example 4: Calling parent method with additional logic
class Vehicle:
    def start(self):
        print("Vehicle started")


class Car(Vehicle):
    def start(self):
        print("Performing safety check")
        super().start()


# c = Car()
# c.start()

# ✅ Example 5: Using super() with multilevel inheritance

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



class Product:
   def __init__(self, name, price):
      self.name = name
      self.price = price

   def show(self):
      print(f"{self.name} costs ₹{self.price}")

# p1 = Product("Laptop", 60000)
# p2 = Product("Tablet", 30000)
# p1.show()
# p2.show()

class Coder:
   def __init__(self):
      self.name = "Unknown"
      self.language = "Python"

   def show(self):
      print(f"{self.name} codes in {self.language}")

# c1 = Coder()
# c1.show()

class Developer:
   def __init__(self):
      self.role = "Backend Developer"

   def show(self):
      print("Role:", self.role)

# d1 = Developer()
# d1.show()

class Rectangle:
   def __init__(self, width=0, height=0):
      if width and height:
         self.width = width
         self.height = height
      elif width:
         self.width = self.height = width
      else:
          self.width = self.height = 0

   def area(self):
      return self.width * self.height


r1 = Rectangle(10, 20)
r2 = Rectangle(10)
r3 = Rectangle()

print(r1.area())  # 200
print(r2.area())  # 100 (treated as square)
print(r3.area())  # 0










