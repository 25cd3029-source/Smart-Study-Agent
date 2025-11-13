import json
import os
from datetime import datetime

class ReminderSystem:
    def __init__(self, file="reminders.json"):
        self.file = file
        self.data = self.load_data()
        self.goals = self.load_goals()

    def load_data(self):
        if os.path.exists(self.file):
            with open(self.file) as f:
                return json.load(f)
        return {"streak": 0, "last_study": None}

    def load_goals(self):
        goals_file = "goals.json"
        if os.path.exists(goals_file):
            with open(goals_file) as f:
                return json.load(f)
        return []

    def save_data(self):
        with open(self.file, 'w') as f:
            json.dump(self.data, f)

        with open("goals.json", 'w') as f:
            json.dump(self.goals, f)

    def add_goal(self, goal):
        self.goals.append({"goal": goal, "created": datetime.now().isoformat(), "completed": False})
        self.save_data()

    def mark_goal_completed(self, idx):
        if 0 <= idx < len(self.goals):
            self.goals[idx]["completed"] = True
            self.save_data()

    def delete_goal(self, idx):
        if 0 <= idx < len(self.goals):
            self.goals.pop(idx)
            self.save_data()

    def increment_streak(self):
        self.data["streak"] = self.data.get("streak", 0) + 1
        self.data["last_study"] = datetime.now().isoformat()
        self.save_data()

    def get_streak(self):
        return self.data.get("streak", 0)

    def get_active_reminders(self):
        reminders = []
        if self.goals:
            pending = sum(1 for g in self.goals if not g.get("completed", False))
            if pending > 0:
                reminders.append(f"📝 You have {pending} pending goals!")

        streak = self.get_streak()
        if streak > 0:
            reminders.append(f"🔥 Keep your {streak} day streak alive!")
        else:
            reminders.append("🚀 Start studying to build a streak!")

        return reminders
