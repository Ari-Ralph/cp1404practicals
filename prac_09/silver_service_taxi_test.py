"""
CP1404 - Practical 09
Testing for Silver Service car.
"""
from silver_service_taxi import SilverServiceTaxi

# Test initialisation of a silver service taxi
default_silver_service = SilverServiceTaxi("Hummer", 200, 4)
assert default_silver_service.name == "Hummer"
assert default_silver_service.fuel == 200
assert default_silver_service.price_per_km == 4.92 # 4 * $1.23

# Test str method
print(default_silver_service)

# Test get fare method
default_silver_service.drive(18)
assert default_silver_service.get_fare() == 93.06