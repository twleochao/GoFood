from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button

class Widget(Widget):
    pass

class App(App):
    def build(self):
        return Widget()

if __name__ == '__main__':
    App().run()