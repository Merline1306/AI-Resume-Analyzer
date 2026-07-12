"""
=========================================================
AI Resume Analyzer
Resume Review Module
=========================================================

Uses GeminiService to generate a professional
resume review.

Author: Merline Princy
"""

from modules.ai.ai_service import AIService
class ResumeReviewer:

    def __init__(self):

        self.ai = AIService()

    # =====================================================

    def review(
        self,
        resume_text,
        job_description,
        ats_score,
        similarity,
        matched_skills,
        missing_skills,
    ):

        prompt = f"""
You are a Senior Technical Recruiter and ATS Expert.

Analyze the following resume against the job description.

Return your response in Markdown.

----------------------------------------------------

Candidate Resume

{resume_text}

----------------------------------------------------

Job Description

{job_description}

----------------------------------------------------

ATS Score

{ats_score}

Resume Similarity

{similarity}%

Matched Skills

{', '.join(matched_skills)}

Missing Skills

{', '.join(missing_skills)}

----------------------------------------------------

Generate the following:

# Candidate Summary

Write a professional summary about the candidate.

# ATS Evaluation

Explain why this ATS score was achieved.

# Resume Strengths

Give at least 5 strengths.

# Resume Weaknesses

Give at least 5 weaknesses.

# Missing Skills

Explain why each missing skill is important.

# Resume Improvement Suggestions

Explain exactly what should be added.

# Resume Rewrite Suggestions

Suggest better wording for projects,
summary and experience.

# Final Recommendation

Would you recommend this resume?

Give a score out of 10.

"""

        return self.ai.generate(prompt)