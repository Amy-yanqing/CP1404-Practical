"""Get ASCII code then display the ASCII code's corresponding  characters"""
LOW_NUMBER = 33
UPPER_NUMBER = 127
# character = input("Enter a character: ")
# print(ord(character))
number = int(input(f"Enter number between {LOW_NUMBER} to {UPPER_NUMBER}: "))
while number < LOW_NUMBER or number > UPPER_NUMBER:
    number = int(input("Enter number: "))
print(f"{number:<4}{chr(number)}")

for i in range(LOW_NUMBER, UPPER_NUMBER + 1):
    print(f"{i:3} {chr(i):>3}")

