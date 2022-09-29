import math

x = int(input("Enter x value "))
y = int(input("Enter y value "))
target_number = 0
choice = input("what's the choice: i ii iii or iv ?")
while choice != "iv":
    if choice == "i":
        print("Even number")
        if x % 2 == 0:
            for i in range(x, y, 2):
                print(i, end=" ")
        elif x % 2 > 0:
            for i in range(x + 1, y, 2):
                print(i, end=" ")
    elif choice == "ii":
        print("Odd numbe")
        if x % 2 == 0:
            for i in range(x + 1, y, 2):
                print(i, end=" ")
        elif x % 2 > 0:
            for i in range(x, y, 2):
                print(i, end=" ")
    elif choice == "iii":
        print("square number")
        for i in range(x, y):  # math.sqrt()开方的函数
            if math.sqrt(i) % 1 == 0:
                print(i)



    else:
        print("invalid choice")
    choice = input("\nwhat's the choice: i ii iii or iv ?")
print("Quit!")
