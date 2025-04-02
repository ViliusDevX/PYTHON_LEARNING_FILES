#def multiply(x, y, z):
    #return x * y * z

#x = multiply(13, 666, 777)
#xy = multiply(111, 98.7, 0.123123)
#print(x, xy) JUODRASTIS

import random
def random_bool():
    return bool(round(random.random()))

petras_got_back_drunk = random_bool()
petras_got_back_late = random_bool()
petras_will_have_problems = petras_got_back_drunk and petras_got_back_late
print(f"Petras grizo girtas: {petras_got_back_drunk} \nPetras grizo velai: {petras_got_back_late} \nPetrui galas: {petras_will_have_problems}")

