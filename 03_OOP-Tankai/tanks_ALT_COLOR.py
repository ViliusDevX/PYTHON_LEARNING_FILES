import cv2
import threading


COLOR_MAP = {
    "blue": (255, 0, 0),     # Blue
    "yellow": (0, 255, 255), # Yellow
    "white": (255, 255, 255), # White
    "red": (0, 0, 255)      # Red
}


class Tank:
    def __init__(self, name):
        self.x = 0
        self.y = 0
        self.name = name
        self.tank_color = None

    def move_up(self):
        self.y -= 1

    def move_down(self):
        self.y += 1

    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1

    def get_coords(self):
        return self.x, self.y

    def return_color(self):
        return self.tank_color

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
            tank_color = COLOR_MAP.get(tank.return_color().lower(), (0, 0, 0))

            cv2.rectangle(
                frame,
                (tank.x * tank_width, tank.y * tank_height),
                (tank.x * tank_width + tank_width, tank.y * tank_height + tank_height),
                tank_color,
                -1,
            )

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
        colors = []
        blue = (0,0,255)
        yellow = (255,255,0)
        white = (255,255,255)
        red = (255,0,0)
        players_qty = int(input("Kiek bus iš viso žaidėjų?: "))
        for player in range(players_qty):
            player_name = input("Įvesk savo vardą:")
            tank_color = input(f"Kokios spalvos bus tankas 1 - melyna, 2 - geltona, 3 - balta, 4 - raudona:")
            if tank_color == 1:
                tank_color = blue
                colors.append(tank_color)
            elif tank_color == 2:
                tank_color = yellow
                colors.append(tank_color)
            elif tank_color == 3:
                tank_color = white
                colors.append(tank_color)
            elif tank_color == 4:
                tank_color = red
                colors.append(tank_color)

            tank_color = tank_color.lower()
            if tank_color in COLOR_MAP:
                print("eroras nx: Blogai pasirinkai spalva")
                continue

            tank = Tank(player_name)
            tank.tank_color = tank_color
            self.add_tank(tank)

    def next_turn(self):
        for tank in self.tanks:
            print(f"{tank.name} eilė. Kur eisi?")
            if (tank.x == 0) and (tank.y == 0):
                player_move = int(input("1 - Į apačią, 2 - Į dešinę:"))
                if player_move == 1:
                    tank.move_down()
                elif player_move == 2:
                    tank.move_right()
            elif (tank.x > 0) and (tank.y == 0):
                player_move = int(input("1 - Į apačią, 2 - Į dešinę, 3 - i kaire:"))
                if player_move == 1:
                    tank.move_down()
                elif player_move == 2:
                    tank.move_right()
                elif player_move == 3:
                    tank.move_left()
            else:
                player_move = int(input("1 - Į apačią, 2 - Į dešinę, 3 - i kaire, 4 - i virsu:"))
                if player_move == 1:
                    tank.move_down()
                elif player_move == 2:
                    tank.move_right()
                elif player_move == 3:
                    tank.move_left()
                elif player_move == 4:
                    tank.move_up()


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
