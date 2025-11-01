"""
CP1404 Practical 06 - Client code to use the Car class.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("My car", 180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)
    print()

    # 1. Create a new Car object called "limo" that is initialised with 100 units of fuel.
    limo = Car("Limo", 100)
    # 2. Add 20 more units of fuel to this new car object using the add method.
    limo.add_fuel(20)
    # 3. Print the amount of fuel in the car.
    print(f"The {limo.name} has {limo.fuel}L of fuel.")
    # 4. Attempt to drive the car 115 km using the drive method.
    print(f"The {limo.name} drove {limo.drive(115)}km.")

    # 7. Print your car objects.
    print(my_car)
    print(limo)


main()
