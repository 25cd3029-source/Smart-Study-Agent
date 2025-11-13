from utils.ai_engine import AIEngine

class SummarizerAgent:
    def __init__(self, text):
        self.text = text
        self.ai_engine = AIEngine()

    def run(self):
        return self.ai_engine.generate_summary(self.text)
