from kivy.config import Config
from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        return Label(text='Hello, world!')


if __name__ == '__main__':
    # Set the window size based on the device's screen size
    Config.set('graphics', 'width', '300')  # Set your default width here
    Config.set('graphics', 'height', '500')  # Set your default height here

    # Perform checks or calculations here to determine the appropriate screen size
    # For instance:
    screen_width = 800  # Replace with actual calculation based on device
    screen_height = 600  # Replace with actual calculation based on device

    Config.set('graphics', 'width', str(screen_width))
    Config.set('graphics', 'height', str(screen_height))

    MyApp().run()