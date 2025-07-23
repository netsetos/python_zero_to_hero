class Video:
    def __init__(self, title):
        self.title = title

class Playlist:
    def __init__(self, name):
        self.name = name
        self.videos = []

    def add_video(self, video):
        self.videos.append(video)
        print(f"Added '{video.title}' to playlist '{self.name}'")

# Aggregation: Playlist has references to Video
v1 = Video("Inheritance Explained")
v2 = Video("Encapsulation in Python")
pl = Playlist("OOP Tutorials")
pl.add_video(v1)
pl.add_video(v2)