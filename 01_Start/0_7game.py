one_answer_correct = 1
player2_total_correctly_answered_question = 0
player1_total_correctly_answered_question = 0


def new_turn(player_turn):
    if player_turn == 1:
        player_name = "Player #1"
        opponent_name = "Player #2"
    else:
        player_name = "Player #2"
        opponent_name = "Player #1"
    question = input(f"{player_name} Ivesk savo klausima:")
    answer1 = input("Ivesk 1 atsakymo varianta:")
    answer2 = input("Ivesk 2 atsakymo varianta:")
    answer3 = input("Ivesk 3 atsakymo varianta:")
    answer_correct = int(input("Kuris atsakymas teisingas?"))
    print(f"Perduok pc {opponent_name}'ui")
    print(question)
    answer_choice = int(input(f"pasirinkite teisinga varianta: 1.{answer1} 2.{answer2} 3.{answer3}"))
    if answer_choice == answer_correct:
        print("viskas gerai")
        return True
    else:
        print("blogai")
        return False




question1_correct = new_turn(1)
question2_correct = new_turn(2)
question3_correct = new_turn(1)
question4_correct = new_turn(2)
question5_correct = new_turn(1)
question6_correct = new_turn(2)

player1_all_questions_correct = question1_correct and question3_correct and question5_correct
player2_all_questions_correct = question2_correct and question4_correct and question6_correct

if player1_all_questions_correct and player2_all_questions_correct:
    print("viskas gerai")
else:
    print("viskas negerai")
