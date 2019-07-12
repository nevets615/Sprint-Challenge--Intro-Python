# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    # base class to FlightVehicle and GroundVehicle
    pass

class FlightVehicle(Vehicle):
    # parent to Starship and Airplane
    pass

class Starship(FlightVehicle):
    pass

class Airplane(FlightVehicle):
    pass

class GroundVehicle(Vehicle):
    # parent to Car and Motorcycle
    pass 

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass