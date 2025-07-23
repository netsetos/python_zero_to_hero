# Base class
class Vehicle:
    def show_type(self):
        print("Vehicle: Used for transportation")

# First level child (single inheritance)
class Car(Vehicle):
    def car_features(self):
        print("Car: Has 4 wheels and AC")

# Another base class for multiple inheritance
class Electric:
    def battery_info(self):
        print("Electric: Runs on battery")

# Hybrid class (inherits from Car and Electric)
class ElectricCar(Car, Electric):
    def features(self):
        print("ElectricCar: Eco-friendly and silent")

# Create object of ElectricCar
ecar = ElectricCar()
ecar.show_type()       # Inherited from Vehicle
ecar.car_features()    # Inherited from Car
ecar.battery_info()    # Inherited from Electric
ecar.features()        # Defined in ElectricCar