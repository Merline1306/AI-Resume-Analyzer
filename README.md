# 📄 AI Resume Analyzer

An AI-powered Resume Analyzer that compares a candidate's resume with a Job Description (JD), calculates an ATS compatibility score, identifies missing skills, and provides AI-driven recommendations to improve the resume.

Built using **Python**, **Streamlit**, **Sentence Transformers**, **Google Gemini AI**, and **NLP** techniques.

---

## 🚀 Features

### 📑 Resume Parsing
- Upload Resume (PDF/DOCX)
- Upload Job Description (PDF/DOCX/TXT)
- Automatic text extraction

### 🤖 AI Resume Review
- Resume quality assessment
- ATS compatibility review
- Resume improvement suggestions
- AI-powered feedback using Google Gemini

### 📊 ATS Analysis
- ATS Score Calculation
- Resume–JD Similarity
- Keyword Analysis
- Missing Skills Detection
- Matching Skills Detection
- Resume Statistics

### 📈 Visual Dashboard
- ATS Score Gauge
- Score Breakdown Chart
- Skill Match Analysis
- Resume Statistics
- Interactive Charts

### 📄 Report Generation
- Professional ATS Report
- Downloadable PDF Report
- Resume Analysis Summary

---

# 🛠️ Tech Stack

## Frontend
- Streamlit
- HTML
- CSS

## Backend
- Python

## Artificial Intelligence
- Google Gemini API

## NLP & Machine Learning
- Sentence Transformers
- spaCy
- NLTK
- Scikit-learn

## Data Processing
- Pandas
- NumPy

## Visualization
- Plotly

## Report Generation
- ReportLab

## Database
- SQLite

---

# 📂 Project Structure

```
resume-analyzer-ai/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── config/
│   ├── settings.py
│   ├── constants.py
│   └── prompts.py
│
├── modules/
│   ├── parser.py
│   ├── preprocessing.py
│   ├── similarity.py
│   ├── skill_extractor.py
│   ├── ats_score.py
│   ├── ai_review.py
│   ├── report.py
│   └── charts.py
│
├── data/
│   ├── skills.csv
│   ├── stopwords.txt
│   └── synonyms.json
│
├── database/
│   ├── init_db.py
│   └── database.db
│
├── reports/
│
├── static/
│   ├── style.css
│   └── logo.png
│
└── templates/
    └── report.html
```

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/resume-analyzer-ai.git

cd resume-analyzer-ai
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Download spaCy Model

```bash
python -m spacy download en_core_web_sm
```

---

# 🔑 Configure Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY

APP_ENV=development

DEBUG=True
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 📊 ATS Scoring Criteria

The overall ATS score is calculated using multiple evaluation metrics.

| Metric | Weight |
|---------|--------|
| Resume–JD Similarity | 35% |
| Skill Match | 30% |
| Experience Match | 15% |
| Education Match | 10% |
| Keyword Match | 10% |

---

# 📸 Application Workflow

```
Upload Resume
        │
        ▼
Extract Resume Text
        │
        ▼
Text Preprocessing
        │
        ▼
Skill Extraction
        │
        ▼
Resume–JD Similarity
        │
        ▼
ATS Score Calculation
        │
        ▼
AI Resume Review
        │
        ▼
Charts & Dashboard
        │
        ▼
Download Report
```

---

# 📌 Future Enhancements

- User Authentication
- Resume History
- Multiple Resume Comparison
- Cover Letter Generator
- Interview Question Generator
- Career Recommendation System
- Resume Ranking
- Dark Mode
- Multi-language Support
- Cloud Deployment

---

# 📜 License

This project is licensed under the MIT License.

---

# 👩‍💻 Author

**Merline Princy**

M.Sc. Data Science  
SASTRA Deemed University

GitHub: https://github.com/Merline1306

---
