"""
=========================================================
AI Resume Analyzer
Gemini AI Service (Latest Google GenAI SDK)
=========================================================
"""

import os
from dotenv import load_dotenv
from google import genai
from matplotlib.style import available

load_dotenv()


class GeminiService:

    def __init__(self):

        self.api_key = os.getenv("GEMINI_API_KEY")

        if not self.api_key:
            raise ValueError(
                "Gemini API Key not found in .env"
            )

        self.client = genai.Client(
            api_key=self.api_key
        )

        self.model = self.get_best_model()

        print(f"✅ Using Gemini Model: {self.model}")

    # =====================================================
    # Automatically choose best available model
    # =====================================================

    def get_best_model(self):

        preferred = [

        "gemini-flash-latest",

        "gemini-flash-lite-latest",

        "gemini-pro-latest",

        "gemini-3.5-flash",

        "gemini-3.1-flash-lite",

        "gemini-2.5-flash-lite",

        "gemini-2.0-flash",

    ]

        available = []

        try:

            for model in self.client.models.list():

                name = model.name.replace("models/", "")

                available.append(name)

        except Exception:

            return "gemini-flash-lite-latest"

        print("\nAvailable Models:\n")

        for m in available:

            print("•", m)

        for model in preferred:

            if model in available:

                print(f"\n✅ Using Model: {model}")

                return model

        print(f"\n⚠ Using First Available Model: {available[0]}")

        return available[0]

    # =====================================================
    # Generic Generate
    # =====================================================

    def generate(

        self,

        prompt,

        temperature=0.3,

        max_tokens=16384,

    ):

        try:
            print("Current Model:", self.model)
            response = self.client.models.generate_content(

                model=self.model,

                contents=prompt,

                config={

                    "temperature": temperature,

                    "max_output_tokens": max_tokens,

                },

            )

            return response.text

        except Exception as e:

            raise RuntimeError(

                f"Gemini Error:\n{e}"

            )