class Upload:
    def get_details(self): ...

class Video(Upload): ...
class Short(Upload): ...
class LiveStream(Upload): ...

'''
📦 What Happens:
All 3 classes (Video, Short, LiveStream) reuse:

    title, description, upload_date, uploader
    
    get_details()

    But they implement unique features:

    Video → duration + views

    Short → MAX_DURATION + special formatting

    LiveStream → live chat + stream state

✅ Why Useful:
    Best for variation on a common concept 
    (i.e., all are uploads, but of different kinds)
'''