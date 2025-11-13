from utils.ai_engine import AIEngine

class PlannerAgent:
    def __init__(self, text):
        self.text = text
        self.ai_engine = AIEngine()

    def run(self):
        return self.ai_engine.generate_study_plan(self.text)
