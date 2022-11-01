from prac_06.person import Person


def main():
    persons = []
    first_name = input("First name: ")
    while first_name != "":
        last_name = input("Last name:  ")
        age = int(input("Age:  "))
        person_to_add = Person(first_name, last_name, age)
        persons.append(person_to_add)
        print(f" {person_to_add} added.")
        first_name = input("First name: ")
    if persons:
        persons.sort()
    for person in persons:
        print(person)


main()
