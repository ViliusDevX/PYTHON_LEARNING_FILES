class Parking:
    def __init__(self):
        self.spaces = [None, None, None, None, None]
        self.total_lot_price = 0
        self.rate_per_minute = 2
        self.lot_price = 1

    def add_car(self):
        number = input("Ivesk masinos numeri: ").strip()
        car = Car(number)

        for i in range(len(self.spaces)):
            if self.spaces[i] is None:
                self.spaces[i] = car
                print(f"Priskirta parkingo vieta : {i + 1}")
                return

    def remove_car(self):
        car_num = input("Ivesk numeri: ")

        for i, car in enumerate(self.spaces):
            if car is not None and car.return_number() == car_num:
                payment = car.get_payment(self.rate_per_minute)
                print(f"Payment for car {car_num}: {payment} EUR")
                self.spaces[i] = None
                self.total_lot_price += payment
                return

        print(f"{car_num} nera tokios masinos.")

    def menu(self):
        while True:
            print("Ka norite daryti?")
            options = "1 - Priimti nauja tačka\n 2 - Isleisti tačka\n 0 - Uždaryti programą"
            decision = int(input(f"{options}\n\nTavo pasirinkimas: "))

            if decision == 1:
                self.add_car()
            elif decision == 2:
                self.remove_car()
            elif decision == 0:
                break