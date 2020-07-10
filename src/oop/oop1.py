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
class Vehicle: #This would be the parent class
    pass

class GroundVehicle(Vehicle):  #This is a subparent/child of the vehicle class
    pass

class Car(GroundVehicle): #This is a child of the groundvehicle class
    pass

class FlightVehicle(Vehicle): #This is a child of the Vehicle class
    pass

class Airplane(FlightVehicle): #This is a child of the FlightVehicle class
    pass

class Motorcycle(GroundVehicle): #This is a child of the GroundVehicle class
    pass

class Starship(FlightVehicle): #This is a child of the Flight Vehicle class
    pass