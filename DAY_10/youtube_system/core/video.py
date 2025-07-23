from youtube_system.core.upload import Upload

class Video(Upload):
    def __init__(self, title, description, uploader, duration):
        super().__init__(title, description, uploader)
        self.duration = duration
        self.views = 0
        self.comments = []

    def increment_views(self):
        self.views += 1

    def add_comment(self, comment):
        self.comments.append(comment)

    def get_details(self):
        base_details = super().get_details()
        return f"{base_details}\nDuration: {self.duration}s\nViews: {self.views}"