import kivy
from kivy.app import App
from kivy.uix.label import Label
kivy.require('1.9.0')


class Win1App(App):

    def build(self):
        self.title = 'titulo da janela'
        l1 = Label(text='John Evan Dizaro')
        return l1

if __name__ == '__main__':
    Win1App().run()
