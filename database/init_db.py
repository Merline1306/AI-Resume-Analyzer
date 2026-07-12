"""
=========================================================
AI Resume Analyzer
Database Initialization
=========================================================
"""

import sqlite3
import os

DATABASE = "database/database.db"

os.makedirs("database", exist_ok=True)

conn = sqlite3.connect(DATABASE)

cursor = conn.cursor()

# =========================================================
# Users
# =========================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT,

    email TEXT UNIQUE,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

# =========================================================
# Resume Analysis
# =========================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS resume_analysis (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER,

    resume_name TEXT,

    ats_score REAL,

    similarity REAL,

    matched_skills INTEGER,

    missing_skills INTEGER,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id)
    REFERENCES users(id)

)
""")

# =========================================================
# AI Review
# =========================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS ai_reviews (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    analysis_id INTEGER,

    review TEXT,

    recommendations TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(analysis_id)
    REFERENCES resume_analysis(id)

)
""")

conn.commit()

conn.close()

print("Database Created Successfully.")