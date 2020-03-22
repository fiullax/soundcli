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
    progressive_url = None
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
        self.progressive_url = self.api_url + "/stream"
        self.permalink_url = api_track["permalink_url"]

    # FIXME: Review in general the function and remove or not?
    def get_track_media_url(self, sound_client):
        """return the media url of the track (ready to be played)"""
        try:
            print('Retriving media url for track #' + str(self.id))

            # res_1 = requests.get(self.api_v2_url, params= { "client_id": sound_client.client_id })
            # progressive_url = json.loads(res_1.content)['media']['transcodings'][1]['url']

            res_2 = requests.get(self.progressive_url, params={"client_id": sound_client.client_id})

            return json.loads(res_2.content)['url']
        except UnicodeDecodeError:
            print("UnicodeDecodeError while getting track media_url for #" + str(self.id))
            return False


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
        res = sound_client.resolve_url(url)
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

    client_id = 'a0f84e7c2d612d845125fb5eebff5b37'
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
    def resolve_url(self, url):
        """resolve track URL into resource"""
        print('Resolving url: ' + url)
        return self.client.get('/resolve', url=url)
        
    def open_player(self):
        """Open a new VLC player"""
        print('Instance a new VLC player..')
        self.player = self.vlc.media_player_new() 
    
    def play_media(self, media_url):
        """Define VLC media and play it"""
        print('Playing track..')
        media = self.vlc.media_new(media_url)

        self.player.set_media(media)
        self.player.play()

    def playlist_sequentially(self, playlist):
        """Playlist with sequentially play"""
        for track in playlist.get_tracks():

            # media_url = track.get_track_media_url(self)
            media_url = track.progressive_url + '?client_id=' + self.client_id
            self.play_media(media_url)
        
            duration_second = float(track.duration) / 1000
            time.sleep(duration_second)

    def playlist_shuffled(self, playlist):
        """Playlist with shuffled play"""
        tracks = playlist.get_tracks()
        while True:
            track = random.choice(tracks)
            
            # media_url = track.get_track_media_url(self)
            media_url = track.progressive_url + '?client_id=' + self.client_id
        
            if media_url:
                print('Playing: ' + track.title)
                self.play_media(media_url)
                
                duration_second = float(track.duration) / 1000
                
                time.sleep(duration_second)
            else:
                print("Can't playing: " + track.title)

    def webplayer(self, media_url):
        """Open media url in a new window of the default browser, if possible"""
        webbrowser.open_new(media_url)

def main():
    sound_client = SoundClient()

    # permalink to a track/playlist
    # playlist_url = 'https://soundcloud.com/mattias-fiullax-games/sets/trap-italiana-free'
    playlist_url = input("Playlist permalink: ")

    playlist = Playlist(sound_client, playlist_url)
    
    sound_client.open_player()

    sound_client.playlist_sequentially(playlist)
            

if __name__ == "__main__":
    main()
