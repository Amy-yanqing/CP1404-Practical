"""
emails
Estimate: 60 minutes
Actual: 120 minutes
"""


def main():
    name_to_email = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        is_right_name = input(f"Is your name {name}? (Y/n)").upper()
        if is_right_name == "" or is_right_name == "Y":
            name = name
        else:
            name = input("Name: ")
        name_to_email[name] = email
        email = input("Email: ")
    for name, email in name_to_email.items():
        print(f"{name} ({email})")


def get_name(email):
    given_name = email.split("@")[0].title()
    parts = given_name.split(".")
    name = " ".join(parts)
    return name


main()
