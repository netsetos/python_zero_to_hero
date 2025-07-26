class Upload:
    def get_details(self): ...

class Video(Upload):  # Level 1
    def increment_views(self): ...

class PremiumVideo(Video):  # Level 2
    def get_details(self): ...

'''
📦 What Happens:
    PremiumVideo gets:
    
    From Video: views, duration, comments
    
    From Upload: title, description, upload_date

✅ Why Useful:
    Good when you want to build progressively enhanced classes:
    
    Upload → Video → PremiumVideo
    
    Each level specializes more.
'''