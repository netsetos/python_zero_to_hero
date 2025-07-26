class Upload:
    def get_details(self): ...

class Video(Upload):  # 👈 Single Inheritance
    def increment_views(self): ...

'''    
📦 What Happens:
Video inherits all attributes from Upload:

    title, description, upload_date, uploader
    
    get_details() method

    Video adds its own: views, duration, comments, etc.

✅ Why Useful:
    Avoids rewriting the upload_date, get_details() logic.
    
    Keeps code clean and DRY (Don’t Repeat Yourself).

'''

'''
  Upload
     ▲
     |
   Video
'''