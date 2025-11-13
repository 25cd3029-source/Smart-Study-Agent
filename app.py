import os, sys, json, datetime
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
import re

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from agents.reader import ReaderAgent
from agents.flashcard import FlashcardAgent
from agents.quiz import QuizAgent
from agents.planner import PlannerAgent
from agents.doubt import DoubtAgent
from agents.summarizer import SummarizerAgent
from utils.ui_styles import load_custom_css
from utils.reminder_system import ReminderSystem
from utils.ai_engine import AIEngine
from voice_flashcards import play_flashcard_audio, play_summary_audio

load_dotenv()

st.set_page_config(
    page_title="🧠 Smart Study Agent",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load enhanced CSS with animations
load_custom_css("dark")

ai_engine = AIEngine()

for key in ["flashcards", "current_card", "quiz_data", "quiz_answers", "progress", 
            "text_content", "summary_text", "quiz_history", "weak_areas"]:
    if key not in st.session_state:
        if key == "flashcards":
            st.session_state[key] = []
        elif key == "progress":
            st.session_state[key] = 0
        elif key == "quiz_history":
            st.session_state[key] = []
        elif key == "weak_areas":
            st.session_state[key] = {}
        else:
            st.session_state[key] = {} if key in ["quiz_answers"] else ""

reminder_system = ReminderSystem()

# SIDEBAR - Always visible
with st.sidebar:
    st.markdown("""<div class="sidebar-header">📚 STUDY TOOLS</div>""", unsafe_allow_html=True)

    st.divider()

    st.markdown("**📤 Upload Your Material**")
    pdf = st.file_uploader("Upload PDF", type=["pdf"], label_visibility="collapsed", key="pdf_upload")

    if pdf:
        try:
            reader = ReaderAgent(pdf)
            st.session_state.text_content = reader.run()
            st.success("✅ PDF loaded successfully!")
        except Exception as e:
            st.error(f"❌ Error: {e}")

    # Show these only after file is uploaded
    if st.session_state.text_content:
        st.divider()

        progress_value = min(st.session_state.progress, 100)
        st.progress(progress_value / 100)
        st.caption(f"📊 Progress: {progress_value}%")

        st.divider()

        st.markdown("**🎯 Add Study Goal**")
        col1, col2 = st.columns([3, 1])
        with col1:
            goal = st.text_input("Goal:", placeholder="e.g., Complete 50 flashcards", label_visibility="collapsed", key="goal_input")
        with col2:
            if st.button("➕", help="Add goal", key="add_goal_btn"):
                if goal:
                    reminder_system.add_goal(goal)
                    st.success("✅ Added!")
                    st.rerun()

        st.divider()

        st.markdown("""<div class="sidebar-footer">
            <strong>🎓 SMART STUDY AGENT</strong><br>
            <small>Enterprise AI Learning</small><br><br>
            ✨ Features:<br>
            • 🃏 Flashcards + Audio<br>
            • 📝 Interactive Quiz<br>
            • 📊 Performance Analytics<br>
            • 🔔 Smart Reminders<br>
            • 🎯 Study Goals<br>
            <br><small>Crafted with 💎</small>
        </div>""", unsafe_allow_html=True)

# UPLOAD PAGE (before file is uploaded)
if not st.session_state.text_content:
    st.markdown("""
    <div class="welcome-container">
        <div class="animated-background"></div>
        <div class="content-wrapper">
            <div class="title-section">
                <div class="animated-title">
                    <span class="title-char">🚀</span>
                    <span class="title-text-animated">Smart Study Agent</span>
                </div>
                <p class="animated-subtitle">AI-Powered Learning Platform</p>
                <p class="animated-description">Transform your study materials into an interactive learning experience with AI-generated flashcards, quizzes, and personalized learning paths.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# MAIN LANDING PAGE (after file is uploaded)
elif st.session_state.text_content:
    st.markdown("""
    <div class="premium-container">
        <div class="main-header-wrapper">
            <div class="main-header">
                <div class="header-glow"></div>
                <div class="animated-title-main">
                    <span class="rocket-icon">🧠</span>
                    <span class="title-text-main">Smart Study Agent</span>
                </div>
                <p class="premium-subtitle">✨ Enterprise AI Learning Platform ✨</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(
        ["📊 Dashboard", "🃏 Flashcards", "📝 Quiz", "📅 Plan", "📄 Summary", "❓ Doubts", "📈 Analytics", "🎯 Goals"]
    )

    with tab1:
        st.markdown("""<div class="premium-card overview-card"><h3>📊 Learning Dashboard</h3></div>""", unsafe_allow_html=True)

        col1, col2, col3, col4 = st.columns(4)
        words_count = len(st.session_state.text_content.split())
        with col1:
            st.metric("📖 Words", f"{words_count:,}")
        with col2:
            st.metric("🔥 Streak", f"{reminder_system.get_streak()} days")
        with col3:
            if st.session_state.quiz_history:
                avg_score = sum([q['score'] for q in st.session_state.quiz_history]) / len(st.session_state.quiz_history)
                st.metric("⭐ Avg Score", f"{avg_score:.1f}%")
            else:
                st.metric("⭐ Avg Score", "N/A")
        with col4:
            st.metric("🎓 Goals", len(reminder_system.goals))

        st.divider()

        st.markdown("<h4>🔔 Active Reminders</h4>", unsafe_allow_html=True)
        reminders = reminder_system.get_active_reminders()
        if reminders:
            for reminder in reminders:
                st.info(f"📍 {reminder}")
        else:
            st.info("No active reminders. Set a study goal!")

    with tab2:
        st.markdown("""<div class="premium-card flashcard-header"><h3>🃏 Interactive Flashcards</h3></div>""", unsafe_allow_html=True)

        col1, col2 = st.columns([2, 1])
        with col1:
            if st.button("✨ Generate Flashcards", key="gen_flashcards", use_container_width=True):
                with st.spinner("🔄 Creating flashcards..."):
                    try:
                        raw_cards = ai_engine.generate_flashcards(st.session_state.text_content)
                        cards = []
                        q = None
                        for line in raw_cards.split("\n"):
                            if line.startswith("Q:"):
                                q = line[2:].strip()
                            elif line.startswith("A:") and q:
                                a = line[2:].strip()
                                cards.append({"question": q, "answer": a, "flipped": False})
                                q = None
                        st.session_state.flashcards = cards
                        st.session_state.current_card = 0
                        st.session_state.progress = min(st.session_state.progress + 15, 100)
                        st.success(f"✅ Created {len(cards)} flashcards!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"❌ Error: {e}")

        with col2:
            if st.session_state.flashcards:
                if st.button("🔀 Shuffle", use_container_width=True):
                    import random
                    random.shuffle(st.session_state.flashcards)
                    st.rerun()

        if st.session_state.flashcards:
            card_count = len(st.session_state.flashcards)
            st.markdown(f"<div class='card-counter'>🃏 Card {st.session_state.current_card + 1} / {card_count}</div>", unsafe_allow_html=True)
            st.progress((st.session_state.current_card + 1) / card_count)

            current_card = st.session_state.flashcards[st.session_state.current_card]

            st.markdown(f"""
            <div class="flashcard-container">
                <div class="premium-flashcard flip-animation">
                    <div class="card-shine"></div>
                    <div class="card-bg-gradient"></div>
                    <h4>❓ Question</h4>
                    <p>{current_card['question']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

            if st.button("👀 Reveal Answer", use_container_width=True, key=f"reveal_{st.session_state.current_card}"):
                st.session_state.flashcards[st.session_state.current_card]["flipped"] = True
                st.rerun()

            if current_card.get("flipped", False):
                st.markdown(f"""
                <div class="flashcard-container">
                    <div class="premium-flashcard-answer flip-animation-reverse">
                        <div class="card-shine"></div>
                        <div class="card-bg-gradient"></div>
                        <h4>✅ Answer</h4>
                        <p>{current_card['answer']}</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🔊 Play Audio", key=f"audio_fc_{st.session_state.current_card}"):
                        try:
                            play_flashcard_audio(current_card['question'], current_card['answer'], st.session_state.current_card)
                            st.success("🔊 Audio playing...")
                        except Exception as e:
                            st.error(f"❌ Error: {e}")
                with col2:
                    st.info("💡 Tip: Use audio for pronunciation!")

            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("⬅️ Previous", use_container_width=True, key="prev_card"):
                    st.session_state.current_card = max(0, st.session_state.current_card - 1)
                    st.rerun()
            with col2:
                st.markdown(f"<div class='card-nav-center'>{st.session_state.current_card + 1}/{card_count}</div>", unsafe_allow_html=True)
            with col3:
                if st.button("Next ➡️", use_container_width=True, key="next_card"):
                    st.session_state.current_card = min(card_count - 1, st.session_state.current_card + 1)
                    st.rerun()
        else:
            st.info("👆 Generate flashcards!")

    with tab3:
        st.markdown("""<div class="premium-card quiz-header"><h3>📝 Interactive Quiz</h3></div>""", unsafe_allow_html=True)

        if st.button("🎯 Generate Quiz", use_container_width=True, key="gen_quiz"):
            with st.spinner("📋 Creating quiz..."):
                try:
                    quiz_json = ai_engine.generate_quiz(st.session_state.text_content)

                    try:
                        st.session_state.quiz_data = json.loads(quiz_json)
                    except json.JSONDecodeError:
                        json_match = re.search(r'\[.*\]', quiz_json, re.DOTALL)
                        if json_match:
                            st.session_state.quiz_data = json.loads(json_match.group())
                        else:
                            raise Exception("Could not parse JSON response")

                    st.session_state.quiz_answers = {}
                    st.session_state.progress = min(st.session_state.progress + 20, 100)
                    st.success("✅ Quiz ready!")
                    st.rerun()
                except json.JSONDecodeError as e:
                    st.error(f"❌ JSON Parse Error: {str(e)}")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")

        if st.session_state.quiz_data:
            quiz = st.session_state.quiz_data
            if isinstance(quiz, list) and len(quiz) > 0:
                st.markdown(f"<div class='quiz-progress'>📋 Questions: {len(quiz)}</div>", unsafe_allow_html=True)

                with st.form(key="quiz_form"):
                    for idx, question in enumerate(quiz):
                        if isinstance(question, dict):
                            q_text = question.get('question', f'Question {idx+1}')
                            st.markdown(f"""
                            <div class="premium-card quiz-question">
                                <h4>Q{idx + 1}: {q_text}</h4>
                            </div>
                            """, unsafe_allow_html=True)

                            options = question.get("options", [])
                            if options:
                                selected = st.radio("Select:", options, key=f"quiz_q{idx}", label_visibility="collapsed")
                                st.session_state.quiz_answers[str(idx)] = selected
                            st.divider()

                    submit = st.form_submit_button("✅ Submit Quiz", use_container_width=True)

                if submit and len(st.session_state.quiz_answers) > 0:
                    score = 0
                    weak_topics = {}

                    for idx, question in enumerate(quiz):
                        correct_answer = question.get("answer", "")
                        user_answer = st.session_state.quiz_answers.get(str(idx), "")

                        st.markdown(f"""
                        <div class="premium-card quiz-result-item">
                            <h4>Question {idx + 1}</h4>
                            <p><strong>Your Answer:</strong> {user_answer}</p>
                            <p><strong>Correct Answer:</strong> {correct_answer}</p>
                        </div>
                        """, unsafe_allow_html=True)

                        if user_answer.strip().lower() == correct_answer.strip().lower():
                            st.success("✅ Correct!")
                            score += 1
                        else:
                            st.error("❌ Incorrect")
                            topic = question.get("topic", "General")
                            weak_topics[topic] = weak_topics.get(topic, 0) + 1
                        st.divider()

                    percentage = (score / len(quiz)) * 100
                    st.session_state.quiz_history.append({"score": percentage, "timestamp": datetime.datetime.now().isoformat()})
                    st.session_state.weak_areas = weak_topics
                    reminder_system.increment_streak()

                    st.markdown(f"""
                    <div class="premium-card quiz-score pulse-animation">
                        <h3>🎉 Score: {score}/{len(quiz)} ({percentage:.1f}%)</h3>
                    </div>
                    """, unsafe_allow_html=True)

                    if weak_topics:
                        st.markdown("<h4>📍 Weak Areas:</h4>", unsafe_allow_html=True)
                        for topic, count in weak_topics.items():
                            st.warning(f"⚠️ {topic}: {count} mistakes")

                    if st.button("🔄 Retake", use_container_width=True):
                        st.session_state.quiz_answers = {}
                        st.session_state.quiz_data = None
                        st.rerun()
            else:
                st.error("❌ Invalid quiz format!")
        else:
            st.info("👆 Generate quiz!")

    with tab4:
        st.markdown("""<div class="premium-card plan-header"><h3>📅 Study Plan</h3></div>""", unsafe_allow_html=True)

        if st.button("📋 Generate Plan", use_container_width=True, key="gen_plan"):
            with st.spinner("📝 Creating..."):
                try:
                    plan = ai_engine.generate_study_plan(st.session_state.text_content)
                    st.markdown(plan)
                    st.session_state.progress = min(st.session_state.progress + 25, 100)
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        else:
            st.info("👆 Generate plan!")

    with tab5:
        st.markdown("""<div class="premium-card summarizer-header"><h3>📄 Smart Summarizer</h3></div>""", unsafe_allow_html=True)

        col1, col2 = st.columns([2, 1])
        with col1:
            if st.button("✨ Generate Summary", use_container_width=True, key="gen_summary"):
                with st.spinner("📝 Creating..."):
                    try:
                        summary = ai_engine.generate_summary(st.session_state.text_content)
                        st.session_state.summary_text = summary
                        st.markdown(summary)
                        st.session_state.progress = min(st.session_state.progress + 15, 100)
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")

        with col2:
            if st.session_state.summary_text and st.button("🔊 Audio", key="audio_summary"):
                try:
                    play_summary_audio(st.session_state.summary_text)
                    st.success("🔊 Playing...")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")

    with tab6:
        st.markdown("""<div class="premium-card doubt-header"><h3>❓ Ask Doubts</h3></div>""", unsafe_allow_html=True)

        doubt_question = st.text_area("Question:", placeholder="Type here...", height=100, label_visibility="collapsed")

        if st.button("💡 Get Answer", use_container_width=True, key="answer_doubt"):
            if doubt_question.strip():
                with st.spinner("🔍 Finding..."):
                    try:
                        answer = ai_engine.solve_doubt(st.session_state.text_content, doubt_question)
                        st.success("✅ Found!")
                        st.markdown(f"""
                        <div class="premium-card answer-card fade-in-up">
                            <h4>💬 Answer</h4>
                            <p>{answer}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        st.session_state.progress = min(st.session_state.progress + 10, 100)
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")
            else:
                st.warning("⚠️ Enter a question!")

    with tab7:
        st.markdown("""<div class="premium-card"><h3>📈 Performance Analytics</h3></div>""", unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("<h4>📊 Quiz History</h4>", unsafe_allow_html=True)
            if st.session_state.quiz_history:
                scores = [q['score'] for q in st.session_state.quiz_history]
                st.line_chart({"Score %": scores})
                st.metric("Average", f"{sum(scores)/len(scores):.1f}%")
                st.metric("Best", f"{max(scores):.1f}%")
                st.metric("Total Quizzes", len(scores))
            else:
                st.info("No quiz history yet!")

        with col2:
            st.markdown("<h4>🎯 Weak Areas</h4>", unsafe_allow_html=True)
            if st.session_state.weak_areas:
                for topic, count in st.session_state.weak_areas.items():
                    st.warning(f"⚠️ {topic}: {count} errors")
            else:
                st.info("No weak areas identified!")

    with tab8:
        st.markdown("""<div class="premium-card"><h3>🎯 Study Goals</h3></div>""", unsafe_allow_html=True)

        goals = reminder_system.goals

        if goals:
            st.markdown("<h4>📝 Your Goals</h4>", unsafe_allow_html=True)

            for idx, goal_item in enumerate(goals):
                goal_text = goal_item.get("goal", "")
                completed = goal_item.get("completed", False)

                col1, col2, col3 = st.columns([3, 1, 1])

                with col1:
                    if completed:
                        st.markdown(f"<div class='goal-completed'>✅ {goal_text}</div>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<div class='goal-pending'>📌 {goal_text}</div>", unsafe_allow_html=True)

                with col2:
                    if not completed:
                        if st.button("✓", key=f"complete_{idx}", use_container_width=True, help="Mark complete"):
                            reminder_system.mark_goal_completed(idx)
                            st.success("✅ Done!")
                            st.rerun()

                with col3:
                    if st.button("🗑️", key=f"delete_{idx}", use_container_width=True, help="Delete"):
                        reminder_system.delete_goal(idx)
                        st.success("Deleted!")
                        st.rerun()

                st.divider()

            st.markdown(f"<div class='goal-stats'>📊 Completed: {sum(1 for g in goals if g.get('completed', False))}/{len(goals)}</div>", unsafe_allow_html=True)
        else:
            st.info("👈 Add goals in settings to get started!")
