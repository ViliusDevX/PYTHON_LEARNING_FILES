player_scores = []
word_list = []
player_names_list = []


def player_names():
    global player_names_list
    player1_name_input = input("player1 ivesk savo varda")
    player_names_list.append(player1_name_input)
    player2_name_input = input("player2 ivesk savo varda")
    player_names_list.append(player2_name_input)


def player_word_and_guess(word_list_1, word_list_2, player2_score, player1_score):
    player1_word = input("Ivesk  zodi:")
    word_list_1.append(player1_word)
    player2_guess = input("atspek jo  zodi:")
    player2_word = input("Ivesk  zodi:")
    word_list_2.append(player2_word)
    player1_guess = input("atspek jo  zodi:")
    if player2_guess == player1_word:
        print("atspejai")
        player2_score += 5
    else:
        print("neastpejai")
    if player1_guess == player2_word:
        print("atspejai")
        player1_score += 5
    else:
        print("neatspejai")




word_input = input("Ivesk sukurta zodi:")
