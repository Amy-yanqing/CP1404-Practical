import random


def main():
    number_of_scores = int(input("Enter number of scores: "))
    for i in range(number_of_scores):
        random_number = random.randint(0, 100)
        print_result(random_number)
        out_file = open("results.txt", "a")
        print(random_number, "is", print_result(random_number), file=out_file)
        out_file.close()


def print_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


#
# def get_valid_score():
#     score = float(input("Enter score: "))
#     while score < 0 or score > 100:
#         print("Invalid score")
#         score = float(input("Enter score: "))
#     return score


main()
