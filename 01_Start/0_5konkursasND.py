one_answer_correct_score = 50
player_total_score = 0

jungle_king_question = int(input("Kas sumuse nepilnameti?: \n1.Viršila \n2.Maybachas \n3.Justinas Jarutis \n:"))
jungle_king_question_correct = 1
if jungle_king_question == jungle_king_question_correct:
    print(f"Gauni: {one_answer_correct_score} balu")
    player_total_score += one_answer_correct_score
else:
    print("neteisingai")

arrest_question = int(input("Kas yra sedejes uz grotu?: \n1.Gražulis \n2.SELas \n3.Valinskas \n:"))
arrest_question_correct = 2
if arrest_question == arrest_question_correct:
    print(f"Gauni: {one_answer_correct_score} balu")
    player_total_score += one_answer_correct_score
else:
    print("neteisingai")

beer_question = int(input("Kur alus pigiausias?: \n1.Norfoj \n2.Siauliuose \n3.Lenkijoj \n:"))
beer_question_correct = 3
if beer_question == beer_question_correct:
    print(f"Gauni: {one_answer_correct_score} balu")
    player_total_score += one_answer_correct_score
else:
    print("neteisingai")

print(f"surinkai: {player_total_score} tasku")
if player_total_score == 150:
    print("laimejai aukso puoda")
