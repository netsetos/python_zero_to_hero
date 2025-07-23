# Tightly coupled to loosley coupled
#Composition
class CommentSystem:
    def add_comment(self, comment):
        print(f"Comment added: {comment}")


class Video:
    def __init__(self):
        self.comment_system = CommentSystem()  # HAS-A relationship

    def comment_on_video(self, text):
        self.comment_system.add_comment(text)

vid = Video()
vid.comment_on_video("Great tutorial!")



#Aggregation

class CommentSystem:
    def add_comment(self, comment):
        print(f"Comment added: {comment}")


class Video:
    def __init__(self, comment_system):
        self.comment_system = comment_system  # Aggregation (HAS-A)

    def comment_on_video(self, text):
        self.comment_system.add_comment(text)