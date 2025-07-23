from DAY_10.youtube_system.core.upload import Upload
class LiveStream(Upload):
    def __init__(self, title, description, uploader, duration=0):
        super().__init__(title, description, uploader)
        self.duration = duration
        self.views = 0
        self.is_live = False
        self.chat_messages = []

    def increment_views(self):
        self.views += 1

    def start_stream(self):
        self.is_live = True
        print(f"Live Stream '{self.title}' has started")

    def end_stream(self):
        self.is_live = False
        print(f"Live Stream '{self.title}' has ended")

    def get_details(self):
        base = super().get_details()
        return f"{base}\nLive: {self.is_live}\nDuration: {self.duration}s\nViews: {self.views}"