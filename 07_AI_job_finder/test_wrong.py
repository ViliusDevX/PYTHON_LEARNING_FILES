```
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineIconListItem
from kivymd.icon_definitions import md_icons
from pylottie import LottieAnimation


KV = '''
BoxLayout:
    orientation: 'vertical'

    MDToolbar:
        title: 'Lottie Animation Example'
        elevation: 10

    ScrollView:

        MDList:
            OneLineIconListItem:
                text: "Play Animation"
                IconLeftWidget:
                    icon: "play"
                on_release: app.play_animation()
'''

class LottieExample(MDApp):
    animation_file = StringProperty("path/to/your/animation.json")

    def build(self):
        return Builder.load_string(KV)

    def play_animation(self):
        animation_layout = LottieBoxLayout(animation_file=self.animation_file)
        self.root.add_widget(animation_layout)
        animation_layout.start_animation()


class LottieBoxLayout(MDBoxLayout):
    def __init__(self, animation_file, **kwargs):
        super(LottieBoxLayout, self).__init__(**kwargs)
        self.animation_file = animation_file

    def start_animation(self):
        animation = LottieAnimation(filename=self.animation_file, loop=True)
        self.add_widget(animation)
        animation.play()


if __name__ == '__main__':
    LottieExample().run()

```