from kivy.app import App
from kivy.lang import Builder
import random


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('products_price_calculator.kv')
        return self.root

    def handle_pressed(self):
        if random.random() <= 5:
            self.root.ids.my_label.text = "Hello World!"
        else:
            self.root.ids.my_label.text = "Goodbye World!"


BoxLayoutDemo().run()

