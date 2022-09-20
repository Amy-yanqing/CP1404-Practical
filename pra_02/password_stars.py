def main():
    minimum_length = 4
    password_character = get_password(minimum_length)
    print_stars_line(password_character)


def print_stars_line(password_character):
    print(len(password_character) * "*")


def get_password(minimum_length):
    password_character = input("Enter new password? ")
    while len(password_character) <= minimum_length:
        print("Invalid")
        password_character = input("Enter new password? ")
    print(password_character)
    return password_character


main()
