from youtube_system.core.upload import Upload

class LiveStream(Upload):
    def __init__(self, title, description, uploader):
        super().__init__(title, description, uploader)
        self.is_live = False
        self.chat_messages = []

    def start_stream(self):
        self.is_live = True
        print(f"Live Stream '{self.title}' has started")

    def end_stream(self):
        self.is_live = False
        print(f"Live Stream '{self.title}' has ended")

    def add_chat_message(self):
        self.chat_messages.append({"user": user.username, "message": message})
