all_players = {
     "1_player": {
         "x" : 0,
         "y" : 0,
         "name" : ""
    },
    "2_player": {
         "x" : 0,
         "y" : 0,
        "name" : ""
    }
}


def reg_player(id):
    player_name = input(f"user N{id} Ivesk savo varda")
    player_tank_x_input = int(input(f"{player_name} Ivesk savo tanko x koordinates"))
    player_tank_y_input = int(input(f"{player_name} Ivesk savo tanko y koordinates"))
    all_players[f"{id}_player"]["name"] = player_name
    all_players[f"{id}_player"]["x"] = player_tank_x_input
    all_players[f"{id}_player"]["y"] = player_tank_y_input


def shoot_tanks(id):
    player_name = all_players[f"{id}_player"]["name"]

    if id == 1:
        enemy_id = 2
    elif id == 2:
        enemy_id = 1

    enemy_cords = all_players[f"{enemy_id}_player"]
    player_shoots_x_tank = int(input(f"{player_name} ivesk x koordinates kur sausi"))
    player_shoots_y_tank = int(input(f"{player_name} ivesk y koordinates kur sausi"))

    if (player_shoots_x_tank == enemy_cords["x"]) and (player_shoots_y_tank == enemy_cords["y"]):
        print(f"Laimejo {player_name}")
    else:
        print("Nepataikei")
        shoot_tanks(id)


def game():
    reg_player(1)
    reg_player(2)
    shoot_tanks(1)


game()
