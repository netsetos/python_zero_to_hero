# Parent class
class Vehicle:
    def start_engine(self):
        print("Engine started")

# Child class 1
class Car(Vehicle):
    def open_trunk(self):
        print("Car: Trunk opened")

# Child class 2
class Motorcycle(Vehicle):
    def kick_start(self):
        print("Motorcycle: Kick-started")

# Creating objects of both child classes
my_car = Car()
my_car.start_engine()   # Inherited from Vehicle
my_car.open_trunk()     # Defined in Car

my_bike = Motorcycle()
my_bike.start_engine()  # Inherited from Vehicle
my_bike.kick_start()    # Defined in Motorcycle