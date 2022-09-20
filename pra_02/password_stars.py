def main():
    minimum_length = 4
    password_character = input("Enter new password? ")
    while len(password_character) <= minimum_length:
        print("Invalid")
        password_character = input("Enter new password? ")
    print(password_character)
    print(len(password_character) * "*")


main()
