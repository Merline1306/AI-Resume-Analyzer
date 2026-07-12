from modules.ai.gemini_service import GeminiService
from modules.ai.ollama_service import OllamaService

import streamlit as st


class AIService:

    def __init__(self):

        provider = st.session_state.get(
            "ai_provider",
            "Gemini 2.5 Flash"
        )

        if provider == "Gemini 2.5 Flash":

            self.ai = GeminiService()

        else:

            self.ai = OllamaService()

    def generate(self, prompt):

        return self.ai.generate(prompt)