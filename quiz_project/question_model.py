class Question:
    def __init__(self, question_text, answer):
        self.question_text = question_text
        self.answer = answer

new_q = Question("What is the capital of France?", "Paris")
print(new_q.question_text)  # Output: What is the capital of France?
print(new_q.answer)  # Output: Paris