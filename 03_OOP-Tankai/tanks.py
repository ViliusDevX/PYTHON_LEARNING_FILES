import pygame, threading


class Tank:
    def __init__(self, name):
        self.x = 0
        self.y = 0
        self.name = name

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1
        
    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1

    def get_cords(self):
        return self.x, self.y


class Battleground:
    def __init__(self):
        self.tanks = []
        self.COLOR_WHITE = (255, 255, 255)
        self.COLOR_GREEN = (0, 255, 0)
        self.screen = None
        self.clock = pygame.time.Clock()
        self.prepare_screen()

    def prepare_screen(self):
        pygame.init()

        screen_width, screen_height = 800, 600

        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Tank Game")

    def display_frame(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        self.screen.fill(self.COLOR_WHITE)
        tank_width, tank_height = 50, 50

        for tank in self.tanks:
            pygame.draw.rect(self.screen, self.COLOR_GREEN, (tank.x, tank.y, tank_width, tank_height))

        pygame.display.flip()

    def run_display(self):
        while True:
            pygame.event.pump()
            self.display_frame()
            self.clock.tick(60)

    def play(self):
        pygame_thread = threading.Thread(target=self.run_display)
        pygame_thread.start()

        while True:
            self.next_turn()

    def player_registration(self):
        players_qty = int(input("Kiek bus is viso zaideju?: "))
        for player in range(players_qty):
            player_name = input("Ivesk savo varda:")
            tank = Tank(player_name)
            self.add_tank(tank)

    def next_turn(self):
        for tank in self.tanks:
            print(f"{tank.name} eile. Kur eisi?")
            player_move = int(input("1 - I virsu, 2- i apacia, 3 - kairen. 4 - i desine:"))

            if player_move == 1:
                tank.move_up()
            elif player_move == 2:
                tank.move_down()
            elif player_move == 3:
                tank.move_left()
            elif player_move == 4:
                tank.move_right()

            print(f"{tank.name} paejo")
            self.print_tank_cords()
            self.display_frame()

    # def play(self):
    #     while True:
    #         self.next_turn()

    def add_tank(self, tank):
        self.tanks.append(tank)

    def print_tank_cords(self):
        for tank in self.tanks:
            tank_cords = tank.get_cords()
            print(tank_cords)


tank = Tank("sfhiaohmfisau892714")
my_game = Battleground()
my_game.add_tank(tank)
my_game.play()
