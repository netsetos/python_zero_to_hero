from core.user import User
from channels.channel import Channel
from core.video import Video
from core.short import Short
from core.live_stream import LiveStream
from core.premium_video import PremiumVideo
from core.comment import Comment
from core.live_coding_stream import LiveCodingStream
from playback.player import BasicVideoPlayer
from playback.premium_player import PremiumVideoPlayer



def main():
    # 1. Create user and channel
    user1 = User("netsetos", "netsetos@gmail.com")
    channel1 = Channel("NetsetosTech", user1)

    # 2. Upload a regular video
    video1 = Video("Intro to Python", "Beginner-friendly Python tutorial", channel1, duration=600)
    channel1.videos.append(video1)

    # 3. Upload a short
    short1 = Short("Python Tip", "Use list comprehensions!", channel1, duration=45)
    channel1.videos.append(short1)

    # 4. Upload a live stream
    stream = LiveStream("Live Python Q&A", "Ask your Python questions", channel1, duration=0)
    channel1.videos.append(stream)

    # 5. Upload a premium video
    premium_video = PremiumVideo("Advanced OOP  ", "Deep dive into Python OOP", channel1, duration=1800)
    channel1.videos.append(premium_video)

    # 6. New user subscribes, likes, and comments
    user2 = User("coder123", "coder@example.com")
    user2.subscribe_to_channel(channel1)
    user2.like_video(video1)
    user2.create_comment(video1, "Great explanation!")

    # 7. Play videos with Basic and Premium players
    basic_player = BasicVideoPlayer()
    premium_player = PremiumVideoPlayer()

    print("\n-- Basic Player Plays --")
    basic_player.play_video(video1)

    print("\n-- Premium Player Plays --")
    premium_player.play_video(premium_video)

    # 8. LiveCodingStream interaction
    live_coding = LiveCodingStream("Live Coding Bootcamp", "Build projects in Python", channel1)
    live_coding.ask_question(user2, "How to use decorators?")
    live_coding.provide_answer(0, "Decorators wrap functions to add extra behavior.")
    live_coding.display_interactive_session_summary()

    # 9. Channel summary
    print("\n-- Channel Overview --")
    channel1.display_channel_info()


if __name__ == "__main__":
    main()