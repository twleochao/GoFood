from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class CarouselSlider(BoxLayout):
    def __init__(self, label_text, **kwargs):
        super(CarouselSlider, self).__init__(**kwargs)
        self.orientation = 'vertical'

        title_bar = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)

        title_bar.add_widget(Label(text=label_text, size_hint_x=0.8, halign='left'))
        title_bar.add_widget(Button(text='See All', size_hint_x=0.2))

        scrollview = ScrollView(size_hint=(1, 1))
        grid_layout = GridLayout(cols=6, spacing=10, size_hint=(None, None))
        grid_layout.bind(minimum_width=grid_layout.setter('width'))

        for _ in range(6):
            button = Button(text=f'Placeholder', size_hint=(None,None), size=(300, 300))
            grid_layout.add_widget(button)

        scrollview.add_widget(grid_layout)
        
        self.add_widget(title_bar)
        self.add_widget(scrollview)
