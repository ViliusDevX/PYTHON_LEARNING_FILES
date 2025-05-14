from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty, BooleanProperty, DictProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivymd.app import MDApp


class QuestionWidget(BoxLayout):  # The viewclass definitions, and property definitions.
    question = StringProperty()
    question_id = StringProperty()
    checkbox1_active = BooleanProperty(False)
    checkbox2_active = BooleanProperty(False)
    checkbox3_active = BooleanProperty(False)


class QuestionList(RecycleView):
    ai_answer = None
    # questions = ListProperty()  # A list property is used to hold the data for the recycleview, see the kv code
    # answers = DictProperty({})  # A list property is used to hold the data for the recycleview, see the kv code

    def __init__(self, **kwargs):
        self.questions = [
            {"question": "I'm 20 years old", "question_id": "1"},
            {"question": "I like to work alone", "question_id": "2"},
            {"question": "I'm systematic", "question_id": "3"},
            {"question": "I'm introverted", "question_id": "4"},
            {"question": "I like flexible environments", "question_id": "5"},
            {"question": "I'm methodical and systematic", "question_id": "6"},
            {"question": "I'm innovative and creative", "question_id": "7"},
            {"question": "I involve and collaborate with others for solutions", "question_id": "8"},
            {"question": "I prefer working independently", "question_id": "9"},
            {"question": "I seek mediation and involve others to find a solution", "question_id": "10"},
            {"question": "I prioritize tasks and manage them sequentially", "question_id": "11"},
            {"question": "I follow a structured schedule and prioritize systematically", "question_id": "12"},
            {"question": "I embrace change by exploring new possibilities", "question_id": "13"},
            {"question": "I prefer structured environments for clarity and focus", "question_id": "14"},
            {"question": "I'm a leader - prefer taking charge and guiding the team", "question_id": "15"},
            {"question": "I find compromises and common ground through discussion", "question_id": "16"},
            {"question": "I enjoy contributing equally with others", "question_id": "17"},
            {"question": "I'm pursuing formal education and certifications", "question_id": "18"},
            {"question": "I've embraced change by exploring new possibilities", "question_id": "19"},
            {"question": "I prioritize tasks and manage them sequentially", "question_id": "20"},
            {"question": "I prefer a quiet and structured environment for focused work", "question_id": "21"},
            {"question": "I seek personal growth and learning", "question_id": "22"},
            {"question": "I'm comfortable with both depending on the nature of the work", "question_id": "23"},
            {"question": "I adapt and prioritize based on urgency and importance", "question_id": "24"},
            {"question": "I've delegated tasks or sought help to manage multiple responsibilities","question_id": "25"},
            {"question": "I enjoy a dynamic and collaborative space for idea exchange", "question_id": "26"},
            {"question": "I enjoy a dynamic and collaborative space for idea exchange", "question_id": "27"},
            {"question": "I manage multiple responsibilities by delegating tasks or seeking help", "question_id": "28"}
        ]

        super().__init__(**kwargs)


    def submit(self):
        answered_questions = []
        for child in self.children:
            widget = child.children[0]

            answer = "No response"

            if widget.checkbox1_active:
                answer = "Disagree"
            elif widget.checkbox2_active:
                answer = "Neutral"
            elif widget.checkbox3_active:
                answer = "Agree"

            question = f"{widget.question} was answered with {answer}"
            answered_questions.append(question)

        chatbot_query = f"Suggest 10 workplaces suitable for a person who did" \
                            f" a questionaire like this: {answered_questions}"

        # After collecting all the answered questions, send them to the chatbot
        # self.send_to_chatbot(chatbot_query)
        print("On Submit")

    def send_to_chatbot(self, questions):
        import requests  # Assuming you use requests library for API requests

        url = "https://simple-chatgpt-api.p.rapidapi.com/ask"
        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "X-RapidAPI-Key": "my api",
            "X-RapidAPI-Host": "simple-chatgpt-api.p.rapidapi.com"
        }

        for question in questions:
            payload = {
                'question': question,
                # Add any other required payload data for your chatbot API
            }

            # Make an API request to send the question to the chatbot
            response = requests.post(url, headers=headers, data=payload)

            # Process the response accordingly
            if response.status_code == 200:
                chatbot_response = response.text  # Extract chatbot's response
                print(f"Question: {question}, Chatbot Response: {chatbot_response}")
            else:
                print(f"Failed to send question: {question}. Status code: {response.status_code}")
                # Handle failed API request accordingly


class MainApp1(MDApp):
    def build(self):
        # Access the QuestionList instance
        # ... (do something with the question_list, add it to your interface, etc.)

        # For the purpose of this example, calling the submit method
        return Builder.load_file('wrong_main.kv')


if __name__ == '__main__':
    MainApp1().run()
