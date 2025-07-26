class Video:
    def __init__(self):
        print("Inside __init__: Initializing the video object")
    def get_display(self):
        print("in display")


# v=Video()
# v.get_display()

v = Video.__new__(Video)
v.__init__()
v.get_display()







# Step-by-step manual object creation

# print("Step 1: Create raw object using __new__")
# v = Video.__new__(Video)     # this only creates the object, doesn't initialize
#
# print("Step 2: Initialize the object using __init__")
# v.__init__()                 # now initialize the object manually
#
# # Check that object works
# print("Object created:", v)
# v.get_display()