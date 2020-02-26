from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class SoundClient(App):
    pass


class PlayerRoot(BoxLayout):

    def previous(self):
        print("Previous track")

    def play_stop(self):
        print("Play/Stop")

    def next(self):
        print("Next track")

    def playlist(self, num):
        print("Playlist #" + str(num))


if __name__ == '__main__':
    SoundClient().run()
