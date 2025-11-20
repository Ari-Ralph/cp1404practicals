"""
CP1404 - Practical 09
Testing for Taxi car.
"""

from taxi import Taxi

# 1. Create my_taxi object
my_taxi = Taxi("Prius 1", 100)

# 2. Drive my_taxi 40km
my_taxi.drive(40)

# 3. Print the taxi's details and current fare
print("Taxi details and current fare:")
print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare():.2f}")

# 4. Restart the current fare and drive 100km
my_taxi.start_fare()
my_taxi.drive(100)

# 5. Print the taxi's details and current fare
print("Taxi details and current fare:")
print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare():.2f}")