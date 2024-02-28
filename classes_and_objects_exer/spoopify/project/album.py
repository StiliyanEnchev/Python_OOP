from project.band import Band
from project.song import Song


class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = [*songs]
        self.published = False

    def add_song(self, track):
        if self.published:
            return "Cannot add songs. Album is published."
        elif track in self.songs:
            return "Song is already in the album."
        elif track.single:
            return f"Cannot add {track.name}. It's a single"
        self.songs.append(track)
        return f"Song {track.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        try:
            song = next(filter(lambda s: s.name == song_name, self.songs))
        except StopIteration:
            return 'Song is not in the album.'

        if self.published:
            return "Cannot remove songs. Album is published."

        self.songs.remove(song)
        return f"Removed song {song.name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        songs_details = '\n'.join(f'== {s.get_info()}' for s in self.songs)
        return (f'Album {self.name}\n'
                f'{songs_details}')

song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34,
False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())