import random

print("welcome ")
population = 1000
for i in range(1, 11):
    print("staring population:{}\nyear {}".format(population, i))
    random_born_rate = random.uniform(0.1, 0.2)
    random_die_rate = random.uniform(0.05, 0.25)
    random_born = int(random_born_rate * population)
    random_die = int(random_die_rate * population)
    population += random_born
    population -= random_die
    print(random_born, "gophers were born", random_die, "died")
    print("population:", population)
