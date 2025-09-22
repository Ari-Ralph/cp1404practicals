"""
CP1404 - Practical 1
by Ari Ralph
Created: 13/09/25
Last Edited: 16/09/2025
Loops
"""
# Example Code: Displays all odd number between 1 and 20
for i in range(1, 21, 2):
    print(i, end=" ")
print()

# Part A: Counts in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=" ")
print()

# Part B: Counts down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=" ")
print()

# Part C: Prints a number of stars
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print("*", end="")
print()

# Part D: Prints lines of increasing stars
number_of_stars = int(input("Number of stars: "))
for i in range(1, number_of_stars + 1):
    print("*" * i)
print()
