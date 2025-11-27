"""
CP1404 - Practical 09
Unreliable Car class.
"""

from car import Car
from random import uniform

class UnreliableCar(Car):
    """Specialised version of a Car, that introduces reliability."""
    def __init__(self, name, fuel, reliability):
        """Initialise an Unreliable Car instance, based on the parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability


    def drive(self, distance):
        """Return distance driven, but determines if the car drives with reliability attribute."""
        if self.reliability <= uniform(0,100):
            distance = 0
        else:
            super().drive(distance)
        return distance
