class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

hSong = ["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"]
happy_bday = Song(hSong)

bulls_on_parade = Song(["They rally round the family","With pocket full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

enter_sand_man = Song(["Say your prayer little one", "Don't forget my son", "To include everyone"])
enter_sand_man.sing_me_a_song()
