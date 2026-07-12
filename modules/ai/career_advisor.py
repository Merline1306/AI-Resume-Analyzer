"""
=========================================================
AI Resume Analyzer
AI Career Advisor
=========================================================

Provides personalized career guidance using Gemini AI.

Author: Merline Princy
"""

from modules.ai.ai_service import AIService
class CareerAdvisor:

    def __init__(self):

        self.ai = AIService()

    # =====================================================

    def advise(

        self,

        resume_text,

        job_role,

        experience_level,

        ats_score,

        similarity,

        matched_skills,

        missing_skills,

    ):

        prompt = f"""
You are a Senior Career Advisor.

Analyze the candidate profile.

==================================================

Target Job Role

{job_role}

Experience Level

{experience_level}

==================================================

Resume

{resume_text}

==================================================

ATS Score

{ats_score}

Resume Similarity

{similarity}%

==================================================

Matched Skills

{', '.join(matched_skills)}

==================================================

Missing Skills

{', '.join(missing_skills)}

==================================================

Generate the response in Markdown.

Include the following sections.

# Candidate Profile

Summarize the candidate.

# Hire Probability

Give percentage.

Explain why.

# Resume Readiness

Rate out of 10.

# Strength Areas

Mention strongest skills.

# Weak Areas

Mention weakest skills.

# Skills to Learn First

Prioritize missing skills.

# Recommended Certifications

Suggest certifications.

# Suggested Projects

Suggest 5 portfolio projects.

# Best Career Paths

Recommend suitable job roles.

# Salary Expectation

Mention expected salary range for India.

# Career Roadmap

Give a 3-month roadmap.

# Final Advice

Give motivational career guidance.

"""
        return self.ai.generate(prompt)