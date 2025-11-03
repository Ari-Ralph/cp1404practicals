"""
CP1404 - Practical 07
Project client file.
Estimate: 2 hours
Actual:
"""
# Stopped at 8:43pm
from prac_07.project import Project

DEFAULT_FILENAME = "projects.txt"
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by da\n- (A)dd new project\n- (U)pdate proje\n- (Q)uit"
INDEX_COST_ESTIMATE = 3
INDEX_COMPLETION_PERCENTAGE = 4


def main():
    """Menu-based project management program."""
    projects = load_projects(DEFAULT_FILENAME)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            in_filename = input("Input Filename: ")
            try:
                load_projects(in_filename)
                print(f"Loaded {len(projects)} projects from {in_filename}")
            except FileNotFoundError:
                print("Invalid filename - Please check your spelling")
        elif menu_choice == "S":
            pass
        elif menu_choice == "D":
            display_projects(projects)
        elif menu_choice == "F":
            pass
        elif menu_choice == "A":
            pass
        elif menu_choice == "U":
            update_project(projects)
        else:
            print()
        print(MENU)
        menu_choice = input(">>> ").upper()


def load_projects(filename):
    """Read a txt file to create a list of Project objects."""
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline()  # Skip headers
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


def update_project(projects):
    for i, project in enumerate(projects):
        print(i, project)
    project_choice = get_valid_number("Project choice:", 0, len(projects) - 1)
    selected_project = projects[project_choice]
    print(selected_project)
    selected_project.completion_percentage = get_valid_number("New Percentage: ", 1, 100)
    selected_project.priority = get_valid_number("New priority: ", 1, 100)


def get_valid_number(prompt: str, minimum: int, maximum: int) -> int:
    """Get a valid number."""
    is_number_valid = False
    while not is_number_valid:
        try:
            number = int(input(prompt))
            if number < minimum:
                print(f"Number must be >= {minimum}")
            elif maximum is not None and number > maximum:
                print(f"Number must be less than {maximum}")

            else:
                is_number_valid = True
        except ValueError:
            print("Invalid input - please enter valid number")
    return number  # Ignore warning


main()
