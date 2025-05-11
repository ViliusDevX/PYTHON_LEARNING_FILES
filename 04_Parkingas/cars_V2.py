from datetime import datetime


class Car:
    def __init__(self):
        self.time_difference = 0
        self.photo = "tačyla - dračyla"
        self.charge_rate_per_s = 1
        self.parked_time = None

    def park(self):
        self.parked_time = datetime.now()

    def calculate_parking_time(self):
        if self.parked_time is not None:
            current_time = datetime.now()
            self.time_difference = current_time - self.parked_time
            parking_time_ms = self.time_difference.total_seconds() * 1000
            return parking_time_ms

    def calculate_charge_for_parking(self):
        total_parking_charge = self.time_difference * self.charge_rate_per_s
        return total_parking_charge


class Truck(Car):
     def __init__(self):
        super().__init__()
        photo = "Trakas - barakas"
        charge_rate_per_second = self.charge_rate_per_s * 2


class Bus(Car):
    def __init__(self):
        super().__init__()
        photo = "Busas - pliusas"
        charge_rate_per_second = self.charge_rate_per_s * 3


car = Car()
car.park()
price = car.calculate_charge_for_parking()
print(price)
