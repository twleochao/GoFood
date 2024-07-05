from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

#LabelBase.register(name="NotoSans", fn_regular="NotoSansTC-VariableFont_wght.ttf")

class Toptaskbar(BoxLayout):
     def __init__(self, **kwargs):
        super(Toptaskbar, self).__init__(**kwargs)
        self.size_hint_y = None
        self.height = 50
        self.orientation = 'horizontal'

        button = Button(text='Map', size_hint_x=0.2)
        self.add_widget(button)

        search_bar = TextInput(hint_text='Search...', size_hint_x=0.8)
        self.add_widget(search_bar)

class Bottomtaskbar(BoxLayout):
    def __init__(self, **kwargs):
        super(Bottomtaskbar, self).__init__(**kwargs)
        self.size_hint_y = None
        self.height = 100
        self.orientation = 'horizontal'

        self.add_widget(Button(text='Nearby'))
        self.add_widget(Button(text='Find'))
        self.add_widget(Button(text='Yum'))
        self.add_widget(Button(text='Profile'))