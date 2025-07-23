from youtube_system.core.comment import Comment

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.subscribed_channels = []
        self.liked_videos = []

    def subscribe_to_channel(self, channel):
        self.subscribed_channels.append(channel)
        print(f"{self.username} subscribed to {channel.channel_name}")

    def like_video(self, video):
        self.liked_videos.append(video)
        print(f"{self.username} liked {video.title}")

    def create_comment(self, video, text):
        comment  = Comment(self, text)
        video.add_comment(comment)
        print(f"{self.username} commented on {video.title}: '{text}'")