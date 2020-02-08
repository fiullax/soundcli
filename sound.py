import soundcloud
#import json
import webbrowser

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
    url = track['permalink_url']
    break

# Open url in a new window of the default browser, if possible
webbrowser.open_new(url)