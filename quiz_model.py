class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

    def _on_honor_gpa(self):
        if self.grade >= 3.5:
            return True
        else:
            return False