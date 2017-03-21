import kivy
kivy.require('1.9.0') # Kivy ver where the code has been tested!
from kivy.app import App
from kivy.uix.label import Label


class Win1App(App):

    def build(self):
        self.title = 'titulo da janela'
        l1 = Label(text='Hello world')
        return l1

if __name__ == '__main__':
    Win1App().run()