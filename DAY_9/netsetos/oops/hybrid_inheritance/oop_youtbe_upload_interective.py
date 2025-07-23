class Upload: ...
class Video(Upload): ...
class LiveStream(Upload): ...
class InteractiveSession: ...

class LiveCodingStream(LiveStream, InteractiveSession): ...

'''
📦 What Happens:
    This combines:
    Multilevel: Upload → LiveStream
    
    Multiple: LiveCodingStream(LiveStream, InteractiveSession)
    
    So LiveCodingStream has:
        Uploading and streaming features
        Real-time chat and interaction

✅ Why Useful:
    Most real-world applications require combining logic.
    
    For example, a YouTube Live Lecture needs:

        Streaming logic
        Upload data
        Interactive Q&A

'''