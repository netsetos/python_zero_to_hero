class BaseVideo:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def upload(self):
        print(f"Uploading: {self.title} ({self.duration})")

    def generate_thumbnail(self):
        print(f"Thumbnail generated for: {self.title}")


class CourseVideo(BaseVideo):
    def __init__(self, title, duration, module_number, downloadable_resources):
        super().__init__(title, duration)
        self.module_number = module_number
        self.downloadable_resources = downloadable_resources

    def upload(self):
        super().upload()
        print(f"Module {self.module_number} uploaded as part of full course.")
        if self.downloadable_resources:
            print(f"Includes {len(self.downloadable_resources)} downloadable resources.")

    def list_resources(self):
        print("📚 Downloadable Resources:")
        for res in self.downloadable_resources:
            print(f" - {res}")

    def mark_as_completed(self):
        print(f"✅ Course module '{self.title}' marked as completed.")


class TutorialVideo(BaseVideo):
    def __init__(self, title, duration, topic):
        super().__init__(title, duration)
        self.topic = topic

    def upload(self):
        super().upload()
        print(f"Topic tagged: {self.topic}")

    def add_chapters(self):
        print("Chapters added for better navigation.")

class LiveStreamVideo(BaseVideo):
    def __init__(self, title, duration, is_chat_enabled):
        super().__init__(title, duration)
        self.is_chat_enabled = is_chat_enabled

    def upload(self):
        super().upload()
        chat_status = "enabled" if self.is_chat_enabled else "disabled"
        print(f"Live chat is {chat_status}.")

    def schedule_stream(self, time):
        print(f"Stream scheduled at {time}")


# Example usage:
# 🎓 Tutorial Video
tutorial = TutorialVideo("Day 10: Functions in Python", "25:00", "Functions")
tutorial.generate_thumbnail()
tutorial.upload()
tutorial.add_chapters()

print("\n" + "-"*40 + "\n")

# 📺 Live Stream
live = LiveStreamVideo("Live Doubt Solving - Week 2", "60:00", True)
live.generate_thumbnail()
live.upload()
live.schedule_stream("Saturday 6 PM")

print("\n" + "-"*40 + "\n")

# 🧠 Course Video
course = CourseVideo(
    "Module 5: Python OOP Mastery",
    "35:00",
    module_number=5,
    downloadable_resources=["OOP Notes.pdf", "Practice Exercises.zip"]
)


course.__new__(CourseVideo)
course.__init__()
course.generate_thumbnail()
course.upload()
course.list_resources()
course.mark_as_completed()