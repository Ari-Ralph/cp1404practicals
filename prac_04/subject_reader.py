"""
CP1404 - Practical 04
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read subject data from file and print it."""
    subject_data = load_data(FILENAME)

    for subject in subject_data:
        print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:3} students")


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_data = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subject_data.append(parts)
    input_file.close()
    return subject_data


main()