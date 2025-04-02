from datetime import datetime

people = []
age_of_all_people = 0
people_qty = int(input("Kiek zmoniu norite uzregistruoti?: "))


def calculate_avg_age():
    global age_of_all_people
    global people_qty
    people_avg_age = age_of_all_people / people_qty
    return people_avg_age


def add_person():
    global age_of_all_people
    today_date = datetime.now()
    people_name = input("Iveskit zmogaus varda: ")
    birth_date = input("Iveskit gimimo data(pvz.: 1955-04-12): ")
    date_of_birth = datetime.strptime(birth_date, "%Y-%m-%d")
    age = today_date.year - date_of_birth.year
    age_of_all_people += age
    person_dict = {
        "name": people_name,
        "date_of_birth": birth_date,
        "age": age
    }
    people.append(person_dict)


def print_people():
    age_average = calculate_avg_age()
    print(f"Visu zmoniu amziaus vidurkis: {age_average}")
    for person in people:
        age = person["age"]
        print(person["name"])
        print(age_average - person["age"])
        if age > age_average:
            more_than_avg_age = age - age_average
            print(f"{more_than_avg_age} daugiau nei vidurkis")
        elif age < age_average:
            less_than_avg_age = age_average - age
            print(f"{less_than_avg_age} maziau nei vidurkis")
        else:
            print("Toks pat kaip bendras amziaus vidurkis")


for person_num in range(people_qty):
    add_person()

print_people()

print(people)


