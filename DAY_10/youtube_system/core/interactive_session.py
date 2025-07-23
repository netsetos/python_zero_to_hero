from datetime import datetime


class InteractiveSession:
    def __init__(self):
        self.questions = []
        self.answers = []

    def ask_question(self, user, question_text):
        question = {"user": user.username, "question":question_text, "timestamp":datetime.now()}
        self.questions.append(question)
        print(f"{user.username} asked: '{question_text}'")

    def provide_answer(self, question_index, answer_text):
        if 0 <= question_index < len(self.questions):
            question = self.questions[question_index]
            self.answers[question["question"]] = answer_text
            print(f"Answered '{question["question"]}' with: '{answer_text}'")
        else:
            print("Invalid question index")


