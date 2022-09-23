"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = covert_celsius_to_fahrenheit(celsius)
            print_covert_result(fahrenheit,"F")

        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = covert_fahrenheit_to_celsius(fahrenheit)
            print_covert_result(celsius,"C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def covert_fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def print_covert_result(result,unit):
    print("Result: {:.2f} ".format(result),unit)


def covert_celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

main()
