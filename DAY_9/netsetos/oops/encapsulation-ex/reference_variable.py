

#object without reference
class Channel:
    def __init__(self):
        self.name='Netsetos'
        self.age = 5


p=Channel()
q=p

# print(id(p))
# print(id(q))
# print(p.name)
# print(q.name)
#change attribute value of 2nd object

q.name = "Google"
# print(q.name)


#Pass By Reference
class Channel:
    def __init__(self, name, age):
        self.name= name
        self.age = age

#Function Outside the class
def run(channel):
    # print("Hi, Welcome to ", channel.name, "We are",channel.age,"years old.")
    c1 = Channel("Google", 26)
    return c1

c = Channel("Netsetos", "5")
ch = run(c)
# print(ch.name)
# print(ch.age)

#Mutable Objects
class Channel:
    def __init__(self, name, age):
        self.name= name
        self.age = age

#Function Outside the class
def run(channel):
    # print(id(channel))
    channel.name = "Google"
    return channel


c = Channel("Netsetos", "5")
print(id(c))
c1 = run(c)
print(id(c))