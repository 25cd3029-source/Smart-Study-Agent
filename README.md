# 🚀 Smart Study Agent

Smart Study Agent is an AI-powered learning platform that transforms your study materials into interactive flashcards, quizzes, summaries, and plans
---

## 🌟 Features

- **PDF Upload & Extraction**  
  Upload your study materials in PDF and instantly extract text for learning!

- **AI Flashcards with Audio**  
  Generate interactive flashcards (with audio support) from your notes using GPT-4o or OpenAI or Ollama.

- **Smart Quiz Generator**  
  Auto-create multiple-choice quizzes and track your performance and weak areas.

- **Plan & Summarize**  
  Instantly generate structured study plans and summaries, personalized by AI.

- **Goal Tracker & Reminders**  
  Set study goals and get smart reminders for motivation and habit building.

- **Beautiful Galaxy UI**  
  Enjoy a unique animated galaxy background, frosted-glass cards, and fluid transitions everywhere.

- **Professional Animations**  
  12+ custom animations — gradient-shifting text, hover glows, scale/slide transitions, and much more.

- **Mobile-Friendly**  
  Responsive and modern, works beautifully across all devices.

- **Sidebar Always Visible**  
  Clean workspace, no toggle/minimize button distractions.

---

## 🖥️ Tech Stack

- **Frontend:** Streamlit + Custom CSS
- **Backend:** Python
- **AI:** OpenAI GPT-4o Mini / Ollama
- **Audio:** gTTS (Google Text-to-Speech)
- **PDF Processing:** PyMuPDF (fitz)

---

## 🚀 Getting Started

### 1. Clone This Repo
```
git clone https://github.com/your-username/smart-study-agent.git
cd smart-study-agent
```

### 2. Install Requirements
```
pip install -r requirements.txt
```

### 3. Run the App
```
streamlit run app.py
```

Visit `http://localhost:8501` in your browser.

---

## 📝 Project Structure

smart-study-agent/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── voice_flashcards.py         # Audio functionality
├── .env.example                # API key template
├── agents/
│   ├── reader.py              # PDF text extraction
│   ├── flashcard.py           # Flashcard generation
│   ├── quiz.py                # Quiz generation
│   ├── planner.py             # Study plan generation
│   ├── summarizer.py          # Summary generation
│   ├── doubt.py               # Q&A agent
│   └── analyzer.py            # Performance analysis
├── utils/
│   ├── ui_styles.py           # ALL custom CSS & galaxy background
│   ├── ai_engine.py           # OpenAI/Ollama integration
│   ├── pdf_utils.py           # PDF processing
│   └── reminder_system.py      # Goal tracking
└── README.md


## 🎨 UI/UX Features

### 12+ Custom Animations
- ✨ Gradient shifting text
- 🎯 Hover glow effects
- 📊 Scale & slide transitions
- 🌀 Floating animations
- 💫 Shimmer effects
- 🔄 Rotate & bounce
- 📍 Blur fade-ins

### Design Elements
- 🌌 Galaxy background (fixed)
- 🎭 Frosted glass cards (backdrop-filter)
- 🎨 Gradient buttons & text
- 📱 Fully responsive
- 🌙 Dark theme optimized

---

## ⚡ Usage Guide

### 1. Upload PDF
- Click "Upload PDF" in sidebar
- Wait for extraction

### 2. Generate Flashcards
- Click "Generate Flashcards"
- Review and flip cards
- Use shuffle for random order
- Play audio for pronunciation

### 3. Take Quiz
- Click "Generate Quiz"
- Answer multiple-choice questions
- Get instant feedback
- Track weak areas

### 4. Create Study Plan
- Click "Generate Plan"
- Get 3-day structured plan
- Personalized learning path

### 5. Get Summary
- Click "Generate Summary"
- Read key points & insights
- Listen to audio summary

### 6. Ask Doubts
- Type any question
- Get AI-powered answers
- Based on your material

### 7. Track Goals
- Set study goals
- Get reminders
- Mark completed
- See progress

---

## 📊 Performance Metrics

- **Flashcard Generation:** ~2-3 seconds
- **Quiz Generation:** ~3-4 seconds
- **Summary Generation:** ~4-5 seconds
- **Page Load:** <1 second
- **Animation FPS:** 60 FPS

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| PDF not uploading | Check file size (<200MB) and format |
| API key errors | Verify `.env` has correct `OPENAI_API_KEY` |
| Animations not smooth | Update browser or try Chrome/Firefox |
| Audio not playing | Install `gtts`: `pip install gtts` |

---

## ❤️ Credits & Acknowledgments

- **OpenAI** - GPT-4o Mini API
- **Streamlit** - Web framework
- **PyMuPDF** - PDF processing
- **gTTS** - Text-to-speech
---

**Made with 💎 and 🚀 by Team Code Commandos**



***

**Ready to upload! 🎉**
