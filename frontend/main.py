from kivy.app import App
from kivy.uix.widget import Widget

class Widget(Widget):
    pass

class App(App):
    def build(self):
        return Widget()

if __name__ == '__main__':
    App().run()