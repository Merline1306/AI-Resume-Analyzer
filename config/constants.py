"""
=========================================================
AI Resume Analyzer
Project Constants
=========================================================
"""

# ==========================================================
# APPLICATION
# ==========================================================

APP_NAME = "AI Resume Analyzer"
APP_VERSION = "1.0.0"

AUTHOR = "Merline Princy"
LICENSE = "MIT"

# ==========================================================
# ATS SCORE THRESHOLDS
# ==========================================================

EXCELLENT_SCORE = 90
GOOD_SCORE = 75
AVERAGE_SCORE = 60
POOR_SCORE = 40

# ==========================================================
# ATS WEIGHTS
# Total = 100
# ==========================================================

SIMILARITY_WEIGHT = 35
SKILL_MATCH_WEIGHT = 30
EXPERIENCE_WEIGHT = 15
EDUCATION_WEIGHT = 10
KEYWORD_WEIGHT = 10

# ==========================================================
# ATS SETTINGS
# ==========================================================

SIMILARITY_THRESHOLD = 70

# ==========================================================
# RESUME SECTIONS
# ==========================================================

RESUME_SECTIONS = [
    "Summary",
    "Education",
    "Experience",
    "Projects",
    "Skills",
    "Certifications",
    "Achievements",
    "Languages",
]

# ==========================================================
# SOFT SKILLS
# Technical skills should come from data/skills.csv
# ==========================================================

SOFT_SKILLS = [
    "Communication",
    "Leadership",
    "Problem Solving",
    "Critical Thinking",
    "Teamwork",
    "Adaptability",
    "Creativity",
    "Time Management",
    "Decision Making",
    "Presentation Skills",
]

# ==========================================================
# EDUCATION KEYWORDS
# ==========================================================

EDUCATION_KEYWORDS = [
    "Bachelor",
    "Master",
    "B.Tech",
    "M.Tech",
    "B.Sc",
    "M.Sc",
    "BE",
    "ME",
    "PhD",
    "University",
    "College",
    "CGPA",
]

# ==========================================================
# EXPERIENCE KEYWORDS
# ==========================================================

EXPERIENCE_KEYWORDS = [
    "Intern",
    "Internship",
    "Experience",
    "Developer",
    "Engineer",
    "Analyst",
    "Research",
    "Project",
    "Company",
]

# ==========================================================
# CERTIFICATION KEYWORDS
# ==========================================================

CERTIFICATION_KEYWORDS = [
    "Certification",
    "Certified",
    "Coursera",
    "Udemy",
    "NPTEL",
    "Google",
    "Microsoft",
    "IBM",
    "AWS",
    "Oracle",
]

# ==========================================================
# COLORS
# ==========================================================

PRIMARY_COLOR = "#4F46E5"
SUCCESS_COLOR = "#22C55E"
WARNING_COLOR = "#F59E0B"
ERROR_COLOR = "#EF4444"
INFO_COLOR = "#3B82F6"

# ==========================================================
# ICONS
# ==========================================================

ICONS = {
    "success": "✅",
    "error": "❌",
    "warning": "⚠️",
    "ai": "🤖",
    "resume": "📄",
    "job": "💼",
    "star": "⭐",
    "search": "🔍",
}

# ==========================================================
# AI
# ==========================================================

DEFAULT_AI_MODEL = "gemini-2.5-flash"

# ==========================================================
# REPORT
# ==========================================================

REPORT_FILE_NAME = "ATS_Report.pdf"

# ==========================================================
# PROMPTS
# ==========================================================

MAX_PROMPT_LENGTH = 25000
MAX_RESPONSE_TOKENS = 2048

# ==========================================================
# DEFAULT UI MESSAGES
# ==========================================================

UPLOAD_RESUME_MSG = "Please upload a resume."

UPLOAD_JD_MSG = "Please upload a job description."

ANALYZING_MSG = "Analyzing your resume..."

SUCCESS_MSG = "Analysis completed successfully."

ERROR_MSG = "Something went wrong. Please try again."