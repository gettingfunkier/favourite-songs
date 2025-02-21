import json

filename = "songs.json"

def load_songs():
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_songs(songs):
    with open(filename, 'w') as file:
        json.dump(songs, file, indent = 4)

def view_songs():
    songs = load_songs()
    if songs:
        for index, song in enumerate(songs, 1):
            print(f"{index}. {song}")
    else:
        print("no songs added!")

def add_songs(song):
    songs = load_songs()
    songs.append(song)
    save_songs(songs)
    print(f"{song} added!")

def remove_songs():
    songs = load_songs()
    view_songs()

    if not songs:
        print("no songs found!")
        return
    
    song = input("which song? ")
    
    if song in songs:
        songs.remove(song)
        save_songs(songs)
        print(f"{song} removed!")
    else:
        print("song not found!")

while True:
    print("(1) view songs (2) add songs (3) remove songs (q) quit")
    user = input("input: ")

    if user == "1":
        view_songs()

    elif user == "2":
        song = input("enter song: ")
        add_songs(song)

    elif user == "3":
        remove_songs()

    elif user == "q":
        print("goodbye!")
        break

    else:
        print("Invalid input!")