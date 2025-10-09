"""
CP1404 - Practical 03
Programs practicing writing to and reading files.
"""

# Get a name and write to file
name = input("Name: ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

# Read name and print
in_file = open("name.txt", 'r')
name = in_file.read().strip()
print(f"Hi {name}!")
in_file.close()

# Read and add first two numbers
in_file = open("numbers.txt")
number = int(in_file.readline()) + int(in_file.readline()) # Add numbers on two consecutive lines
in_file.close()
print(number)

# Total all numbers in reading file
total = 0
with open("numbers.txt", 'r') as in_file:
    for line in in_file:
        total += int(line)
    print(total)