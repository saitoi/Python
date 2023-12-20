from nested_data import albums

SONG_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

def valid_input(lists):
    choice = input()
    if choice.isdigit() and 1 <= int(choice) <= len(lists):
        return int(choice) - 1  # Adjust the index to start from 0
    else:
        print("Exiting jukebox..")
        exit(1)

while True:
    print("Please choose your album (invalid choice exits):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print(f"{index + 1}: {title}")
    album_choice = valid_input(albums)

    print("Please choose your song:")
    for index, song in enumerate(albums[album_choice][SONG_LIST_INDEX]):
        print(f"{index + 1}: {song[SONG_TITLE_INDEX]}")  # Access the song title correctly
    song_choice = valid_input(albums[album_choice][SONG_LIST_INDEX])

    chosen_song = albums[album_choice][SONG_LIST_INDEX][song_choice]
    print(f"Playing {chosen_song[SONG_TITLE_INDEX]}")
    print("=" * 40)
