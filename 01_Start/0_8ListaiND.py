def ask_one_more_question(question_list=[]):
    if question_list:
        question_list = []
    ask = input("Ar dar nori sukurti viena klausima? (T/N)")
    if ask == "T":
        question_input = input("Iveskite klausima:")
        answer_input = input("Iveskite teisinga atsakyma:")
        question_list.append([question_input, answer_input])
        ask_one_more_question(question_list)
    else:
        print(question_list)


ask_one_more_question()
