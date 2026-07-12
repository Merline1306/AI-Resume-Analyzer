# 🤖 AI Resume Analyzer

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit)
![Gemini](https://img.shields.io/badge/Google-Gemini_AI-blue?style=for-the-badge&logo=google)
![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

### 🚀 AI-Powered ATS Resume Analyzer with Career Guidance

Analyze resumes against job descriptions, calculate ATS scores, identify missing skills, generate AI-powered resume reviews, interview questions, learning roadmaps, and professional PDF reports.

</div>

---

# 📌 Overview

AI Resume Analyzer is an intelligent web application that helps job seekers improve their resumes using Artificial Intelligence.

The application compares a resume with a selected job description and provides:

- ATS Compatibility Score
- Resume Similarity Score
- Skill Gap Analysis
- AI Resume Review
- Learning Roadmap
- Interview Questions
- Career Guidance
- Professional PDF Report

The application supports both:

- Google Gemini API
- Ollama (Local AI Models)

---

# ✨ Features

## 📄 Resume Analysis

- Upload Resume (PDF/DOCX)
- Automatic Resume Parsing
- Job Description Matching
- Resume Similarity Analysis
- ATS Score Calculation

---

## 🧠 AI Resume Review

Generate a complete AI review including:

- Resume Strengths
- Resume Weaknesses
- Missing Skills
- ATS Improvement Suggestions
- Recruiter Impression
- Final Recommendation

---

## 🎯 Skill Matching

- Resume Skills Extraction
- Job Description Skills Extraction
- Matching Skills
- Missing Skills
- Skill Match Percentage

---

## 📚 Learning Roadmap

Generate a personalized roadmap for missing skills including:

- Learning Priority
- Difficulty Level
- Estimated Learning Time
- Recommended Resources
- Mini Projects
- Certifications

---

## 🎤 Interview Preparation

Generate:

- Technical Questions
- Python Questions
- SQL Questions
- HR Questions
- Project-Based Questions

---

## 💼 Career Advisor

Receive AI-powered guidance including:

- Resume Readiness
- Hire Probability
- Skills to Learn First
- Career Advice
- 30-Day Improvement Plan

---

## 📑 Professional PDF Report

Download a comprehensive report containing:

- ATS Score
- Resume Similarity
- Matched Skills
- Missing Skills
- AI Resume Review
- Learning Roadmap
- Interview Questions
- Career Advice

---

# 🛠 Tech Stack

## Frontend

- Streamlit
- HTML
- CSS

## Backend

- Python

## Artificial Intelligence

- Google Gemini API
- Ollama

## Machine Learning

- Sentence Transformers
- Scikit-learn

## NLP

- NLTK

## PDF Processing

- PyPDF2
- python-docx
- pdfplumber

## Report Generation

- ReportLab

## Visualization

- Plotly
- Matplotlib

---

# 📂 Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── modules/
│   ├── parser.py
│   ├── preprocessing.py
│   ├── similarity.py
│   ├── ats_score.py
│   ├── skill_extractor.py
│   ├── report.py
│   ├── charts.py
│   ├── job_loader.py
│   └── ai/
│       ├── ai_service.py
│       ├── gemini_service.py
│       ├── ollama_service.py
│       ├── resume_review.py
│       ├── roadmap.py
│       ├── interview.py
│       └── career_advisor.py
│
├── static/
│   ├── style.css
│   └── images/
│       └── logo.png
│
├── templates/
│   └── report.html
│
└── reports/
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Merline1306/AI-Resume-Analyzer.git
```

Go to the project directory

```bash
cd AI-Resume-Analyzer
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

If using Ollama locally, install Ollama and pull the required model.

Example:

```bash
ollama pull gemma3
```

Start the Ollama server before selecting the Ollama provider in the application.

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

Open:

```
http://localhost:8501
```

# ⚠️ Important Notes

This project supports two AI providers:

### Google Gemini

- Works locally
- Works on cloud deployment
- Requires a Gemini API Key

### Ollama

- Works only on local machines
- Requires Ollama installation
- Not supported on Streamlit Community Cloud

---

# 🔮 Future Enhancements

- Resume Builder
- Cover Letter Generator
- LinkedIn Profile Analyzer
- Resume Keyword Optimizer
- Multi-language Support
- Resume Ranking
- AI Chat Assistant
- Mock Interview Simulator
- Company-wise Resume Optimization
- Resume Version Management

---

# 👩‍💻 Author

**Merline Princy**

M.Sc. Data Science  
SASTRA Deemed University

GitHub:

https://github.com/Merline1306

---

# ⭐ Support

If you found this project helpful,

please ⭐ the repository.

It helps others discover the project.

---

## 📜 License

This project is licensed under the MIT License.
