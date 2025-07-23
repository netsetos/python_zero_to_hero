from DAY_10.youtube_system.playback.player import VideoPlayer

class PremiumVideoPlayer(VideoPlayer):
    def play_video(self, video):
        print(f"[Premium] Now playing ad-free: '{video.title}' by {video.uploader.channel_name}")
        video.increment_views()
        print(f"[Premium] Video '{video.title}' finished playing. Enjoyed in high quality!")