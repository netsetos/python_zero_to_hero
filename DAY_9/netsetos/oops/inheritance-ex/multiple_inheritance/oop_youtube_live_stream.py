class LiveStream(Upload):
    def start_stream(self): ...

class InteractiveSession:
    def ask_question(self): ...

class LiveCodingStream(LiveStream, InteractiveSession):  # 👈 Multiple Inheritance
    def display_interactive_session_summary(self): ...

'''    
📦 What Happens:
LiveCodingStream inherits:

    Upload & live stream features from LiveStream
    Interactive Q&A features from InteractiveSession
    It gets both behaviors in one class.

✅ Why Useful:
    Perfect for a hybrid YouTube class that 
    mixes video streaming with interactive chat — like a live coding tutorial.

'''