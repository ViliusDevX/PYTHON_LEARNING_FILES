import random
players_word_list = []


def write_your_word():
    global players_word_list
    player_word_input_in_list = input("Ivesk savo zodi:")
    print("sugalvok dar viena zodi arba spausk enter")
    if player_word_input_in_list != "":
        players_word_list.append(player_word_input_in_list)
        write_your_word()


def random_list_word():
    global players_word_list
    how_much_words_in_list = len(players_word_list)
    random_number = random.randint(0, how_much_words_in_list - 1)
    random_word_from_list = players_word_list[random_number]
    player_guess_random_word = int(input(f"Kelintas zodis yra {random_word_from_list}?:"))
    if player_guess_random_word == random_number + 1:
        print("Su atmintim viskas gerai")
    else:
        print("Maziau gerk")


write_your_word()
random_list_word()




