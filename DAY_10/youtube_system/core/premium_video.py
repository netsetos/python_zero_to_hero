from .video import Video

class PremiumVideo(Video):
    def __init__(self, title, description, uploader, duration, subscription_required=True):
        super().__init__(title, description, uploader, duration)
        self.subscription_required = subscription_required
        self.ad_free = True

    def get_details(self):
        base_details = super().get_details()
        premium_info = "\nPremium: Yes (Ad-Free)" if self.subscription_required else "\nPremium: No"
        return base_details + premium_info