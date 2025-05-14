import requests
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.screen import MDScreen
from kivy.config import Config
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox


class SurveyApp(MDApp):
    GPT_API_ENDPOINT = 'my api'

    def submit(self, instance):
        user_summary = self.generate_user_summary()
        if user_summary:
            response = self.send_to_chatgpt(user_summary)
            self.display_chatgpt_response(response)
        else:
            self.display_incomplete_survey_message()

    def generate_user_summary(self):
        summary_parts = []
        for question, choices in self.questions:
            answered = False
            for choice in choices:
                checkbox_id = (question + choice).replace(" ", "").lower()
                if checkbox_id in self.checkboxes:  # Access checkboxes dictionary
                    checkbox = self.checkboxes[checkbox_id]
                    if checkbox.active:  # Check the checkbox state using 'active'
                        summary_parts.append(choice)
                        answered = True
                        break
            if not answered:
                return None

        return ', '.join(summary_parts)  # Return a summa

    def display_incomplete_survey_message(self):
        dialog = MDDialog(
            title="Incomplete Survey",
            text="Please answer all questions before submitting.",
            size_hint=(None, None),
            size=(dp(400), dp(200)),
        )
        dialog.open()

    def send_to_chatgpt(self, text):
        response = requests.post(self.GPT_API_ENDPOINT, data=text)
        return response.text if response.status_code == 200 else None

    def display_chatgpt_response(self, response):
        if response:
            popup = Popup(title='ChatGPT Response', content=Label(text=response), size_hint=(None, None),
                          size=(400, 300))
            popup.open()
        else:
            popup = Popup(title='Error', content=Label(text='Failed to get ChatGPT response'),
                          size_hint=(None, None), size=(300, 200))
            popup.open()

    def build_question(self, question, choices):
        question_label = MDLabel(text=question)
        checkboxes_layout = BoxLayout(orientation='vertical')

        checkboxes = {}  # Store checkbox instances

        total_choices = len(choices)
        spacing_factor = 1.0 / max(total_choices, 1)  # Avoid division by zero
        for choice in choices:
            checkbox_id = question + choice
            checkbox_id = checkbox_id.replace(" ", "").lower()
            checkbox = MDCheckbox(id=checkbox_id)
            checkbox.size_hint_y = spacing_factor
            checkboxes_layout.add_widget(checkbox)

            checkboxes[checkbox_id] = checkbox  # Store checkbox instance

        return question_label, checkboxes_layout, checkboxes

    def build_survey_layout(self):
        questions_layout = BoxLayout(orientation='vertical', spacing=dp(30), size_hint_y=None, padding=dp(10))
        questions_layout.bind(minimum_height=questions_layout.setter('height'))

        checkboxes_dict = {}  # Store checkboxes for future access

        for question, choices in self.questions:
            question_label, checkboxes_layout, checkboxes = self.build_question(question, choices)
            questions_layout.add_widget(question_label)
            questions_layout.add_widget(checkboxes_layout)

            checkboxes_dict.update(checkboxes)  # Add checkboxes to the main dictionary

        submit_button = MDRectangleFlatButton(
            text='Submit',
            size_hint=(None, None),
            size=(dp(0.25 * Window.width), dp(0.1 * Window.height)),
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            md_bg_color=(0.05, 0.15, 0.5, 1),
        )
        submit_button.bind(on_release=self.submit)

        return questions_layout, submit_button, checkboxes_dict

    def build(self):
        main_layout = MDScreen()

        self.questions = [
            ("I'm 20 years old", ['Under 25', '25-35', 'Over 35']),
            ("I like to work alone", ['Strongly Disagree', 'Neutral', 'Strongly Agree']),
            ("I'm systematic", ['Strongly Disagree', 'Neutral', 'Strongly Agree']),
            ("I'm introvert", ['Strongly Disagree', 'Neutral', 'Strongly Agree']),
            ("I like flexible environments", ['Strongly Disagree', 'Neutral', 'Strongly Agree']),
            ("I'm methodical and systematic", ['Strongly Disagree', 'Neutral', 'Strongly Agree']),
            ("I'm innovative and creative", ['Strongly Disagree', 'Neutral', 'Strongly Agree']),
            ("I involve and collaborate with others for solutions", ['Strongly Disagree', 'Neutral', 'Strongly Agree']),
            ("I prefer working independently", ['Strongly Disagree', 'Neutral', 'Strongly Agree']),
            ("I seek mediation and involve others to find a solution", ['Strongly Disagree', 'Neutral', 'Strongly Agree']),
            ("I prioritize tasks and manage them sequentially", ['Strongly Disagree', 'Neutral', 'Strongly Agree']),
            ("I follow a structured schedule and prioritize systematically", ['Strongly Disagree', 'Neutral', 'Strongly Agree']),
            ("I embrace change by exploring new possibilities", ['Strongly Disagree', 'Neutral', 'Strongly Agree']),
            ("I prefer structured environments for clarity and focus", ['Strongly Disagree', 'Neutral', 'Strongly Agree']),
            ("I'm a leader - prefer taking charge and guiding the team", ['Strongly Disagree', 'Neutral', 'Strongly Agree']),
            ("I find compromises and common ground through discussion", ['Strongly Disagree', 'Neutral', 'Strongly Agree']),
            ("I enjoy contributing equally with others", ['Strongly Disagree', 'Neutral', 'Strongly Agree']),
            ("I'm pursuing formal education and certifications", ['Strongly Disagree', 'Neutral', 'Strongly Agree']),
            ("I've embraced change by exploring new possibilities", ['Strongly Disagree', 'Neutral', 'Strongly Agree']),
            ("I prioritize tasks and manage them sequentially", ['Strongly Disagree', 'Neutral', 'Strongly Agree']),
            ("I prefer a quiet and structured environment for focused work", ['Strongly Disagree', 'Neutral', 'Strongly Agree']),
            ("I seek personal growth and learning", ['Strongly Disagree', 'Neutral', 'Strongly Agree']),
            ("I'm comfortable with both depending on the nature of the work", ['Strongly Disagree', 'Neutral', 'Strongly Agree']),
            ("I adapt and prioritize based on urgency and importance", ['Strongly Disagree', 'Neutral', 'Strongly Agree']),
            ("I've delegated tasks or sought help to manage multiple responsibilities", ['Strongly Disagree', 'Neutral', 'Strongly Agree']),
            ("I enjoy a dynamic and collaborative space for idea exchange", ['Strongly Disagree', 'Neutral', 'Strongly Agree']),
            ("I enjoy a dynamic and collaborative space for idea exchange", ['Strongly Disagree', 'Neutral', 'Strongly Agree']),
            ("I manage multiple responsibilities by delegating tasks or seeking help", ['Strongly Disagree', 'Neutral', 'Strongly Agree']),
        ]

        survey_layout, submit_button, _ = self.build_survey_layout()

        scroll_view = ScrollView()
        survey_layout.add_widget(submit_button)
        scroll_view.add_widget(survey_layout)

        main_layout.add_widget(scroll_view)

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

        return main_layout


if __name__ == '__main__':
    SurveyApp().run()
