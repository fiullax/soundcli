from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class SoundClient(App):
    pass


class PlayerRoot(BoxLayout):

    def previous(self):
        print("Previous")

    def play_stop(self):
        print("Play/Stop")


    def next(self):
        print("Next")

    def shutdown(self):
        print("Shutdown")

    def channel(self, num):
        print("Channel")


if __name__ == '__main__':
    SoundClient().run()
