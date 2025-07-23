from DAY_10.youtube_system.core.video import Video

class Channel:
    def __init__(self, channel_name, owner):
        self.channel_name = channel_name
        self.owner = owner
        self.videos = []
        self.subscribers = []

    def upload_video(self, title, description, duration):
        video = Video(self, title, description, duration)
        self.videos.append(video)
        print(f"{self.channel_name} uploaded a new video: '{title}'")
        return video

    def add_subscriber(self, user):
        self.subscribers.append(user)

    def display_channel_info(self):
        print(f"--- Channel: {self.channel_name} ---")
        print(f"Owner: {self.owner.username}")
        print(f"Subscribers: {len(self.subscribers)}")
        print("Videos:")
        for video in self.videos:
            print(f" - {video.title} ({video.duration}s) - Views: {video.views}")



