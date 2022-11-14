"""
time:15:30
"""
from prac_07.project import Project


def main():
    projects = []
    choice = input("Enter choice: ").upper()
    while choice != "":
        if choice == "L":
            load_file()
        # elif choice == "S":
        #     # save_file(projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid input")
        choice = input("Enter choice: ").upper()


def load_file():
    file_name = "projects.txt"
    projects = []
    with open(file_name, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            projects.append(Project(parts[0], parts[1], parts[2], parts[3], parts[4]))
    for project in projects:
        print(project)

# def save_file(projects):
#     out_file_name = input("Enter your out file name: ")
#     for project in projects:
#         print(project, file=out_file_name)


def display_projects(projects):
    incomplete = [project for project in projects if not project.is_completed]
    complete = [project for project in projects if project.is_completed]
    incomplete.sort()
    print("Incomplete projects: ")
    for i in incomplete:
        print(i)
    complete.sort()
    print("complete projects: ")
    for i in complete:
        print(i)


main()
