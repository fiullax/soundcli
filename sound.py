import soundcloud
import json
import webbrowser
import vlc
import time
import random
import requests


class Track:

    id = None
    title = None
    duration = None
    genre = None
    
    api_url = None
    api_v2_url = None
    permalink_url = None
    img_url = None

    def __init__(self, api_track):
        self.title = api_track["title"]
        self.duration = api_track["duration"]
        self.img_url = api_track["artwork_url"]
        self.genre = api_track["genre"]
        self.id = api_track["id"]
        self.api_url = api_track["uri"]
        self.api_v2_url = 'https://api-v2.soundcloud.com/tracks/' + str(self.id)
        self.permalink_url = api_track["permalink_url"]


class Playlist:

    id = None
    title = None
    description = None
    genre = None
    duration = None
    track_count = None
    tracks = []

    permalink_url = None
    api_url = None
    img_url = None

    def __init__(self, sound_client, url):
        print("Playlist __init__")
        # TODO: To manage api errors
        res = sound_client.resolve_url('https://soundcloud.com/mattias-fiullax-games/sets/trap-italiana-free')
        self.id = res.obj["id"]
        self.title = res.obj["title"]
        self.description = res.obj["description"]
        self.genre = res.obj["genre"]
        self.duration = res.obj["duration"]
        self.track_count = res.obj["track_count"]

        for track in res.obj["tracks"]:
            self.tracks.append(Track(track))

        self.permalink_url = res.obj["permalink_url"]
        self.api_url = res.obj["uri"]
        self.img_url = res.obj["artwork_url"]

    # return a dict with the tracks of the playlist
    def get_tracks(self):
        print("Getting tracks from playlist: " + self.title + " #" + str(self.id))
        return self.tracks


class SoundClient:

    client_id = 'cZQKaMjH39KNADF4y2aeFtVqNSpgoKVj'
    client = None
    """ TODO: Secret code for log in user private area
    client_secret = '3332dcf51a6f9d2c659dbb57c8068ed'
    """
    vlc = None
    player = None

    def __init__(self):
        self.client = soundcloud.Client(client_id=self.client_id)
        self.vlc = vlc.Instance('--input-repeat=-1', '--fullscreen')

    # FIXME: Review the description
    # resolve track URL into resource
    def resolve_url(self, url):
        print('Resolving url: ' + url)
        return self.client.get('/resolve', url=url)

    # TODO: Review in general the function
    # return the media url of the track (ready to be played)
    def get_track_media_url(self, track):
        try:
            print('Retriving media url for track #' + str(track.id))

            res_1 = requests.get(track.api_v2_url, params= { "client_id": self.client_id })
            progressive_url = json.loads(res_1.content)['media']['transcodings'][1]['url']

            res_2 = requests.get(progressive_url, params= { "client_id": self.client_id })
            
            return json.loads(res_2.content)['url']
        except UnicodeDecodeError:
            print("UnicodeDecodeError while getting track media_url for #" + str(track.id))
            return False
        
    # Open a new VLC player
    def open_player(self):
        print('Instance a new VLC player..')
        self.player = self.vlc.media_player_new() 
    
    # Define VLC media and play it
    def play_media(self, media_url):
        print('Playing track..')
        media = self.vlc.media_new(media_url)

        self.player.set_media(media)
        self.player.play()


def main():
    sound_client = SoundClient()

    # a permalink to a track/playlist
    playlist_url = 'https://soundcloud.com/mattias-fiullax-games/sets/trap-italiana-free'

    # playlist = sound_client.resolve_url(playlist_url) 

    playlist = Playlist(sound_client, 'url')
    
    sound_client.open_player()

    """ Playlist play in order
    for track in sound_client.get_playlist_tracks(playlist):
        track_id = track['id']
        
        media_url = sound_client.get_track_media_url(track_id)
    
        sound_client.play_media(media_url)
        
        duration_second = float(track['duration']) / 1000
        
        time.sleep(duration_second)
    """        
    
    # Open url in a new window of the default browser, if possible
    # webbrowser.open_new(data_1['url'])
    
    # Playlist random play
    tracks = playlist.get_tracks()
    while True:
        track = random.choice(tracks)
        
        media_url = sound_client.get_track_media_url(track)
    
        if media_url:
            print('Playing: ' + track.title)
            sound_client.play_media(media_url)
            
            duration_second = float(track.duration) / 1000
            
            time.sleep(duration_second)
        else:
            print("Can't playing: " + track.title)
            

if __name__ == "__main__":
    main()
