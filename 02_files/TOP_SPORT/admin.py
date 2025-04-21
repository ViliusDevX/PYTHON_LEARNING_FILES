from lib import sim_run, sim_print, print_dogs, csv_load, csv_save


dogs = csv_load("./data/dogs.csv")


def menu():
    what_to_do = int(input("Ka nori, 1- jeigu isspausdinti turimus sunys, "
                            "2- jeigu sukurti nauja, 3- paleist simuliacija:"))
    if what_to_do == 1:
        print_dogs()
    elif what_to_do == 2:
        add_dogs_admin()
        csv_save("./data/dogs.csv", dogs)
    elif what_to_do == 3:
        all_dogs_chances = sim_run(dogs)
        sim_print(all_dogs_chances)
    else:
        raise Exception("kazkas blogai")
    want_more = input("ar dar vesi kazka? (T arba N): ")
    if want_more == "T":
        menu()


def add_dogs_admin():
    global dogs
    how_much_dogs_to_add = int(input("Kiek sunu nori sukurti?: "))
    for dog in range(how_much_dogs_to_add):
        dogs_name = input("Sukurk varda suniui: ")
        dog_power = int(input("Koks suns power'is?: "))
        dog = {
            "dogs_name": dogs_name,
            "dogs_power": dog_power,
        }
        dogs.append(dog)


menu()




