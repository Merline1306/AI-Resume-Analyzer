import streamlit as st

def get_ai_provider():

    return st.session_state.get(
        "ai_provider",
        "Gemini"
    )