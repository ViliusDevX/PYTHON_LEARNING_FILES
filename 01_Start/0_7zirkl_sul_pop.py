import random


def get_player_choice():
    player_input = int(input("pasirinkite: \n1.Sulinys \n2.zirkles \n3.popierius \n:"))
    return player_input


def get_computer_choice():
    return random.randint(1, 3)


def translate_choice(choice):
    if choice == 1:
        return "Sulinys"
    elif choice == 2:
        return "zirkles"
    elif choice == 3:
        return "popierius"

def player_draw(player_choice, computer_choice):
    if computer_choice == player_choice:
        return True
    else:
        return False

def new_game():
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    print(f"Kompas pasirinko:", translate_choice(computer_choice))
    if player_won(player_choice, computer_choice):
        print("laimejai")
    elif player_draw(player_choice, computer_choice):
        print("lygiosios")
    else:
        print("pralaimejai")


def player_won(player_choice, computer_choice):
    paper_over_rock = (player_choice == 3 and computer_choice == 1)
    scissors_over_paper = (player_choice == 2 and computer_choice == 3)
    rock_over_scissors = (player_choice == 1 and computer_choice == 2)
    if rock_over_scissors or paper_over_rock or scissors_over_paper:
        return True
    else:
        return False


new_game()


