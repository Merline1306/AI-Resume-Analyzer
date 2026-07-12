"""
=========================================================
AI Resume Analyzer
AI Prompt Templates
=========================================================

This file contains all prompts used with the
Google Gemini API.

Author: Merline Princy
"""

# ==========================================================
# SYSTEM PROMPT
# ==========================================================

SYSTEM_PROMPT = """
You are an expert ATS Resume Reviewer, Senior Technical Recruiter,
Career Coach, and Hiring Manager.

Your responsibilities are to:

1. Analyze resumes professionally.
2. Compare resumes with job descriptions.
3. Calculate ATS compatibility.
4. Identify missing technical and soft skills.
5. Suggest improvements.
6. Recommend ATS-friendly keywords.
7. Provide constructive and actionable feedback.
8. Never invent information that is not present.
9. Respond in professional, well-formatted Markdown.
"""

# ==========================================================
# RESUME REVIEW
# ==========================================================

RESUME_REVIEW_PROMPT = """
Analyze the following resume.

Resume:
{resume}

Provide the response in the following format.

# Overall Resume Score
(Give a score out of 10)

# Strengths

# Weaknesses

# ATS Compatibility

# Formatting Issues

# Grammar Suggestions

# Missing Sections

# Recommendations

Keep the review concise and professional.
"""

# ==========================================================
# ATS IMPROVEMENT
# ==========================================================

ATS_IMPROVEMENT_PROMPT = """
Compare the Resume with the Job Description.

Resume:

{resume}

--------------------------------------------------

Job Description:

{jd}

Provide:

# ATS Match Analysis

# Matching Skills

# Missing Technical Skills

# Missing Soft Skills

# Missing Keywords

# Suggestions to Increase ATS Score

# Final Recommendation

Do not invent skills that are not in the Job Description.
"""

# ==========================================================
# RESUME SUMMARY
# ==========================================================

RESUME_SUMMARY_PROMPT = """
Read the resume below.

Resume:

{resume}

Generate:

# Professional Summary

# Candidate Profile

# Technical Skills

# Soft Skills

# Education

# Experience

# Certifications

# Projects

Limit the summary to around 250 words.
"""

# ==========================================================
# PROJECT REVIEW
# ==========================================================

PROJECT_ANALYSIS_PROMPT = """
Analyze every project in the resume.

Resume:

{resume}

For each project provide:

Project Name

Technologies Used

Strengths

Weaknesses

ATS Friendliness

Suggestions for Improvement
"""

# ==========================================================
# INTERVIEW QUESTIONS
# ==========================================================

INTERVIEW_QUESTIONS_PROMPT = """
Generate interview questions based on the resume.

Resume:

{resume}

Generate:

• HR Questions

• Technical Questions

• SQL Questions

• Python Questions

• Machine Learning Questions

• Project-based Questions

Provide at least 20 questions.
"""

# ==========================================================
# COVER LETTER
# ==========================================================

COVER_LETTER_PROMPT = """
Write a professional ATS-friendly cover letter.

Resume:

{resume}

--------------------------------------------------

Job Description:

{jd}

Requirements:

- Professional tone
- Less than 400 words
- Highlight matching skills
- Mention relevant projects
- End with a professional closing
"""

# ==========================================================
# RESUME REWRITE
# ==========================================================

RESUME_REWRITE_PROMPT = """
Rewrite the resume professionally.

Resume:

{resume}

Improve:

Professional Summary

Experience

Projects

Skills

Achievements

Formatting

Use strong action verbs and ATS-friendly wording.
"""

# ==========================================================
# CAREER GUIDANCE
# ==========================================================

CAREER_GUIDANCE_PROMPT = """
Based on the resume below, provide career guidance.

Resume:

{resume}

Include:

Suitable Job Roles

Skills to Learn

Recommended Certifications

Career Roadmap

Future Opportunities

Learning Resources
"""

# ==========================================================
# SKILL GAP ANALYSIS
# ==========================================================

SKILL_GAP_PROMPT = """
Compare the Resume with the Job Description.

Resume:

{resume}

--------------------------------------------------

Job Description:

{jd}

Provide:

Matching Skills

Missing Skills

Priority Skills to Learn

Suggested Learning Order

Overall Skill Gap Analysis
"""

# ==========================================================
# SCORE EXPLANATION
# ==========================================================

SCORE_EXPLANATION_PROMPT = """
Explain the ATS score.

Resume:

{resume}

--------------------------------------------------

Job Description:

{jd}

Explain:

Why the score is high or low

Positive Points

Negative Points

Missing Keywords

Missing Sections

Top 5 Improvements
"""

# ==========================================================
# RESUME OPTIMIZATION
# ==========================================================

RESUME_OPTIMIZATION_PROMPT = """
Optimize the resume for the following job description.

Resume:

{resume}

--------------------------------------------------

Job Description:

{jd}

Rewrite the important sections so the resume becomes more ATS-friendly without adding false information.

Improve:

Professional Summary

Skills

Projects

Experience

Achievements
"""

# ==========================================================
# KEYWORD EXTRACTION
# ==========================================================

KEYWORD_EXTRACTION_PROMPT = """
Extract the important ATS keywords from the Job Description.

Job Description:

{jd}

Return only:

Technical Skills

Soft Skills

Tools

Frameworks

Programming Languages

Databases

Cloud Technologies

Certifications

Keywords
"""