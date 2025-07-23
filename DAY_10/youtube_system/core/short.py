from youtube_system.core.upload import Upload

class Short(Upload):
    MAX_DURATION = 60

    def __init__(self, title, description, uploader, duration):
        if duration > self.MAX_DURATION:
            raise ValueError(f"Shorts cannot be longer than {self.MAX_DURATION} seconds. ")
        super().__init__(self, title, description, uploader)
        self.duration = duration
        self.views = 0

    def increment_views(self):
        self.views += 1

    def get_details(self):
        base_details = super().get_details()
        return f"{base_details}\nDuration: {self.duration}s\nViews: {self.views} (Short)"
