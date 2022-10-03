import random

for i in range(1, 20):
    print(random.randint(5, 20), "-", end="")  # line 1
print()

for i in range(1, 20):
    print(random.randrange(3, 10, 2), "-", end="")  # line 2
print()

for i in range(1, 20):
    print(random.uniform(2.5, 5.5))  # line 3

# Random Numbers Question
"""
What did you see on line 1?
Answer: Return random integer from 5 to 20, 
including the start number 5 and end number 20.

What was the smallest number you could have seen, what was the largest?
Answer: smallest number is 5,largest number is 20.

What did you see on line 2?
Answer: Return a random odd integer in the range of 3 to 10.

What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?
Answer: the smallest number is 3,the largest number is 9.
and Line 2 didn't produce a 4.

What did you see on line 3?
Answer: return a random float number in the range of 2.5 to 5.5.

What was the smallest number you could have seen, what was the largest?
Answer: 
Smallest number: 2.505422128030026
Largest number: 5.49908363696613
"""

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))  # random module already import from the top,just do print.
