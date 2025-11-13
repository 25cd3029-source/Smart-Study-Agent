from utils.ai_engine import AIEngine

class DoubtAgent:
    def __init__(self, text):
        self.text = text
        self.ai_engine = AIEngine()

    def solve(self, question):
        return self.ai_engine.solve_doubt(self.text, question)
