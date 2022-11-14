import csv
from prac_07.guitar import Guitar

file_name = 'guitars.csv'


def main():
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
    with open(file_name, 'w') as out_file:
        for guitar in guitars:
            print(guitar.name, ",", guitar.year, ",", guitar.cost, file=out_file)


def add_guitar(guitars):
    name = input("Guitar name: ")
    while name != "":
        year = int(input("year: "))
        cost = float(input("Cost: "))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        name = input("Name: ")


def load_guitar_file():
    guitars = []
    with open(file_name, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitars.append(Guitar(parts[0], parts[1], parts[2]))
    return guitars


def display_guitar(guitars):
    for guitar in guitars:
        print(guitar)


main()
