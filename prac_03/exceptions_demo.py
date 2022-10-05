"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Answer: float number, Arabic letter, symbol, etc. anything that is not an integer
2. When will a ZeroDivisionError occur?
Answer:denominator value is 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Answer:Yes, see code as below, add error check while loop.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("denominator value not allow to be 0")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")