from utils.ai_engine import AIEngine

class QuizAgent:
    def __init__(self, text):
        self.text = text
        self.ai_engine = AIEngine()

    def run(self):
        return self.ai_engine.generate_quiz(self.text)
