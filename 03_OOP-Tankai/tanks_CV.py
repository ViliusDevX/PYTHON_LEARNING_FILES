import cv2
import threading
import random
import numpy as np


class Tank:
    def __init__(self, name, x, y, skin):
        self.x = x
        self.y = y
        self.name = name
        self.direction = "up"
        self.tank_skin = skin

    def move_up(self):
        self.y -= 1
        self.direction = "up"

    def move_down(self):
        self.y += 1
        self.direction = "down"

    def move_right(self):
        self.x += 1
        self.direction = "right"

    def move_left(self):
        self.x -= 1
        self.direction = "left"

    def get_coords(self):
        return self.x, self.y

    def get_direction(self):
        return self.direction

    def get_enemy_tanks_in_direction(self, tanks):
        cord_list = []
        targets = []
        print(self.direction)
        if self.direction == "up":
            for i in range(0, self.y - 1):
                cord_list.append((self.x, i))

        elif self.direction == "down":
            for i in range(self.y + 1, 16):
                cord_list.append((self.x, i))

        elif self.direction == "left":
            for i in range(0, self.x - 1):
                cord_list.append((i, self.y))

        elif self.direction == "right":
            for i in range(self.x + 1, 16):
                cord_list.append((i, self.y))

        for tank in tanks:
            print(self.x, self.y)
            print(cord_list)
            if (tank.x, tank.y) in cord_list:
                targets.append(tank)

        return targets


class Battleground:
    def __init__(self):
        self.tanks = []
        self.COLOR_WHITE = (255, 255, 255)
        self.COLOR_GREEN = (0, 255, 0)
        self.prepare_screen()

    def prepare_screen(self):
        self.screen_width, self.screen_height = 800, 800
        frame = None

    def display_frame(self):
        frame = cv2.imread("background.jpg")

        tank_width, tank_height = 50, 50

        grid_spacing = 50
        grid_color = (255, 255, 255)
        line_thickness = 1

        for x in range(0, frame.shape[1], grid_spacing):
            cv2.line(frame, (x, 0), (x, frame.shape[0]), grid_color, line_thickness)

        for y in range(0, frame.shape[0], grid_spacing):
            cv2.line(frame, (0, y), (frame.shape[1], y), grid_color, line_thickness)

        for tank in self.tanks:
            tank_x = tank.x * tank_width
            tank_y = tank.y * tank_height
            image = cv2.imread(tank.tank_skin, cv2.IMREAD_UNCHANGED)
            tank_direction = tank.get_direction()

            if tank_direction == "down":
                angle = 0
            elif tank_direction == "up":
                angle = 180
            elif tank_direction == "right":
                angle = 90
            elif tank_direction == "left":
                angle = 270

            center = (image.shape[1] // 2, image.shape[0] // 2)

            rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
            rotated_tank_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))

            for c in range(0, 3):
                frame[tank_y:tank_y + tank_height, tank_x:tank_x + tank_width, c] = \
                    frame[tank_y:tank_y + tank_height, tank_x:tank_x + tank_width, c] * \
                    (1 - rotated_tank_image[:, :, 3] / 255.0) + rotated_tank_image[:, :, c] * (rotated_tank_image[:, :, 3] / 255.0)

        cv2.imshow("Tank Game", frame)
        cv2.waitKey(1)

    def run_display(self):
        while True:
            self.display_frame()

    def play(self):
        pygame_thread = threading.Thread(target=self.run_display)
        pygame_thread.start()

        while True:
            self.next_turn()

    def player_registration(self):
        skins = ["tank1.png", "tank2.png", "tank3.png", "tank4.png"]
        players_qty = int(input("Kiek bus iš viso žaidėjų?(maks. 4): "))
        starting_positions = [(0, 0), (15, 0), (15, 15), (0, 15)]
        for player in range(players_qty):
            player_name = input("Įvesk savo vardą:")
            starting_x, starting_y = starting_positions[player]
            tank = Tank(player_name, starting_x, starting_y, skins[player])
            print(player)
            self.add_tank(tank)

    def can_hit(self, shooter_tank):
        target_tank = None
        for t in self.tanks:
            if shooter_tank != t:
                if shooter_tank.direction == "up" and t.direction == "down" and \
                        shooter_tank.x == t.x and shooter_tank.y > t.y:
                    target_tank = t
                elif shooter_tank.direction == "down" and t.direction == "up" and \
                        shooter_tank.x == t.x and shooter_tank.y < t.y:
                    target_tank = t
                elif shooter_tank.direction == "left" and t.direction == "right" and \
                        shooter_tank.y == t.y and shooter_tank.x > t.x:
                    target_tank = t
                elif shooter_tank.direction == "right" and t.direction == "left" and \
                        shooter_tank.y == t.y and shooter_tank.x < t.x:
                    target_tank = t

        if target_tank:
            print(f"{shooter_tank.name} can hit {target_tank.name}!")
            user_choice = input(f"Do you want to destroy {target_tank.name}? (yes/no): ")
            if user_choice.lower() == "yes":
                self.tanks.remove(target_tank)
                print(f"{shooter_tank.name} destroyed {target_tank.name}!")
                return True

            return False

    def next_turn(self):
        for tank in self.tanks:
            available_directions = {"up": "Į viršų", "down": "Į apačią", "left": "Į kairę", "right": "Į dešinę"}

            if tank.x == 0:
                del available_directions["left"]
            elif tank.x == 15:
                del available_directions["right"]

            if tank.y == 0:
                del available_directions["up"]
            elif tank.y == 15:
                del available_directions["down"]

            print("Galimos kryptis: ")

            dir_index = 1
            for i in available_directions.values():
                print(f"{dir_index} - {i}")
                dir_index += 1

            player_move = int(input("Tavo pasirinkimas: "))
            tank_direction = list(available_directions)[player_move - 1]

            if tank_direction == "left":
                tank.move_left()
            if tank_direction == "right":
                tank.move_right()
            if tank_direction == "up":
                tank.move_up()
            if tank_direction == "down":
                tank.move_down()

            enemies = tank.get_enemy_tanks_in_direction(self.tanks)

            if len(enemies) > 0:
                for target in enemies:
                    print(f"{tank.name} pastebėjo priešą ({target.name})!")

                tank_shooting = input("Jeigu nori sunaikinti tanką, spausk - 1, jeigu ne - 2: ")

                if tank_shooting == "1":
                    for enemy in enemies:
                        self.tanks.remove(enemy)
                        print(f"{tank.name} sunaikino tanką {enemy.name}!")

            print(f"{tank.name} pajudėjo")
            self.print_tank_coords()
            self.display_frame()

    def add_tank(self, tank):
        self.tanks.append(tank)

    def print_tank_coords(self):
        for tank in self.tanks:
            tank_cords = tank.get_coords()
            print(tank_cords)


my_game = Battleground()
my_game.player_registration()
my_game.play()
