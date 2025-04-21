import random, csv


def sim_run(dogs):
    all_dogs_chances = []
    for dog in dogs:
        dogs_chance_to_win = random.randint(0, dog['dogs_power'])
        dog_sim = {
            "dogs_name": dog['dogs_name'],
            "dogs_winning_chance": dogs_chance_to_win
        }
        all_dogs_chances.append(dog_sim)
    all_dogs_chances.sort(key=lambda x: x['dogs_winning_chance'], reverse=True)
    return all_dogs_chances


def sim_print(results):
    for dog in results:
        print(f"suns vardas: {dog['dogs_name']}, suns tikimybe laimeti: {dog['dogs_winning_chance']}")


def print_dogs(dogs):
    for dog in dogs:
        print(f"vardas: {dog['dogs_name']}\t\t {dog['dogs_power']}")


def csv_load(file_path):
    with open(file_path, 'r') as file:
        file_data = csv.DictReader(file, quoting=csv.QUOTE_NONNUMERIC)
        list_of_dicts = list(file_data)
        return list_of_dicts


def csv_save(file_path, list_of_dicts):
    keys = list_of_dicts[0].keys()
    with open(file_path, "w", newline="", encoding="utf-8") as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys, quoting=csv.QUOTE_NONNUMERIC)
        dict_writer.writeheader()
        dict_writer.writerows(list_of_dicts)
