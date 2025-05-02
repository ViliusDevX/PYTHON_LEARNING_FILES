def player_registration(self):
    colors = []
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
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
        if tank_color in colors:
            print("spalva jau naudojama kito tanko")
        tank = Tank(player_name)
        tank.tank_color = tank_color
        self.add_tank(tank)

if chosen_tank_direction == "up":
    tank.move_up()
elif chosen_tank_direction == "down":
    tank.move_down()
elif chosen_tank_direction == "left":
    tank.move_left()
elif chosen_tank_direction == "right":
    tank.move_right()