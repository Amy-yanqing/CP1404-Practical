MENU = """
-G get valid score
-P print result
-s print as many stars as the score
-Q Quit
"""


def main():
    score = 0
    star = "*"
    print(MENU)
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
            print(score)
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            print_stars(score, star)
        else:
            print("Invalid choice")
        choice = input("> ").upper()
    print("Quit")


def get_valid_score():
    score = int(input("Enter your score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter your score: "))
    return score


def print_result(score):
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def print_stars(score, star):
    print(score * star)


main()
