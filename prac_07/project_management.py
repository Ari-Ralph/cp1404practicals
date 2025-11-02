"""
CP1404 - Practical 07
Project client file.
Estimate: 2 hours
Actual:
"""

from prac_07.project import Project

FILENAME = "projects.txt"
MENU = "\n- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by da\n- (A)dd new project\n- (U)pdate proje\n- (Q)uit"
INDEX_COST_ESTIMATE = 3
INDEX_COMPLETION_PERCENTAGE = 4

def main():
    """Menu-based project management program."""
    projects = load_projects()
    for project in projects:
        print(project)
    print("Welcome to Pythonic Project Management")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print()
        print(MENU)
        choice = input(">>> ").upper()


def load_projects():
    """Read a txt file to create a list of Project objects."""
    projects = []
    with open(FILENAME, 'r') as in_file:
        in_file.readline() # Skip headers
        for line in in_file:
            project_data = line.strip().split("\t")
            projects.append(Project(*project_data))
    return projects

main()
