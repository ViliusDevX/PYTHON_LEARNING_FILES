import math

all_info = {
    "starting position" :{
        "x": 0,
        "y": 0
    },
    "current position" :{
        "x": 0,
        "y": 0
    },
    "all_moves" : []
}


LEFT = "kairen"
RIGHT = "desinen"
UP = "virsun"
DOWN = "apacion"


def set_start_pos(x, y):
    all_info["starting position"]["x"] = x
    all_info["starting position"]["y"] = y


def set_current_pos(x, y):
    all_info["current position"]["x"] = x
    all_info["current position"]["y"] = y


def ask_where_user_goes():
    possible_moves = LEFT, RIGHT, UP, DOWN
    print("Pasirinkimai:", possible_moves)
    print("Parasyk stop jeigu nori iseiti")
    ask_for_move = input(f"Kur eisi?")
    if ask_for_move in possible_moves:
        return ask_for_move
    elif ask_for_move == "stop":
        return None
    else:
        raise Exception("Negali ten eiti")


def game_turn():
    direction = ask_where_user_goes()
    if direction is not None:
        move_player(direction)
        print(all_info["current position"])
        game_turn()
    else:
        calculate_all_math_thing()


def adjust_current_pos(x, y):
    all_info["current position"]["x"] += x
    all_info["current position"]["y"] += y


def move_player(direction):
    if direction == LEFT:
        adjust_current_pos(-1, 0)
    elif direction == RIGHT:
        adjust_current_pos(1, 0)
    elif direction == UP:
        adjust_current_pos(0, 1)
    elif direction == DOWN:
        adjust_current_pos(0, -1)
    all_info["all moves"].append(direction)


def calculate_all_math_thing():
    all_moves = all_info["all moves"]
    current = all_info["current position"]
    starting = all_info["starting position"]
    distance_start_to_current = math.sqrt(math.pow(current["x"], 2) + math.pow(current["y"], 2))
    total_moves = len(all_info["all moves"])
    print(f"tavo dabartines koordinates: {current}, o startines: {starting}")
    print(f"Distancija nuo starto iki dabar: {distance_start_to_current}")
    print(f"Is viso buvo padaryta ejimu: {total_moves}")
    print(f"Ejimu istorija: {all_moves}")


game_turn()
