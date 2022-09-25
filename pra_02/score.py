"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = get_valid_score()
    print_result(score)
    random_score = random.randint(1, 100)
    print("The random score is:", random_score)
    print_result(random_score)


def print_result(score):
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def get_valid_score():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


main()
