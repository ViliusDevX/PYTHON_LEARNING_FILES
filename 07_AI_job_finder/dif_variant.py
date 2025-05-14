from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivymd.app import MDApp


class QuestionWidget(BoxLayout):  # The viewclass definitions, and property definitions.
    question = StringProperty()
    question_id = StringProperty()
    checkbox1_active = BooleanProperty(False)
    checkbox2_active = BooleanProperty(False)
    checkbox3_active = BooleanProperty(False)

    def on_checkbox_update(self, checkbox_num, is_checked):
        # Kai užcheckini vieną box'ą, kitas nusicheckina
        # šitas kviečiasi du kartus užcheckintam ir nucheckintam box'ui
        # todėl galim pafiltruot:
        if is_checked:
            print(f"Checkbox #{checkbox_num} checked for question {self.question_id}")


class QuestionList(RecycleView):
    questions = ListProperty()  # A list property is used to hold the data for the recycleview, see the kv code

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.questions = [{
            'question': f'Question {i}',
            'question_id': f'question_{i}'
        } for i in range(1, 11)]
        # This list comprehension is used to create the data list for this simple example.
        # The data created looks like:
        # [{'left_text': 'Left 0', 'right_text': 'Right 0'}, {'left_text': 'Left 1', 'right_text': 'Right 1'},
        # {'left_text': 'Left 2', 'right_text': 'Right 2'}, {'left_text': 'Left 3'},...
        # notice the keys in the dictionary correspond to the kivy properties in the TwoButtons class.
        # The data needs to be in this kind of list of dictionary formats.  The RecycleView instances the
        # widgets, and populates them with data from this list.

    def submit(self):
        print("On Submit")

kv_string = '''
BoxLayout:
    QuestionWidget:
    QuestionList:
'''

class MainApp1(MDApp):

    def build(self):
        return Builder.load_file('tyler_durden_variant.py')


if __name__ == '__main__':
    MainApp1().run()
