"""
=========================================================
AI Resume Analyzer
Configuration Settings
=========================================================
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# =========================================================
# APPLICATION SETTINGS
# =========================================================

APP_NAME = "AI Resume Analyzer"
APP_VERSION = "1.0.0"

PAGE_TITLE = "AI Resume Analyzer"
PAGE_ICON = "📄"

# =========================================================
# FILE SETTINGS
# =========================================================

# Maximum upload size (MB)
MAX_FILE_SIZE = 10

# Allowed resume formats
ALLOWED_RESUME_TYPES = [
    "pdf",
    "docx"
]

# Allowed Job Description formats
ALLOWED_JD_TYPES = [
    "pdf",
    "docx",
    "txt"
]

# =========================================================
# DIRECTORY PATHS
# =========================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")
STATIC_DIR = os.path.join(BASE_DIR, "static")
REPORT_DIR = os.path.join(BASE_DIR, "reports")
DATABASE_DIR = os.path.join(BASE_DIR, "database")

# =========================================================
# DATABASE
# =========================================================

DATABASE_NAME = "database.db"
DATABASE_PATH = os.path.join(
    DATABASE_DIR,
    DATABASE_NAME
)

# =========================================================
# AI SETTINGS
# =========================================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash-lite"
)

# =========================================================
# SKILL FILES
# =========================================================

SKILLS_FILE = os.path.join(
    DATA_DIR,
    "skills.csv"
)

SYNONYMS_FILE = os.path.join(
    DATA_DIR,
    "synonyms.json"
)

STOPWORDS_FILE = os.path.join(
    DATA_DIR,
    "stopwords.txt"
)

# =========================================================
# REPORT SETTINGS
# =========================================================

REPORT_NAME = "Resume_Report.pdf"

# =========================================================
# CHART SETTINGS
# =========================================================

PRIMARY_COLOR = "#4F46E5"
SUCCESS_COLOR = "#10B981"
WARNING_COLOR = "#F59E0B"
DANGER_COLOR = "#EF4444"

# =========================================================
# DEBUG MODE
# =========================================================

DEBUG = os.getenv(
    "DEBUG",
    "False"
).lower() == "true"