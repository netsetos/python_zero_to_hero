class CreatorProfile:
    def __init__(self, bio, subscribers):
        self.bio = bio
        self.subscribers = subscribers

    def display_profile(self):
        print(f"Bio: {self.bio}, Subscribers: {self.subscribers}")


class YouTubeChannel1:
    def __init__(self, name, bio, subs):
        self.name = name
        self.profile = CreatorProfile(bio, subs)       # Composition


    def show_channel(self):
        print(f"Channel: {self.name}")
        self.profile.display_profile()

# Composition: Channel owns CreatorProfile
# channel = YouTubeChannel("NetsetosTech", "Learn Python Easily", 1000000)
# channel.show_channel()


class YouTubeChannel2(CreatorProfile):
    def __init__(self, name, bio, subs):
        self.name = name
        super().__init__(bio, subs)       # Inheritance


    def show_channel(self):
        print(f"Channel: {self.name}")
        self.display_profile()

# Composition: Channel owns CreatorProfile
# channel = YouTubeChannel("NetsetosTech", "Learn Python Easily", 1000000)
# channel.show_channel()

