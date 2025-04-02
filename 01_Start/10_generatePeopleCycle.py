import random

people_qty = int(input("Kiek zmoniu norite uzregistruoti?: "))
names = ["Arūnas", "Romualdas", "Marija", "Deividas", "Stefanija"]
surnames = ["Kazlauskas", "Urbonas", "Uspaskich", "Veronaite", "Kazlauskaite"]
people = []


def gen_random_name():
    global names
    len_names = len(names)
    random_name_number = random.randint(0, len_names -1)
    random_name = names[random_name_number]
    return random_name


def gen_random_surname():
    global surnames
    len_surnames = len(surnames)
    random_surname_number = random.randint(0, len_surnames -1)
    random_surname = surnames[random_surname_number]
    return random_surname


def gen_random_age():
    return random.randint(15, 80)


def generate_person():
    global people
    random_name = gen_random_name()
    random_surname = gen_random_surname()
    random_age = gen_random_age()
    return {
        "name": random_name,
        "surname": random_surname,
        "age": random_age
    }


for human in range(people_qty):
    people.append(generate_person())

print(people)