from abc import ABC, abstractmethod

class VideoPlayer(ABC):
    @abstractmethod
    def play_video(self, video):
        pass


class BasicVideoPlayer(VideoPlayer):
    def play_video(self, video):
        print(f"Now playing: '{video.title}' by {video.uploader.channel_name}")
        video.increment_views()
        print(f"Video '{video.title}' finished playing.")