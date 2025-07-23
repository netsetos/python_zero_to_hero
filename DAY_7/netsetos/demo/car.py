class Car:
    # Class attribute
    wheels = 4

    def __init__(self, brand, color):
        # Instance attributes
        self.brand = brand
        self.color = color

    def display(self):
        print(f"Brand: {self.brand}, Color: {self.color}, Wheels: {Car.wheels}")

# Create objects
car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")
car3= Car("Tesla" , "BLACK")
car1.display()  # Output: Brand: Toyota, Color: Red, Wheels: 4
car2.display()  # Output: Brand: Honda, Color: Blue, Wheels: 4
car3.display()  # Output: Brand: Honda, Color: Blue, Wheels: 4