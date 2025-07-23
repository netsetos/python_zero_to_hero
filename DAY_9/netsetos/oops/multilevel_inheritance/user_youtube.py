class User:
    def login(self):
        print("User logged in")

class Creator(User):
    def upload(self):
        print("Video uploaded")

class MonetizedCreator(Creator):
    def enable_ads(self):
        print("Ads enabled on video")

# Demonstrate multilevel inheritance
mc = MonetizedCreator()
mc.login()        # Inherited from User
mc.upload()       # Inherited from Creator
mc.enable_ads()   # Defined in MonetizedCreator

'''
     User
      ▲
   Creator
      ▲
MonetizedCreator
'''