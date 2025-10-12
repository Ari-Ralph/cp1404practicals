"""
CP1404 - Practical 04
Quick Picks Program
"""
import random

NUMBER_OF_RANDOM_NUMBERS = 6
RANDOM_NUMBER_MAXIMUM = 45
RANDOM_NUMBER_MINIMUM = 1


def main():
    number_of_rows = int(input("How many quick picks? "))
    for row in range(number_of_rows):
        random_numbers = get_random_numbers()
        for i in random_numbers:
            print(f"{i:>2}", end=" ")
        print()


def get_random_numbers():
    random_numbers = []
    while len(random_numbers) != NUMBER_OF_RANDOM_NUMBERS:
        number = random.randint(RANDOM_NUMBER_MINIMUM, RANDOM_NUMBER_MAXIMUM)
        if number not in random_numbers:
            random_numbers.append(number)
    return random_numbers

main()