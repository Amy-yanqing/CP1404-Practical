""" Quick Pick program"""
import random

NUMBER_OF_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Quick picks program - choose sets of random numbers."""
    number_of_quick_picks = int(input("How many number of quick picks: "))
    for i in range(number_of_quick_picks):
        numbers = []
        for line in range(NUMBER_OF_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while random.randint(MINIMUM, MAXIMUM) in numbers:
                number = random.randint(MINIMUM, MAXIMUM)
            numbers.append(number)
        numbers.sort()
        print(" ".join(f"{number:2}" for number in numbers))


main()
