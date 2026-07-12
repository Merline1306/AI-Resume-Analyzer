"""
=========================================================
AI Resume Analyzer
Interview Question Generator
=========================================================

Uses Gemini AI to generate personalized interview
questions based on the resume and selected job role.

Author: Merline Princy
"""

from modules.ai.ai_service import AIService
class InterviewGenerator:

    def __init__(self):

        self.ai = AIService()

    # =====================================================

    def generate(

        self,

        resume_text,

        job_role,

        experience_level,

        matched_skills,

        missing_skills,

    ):

        prompt = f"""
You are a Senior Technical Interviewer.

Generate interview questions for the following candidate.

----------------------------------------------------

Job Role

{job_role}

Experience Level

{experience_level}

----------------------------------------------------

Resume

{resume_text}

----------------------------------------------------

Matched Skills

{', '.join(matched_skills)}

Missing Skills

{', '.join(missing_skills)}

----------------------------------------------------

Return the response in Markdown.

Include:

# Technical Questions

Generate 20 technical questions.

# Python Coding Questions

Generate 10 coding questions.

# SQL Questions

Generate 10 SQL questions.

# HR Questions

Generate 10 HR questions.

# Project-Based Questions

Generate 10 questions based on projects.

# Interview Tips

Give preparation tips.

# Important Topics

Mention important concepts to revise.

# Difficulty

Easy

Medium

Hard

Categorize the questions.
"""

        return self.ai.generate(prompt)