import csv
from prac_07.guitar import Guitar

file_name = 'guitars.csv'


def main():
    guitars = []
    with open(file_name, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitars.append(Guitar(*parts))

    guitars.sort()
    for guitar in guitars:
        print(guitar)
main()
