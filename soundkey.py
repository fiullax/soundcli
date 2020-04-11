from modules.soundclient import SoundClient, Playlist


def main():
    sound_client = SoundClient()

    # permalink to a track/playlist
    playlist_url = 'https://soundcloud.com/fiullax/sets/trap-italiana-free'
    # playlist_url = input("Playlist permalink: ")

    playlist = Playlist(sound_client, playlist_url)
    
    sound_client.open_player()

    sound_client.playlist_sequentially(playlist)
            

if __name__ == "__main__":
    main()
