# Parent class1

class Teacher:
    def teach(self):
        print("Teaches Computer and English")

# Parent class2
class Coach:
    def train(self):
        print("Trains in Basketball and VolleyBall")

# Child class inherits from both Teacher and Coach
class Student(Teacher, Coach):
    def activities(self):
        print("Student is active in both academics and sports")
        self.teach()  # Calling method from Teacher
        self.train()  # Calling method from Coach

# Create object of Student
s = Student()
s.activities()