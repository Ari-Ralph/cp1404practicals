"""
CP1404 - Practical 07
Project client file.
Estimate: 2 hours
Actual:
"""

from prac_07.project import Project

FILENAME = "projects.txt"
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by da\n- (A)dd new project\n- (U)pdate proje\n- (Q)uit"
INDEX_COST_ESTIMATE = 3
INDEX_COMPLETION_PERCENTAGE = 4

def main():
    """Menu-based project management program."""
    projects = load_projects()
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            update_project(projects)
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

def display_projects(projects):
    """Display projects organised into completion status."""
    completed_projects = []
    incomplete_projects = []
    for project in projects:
        if project.is_complete():
            completed_projects.append(project)
        else:
            incomplete_projects.append(project)
    print("Incomplete projects: ")
    for incomplete_project in incomplete_projects:
        print(f"  {incomplete_project}")
    print("Completed projects: ")
    for completed_project in completed_projects:
        print(f"  {completed_project}")

main()
