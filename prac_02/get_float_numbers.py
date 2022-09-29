import random

out_file = open("temps_input.txt", "a")
for i in range(20):
    random_float_number = float(random.uniform(-200, 200))
    print(random_float_number, file=out_file)
out_file.close()
