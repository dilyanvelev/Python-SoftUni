class Music:
    def __init__(self,title, artist,lyric):
        self.title = title
        self.artist = artist
        self.lyric = lyric

    def print_info(self):
        return f"This is'{self.title}' from {self.artist}"

    def play(self):
        return