class User:
    def login(self, username):
        print(f"{username} logged in to YouTube.")

class Creator(User):  # Inheriting from User
    def upload_video(self, title):
        print(f"Uploaded video: {title}")

# Demonstrate single inheritance
c = Creator()
c.login("Tech Creator")     # Inherited from User
c.upload_video("Python OOP")  # Defined in Creator

'''
   User
     ▲
     |
  Creator
'''