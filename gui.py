from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window


class Interface(AnchorLayout):

    def __init__(self, **kwargs):
        super(Interface, self).__init__(**kwargs)
        anchor_lc = AnchorLayout(anchor_x='center', anchor_y='center')
        lbl = Label(text="Am i a Label ?", size=(100, 100), size_hint=(None, None))
        anchor_lc.add_widget(lbl)
        self.add_widget(anchor_lc)
        # red background color
        Window.clearcolor = (1, 0, 0, 0)


class SoundClient(App):

    def build(self):
        return Interface()


if __name__ == '__main__':
    SoundClient().run()
