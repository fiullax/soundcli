import soundcloud
import json
import webbrowser
import vlc
import time
import random
import requests


class Track:

    title = None # Sfera Ebbasta - Blunt & Sprite (Prod. Charlie Charles),
    duration = None # 170229,
    artwork_url = None # https://i1.sndcdn.com/artworks-000142577548-kzeciq-large.jpg,
    genre = None # Trap,
    id = None # 241265638,
    uri = None # https:None//api.soundcloud.com/tracks/241265638,
    # waveform_url https://w1.sndcdn.com/32F8POxk3bVa_m.png,
    permalink_url = None # https://soundcloud.com/sickago/sfera-ebbasta-blunt-sprite-prod-charlie-charles,
    # stream_url https://api.soundcloud.com/tracks

	def __init__(self):
		pass


class Playlist:

	id = None
	title = None
	description = None
	genre = None
	duration = None
	track_count = None
	tracks = None

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
		# TODO: Array with Track obj
		self.tracks = res.obj["tracks"]

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
	def get_track_media_url(self, track_id):
		try:
			print('Retriving media url for track #' + str(track_id))
			track_url = 'https://api-v2.soundcloud.com/tracks/' + str(track_id)

			res_1 = requests.get(track_url, params= { "client_id": self.client_id })
			progressive_url = json.loads(res_1.content)['media']['transcodings'][1]['url']

			res_2 = requests.get(progressive_url, params= { "client_id": self.client_id })
			
			return json.loads(res_2.content)['url']
		except UnicodeDecodeError:
			print("UnicodeDecodeError while getting track media_url for #" + str(track_id))
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
		track_id = track['id']
		
		media_url = sound_client.get_track_media_url(track_id)
	
		if media_url:
			print('Playing: ' + track['title'])
			sound_client.play_media(media_url)
			
			duration_second = float(track['duration']) / 1000
			
			time.sleep(duration_second)
		else:
			print("Can't playing: " + track['title'])
			

if __name__ == "__main__":
	main()
