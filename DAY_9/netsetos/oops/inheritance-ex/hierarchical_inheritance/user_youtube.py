class User:
    def login(self, username):
        print(f"{username} logged in")

class Viewer(User):


    def watch_video(self, title):
        print(f"Watching: {title}")

class Creator(User):



    def upload_video(self, title):
        print(f"Uploaded: {title}")

# Demonstrate hierarchical inheritance
v = Viewer()
v.login("Viewer123")
v.watch_video("Python Basics")

c = Creator()
c.login("Creator456")
c.upload_video("Advanced Python")