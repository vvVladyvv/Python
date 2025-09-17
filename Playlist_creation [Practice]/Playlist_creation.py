print("Playlist system\n----------------------\n")
playlist = []
playlist_name = input("Playlist name: ")
songs = int(input("How many songs you want add: "))
while songs > 0:
    print()
    name_song_request = input("Into song name: ")
    song_duration_request = input("Into song duration: ")
    print('\n------------------------\n')
    dictionary = {
    'name_song': name_song_request,
    'song_duration': song_duration_request
}
    songs -= 1
    playlist.append(dictionary)


print()
print(f"\n--------------------   \n{playlist_name}\n   ----------------------\n")
print()
print('Songs.             Duration.\n\n---------------------------\n')
for songs in sorted(playlist, key=lambda s: s['name_song']):
    print(f"{songs['name_song']}                  {songs['song_duration']}")

