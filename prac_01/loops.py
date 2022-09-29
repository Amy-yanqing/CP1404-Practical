# """
# a) count in 10s from 0 to 100
# """
# for i in range(0, 101, 10):
#     print(i, end=' ')
# print()

# """
# b) count down from 20 to 1
# """
# for i in range(20, 0, -1):
#     print(i, end=' ')
# print()

# """
# c) print n stars
# """
# number_of_star = int(input("number of stars: "))
# for i in range(0, number_of_star):
#     stars = "*"
#     print(stars, end="")
#
"""
d) print n lines of increasing stars
"""
number_of_lines = int(input("number of lines: "))
for line in range(1, number_of_lines+1):
    print("*"*line)

