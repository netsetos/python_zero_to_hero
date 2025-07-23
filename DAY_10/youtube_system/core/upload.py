from datetime import datetime

class Upload:
    def __init__(self, title, description, uploader):
        self.title = title
        self.description = description
        self.uploader = uploader
        self.upload_date = datetime.now()

    def get_details(self):
        return f"Title: {self.title}\nDescription: {self.description}\nUploader: {self.uploader.channel_name}\nUpload Date: {self.upload_date}"