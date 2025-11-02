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
    guitars = process_guitars_file()
    for guitar in sorted(guitars):
        print(guitar)

def process_guitars_file():
    guitars = []
    with open(FILENAME, 'r') as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip headers
        for row in reader:
            row[INDEX_YEAR] = int(row[INDEX_YEAR])
            row[INDEX_COST] = float(row[INDEX_COST])
            guitars.append(Guitar(*row))
    return guitars


main()
