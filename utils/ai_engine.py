import os
from dotenv import load_dotenv
from openai import OpenAI
import json
import re

load_dotenv()

class AIEngine:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        ollama_model = os.getenv("OLLAMA_MODEL", None)

        self.use_ollama = False
        self.client = None
        self.model = None

        if api_key:
            self.client = OpenAI(api_key=api_key)
            self.model = "gpt-4o-mini"
        elif ollama_model:
            try:
                from ollama import Client
                self.client = Client(host='http://localhost:11434')
                self.model = ollama_model
                self.use_ollama = True
            except:
                raise Exception("Set OPENAI_API_KEY or configure Ollama")

    def call_ai(self, prompt):
        """Call AI with fallback"""
        try:
            if self.use_ollama:
                response = self.client.generate(model=self.model, prompt=prompt)
                return response['response']
            else:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )
                return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"AI Error: {e}")

    def generate_flashcards(self, text):
        prompt = f"""Create EXACTLY 5 flashcards from this text. Use ONLY this format:
Q: question text
A: answer text

Text: {text[:5000]}"""
        return self.call_ai(prompt)

    def generate_quiz(self, text):
        prompt = f"""Create EXACTLY 5 multiple-choice questions as valid JSON array.
Return ONLY valid JSON:

[
  {{"question": "What is...", "options": ["Option A", "Option B", "Option C", "Option D"], "answer": "Option A", "topic": "Topic"}}
]

Text: {text[:5000]}"""
        return self.call_ai(prompt)

    def generate_study_plan(self, text):
        prompt = f"""Create a 3-day study plan with emojis and clear structure.

Text: {text[:6000]}"""
        return self.call_ai(prompt)

    def generate_summary(self, text):
        prompt = f"""Create a well-structured summary with:
📌 Key Points
💡 Insights
📝 Facts

Text: {text[:8000]}"""
        return self.call_ai(prompt)

    def solve_doubt(self, text, question):
        prompt = f"""Answer this question based on the material provided:

Material: {text[:6000]}

Question: {question}

Answer:"""
        return self.call_ai(prompt)
