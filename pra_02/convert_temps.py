"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    in_file = open("temps_input.txt", "r")
    out_file = open("temps_output.txt", "a")
    for line in in_file:
        fahrenheit = float(line)
        covert_fahrenheit_to_celsius(fahrenheit)
        print(covert_fahrenheit_to_celsius(fahrenheit), file=out_file)
    in_file.close()
    out_file.close()


def covert_fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
