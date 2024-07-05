from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.text import LabelBase
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

LabelBase.register(name="NotoSans", fn_regular="NotoSansTC-VariableFont_wght.ttf")

class Widget(Widget):
    pass

class GoFoodApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical')

        main_layout.add_widget(Label(text="lloyd小雞雞",font_name="NotoSans"))

        bottom_task_bar = BoxLayout(size_hint_y=None, height=50, orientation='horizontal')
        top_task_bar = BoxLayout(size_hint_y=None, height=50, orientation='horizontal')

        bottom_task_bar.add_widget(Button(text='Nearby'))
        bottom_task_bar.add_widget(Button(text='Find'))
        bottom_task_bar.add_widget(Button(text='Yum'))
        bottom_task_bar.add_widget(Button(text='Profile'))

        main_layout.add_widget(bottom_task_bar)
        
        return main_layout

if __name__ == '__main__':
    GoFoodApp().run()