"""
CP1404 - Practical 09
Testing for Unreliable car.
"""
from unreliable_car import UnreliableCar

# Initialise unreliable car
my_unreliable_car = UnreliableCar("Ford LW Focus", 52, 20)

# Test drive, with refueling to ensure the fuel is not a limiting factor
for i in range(10):
    print(f"The car drove {my_unreliable_car.drive(52)}km")
    my_unreliable_car.add_fuel(52)

