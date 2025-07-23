from DAY_10.youtube_system.core.live_stream import LiveStream
from DAY_10.youtube_system.core.interactive_session import InteractiveSession

class LiveCodingStream(LiveStream, InteractiveSession):
    def __init__(self, title, description, uploader):
        LiveStream.__init__(self, title, description, uploader)
        InteractiveSession.__init__(self)
        print(f"Live Coding Stream '{self.title}' created, ready for interactive session!")

    def display_interactive_session_summary(self):
        print(f"\n--- Interactive Session Summary for '{self.title}' ---")
        if not self.questions:
            print("No questions asked yet. ")
            return

        for i, question in enumerate(self.questions):
            print(f"Q{i+1} by {question['user']} at {question['timestamp'].strftime('%H:%M:%S')}: {question['question']}")
            if question['question'] in self.answers:
                print(f"  A: {self.answers[question['question']]}")
            else:
                print(f" (Unanswered")
        print("-" * 40)
