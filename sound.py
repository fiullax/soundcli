import soundcloud
import json

# Client_id retrived from kodi add-on
key = 'cZQKaMjH39KNADF4y2aeFtVqNSpgoKVj'

""" TODO: Secret code for log in user private area
client_secret = '3332dcf51a6f9d2c659dbb57c8068ed'
"""

client = soundcloud.Client(client_id=key)

# a permalink to a track
track_url = 'https://soundcloud.com/mattias-fiullax-games/sets/trap-italiana-free'

# resolve track URL into track resource
playlist = client.get('/resolve', url=track_url)

data = json.loads(str(playlist))
print data['two']

"""
for track in playlist.tracks:    
    data = json.loads(track)
    print(data)
    break

# now that we have the track id, we can get a list of comments, for example
for track in client.get('/tracks/%d/comments' % track.id):
    print 'Someone said: %s at %d' % (comment.body, comment.timestamp)


tracks = client.get('/tracks', limit=1)
for track in tracks:
    print (track.author + '|' + track.title)
    
    # get the tracks streaming URL
    stream_url = client.get(track.stream_url, allow_redirects=False)

    # print the tracks stream URL
    print (stream_url.location)
    """