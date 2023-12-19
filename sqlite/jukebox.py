from nested_data import albums

SONG_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

def valid_input(lists):
    choice = input()
    if choice.isdigit() and 1 <= int(choice) <= len(lists):
        return int(choice)
    else:
        print("Exiting jukebox..")
        exit(1)

while True:
    print("Please choose your album (invalid choice exits):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print(f"{index + 1}: {title}")
    choice = valid_input(albums)
    print("Please choose your song:")
    for index, song in albums[choice][SONG_LIST_INDEX]:
        print(f"{index + 1}: {song}")
    choice =  valid_input(albums[choice][SONG_LIST_INDEX])
    print(f"Playing {albums[choice][SONG_LIST_INDEX][choice - 1][SONG_TITLE_INDEX]}")
    print("=" * 40)
