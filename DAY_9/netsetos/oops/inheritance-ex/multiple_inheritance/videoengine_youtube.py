class VideoEngine:
    def play(self):
        print("Video playing...")

class CommentSystem:
    def add_comment(self, text):
        print(f"Comment added: {text}")

class YouTubeVideo(VideoEngine, CommentSystem):
    def like(self):
        print("Video liked.")

# Demonstrate multiple inheritance
yt = YouTubeVideo()
yt.play()                # Inherited from VideoEngine
yt.add_comment("Nice!")  # Inherited from CommentSystem
yt.like()                # Defined in YouTubeVideo