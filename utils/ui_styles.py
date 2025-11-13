import streamlit as st

def load_custom_css(theme="dark"):
    """Load FINAL ENHANCED CSS - Premium animations + no sidebar toggle"""

    css = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');

        * { 
            font-family: 'Poppins', sans-serif !important;
        }

        /* PREMIUM ANIMATIONS */
        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        @keyframes floatingGlow {
            0%, 100% { transform: translateY(0px); opacity: 0.3; }
            50% { transform: translateY(-20px); opacity: 0.6; }
        }

        @keyframes shimmer {
            0% { background-position: -1000px 0; }
            100% { background-position: 1000px 0; }
        }

        @keyframes glow {
            0%, 100% { box-shadow: 0 0 20px rgba(96, 165, 250, 0.5), 0 0 40px rgba(96, 165, 250, 0.2); }
            50% { box-shadow: 0 0 40px rgba(167, 139, 250, 0.8), 0 0 60px rgba(167, 139, 250, 0.4); }
        }

        @keyframes slideInDown {
            from { opacity: 0; transform: translateY(-40px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes slideInUp {
            from { opacity: 0; transform: translateY(40px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes slideInLeft {
            from { opacity: 0; transform: translateX(-40px); }
            to { opacity: 1; transform: translateX(0); }
        }

        @keyframes scaleIn {
            from { opacity: 0; transform: scale(0.85); }
            to { opacity: 1; transform: scale(1); }
        }

        @keyframes fadeInGlow {
            0% { opacity: 0; filter: blur(10px); }
            100% { opacity: 1; filter: blur(0); }
        }

        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
        }

        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-5px); }
        }

        /* WELCOME CONTAINER */
        .welcome-container {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 60px 40px;
            position: relative;
            overflow: hidden;
            background: linear-gradient(135deg, #0a0e27 0%, #0f172a 20%, #1a1f2e 40%, #0f172a 60%, #0a0e27 100%);
        }

        .animated-background {
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(96, 165, 250, 0.15) 1px, transparent 1px);
            background-size: 50px 50px;
            animation: floatingGlow 12s ease-in-out infinite;
            z-index: 0;
        }

        .content-wrapper {
            position: relative;
            z-index: 1;
            width: 100%;
            max-width: 900px;
            text-align: center;
        }

        .title-section {
            animation: slideInDown 1.2s cubic-bezier(0.34, 1.56, 0.64, 1);
        }

        /* ANIMATED TITLE */
        .animated-title {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 20px;
            margin-bottom: 30px;
        }

        .title-char {
            font-size: 6em;
            animation: bounce 2s cubic-bezier(0.34, 1.56, 0.64, 1), scaleIn 1s ease-out;
        }

        .title-text-animated {
            font-size: 5em;
            font-weight: 800;
            background: linear-gradient(90deg, #60a5fa 0%, #a78bfa 25%, #06b6d4 50%, #a78bfa 75%, #60a5fa 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: gradientShift 6s ease infinite, slideInUp 1s ease-out 0.1s backwards;
            letter-spacing: -2px;
        }

        .animated-subtitle {
            font-size: 2.2em;
            font-weight: 700;
            color: #a78bfa;
            margin-bottom: 30px;
            animation: slideInUp 1s ease-out 0.2s backwards;
        }

        .animated-description {
            font-size: 1.3em;
            color: #cbd5e1;
            font-weight: 400;
            line-height: 1.8;
            margin-bottom: 60px;
            animation: slideInUp 1s ease-out 0.3s backwards;
        }

        /* MAIN HEADER */
        .main-header {
            background: linear-gradient(135deg, #60a5fa 0%, #a78bfa 50%, #06b6d4 100%);
            background-size: 200% 200%;
            padding: 60px 40px;
            border-radius: 30px;
            color: white;
            text-align: center;
            box-shadow: 0 20px 60px rgba(96, 165, 250, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.2);
            position: relative;
            overflow: hidden;
            animation: slideInDown 1s ease-out, glow 4s ease-in-out infinite;
        }

        .header-glow {
            position: absolute;
            top: -50%;
            right: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255, 255, 255, 0.15) 0%, transparent 70%);
            animation: floatingGlow 8s ease-in-out infinite;
        }

        .animated-title-main {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 20px;
            position: relative;
            z-index: 2;
        }

        .rocket-icon {
            font-size: 3.5em;
            animation: bounce 2s cubic-bezier(0.34, 1.56, 0.64, 1), scaleIn 0.8s ease-out;
        }

        .title-text-main {
            font-size: 3em;
            font-weight: 800;
            color: white;
            text-shadow: 0 4px 30px rgba(0, 0, 0, 0.4);
            letter-spacing: -1px;
            animation: slideInUp 1s ease-out 0.2s backwards;
        }

        .premium-subtitle {
            font-size: 1.3em;
            font-weight: 600;
            color: rgba(255, 255, 255, 0.95);
            animation: slideInUp 1s ease-out 0.3s backwards;
        }

        /* ENHANCED CARD STYLES */
        .premium-card {
            background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
            border-left: 6px solid #60a5fa;
            border-radius: 22px;
            padding: 30px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(96, 165, 250, 0.1);
            border: 1px solid rgba(96, 165, 250, 0.2);
            margin-bottom: 25px;
            animation: slideInUp 0.7s cubic-bezier(0.34, 1.56, 0.64, 1);
            transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }

        .premium-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
            transition: left 0.5s;
        }

        .premium-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 25px 70px rgba(96, 165, 250, 0.4), inset 0 1px 0 rgba(96, 165, 250, 0.2);
            border-color: #a78bfa;
            border-left-color: #06b6d4;
        }

        .premium-card:hover::before {
            left: 100%;
        }

        .premium-card h3, .premium-card h4 {
            color: #60a5fa;
            font-weight: 800;
            animation: slideInDown 0.7s ease-out 0.2s backwards;
        }

        .premium-card p {
            color: #e2e8f0 !important;
        }

        /* FLASHCARDS */
        .premium-flashcard {
            background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
            border: 2px solid rgba(96, 165, 250, 0.3);
            border-radius: 25px;
            padding: 60px;
            min-height: 380px;
            display: flex;
            align-items: center;
            justify-content: center;
            animation: slideInUp 0.8s ease-out;
            transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .premium-flashcard:hover {
            transform: scale(1.02);
            box-shadow: 0 20px 60px rgba(96, 165, 250, 0.3);
            border-color: #a78bfa;
        }

        .premium-flashcard h4 { 
            color: #60a5fa; 
            font-weight: 800;
            animation: slideInDown 0.6s ease-out;
        }

        .premium-flashcard p { 
            color: #f1f5f9; 
            font-size: 1.3em;
            animation: slideInUp 0.6s ease-out 0.2s backwards;
        }

        /* BASE STYLES */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
            background: linear-gradient(135deg, #0a0e27 0%, #0f172a 20%, #1a1f2e 40%, #0f172a 60%, #0a0e27 100%) !important;
            color: #f1f5f9 !important;
            transition: background 0.8s ease;
        }

        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%) !important;
            box-shadow: inset -3px 0 15px rgba(0, 0, 0, 0.5);
        }

        [data-testid="stSidebar"] * {
            color: #f1f5f9 !important;
        }

        /* HIDE SIDEBAR TOGGLE */
        [data-testid="stSidebarCollapseButton"] {
            display: none !important;
        }

        .sidebar-header {
            background: linear-gradient(135deg, #60a5fa 0%, #a78bfa 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 900;
            font-size: 1.2em;
            margin-bottom: 20px;
            animation: slideInDown 0.7s ease-out;
        }

        .sidebar-footer {
            background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
            padding: 20px;
            border-radius: 16px;
            font-size: 0.9em;
            color: #cbd5e1;
            margin-top: 30px;
            border: 1px solid rgba(96, 165, 250, 0.2);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
            animation: slideInUp 0.7s ease-out;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .sidebar-footer:hover {
            border-color: #60a5fa;
            box-shadow: 0 12px 40px rgba(96, 165, 250, 0.25);
            transform: translateY(-2px);
        }

        /* INPUTS */
        [data-testid="stFileUploader"] {
            background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
            border: 2px dashed rgba(96, 165, 250, 0.3) !important;
            border-radius: 12px !important;
            padding: 20px !important;
            transition: all 0.4s ease;
        }

        [data-testid="stFileUploader"]:hover {
            border-color: #60a5fa !important;
            background: linear-gradient(135deg, #334155 0%, #1e293b 100%);
        }

        .stTextInput > div > div > input {
            background-color: #1e293b !important;
            color: #f1f5f9 !important;
            border: 2px solid rgba(96, 165, 250, 0.2) !important;
            border-radius: 8px !important;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        }

        .stTextInput > div > div > input:focus {
            border-color: #60a5fa !important;
            color: #f1f5f9 !important;
            box-shadow: 0 0 20px rgba(96, 165, 250, 0.3) !important;
        }

        /* BUTTONS */
        .stButton > button {
            background: linear-gradient(135deg, #60a5fa 0%, #a78bfa 50%, #06b6d4 100%);
            background-size: 200% 200%;
            color: white;
            font-weight: 800;
            text-transform: uppercase;
            border-radius: 12px;
            transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 5px 20px rgba(96, 165, 250, 0.2), inset 0 1px 0 rgba(255, 255, 255, 0.1);
            animation: slideInUp 0.7s ease-out;
        }

        .stButton > button:hover {
            transform: translateY(-4px);
            box-shadow: 0 15px 40px rgba(96, 165, 250, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.2);
            background-position: 200% 0;
        }

        .stButton > button:active {
            transform: translateY(-2px);
        }

        /* TEXT */
        label { 
            color: #e2e8f0 !important; 
            font-weight: 700 !important;
            transition: color 0.3s ease;
        }

        p { 
            color: #e2e8f0 !important;
            transition: color 0.3s ease;
        }

        h1, h2, h3, h4, h5, h6 { 
            color: #f1f5f9 !important;
            animation: slideInDown 0.7s ease-out;
        }

        /* GOALS */
        .goal-completed {
            background: linear-gradient(135deg, #0d3b35 0%, #155e75 100%);
            padding: 15px;
            border-radius: 10px;
            border-left: 4px solid #34d399;
            color: #34d399;
            font-weight: 600;
            text-decoration: line-through;
            animation: slideInLeft 0.7s ease-out;
            transition: all 0.4s ease;
        }

        .goal-pending {
            background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
            padding: 15px;
            border-radius: 10px;
            border-left: 4px solid #60a5fa;
            color: #e2e8f0;
            font-weight: 600;
            animation: slideInLeft 0.7s ease-out;
            transition: all 0.4s ease;
        }

        .goal-pending:hover {
            transform: translateX(8px);
            border-left-color: #a78bfa;
            box-shadow: 0 5px 20px rgba(96, 165, 250, 0.1);
        }

        .goal-stats {
            background: linear-gradient(135deg, #1e3a5f 0%, #2d5a8c 100%);
            padding: 15px;
            border-radius: 10px;
            color: #60a5fa;
            font-weight: 700;
            text-align: center;
            animation: slideInUp 0.7s ease-out;
            box-shadow: 0 5px 20px rgba(96, 165, 250, 0.1);
        }
    </style>
    """

    st.markdown(css, unsafe_allow_html=True)
