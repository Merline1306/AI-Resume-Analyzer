"""
=========================================================
AI Resume Analyzer
AI Resume Review Module (OpenAI)
=========================================================
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

from config.prompts import (
    SYSTEM_PROMPT,
    RESUME_REVIEW_PROMPT,
    ATS_IMPROVEMENT_PROMPT,
    SCORE_EXPLANATION_PROMPT,
)

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


class AIResumeReviewer:

    def _generate(self, prompt):

        try:

            response = client.responses.create(

                model="gpt-5-mini",

                input=[
                    {
                        "role": "system",
                        "content": SYSTEM_PROMPT
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]

            )

            return response.output_text.strip()

        except Exception as e:

            raise RuntimeError(
                f"OpenAI API Error: {e}"
            )

    # --------------------------------------------

    def review_resume(self, resume_text):

        return self._generate(

            RESUME_REVIEW_PROMPT.format(

                resume=resume_text

            )

        )

    # --------------------------------------------

    def ats_improvement(
        self,
        resume_text,
        jd_text,
    ):

        return self._generate(

            ATS_IMPROVEMENT_PROMPT.format(

                resume=resume_text,

                jd=jd_text,

            )

        )

    # --------------------------------------------

    def explain_score(
        self,
        resume_text,
        jd_text,
    ):

        return self._generate(

            SCORE_EXPLANATION_PROMPT.format(

                resume=resume_text,

                jd=jd_text,

            )

        )