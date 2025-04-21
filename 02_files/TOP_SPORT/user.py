from lib import sim_run, sim_print, print_dogs, csv_load, csv_save

logged_user = None

dogs = csv_load("./data/dogs.csv")
users = csv_load("./data/users.csv")


def registration():
    global users
    username_input = input("Ivesk username'a: ")
    pass_input = input("Ivesk pasworda:")
    bucks_qty_input = int(input("Ivesk pinigu kieki: "))
    user = {
        "username": username_input,
        "password": pass_input,
        "money": bucks_qty_input
    }
    users.append(user)


def login():
    global users
    ask_username = input("Ivesk savo userneima: ")
    ask_pass = input("Ivesk passworda: ")
    for user in users:
        if ask_username == user['username']:
            if ask_pass == user['password']:
                print("sekmingai uzsiloginai")
                return user
            else:
                raise Exception("blogas passwordas")
    raise Exception("blogas username'as")


def main_menu():
    global logged_user
    reg_or_login = int(input("1- Jeigu nori uzsireginti, 2- jeigu nori uzsiloginti: "))
    if reg_or_login == 1:
        registration()
        csv_save("data/users.csv", users)
    elif reg_or_login == 2:
        logged_user = login()
        user_menu()


def add_money():
    global logged_user
    how_much = int(input("Kiek nori prideti: "))
    logged_user['money'] += how_much
    csv_save("data/users.csv", users)


def betting():
    global dogs
    print(f"Sunu listas ir power'is :")
    print_dogs(dogs)
    bet_on_what_dog = input("Ant kokio suns betinsi (vardas/username): ")
    bet_how_much = int(input("Kiek euru betinsi:"))
    if bet_how_much > logged_user['money']:
        print("neturi pinigu")
        user_menu()
    sorted_dogs_run = sim_run(dogs)
    sim_print(sorted_dogs_run)
    if sorted_dogs_run[0]['dogs_name'] == bet_on_what_dog:
        print("laimejai")
        logged_user['money'] += (bet_how_much * 2)
    else:
        print("pralaimejai")
        logged_user['money'] -= bet_how_much
    csv_save("data/users.csv", users)


def user_menu():
    global logged_user
    print(f"Sveikas {logged_user['username']}")
    print(f"pasalpa: {logged_user['money']}")
    what_to_do = int(input("Ka nori, 1- jeigu inesti shaibu, 2- pabetinti ant suns, 3- atsijungti:"))
    if what_to_do == 1:
        add_money()
    elif what_to_do == 2:
        betting()
    elif what_to_do == 3:
        logged_user = None
        main_menu()
    else:
        raise Exception("kzk blogai")
    want_more = input("ar dar vesi kzk? (T arba N): ")
    if want_more == "T":
        user_menu()


# run_simulation()
main_menu()

#run_simulation grazina rezultatu lista
