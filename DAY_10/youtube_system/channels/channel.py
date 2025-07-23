from youtube_system.core.video import Video

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



from youtube_system.core.live_stream import LiveStream
from youtube_system.core.interactive_stream import InteractiveSession

class LiveCodingStream(LiveStream, InteractiveSession):
    def __init__(self, title, description, uploader):
        LiveStream.__init__(self, title, description, uploader)
        InteractiveSession.__init__(self)
        print(f"Live Coding Stream '{self.title}' created, ready for interactive session!")

    def display_interactive_session_summary(self):
        print(f"\n--- Interactive Session Summary for '{self.title}' ---")
        if not self.questions:
            print("No questions asked yet. ")
            return

        for i, question in enumerate(self.questions):
            print(f"Q{i+1} by {question['user']} at {question['timestamp'].strftime('%H:%M:%S')}: {question['question']}")
            if question['question'] in self.answers:
                print(f"  A: {self.answers[question['question']]}")
            else:
                print(f" (Unanswered")
        print("-" * 40)