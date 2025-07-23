class Viewer:
    def __init__(self, username):
        self.username = username

    def watch(self, video):
        print(f"{self.username} is watching '{video.title}'")


class Video:
    def __init__(self, title):
        self.title = title

# Association: Viewer uses Video
v = Viewer("pranav")
vid = Video("DAY 32 OOP in Python")
v.watch(vid)