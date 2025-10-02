"""
CP1404 - Practical 03
Programs practicing writing to and reading files.
"""

# Get a name and write to file
out_file = open("name.txt", 'w')
name = input("Name: ")
print(name, file=out_file)
out_file.close()