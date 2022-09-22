def main():
    minimum_length = 4
    password = get_password(minimum_length)
    print_stars_line(password)


def print_stars_line(password):
    print(len(password) * "*")


def get_password(minimum_length):
    password = input("Enter new password? ")

    while len(password) <= minimum_length:
        print("Invalid")
        password = input("Enter new password? ")
    print(password)
    return password


main()
