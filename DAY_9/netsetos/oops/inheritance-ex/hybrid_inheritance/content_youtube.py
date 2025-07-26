class Content:
    def report(self):
        print("Content reported.")

class Video(Content):
    def play(self):
        print("Playing video...")

class Comment(Content):
    def add(self, text):
        print(f"Comment: {text}")

class YouTube(Video, Comment):
    def share(self):
        print("Shared to WhatsApp.")

# Demonstrate hybrid inheritance
yt = YouTube()
yt.play()           # Inherited from Video
yt.add("Nice video!") # Inherited from Comment
yt.report()         # Inherited from Content (via Video/Comment)
yt.share()          # Defined in YouTube