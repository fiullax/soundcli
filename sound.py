import soundcloud
import json
import webbrowser
import urllib2
import vlc
import time


class SoundClient:

	client_id = 'cZQKaMjH39KNADF4y2aeFtVqNSpgoKVj'
	client = None
	""" TODO: Secret code for log in user private area
	client_secret = '3332dcf51a6f9d2c659dbb57c8068ed'
	"""

	def __init__(self):
		self.client = soundcloud.Client(client_id=self.client_id)

	# resolve track URL into  resource
	def resolve_url(self, url):
		return self.client.get('/resolve', url=url)

	# retrive a dict with the tracks of the playlist
	def get_playlist_tracks(self, playlist):
		return playlist.obj['tracks']


def main():
	sound_client = SoundClient()

	# a permalink to a track/playlist
	playlist_url = 'https://soundcloud.com/mattias-fiullax-games/sets/trap-italiana-free'

	playlist = sound_client.resolve_url(playlist_url) 

	for track in sound_client.get_playlist_tracks(playlist):
		track_id = track['id']
		break

	first_url = 'https://api-v2.soundcloud.com/tracks/TRACK_ID?client_id=cZQKaMjH39KNADF4y2aeFtVqNSpgoKVj'
	first_url = first_url.replace('TRACK_ID', str(track_id))

	print("First url: " + first_url)


	res = urllib2.urlopen(first_url)
	data = json.loads(res.read().decode())

	progressive_url = data['media']['transcodings'][1]['url']

	progressive_url += '?client_id=cZQKaMjH39KNADF4y2aeFtVqNSpgoKVj'

	res_progressive_url = urllib2.urlopen(progressive_url)
	data_1 = json.loads(res_progressive_url.read().decode())

	print(data_1['url'])

	url = data_1['url']

	# Open url in a new window of the default browser, if possible
	# webbrowser.open_new(data_1['url'])

	# define VLC instance
	instance = vlc.Instance('--input-repeat=-1', '--fullscreen')

	# Define VLC player
	player = instance.media_player_new()

	# Define VLC media
	media = instance.media_new(url)

	# Set player media
	player.set_media(media)

	# Play the media
	player.play()

	time.sleep(150)


if __name__ == "__main__":
	main()