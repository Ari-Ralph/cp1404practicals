"""
CP1404 - Practical 07
Project client file.
Estimate: 2 hours
Actual:
"""
from prac_07.project import Project

MENU = "\n- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by da\n- (A)dd new project\n- (U)pdate proje\n- (Q)uit"


def main():
    """Menu-based project management program."""
    projects = load_projects()
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


main()
