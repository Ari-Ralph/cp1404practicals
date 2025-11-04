"""
CP1404 - Practical 07
Project client file.
Estimate: 2 hours
Actual:
"""
# Stopped at 8:43pm

# 1 hour 15 minutes
from prac_07.project import Project
import datetime
from operator import attrgetter

DEFAULT_FILENAME = "projects.txt"
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"
INDEX_DATE = 1
INDEX_COST_ESTIMATE = 3
INDEX_COMPLETION_PERCENTAGE = 4
PRIORITY_MAXIMUM = 9


def main():
    """Menu-based project management program."""
    projects, header = load_projects()
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
            out_filename = input("Save Filename: ")
            try:
                save_projects(projects, header, out_filename)
            except FileNotFoundError:
                print("Invalid filename - Please check your spelling")
        elif menu_choice == "D":
            display_projects(projects)
        elif menu_choice == "F":
            filter_by_date(projects)
        elif menu_choice == "A":
            add_new_project(projects)
        elif menu_choice == "U":
            update_project(projects)
        else:
            print()
        print(MENU)
        menu_choice = input(">>> ").upper()
    save_choice = input(f"Would you like to save to {DEFAULT_FILENAME}? ").upper()
    if save_choice == "Y":
        save_projects(projects, header)
    print("Thank you for using custom-built project management software.")


def load_projects(in_filename=DEFAULT_FILENAME):
    """Read a txt file to create a list of Project objects."""
    projects = []
    with open(in_filename, 'r') as in_file:
        header = in_file.readline().strip()  # Skip headers
        for line in in_file:
            project_data = line.strip().split("\t")
            project_data[INDEX_DATE] = datetime.datetime.strptime(project_data[INDEX_DATE],
                                                                  "%d/%m/%Y").date()  # Ignore PyCharm warning
            projects.append(Project(*project_data))
    return projects, header


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
    for incomplete_project in sorted(incomplete_projects, key=attrgetter('priority')):
        print(f"  {incomplete_project}")
    print("Completed projects: ")
    for completed_project in sorted(completed_projects, key=attrgetter('priority')):
        print(f"  {completed_project}")


def add_new_project(projects):
    """Get input for a new project object"""
    print("Let's add a new project")
    name = get_valid_input("Name: ")
    start_date = get_valid_date("Start date(dd / mm / yy): ")
    priority = get_valid_number("Priority: ", 1, PRIORITY_MAXIMUM)
    cost_estimate = get_valid_number("Cost estimate:", 1, input_type="float")
    cost_estimate = get_valid_number("Percent complete:", 0, 100)


def update_project(projects):
    """Update the completion percentage and priority if inputs are not blank."""
    for i, project in enumerate(projects):
        print(i, project)
    project_choice = get_valid_number("Project choice:", 0, len(projects) - 1)
    selected_project = projects[project_choice]
    print(selected_project)
    new_percentage = get_valid_number("New Percentage: ", 0, 100, True)
    # If input was empty, percentage remains the same value
    selected_project.completion_percentage = new_percentage if new_percentage != "" else selected_project.completion_percentage
    new_priority = get_valid_number("New priority: ", 1, PRIORITY_MAXIMUM, True)
    # If input was empty, priority remains the same value
    selected_project.priority = new_priority if new_priority != "" else selected_project.priority


def get_valid_date(prompt):
    """Get a date from user with error checking."""
    is_valid = False
    while not is_valid:
        date_parts = input(prompt)
        try:
            date = datetime.datetime.strptime(date_parts, "%d/%m/%Y").date()
            is_valid = True
        except ValueError:
            print("Invalid date")
    return date  # Ignore PyCharm warning


def get_valid_input(prompt: str) -> str:
    """Get an input that is not empty."""
    user_input = input(prompt)
    while user_input == "":
        print("Input can not be blank")
        user_input = input(prompt)
    return user_input


def get_valid_number(prompt: str, minimum: int, maximum=None, is_empty_allowed=False, input_type=""):
    """Get a valid number."""
    is_number_valid = False
    while not is_number_valid:
        try:
            if input_type == "float":
                number = float(input(prompt))
            else:
                number = int(input(prompt))
            if number < minimum:
                print(f"Number must be >= {minimum}")
            elif maximum is not None and number > maximum:
                print(f"Number must be less than {maximum}")
            else:
                is_number_valid = True
        except ValueError:
            if is_empty_allowed:
                number = ""
                is_number_valid = True
            else:
                print("Invalid input")
    return number  # Ignore warning


def save_projects(projects, header, out_filename=DEFAULT_FILENAME):
    """Write projects to an out file."""
    with open(out_filename, 'w') as out_file:
        print(header, file=out_file)
        for project in projects:
            project.cost_estimate = str(project.cost_estimate)
            project.completion_percentage = str(project.completion_percentage)
            print(project.save_format(), file=out_file)
    print(f"{len(projects)} projects saved to {out_filename}")

def filter_by_date(projects):
    """Filter projects list to get projects starting after inputted date."""
    filter_start_date = get_valid_date("Show projects that start after date (dd/mm/yy):")
    valid_projects = [project for project in projects if project.start_date >= filter_start_date]
    for valid_project in sorted(valid_projects, key=attrgetter('start_date')):
        print(valid_project)

main()
# get_valid_date("Date: ")
