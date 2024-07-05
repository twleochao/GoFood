from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from widgets.taskbar import Toptaskbar, Bottomtaskbar
from widgets.carousel import CarouselSlider
from kivy.uix.label import Label

class GoFoodApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical')

        top_task_bar = Toptaskbar()
        bottom_task_bar = Bottomtaskbar()
        carousel1 = CarouselSlider(label_text='Don\t miss out today!')
        carousel2 = CarouselSlider(label_text='Looking to save money tomorrow?')

        main_layout.add_widget(top_task_bar)
        main_layout.add_widget(carousel1)
        main_layout.add_widget(carousel2)
        main_layout.add_widget(bottom_task_bar)

        return main_layout

if __name__ == '__main__':
    GoFoodApp().run()