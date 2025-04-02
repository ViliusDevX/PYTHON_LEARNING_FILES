from datetime import datetime
list_of_cars = {
    "KRT466": {
        "tech_inspect_date": "1999-1-1",
        "mark": "Tayota",
        "model": "Gorola"
    },
    "JRI913": {
        "tech_inspect_date": "2000-12-20",
        "mark": "Audi",
        "model": "Silke"
    },
    "SFM555": {
        "tech_inspect_date": "1889-12-01",
        "mark": "Daimler",
        "model": "Stahlradwagen"
    },
    "AFJ457": {
        "tech_inspect_date": "2024-01-02",
        "mark": "Volkswagen",
        "model": "Golf"
    }
}


def ask_for_license_plate():
    input_license_plate = input("Ivesk tachkos numeri")
    if input_license_plate != "":
        if input_license_plate not in list_of_cars:
            raise Exception("Nera tokios masinos numerio")
    return input_license_plate


def check_if_license_plate_valid(car_plate_num):
    present = datetime.now()
    car = list_of_cars.get(car_plate_num, None)
    if car is not None:
        get_car_expiration_date = datetime.strptime(car["tech_inspect_date"], "%Y-%m-%d")
        if get_car_expiration_date > present:
            return True
        elif get_car_expiration_date < present:
            return False
    else:
        raise Exception("Nera masinos su tokiais numeriais")


def check_license_plates():
    input_license_plate = ask_for_license_plate()
    if input_license_plate != "":
        license_valid = check_if_license_plate_valid(input_license_plate)
        print(f"Tech apziura masinai: ", "Galioja" if license_valid else "Negalioja")
        check_license_plates()


check_license_plates()
