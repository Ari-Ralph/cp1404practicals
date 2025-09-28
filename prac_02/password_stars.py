"""
CP1404 - Practical 02
Ari Ralph
Get password with a minimum length and print sequence of asterisks.
"""

MINIMUM_LENGTH = 5


def main():
    """Get password and print number of asterisks equal to password length."""
    password = get_valid_password()
    print_number_of_asterisks(password)


def get_valid_password() -> str:
    """Get password with a length >= to a minimum length."""
    password = input(f"Enter password with at least {MINIMUM_LENGTH} characters: ")
    while len(password) < MINIMUM_LENGTH:
        print("INVALID PASSWORD!")
        password = input(f"Enter password with at least {MINIMUM_LENGTH} characters: ")
    return password


def print_number_of_asterisks(sequence: str) -> None:
    """Print number of asterisks equal to length of sequence."""
    for i in range(len(sequence)):
        print("*", end="")


main()
