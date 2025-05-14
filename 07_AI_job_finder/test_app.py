from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
import requests


class QuestionnaireApp(App):
    def build(self):
        self.questions = [
            "I am systematic.",
            "I am introverted.",
            "I enjoy working in teams.",
            "I am detail-oriented.",
            "I prefer creative tasks.",
            "I am comfortable with public speaking.",
            "I am adaptable to change.",
            "I am good at problem-solving.",
            "I am highly organized.",
            "I am a quick learner.",
            "I prefer routine tasks.",
            "I am comfortable with ambiguity.",
            "I enjoy helping others.",
            "I am good at multitasking.",
            "I am comfortable with technology.",
            "I prefer working independently.",
            "I am assertive.",
            "I am patient.",
            "I enjoy analyzing data.",
            "I am a good communicator."
            # Add more questions here...
        ]
        self.answers = {}

        layout = BoxLayout(orientation='vertical')
        for question in self.questions:
            checkbox_layout = BoxLayout(orientation='horizontal')
            checkbox_layout.add_widget(CheckBox())
            checkbox_layout.add_widget(Button(text='Agree', on_press=self.submit_answer))
            layout.add_widget(checkbox_layout)

        submit_button = Button(text='Submit Answers', on_press=self.submit_answers)
        layout.add_widget(submit_button)
        return layout

    def submit_answer(self, instance):
        for index, child in enumerate(instance.parent.children):
            if child == instance:
                self.answers[self.questions[index]] = 'Agree'
                self.answers[self.questions[index]] = 'Neutral'
                self.answers[self.questions[index]] = 'DisagreeDisagree'

    def submit_answers(self, instance):
        # Assuming self.answers is fully populated
        text = f"Give 5 suitable jobs for a person that answered questionnaire like this: {self.answers}"

        # headers = {
        #     'content-type': 'application/x-www-form-urlencoded',
        #     'X-RapidAPI-Key': '61ae18e284msha3b0829248b1f92p168783jsn35231083b64e',
        #     'X-RapidAPI-Host': 'simple-chatgpt-api.p.rapidapi.com'
        # }
        #
        # response = requests.post(
        #     'https://simple-chatgpt-api.p.rapidapi.com/ask',
        #     headers=headers,
        #     data={'text': text}
        # )
        #
        # if response.status_code == 200:
        #     ai_response = response.json()
            # Display ai_response in a popup or alert


if __name__ == '__main__':
    QuestionnaireApp().run()
