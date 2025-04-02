import random

list_of_cars = {
    {
        "Markė": "Nissan",
        "Modelis": "Skyline",
        "Yra sandėlyje": "Taip"

    },
    {
        "Markė": "Buggati",
        "Modelis": "Veyron",
        "Yra sandėlyje": "Ne"
    },
    {
        "Markė": "Pontiac",
        "Modelis": "Aztec",
        "Yra sandėlyje": "Ne"
    }
}


def get_random_car():
    random_number = random.randint(0, 2)
    random_word_from_list = list_of_cars[random_number]
    return random_word_from_list


print(list_of_cars.get(get_random_car(), None))
