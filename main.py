from modules.soundclient import SoundClient, Playlist


def main():
    sound_client = SoundClient()

    playlist_url = input("Playlist link: ")
    print("1 - Sequentially | 2 - Shuffled")
    play_mode = input("Play mode: ")

    playlist = Playlist(sound_client, playlist_url)
    
    sound_client.open_player()

    if (play_mode == "1") :
        sound_client.playlist_sequentially(playlist)
    elif (play_mode == "2") :
        sound_client.playlist_shuffled(playlist)
    else :
        sound_client.playlist_sequentially(playlist)

if __name__ == "__main__":
    main()
