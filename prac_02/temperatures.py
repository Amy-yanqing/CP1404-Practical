"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    """Temperature conversion program."""
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":  # Q is quit option"
        if choice == "C":  # Convert Celsius to Fahrenheit
            celsius = get_value()
            fahrenheit = covert_celsius_to_fahrenheit(celsius)
            print_result(fahrenheit, result_unit="F")
        elif choice == "F":  # Convert Fahrenheit to Celsius
            fahrenheit = get_value()
            celsius = covert_fahrenheit_to_celsius(fahrenheit)
            print_result(celsius, result_unit="C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def get_value():
    """Get temperatures value that needs to convert"""
    value = float(input("the value need to convert is:  "))
    return value


def covert_celsius_to_fahrenheit(celsius):
    """Covert celsius to fahrenheit"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def covert_fahrenheit_to_celsius(fahrenheit):
    """Covert fahrenheit to celsius"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def print_result(result, result_unit):
    """Display converted result"""
    print("The convert result is : {:.2f}{}".format(result, result_unit))


main()
