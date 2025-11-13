from gtts import gTTS
import os
import streamlit as st

def play_flashcard_audio(q, a, idx=0):
    try:
        text = f"Question. {q}. Answer: {a}."
        tts = gTTS(text, lang='en', slow=False)

        os.makedirs("outputs", exist_ok=True)
        path = f"outputs/flashcard_{idx}.mp3"
        tts.save(path)

        with open(path, 'rb') as f:
            st.audio(f, format='audio/mp3')
    except Exception as e:
        st.error(f"Error: {e}")

def play_summary_audio(text):
    try:
        tts = gTTS(text[:5000], lang='en', slow=False)
        os.makedirs("outputs", exist_ok=True)
        path = "outputs/summary.mp3"
        tts.save(path)
        with open(path, 'rb') as f:
            st.audio(f, format='audio/mp3')
    except Exception as e:
        st.error(f"Error: {e}")
