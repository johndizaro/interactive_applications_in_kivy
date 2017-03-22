import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
kivy.require('1.7.0')


class FloatLayoutApp(App):
    def build(self):
        return FloatLayout()

if __name__ == "__main__":
    FloatLayoutApp().run()
