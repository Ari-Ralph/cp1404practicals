"""
CP1404 - Practical 06
Guitar class client file.
Estimate: 40 minutes
Actual:
"""

from prac_06.guitar import Guitar

guitars = []

print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)
    print(f"{new_guitar} added")
    print()
    name = input("Name: ")
print()
print("...snip...")
print()
print("These are my guitars:")
name_spacing = max(len(guitar.name) for guitar in guitars)
cost_spacing = max(len(str(f"{guitar.cost:,.2f}")) for guitar in guitars)
for i, guitar in enumerate(guitars, 1):
    vintage_string = "(vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>{name_spacing}} ({guitar.year}), worth ${guitar.cost:{cost_spacing},.2f} {vintage_string}")
