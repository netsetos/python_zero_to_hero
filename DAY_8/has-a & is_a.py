
# IS-A Relationship
# class User:
#     def login(self):
#         print("User logged in")
#
# class Creator(User):  # IS-A relationship
#     def upload_video(self):
#         print("Video uploaded")
#
# # # Demonstrate IS-A relationship
# c = Creator()
# c.login()         # Inherited from User
# c.upload_video()  # Defined in Creator

# HAS-A Relationship

# class CommentSystem:
#     def add_comment(self, comment):
#         print(f"Comment added: {comment}")
#
#
# class Video:
#     def __init__(self):
#         self.comment_system = CommentSystem()  # HAS-A relationship
#
#     def comment_on_video(self, text):
#         self.comment_system.add_comment(text)
#
#
# # Demonstrate HAS-A relationship
# vid = Video()
# vid.comment_on_video("Great tutorial!")