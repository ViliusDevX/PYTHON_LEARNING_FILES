from datetime import datetime
import cv2
import numpy as np
import time
import threading
import math


class Vehicle:
    def __init__(self):
        self.entry_time = time.time()
        self.payment_rate = 2 #EUR/s

    def get_stay_time(self):
        return int(time.time() - self.entry_time)

    def get_payment(self):
        stay_time = self.get_stay_time()
        return stay_time * self.payment_rate


class Car(Vehicle):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def get_payment(self):
        stay_time = self.get_stay_time()
        return stay_time * self.payment_rate

    def get_veichle_type(self):
        vehicle_type = Car()
        return vehicle_type


class Truck(Vehicle):
    def __init__(self, number):
        super().__init__()
        self.number = number
        self.charge_rate_per_s = self.payment_rate * 2

    def get_payment(self):
        stay_time = self.get_stay_time()
        return stay_time * self.charge_rate_per_s

    def get_veichle_type(self):
        vehicle_type = Truck()
        return vehicle_type


class Bus(Vehicle):
    def __init__(self, number):
        super().__init__()
        self.number = number
        self.charge_rate_per_s = self.payment_rate * 3

    def get_payment(self):
        stay_time = self.get_stay_time()
        return stay_time * self.charge_rate_per_s

    def get_veichle_type(self):
        vehicle_type = Bus()
        return vehicle_type


class Parking:
    def __init__(self):
        self.total_lot_price = 0
        self.spaces = []
        self.max_hor_lots = 4

    def menu(self):
        max_horizontal_parking = int(input("Max horizontal lots:"))
        num_parking_spaces = int(input("Max total lots:"))

        park = Parking()
        park.set_spaces(num_parking_spaces)
        park.set_max_horiontal_lots(max_horizontal_parking)

        display = Display(park, 100, 400)

        while True:
            display.display_parking_lot()

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break

            print("What would you like to do?")
            options = "1 - Accept a new vehicle\n2 - Release a vehicle\n0 - Close the program"
            decision = int(input(f"{options}\n\nYour choice: "))

            if decision == 1:
                print("1 - Car\n2 - Truck\n3 - Minibus")
                vehicle_type = input("Choose the type of vehicle: ")
                if vehicle_type == "1":
                    park.add_vehicle(Car, input("Enter vehicle number: ").strip())
                elif vehicle_type == "2":
                    park.add_vehicle(Truck, input("Enter vehicle number: ").strip())
                elif vehicle_type == "3":
                    park.add_vehicle(Bus, input("Enter vehicle number: ").strip())
            elif decision == 2:
                vehicle_num = input("Enter vehicle number: ")
                park.remove_vehicle(vehicle_num)
            elif decision == 0:
                break

        cv2.destroyAllWindows()

    def set_spaces(self, num_parking_spaces):
        self.spaces = [None] * num_parking_spaces

    def set_max_horiontal_lots(self, max_horizontal_lots):
        self.max_hor_lots = max_horizontal_lots

    def add_vehicle(self, vehicle_type, number):
        vehicle = vehicle_type(number)

        for i, space in enumerate(self.spaces):
            if space is None:
                self.spaces[i] = vehicle
                print(f"Assigned parking space: {i + 1}")
                return

    def remove_vehicle(self, vehicle_num):
        for i, vehicle in enumerate(self.spaces):
            if vehicle is not None and vehicle.number == vehicle_num:
                payment = vehicle.get_payment()
                print(f"Payment for vehicle {vehicle_num}: {payment} EUR")
                self.spaces[i] = None
                self.total_lot_price += payment
                return


class Display:
    def __init__(self, park, parking_space_width, parking_space_height):
        self.vehicle_images = {
            "car": cv2.imread("parked_car.png", cv2.IMREAD_UNCHANGED),
            "truck": cv2.imread("truck.png", cv2.IMREAD_UNCHANGED),
            "bus": cv2.imread("minibus.png", cv2.IMREAD_UNCHANGED),
        }

        self.space_images = {
            "single_space": cv2.imread("parking-single-space.png"),
            "empty_space": cv2.imread("parking-empty-space.png")
        }
        self.parking_inst = park
        self.parking_space_width = parking_space_width
        self.parking_space_height = parking_space_height

    def display_parking_lot(self):

        num_spaces = len(self.parking_inst.spaces)
        ceiled_lot_rows = math.ceil(num_spaces / self.parking_inst.max_hor_lots)
        parking_lot_width = self.parking_inst.max_hor_lots * self.parking_space_width
        parking_lot_height = self.parking_space_height * ceiled_lot_rows

        parking_lot_image = np.zeros((parking_lot_height, parking_lot_width, 3), dtype=np.uint8)
        total = 0
        for row_index in range(ceiled_lot_rows):
            for col in range(self.parking_inst.max_hor_lots):
                x, y = (col * 100, row_index * 400)
                total += 1

                image_to_display = self.space_images["empty_space"] if total > num_spaces else self.space_images[
                    "single_space"]
                self.display_parking_space(parking_lot_image, image_to_display, x, y)

        print(total)

        text = f"Earnings: {self.parking_inst.total_lot_price}"
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        font_color = (255, 255, 255)
        font_thickness = 2

        # cv2.putText(parking_lot_image, text, (x, y), font, font_scale, font_color, font_thickness)
        for lot, vehicle in enumerate(self.parking_inst.spaces):
            if vehicle is not None:
                self.display_vehicle(parking_lot_image, vehicle, lot)



        #todo: sutavrkyti putText cv2




        cv2.imshow("Parking Lot with Vehicle and Text", parking_lot_image)

    def display_parking_space(self, background, parking_image, x, y):
        background[y:y+parking_image.shape[0], x:x+parking_image.shape[1]] = parking_image

    def display_vehicle(self, parking_lot_image, vehicle, lot_num):
        vehicle_type = self.get_vehicle_type(vehicle)
        vehicle_image = self.vehicle_images[vehicle_type]

        if vehicle_image.shape[2] == 4:
            vehicle_image = cv2.cvtColor(vehicle_image, cv2.COLOR_BGRA2BGR)

        vehicle_height, vehicle_width, _ = vehicle_image.shape


        if lot_num * self.parking_space_width + vehicle_width <= parking_lot_image.shape[1] and \
                vehicle_height <= self.parking_space_height:
            parking_lot_image[0:vehicle_height,
            lot_num * self.parking_space_width:(lot_num + 1) * self.parking_space_width] = vehicle_image

    def get_vehicle_type(self, vehicle):
        if isinstance(vehicle, Car):
            return "car"
        elif isinstance(vehicle, Truck):
            return "truck"
        elif isinstance(vehicle, Bus):
            return "bus"


park = Parking()
park.menu()