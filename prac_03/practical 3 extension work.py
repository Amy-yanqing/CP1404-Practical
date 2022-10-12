import random  # version 1

print(bool(random.randint(0, 1)))

random_number = bool(random.choice([True, False]))  # version 2
print(random_number)

random_number = bool(random.getrandbits(1))  # version 3
print(random_number)
