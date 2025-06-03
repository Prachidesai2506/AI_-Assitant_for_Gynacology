import streamlit as st
from main import ask_obstetric_ai  # Ensure 'main.py' contains the backend logic

# Page configuration
st.set_page_config(
    page_title="Obstetrics AI",
    page_icon="🩺",
    layout="centered"
)

# Apply custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f3f4f6;
        }
        .main {
            background-color: #ffffff;
            border-radius: 12px;
            padding: 2rem;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
            color: #3b82f6;
        }
        .stTextInput > div > input {
            background-color: #eef2ff;
            padding: 10px;
            border-radius: 10px;
        }
        .stButton > button {
            background-color: #3b82f6;
            color: white;
            font-weight: bold;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Title & description
st.title("🩺 Obstetrics AI Chat")
st.markdown(
    "<p style='text-align: center; color: #6b7280;'>Ask any medical question related to obstetrics and get AI-powered answers.</p>",
    unsafe_allow_html=True
)

# Input and response area
with st.container():
    user_input = st.text_input("👩‍⚕️ Enter your question here:")

    if st.button("Ask"):
        if user_input.strip() == "":
            st.warning("⚠️ Please enter a valid question.")
        else:
            with st.spinner("🤖 Thinking..."):
                response = ask_obstetric_ai(user_input)
                st.success("💬 AI Response:")
                st.markdown(f"<div style='color:#374151; font-size: 16px;'>{response}</div>", unsafe_allow_html=True)
