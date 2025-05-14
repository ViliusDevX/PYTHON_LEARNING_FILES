import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.checkbox import CheckBox
from kivy.uix.widget import Widget


class SurveyApp(App):
    def submit(self, instance):
        popup = Popup(title='Submission',
                      content=Label(text='Your survey has been submitted!'),
                      size_hint=(None, None), size=(300, 200))
        popup.open()

    def build(self):
        main_layout = BoxLayout(orientation='vertical', spacing=10)
        scroll_view = ScrollView()

        questions_layout = BoxLayout(orientation='vertical', spacing=30, size_hint_y=None, padding=10)
        questions_layout.bind(minimum_height=questions_layout.setter('height'))

    def generate_user_summary(self):
        # Placeholder for generating user's summary based on selected checkboxes
        summary_parts = []
        # Loop through each question and its checkboxes to form a summary
        # Replace this with logic to generate the user summary based on checkbox selections
        # For demonstration, let's create a placeholder summary
        questions = [
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
        for question, choices in questions:
            selected_choice = None
            for choice in choices:
                checkbox = self.root.ids[question + choice]
                if checkbox.active:
                    selected_choice = choice
                    break
            if selected_choice:
                summary_parts.append(selected_choice)

        def send_to_chatgpt(self, text):
            # Send the user summary to ChatGPT API
            response = requests.post(self.GPT_API_ENDPOINT, data=text)
            return response.text if response.status_code == 200 else None

        def display_chatgpt_response(self, response):
            # Display ChatGPT response in a popup
            if response:
                popup = Popup(title='ChatGPT Response', content=Label(text=response), size_hint=(None, None),
                              size=(400, 300))
                popup.open()
            else:
                popup = Popup(title='Error', content=Label(text='Failed to get ChatGPT response'),
                              size_hint=(None, None), size=(300, 200))
                popup.open()

        def build(self):
            main_layout = BoxLayout(orientation='vertical', spacing=10)
            scroll_view = ScrollView()

            questions_layout = BoxLayout(orientation='vertical', spacing=30, size_hint_y=None, padding=10)
            questions_layout.bind(minimum_height=questions_layout.setter('height'))

            for question, choices in questions:
                question_label = Label(text=question)
                checkboxes_layout = BoxLayout(orientation='horizontal', spacing=10)
                for choice in choices:
                    checkbox = CheckBox(group=question)
                    checkbox.id = question + choice  # Create unique IDs for each checkbox
                    checkboxes_layout.add_widget(checkbox)
                    checkboxes_layout.add_widget(Label(text=choice))

                questions_layout.add_widget(question_label)
                questions_layout.add_widget(checkboxes_layout)

            submit_button = Button(text='Submit', padding=(10, 5))
            submit_button.bind(on_press=self.submit)
            questions_layout.add_widget(submit_button)

            scroll_view.add_widget(questions_layout)
            main_layout.add_widget(scroll_view)

            return main_layout


if __name__ == '__main__':
    SurveyApp().run()