"""
CP1404 - Practical 02
Ari Ralph
Get password with a minimum length and print sequence of asterisks
"""

MINIMUM_LENGTH = 5


def main():
    password = input(f"Enter password with at least {MINIMUM_LENGTH} characters: ")
    while len(password) < MINIMUM_LENGTH:
        print("INVALID PASSWORD!")
        password = input(f"Enter password with at least {MINIMUM_LENGTH} characters: ")
    for i in range(len(password)):
        print("*", end="")


main()
