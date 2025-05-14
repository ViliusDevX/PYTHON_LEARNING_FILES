from kivy.uix.boxlayout import BoxLayout


class QuestionWidget(BoxLayout):  # The viewclass definitions, and property definitions.
    # Nereikia šito answer
    # answer = StringProperty()


def submit(self):
    answered_questions = []
    for child in self.children:
        widget = child.children[0]

        # Tau reikėjo su debuggeriu pasižiūrėt kas yra widget viduje
        # ten yra trys varaiblai pagal tai kuris checkbox'as užcheckintas:
        # checkbox1_active
        # checkbox2_active
        # checkbox3_active

        if widget.checkbox1_active:
            answer = "Disagree"
        elif widget.checkbox2_active:
            answer = "Neutral"
        elif widget.checkbox3_active:
            answer = "Agree"

        answered_questions.append(f"{widget.question} was answered with {answer}")

        # Čia buvo blogai, nes propertis answer visada tuščias widgete:
        # self.answers[question_id] = answer
        # ir tas self.answers bbž ką daro apskritai

    # Generate a sentence from the collected answers
    # Turejai pasidebugint koks gaunasi answer_sentence
    answered_questions_string = ", ".join(answered_questions)

    # Šitą žinutę gali dar patobulint, su debugeriu gali pasižiūrėt kaip susilipdo pilnai
    chatbot_query = f"Suggest 10 workplaces suitable for a person who did" \
                    f" a questionaire like this: {answered_questions_string}"

    # Šita f-ja nebeuri daryti visokių fancy dalykų, tiesiog nusiusti chatbot_query
    self.send_to_chatbot(chatbot_query)
    print("On Submit")
    # TODO: (RETURN?) checkbox_active, question, question_id