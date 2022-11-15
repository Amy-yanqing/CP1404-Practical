"""
Estimate:3 hour
Finished: 3 days
"""
from prac_07.project import Project
from datetime import datetime


HEADER = "Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage"
FILE_NAME = "projects.txt"
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n" \
       "- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    """A program about display projects"""
    projects = load_projects(FILE_NAME)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            projects.clear()
            file_name = input("file name: ")
            projects = load_projects(file_name)
        elif choice == "S":
            file_name = input("file name to save: ")
            save_file(projects, file_name)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            date = get_date("Show projects that start after date (dd/mm/yy):")
            filter_projects(projects, date)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_projects(projects)
        else:
            print("Invalid input")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """load projects file to a list"""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()  # remove the header
        for line in in_file:
            parts = line.strip().split("\t")
            date = datetime.strptime(parts[1], "%d/%m/%Y").date()
            project = Project(parts[0], date, int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
        return projects


def save_file(projects, file_name):
    """Save date to file"""
    with open(file_name, "w") as out_file:
        print(HEADER, file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date}{project.priority}"
                  f"\t{project.cost_estimate}\t{project.completion_percentage}", file=out_file)


def display_projects(projects):
    """Display projects with different category"""
    incomplete_projects = [project for project in projects if not project.is_complete()]
    print("Incomplete projects: ")
    incomplete_projects.sort()
    for project in incomplete_projects:
        print(" ", project)
    complete_projects = [project for project in projects if project.is_complete()]
    complete_projects.sort()
    print("completed projects: ")
    for project in complete_projects:
        print(" ", project)


def filter_projects(projects, date):
    """filter projects, user input date compare with projects' date """
    projects.sort()
    for project in projects:
        if project.start_date >= date:
            print(project)


def get_date(prompt):
    """Get datetime type date"""
    date_string = input(prompt)
    return datetime.strptime(date_string, "%d/%m/%Y").date()


def add_project(projects):
    """Add new project"""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("start date (dd/mm/yy): ")
    date = datetime.strptime(start_date, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("cost estimate: $ "))
    completion_percentage = int(input("Percent complete: "))
    project = Project(name, date, priority, cost_estimate, completion_percentage)
    projects.append(project)


def update_projects(projects):
    """Update projects' completion percentage and priority"""
    for i, project in enumerate(projects):
        print(i, project)
    index = get_valid_index(projects)
    project = projects[index]
    print(project)
    try:
        completion_percentage = int(input("New Percentage: "))
        project.completion_percentage = completion_percentage
    except ValueError:
        pass
    try:
        priority = int(input("New priority: "))
        project.priority = priority
    except ValueError:
        pass


def get_valid_index(projects):
    """Get valid projects choice index"""
    is_valid_index = False
    while not is_valid_index:
        try:
            index = int(input("Project choice: "))
            if index > len(projects) - 1 or index < 0:
                print("index out of range")
            else:
                is_valid_index = True
                return index
        except ValueError:
            print("Invalid (not an integer)")


main()
