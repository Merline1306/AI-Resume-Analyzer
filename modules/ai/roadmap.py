"""
=========================================================
AI Resume Analyzer
Learning Roadmap Generator
=========================================================

Uses Gemini AI to generate a personalized
learning roadmap.

Author: Merline Princy
"""

from modules.ai.ai_service import AIService
class RoadmapGenerator:

    def __init__(self):

        self.ai = AIService()

    # =====================================================

    def generate(

        self,

        job_role,

        missing_skills,

        experience_level,

    ):

        prompt = f"""
You are an expert Career Coach.

Generate a detailed learning roadmap.

Job Role

{job_role}

Experience Level

{experience_level}

Missing Skills

{', '.join(missing_skills)}

Generate the roadmap in Markdown.

Include the following sections:

# Learning Priority

Mention which skills should be learned first.

# 30-Day Learning Plan

Week 1

Week 2

Week 3

Week 4

# Recommended Courses

Mention high-quality free and paid resources.

# Certifications

Suggest industry-recognized certifications.

# Practice Projects

Suggest 5 projects.

# Interview Preparation

Mention important topics.

# Final Advice

Motivate the candidate and explain how to improve
their chances of getting hired.
"""

        return self.ai.generate(prompt)