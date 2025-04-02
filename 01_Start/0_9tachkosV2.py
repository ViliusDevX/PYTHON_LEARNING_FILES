import random

list_of_cars = [
    {
        "mark": "Nissan",
        "model": "Skyline",
        "in_garage": True

    },
    {
        "mark": "Buggati",
        "model": "Veyron",
        "in_garage": False
    },
    {
        "mark": "Pontiac",
        "model": "Aztec",
        "in_garage": False
    }
]


def get_random_car():
    len_cars = len(list_of_cars)
    random_index = random.randint(0, len_cars - 1)
    random_car_from_list = list_of_cars[random_index]
    return random_car_from_list


car_get = get_random_car()
print(car_get)
