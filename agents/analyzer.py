from utils.ai_engine import AIEngine

class AnalyzerAgent:
    def __init__(self, quiz_data, weak_areas):
        self.quiz_data = quiz_data
        self.weak_areas = weak_areas
        self.ai_engine = AIEngine()

    def analyze(self):
        prompt = f"""Based on these weak areas: {self.weak_areas}
        Generate personalized learning recommendations."""
        return self.ai_engine.call_ai(prompt)
