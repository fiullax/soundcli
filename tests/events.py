# Try to manage VLC event.
import vlc


def SongFinished(event):
        print("Event reports - finished")
        media = instance.media_new(media_url)
        player.play()


global instance
instance = vlc.Instance('--input-repeat=-1', '--fullscreen')

global player
player = instance.media_player_new()
events = player.event_manager()
events.event_attach(vlc.EventType.MediaPlayerEndReached, SongFinished)

global media_url
media_url = 'https://api.soundcloud.com/tracks/241265638/stream' + '?client_id=a0f84e7c2d612d845125fb5eebff5b37'
media = instance.media_new(media_url)

player.set_media(media)
player.play()

while True:
    pass
