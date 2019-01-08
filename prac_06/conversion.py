from kivy.app import App
from kivy.lang import Builder


class ConversionApp(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('conversion.kv')
        return self.root

    def get_input(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0

    def handle_convert(self):
        value = self.get_input()
        answer = value * 1.60934
        self.root.ids.output_label.text = str(answer)

    def handle_increment(self, change):
        value = self.get_input() + change
        self.root.ids.input_number.text = str(value)
        self.handle_convert()


ConversionApp().run()