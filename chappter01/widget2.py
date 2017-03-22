import kivy
from kivy.app import App
from kivy.uix.widget import Widget
kivy.require('1.9.1')


class MyWidget(Widget):
    pass


class WidgetsApp(App):
    def build(self):
        return MyWidget()


if __name__ == "__main__":
    WidgetsApp().run()
