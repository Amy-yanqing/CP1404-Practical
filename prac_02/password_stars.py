def main():
    """Get a password of valid size and print stars."""
    minimum_length = 4
    password = get_password(minimum_length)
    print_stars_line(password)


def print_stars_line(password):
    """Print as many stars as there are characters in the passed-in sequence"""
    print(len(password) * "*")


def get_password(minimum_length):
    """Get password, ensuring it meets the minimum_length requirement."""
    password = input("Enter new password? ")
    while len(password) <= minimum_length:
        print("Invalid")
        password = input("Enter new password? ")
    print(password)
    return password


main()
