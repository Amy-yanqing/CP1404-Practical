"""
Estimate: 60 minutes
Actual: 120 minutes
Programming guitar
"""
import csv
from prac_07.guitar import Guitar

file_name = 'guitars.csv'


def main():
    """A program about modify guitar data"""
    guitars = []
    choice = input("L(oad),D(display),A(dd),S(ave),Q(uit)?  ").upper()
    while choice != "Q":
        if choice == "L":
            guitars = load_guitar_file()
            print(f"Guitar {len(guitars)} file load")
        elif choice == "D":
            display_guitar(guitars)
        elif choice == "A":
            add_guitar(guitars)
        elif choice == "S":
            save_guitar(guitars)
        else:
            print("Invalid Choices")
        choice = input("L(oad),D(display),A(dd),S(ave),Q(uit)?  ").upper()
    print("Bye")


def save_guitar(guitars):
    """Save guitar data to file"""
    with open(file_name, 'w') as out_file:
        for guitar in guitars:
            print(guitar.name, ",", guitar.year, ",", guitar.cost, file=out_file)


def add_guitar(guitars):
    """Add new guitar to file"""
    name = input("Guitar name: ")
    while name != "":
        year = int(input("year: "))
        cost = float(input("Cost: "))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        name = input("Name: ")


def load_guitar_file():
    """Load guitar data"""
    guitars = []
    with open(file_name, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitars.append(Guitar(parts[0], parts[1], parts[2]))
    return guitars


def display_guitar(guitars):
    """Display guitar in the guitars"""
    for guitar in guitars:
        print(guitar)


main()
