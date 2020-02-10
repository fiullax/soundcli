import soundcloud
import json
import webbrowser
import urllib.request

# Client_id retrived from kodi add-on
key = 'cZQKaMjH39KNADF4y2aeFtVqNSpgoKVj'

""" TODO: Secret code for log in user private area
client_secret = '3332dcf51a6f9d2c659dbb57c8068ed'
"""

client = soundcloud.Client(client_id=key)

# a permalink to a track/playlist
playlist_url = 'https://soundcloud.com/mattias-fiullax-games/sets/trap-italiana-free'

# resolve track URL into  resource
playlist = client.get('/resolve', url=playlist_url)

print(playlist.obj['tracks'])

for track in playlist.obj['tracks']:
    track_id = track['id']
    break

first_url = 'https://api-v2.soundcloud.com/tracks/TRACK_ID?client_id=cZQKaMjH39KNADF4y2aeFtVqNSpgoKVj'
first_url = first_url.replace('TRACK_ID', str(track_id))

print("First url: " + first_url)


res = urllib.request.urlopen(first_url)
data = json.loads(res.read().decode())

progressive_url = data['media']['transcodings'][1]['url']

progressive_url += '?client_id=cZQKaMjH39KNADF4y2aeFtVqNSpgoKVj'

res_progressive_url = urllib.request.urlopen(progressive_url)
data_1 = json.loads(res_progressive_url.read().decode())

print(data_1['url'])

# Open url in a new window of the default browser, if possible
webbrowser.open_new(data_1['url'])