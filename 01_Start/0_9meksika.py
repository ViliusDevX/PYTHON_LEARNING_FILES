import random

autostop_list = [
    {
        "distance" : 70,
        "money" : 20,
        "energy" : 2,
        "health" : 1,
        "max_uses": 2,
        "name": "Verslininkas"
    },
    {
        "distance" : 5,
        "money" : -10,
        "max_uses": 2,
        "name": "Vagis"
    }
]

bus = [
    {
        "distance": 100,
        "energy": 2,
        "money": -10,
        "name": "Trumpieji_reisai"
    },
    {
        "distance": 250,
        "energy": 4,
        "money": -25,
        "name": "Ilgieji reisai"
    }
]

game = {
    "moves" : 0,
    "distance_to_wall" : 1000,
    "money" : 10,
    "energy" : 10,
    "health" : 10
}


def choose_how_to_move():
    random_num = random.randint(0, 1)
    end_of_move = print(f"Ejimo nr. ")
    ON_FOOT = "Eiti peskomis"
    BY_BUS = "Vaziuoti autobusu"
    AUTOSTOP = "Tranzuoti"
    choose_moves = input(f"Kaip nori judeti? Galimi ejimai: {ON_FOOT, BY_BUS, AUTOSTOP}")
    if choose_moves == ON_FOOT:
        random_distance = random.randint(10, 35)
        game["moves"] += 1
        game["energy"] -= 3
        game["distance_to_wall"] -= random_distance
        money_chance = bool(round(random_num))
        if money_chance:
            money_qty = random.randint(5, 20)
            game["money"] += money_qty
    elif choose_moves == BY_BUS:
        random_bus = random.choice(bus)
        game["moves"] += 1
        game["energy"] += random_bus["energy"]
        game["money"] += random_bus["money"]
        game["distance_to_wall"] -= random_bus["distance"]
    elif choose_moves == AUTOSTOP:
        random_car = random.choice(autostop_list)
        game["moves"] += 1
        game["energy"] += random_car["energy"]
        game["money"] += random_car["money"]
        game["distance_to_wall"] -= random_car["distance"]
    else:
        print("Kazka blogai ivedei")
    print(game)



def player_dies():
    if game["health"] <= 0:
        print("Sveikatai blogai")
    elif game["energy"] <= 0:
        print("Mirei nuo issekimo")

def end_game():
    choose_how_to_move()
    if choose_how_to_move() != player_dies():
        choose_how_to_move()

end_game()