"""
CP1404 - Practical 07
Guitar client file - Get and sort guitars from file and user.
"""
import csv

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"
INDEX_YEAR = 1
INDEX_COST = 2


def main():
    """Get, display and save guitar data from csv file and user."""
    guitars = load_guitars_file()
    guitars = get_new_guitar(guitars)
    for guitar in sorted(guitars):
        print(guitar)
    save_guitars(guitars)


def load_guitars_file():
    """Form guitars list from input of csv file."""
    guitars = []
    with open(FILENAME, 'r', encoding="utf-8") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip headers
        for row in reader:
            row[INDEX_YEAR] = int(row[INDEX_YEAR])  # Ignore PyCharm warning
            row[INDEX_COST] = float(row[INDEX_COST])  # Ignore PyCharm warning
            new_guitar = Guitar(*row)
            guitars.append(new_guitar)
    return guitars


def get_new_guitar(guitars):
    """Get guitar data from the user."""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{Guitar(name, year, cost)} added")
        print()
        name = input("Name: ")
    return guitars


def save_guitars(guitars):
    """Save guitars to csv file."""
    with open(FILENAME, 'w', encoding="utf-8") as out_file:
        for guitar in guitars:
            guitar.year, guitar.cost = str(guitar.year), str(guitar.cost)  # Convert int to str
            print(",".join([guitar.name, guitar.year, guitar.cost]), file=out_file)


main()
