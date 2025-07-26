class CreatorAnalytics:
    def __init__(self, earnings):
        self.__earnings = earnings  # private

    def __show_earnings(self):  # private method
        print(f"Earnings: ${self.__earnings}")

    def display(self):  # public method to access private
        self.__show_earnings()

    # Usage


yt = CreatorAnalytics(1200)

# Cannot access directly:
# print(yt.__earnings) #❌
# yt.__show_earnings() #❌

yt.display()  # ✅ OK