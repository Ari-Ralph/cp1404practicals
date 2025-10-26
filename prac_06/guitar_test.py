"""
CP1404 - Practical 06
Guitar class testing file.
Estimate: 40 minutes
Actual:
"""

from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.4)
another_guitar = Guitar("Another Guitar", 2013, 10942.514)
print("Test str method")
print(gibson)
print(another_guitar)

print("Test get_age method")
print(f"{gibson.name} get_age() - Expected 100. Got {gibson.get_age()}")
print(f"{another_guitar.name} get_age() - Expected 9. Got {another_guitar.get_age()}")

print("Test is_vintage method")
print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")