import random

# Produce an integer between 5 and 20, inclusive
print(random.randint(5, 20))

# Produce an odd integer between 3 and 9, inclusive
# Four cannot be produced in this expression
print(random.randrange(3, 10, 2))

# Produce a float between 2.5 and 5.5, inclusive
print(random.uniform(2.5, 5.5))

# Produce a number (integer) between 1 and 100, inclusive
print(random.randint(1, 100))
