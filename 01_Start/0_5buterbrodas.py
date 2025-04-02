bread_question = int(input("Kur geriausia ieskoti duonos?: \n1.Senukuose \n2.Paste \n3.Kuprineje :\n"))
bread_question_correct = 3
if bread_question == bread_question_correct:
    print("teisingai")
else:
    print("neteisingai")

butter_question = int(input("kur geriausia ieskoti sviesto?: \n1.Kalvarijuose \n2.Pasienyje \n3.Garaze :\n"))
butter_question_correct = 1
if butter_question == butter_question_correct:
    print("teisingai")
else:
    print("neteisingai")

meat_question = int(input("kur geriausia ieskoti mesos?: \n1.Gyme \n2.Lenkijoje \n3.Miske :\n"))
meat_question_correct = 2
if meat_question == meat_question_correct:
    print("teisingai")
else:
    print("neteisingai")

all_questions_correct = bread_question_correct and butter_question_correct and meat_question_correct

if all_questions_correct:
    print("Laimejai")
else:
    print("Nelaimejai")