"""Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it. Remember to close your file.

(In the same file, but as if it were a separate program) Write code that opens "name.txt" and reads the name (as above) then prints,
"Your name is Bob" (or whatever the name is in the file).

Create a text file called numbers.txt and save it in your prac directory. Put the following three numbers on separate lines in the file and save it:
17
42
400
Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result, which should be... 59.
*****
Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number of numbers.
"""
# Programming 1
name = input("name: ")
out_file = open("name.txt", "w")  #
print(name, file=out_file)
out_file.close()

# Programming 2
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()

# Programming 3
in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)

# Programming 4
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(f"total is {total}")
