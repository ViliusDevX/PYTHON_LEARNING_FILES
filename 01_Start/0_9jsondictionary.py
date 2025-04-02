people = [
    {
        'name': 'Stasys Dešritas',
        'age': 23
    },
    {
        'name': 'Rokas Elektronas',
        'age': 26
    },
    {
        'name': 'Ruta Krūta',
        'age': 19
    }
]


def add_person(name, surname, age):
    global people
    people.append({
        "name" : f"{name} {surname}",
        "age" : age
    })

add_person('martynas', 'mazvydas', 12)

def remove_person(list_index):
    global people
    people.pop(list_index)


def get_person(list_index):
    global people
    return people[list_index]


get_person_3 = get_person(3)

print(get_person_3)
print(f"{people}, {add_person(0, 0, 0)}, {remove_person(0)}, {get_person(0)}")

