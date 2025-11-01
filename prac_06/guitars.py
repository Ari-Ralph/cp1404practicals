"""
CP1404 - Practical 06
Guitar class client file.
Note: Adding standard guitars may not be needed.
Estimate: 40 minutes
Actual: 56 minutes
"""

from prac_06.guitar import Guitar

guitars =  []

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
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40)) # Add standard guitars
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
print()
print("...snip...")
print()
print("These are my guitars:")
max_name_width = max(len(guitar.name) for guitar in guitars)
max_cost_width = max(len(str(f"{guitar.cost:,.2f}")) for guitar in guitars)
for i, guitar in enumerate(guitars, 1):
    vintage_string = "(vintage)" if guitar.is_vintage() else ""
    print(
        f"Guitar {i}: {guitar.name:>{max_name_width}} ({guitar.year}), worth ${guitar.cost:{max_cost_width},.2f} {vintage_string}")
