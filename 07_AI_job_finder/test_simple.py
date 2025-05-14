from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty, NumericProperty
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class QuestionWidget(BoxLayout):  # The viewclass definitions, and property definitions.
    index = NumericProperty() # Klausimo indeksas
    question = StringProperty()
    question_id = StringProperty()

    # Nedeam checkbox'ų properčių, nes jie buginasi
    # Reikia pačiam .kv faile subindinti per app.questions[?? widgeto indexas ??].checkbox1_active

    def __init__(self, **kwargs):
        super(QuestionWidget, self).__init__(**kwargs)

    # Pareina atgal tik checkboxo indeksas, todėl reikia jį "konvertuoti" į tekstą
    def get_answer(self, checkbox_index):
        answers = ['Strongly Disagree', 'Neutral', 'Strongly Agree']
        if 0 <= checkbox_index < len(answers):
            return answers[checkbox_index]
        else:
            return "Index out of range"

    def on_checkbox_active(self, checkbox_index, is_checked):
        print(f"Question index: {self.index} Checkbox index: {checkbox_index} Checked: {is_checked}")

        # Su šitu patenkam prie MainApp1(MDApp) instance'o
        app =  App.get_running_app()

        # Tiesiogiai pakeiciam checkboxo verte True/False
        app.questions[self.index][f'checkbox{checkbox_index}_active'] = is_checked

        # Kad būtų lengviau sugeneruot promptą, galim prie kiekvieno klausimo išsaugot tekstinį atsakymą
        if (is_checked):
            app.questions[self.index]['answer'] = self.get_answer(checkbox_index)


class QuestionList(RecycleView):
    questions = ListProperty()  # A list property is used to hold the data for the recycleview, see the kv code

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        app = MDApp.get_running_app()
        self.questions = app.questions

    def submit(self):
        print("On Submit")

        app = App.get_running_app()
        questions = app.questions

        for question_widget in questions:
            question_1 = question_widget['question']
            question_id = question_widget['question_id']

            # Find the corresponding question index in the questions list based on question_id
            index = next((index for index, q in enumerate(questions) if q['question_id'] == question_id), None)

            if index is not None:
                # Assuming 'index' is the correct checkbox_index for the question
                answer = QuestionWidget().get_answer(index)
                print(f"Question: {question_1} was answered with {answer}")


class MainApp1(MDApp):
    questions = ListProperty()

    def build(self):
        self.questions = [{
            'index': i-1,
            'question': f'Question {i}',
            'question_id': f'question_{i}', # Naudojamas checkbox'ų groupsams
            'checkbox1_active': False,
            'checkbox2_active': False,
            'checkbox3_active': False,
            'answer': None
        } for i in range(1, 10)]

        return Builder.load_file('main.kv')


if __name__ == '__main__':
    MainApp1().run()
