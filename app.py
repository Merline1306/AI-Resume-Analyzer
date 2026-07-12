import os
from pathlib import Path

import streamlit as st

# =====================================================
# LOCAL MODULES
# =====================================================

from modules.parser import FileParser
from modules.preprocessing import TextPreprocessor
from modules.skill_extractor import SkillExtractor
from modules.similarity import SimilarityCalculator
from modules.ats_score import ATSScorer
from modules.report import ReportGenerator
from modules.charts import ChartGenerator
from modules.job_loader import JobLoader
from PIL import Image
# =====================================================
# AI MODULES
# =====================================================

from modules.ai.resume_review import ResumeReviewer
from modules.ai.roadmap import RoadmapGenerator
from modules.ai.interview import InterviewGenerator
from modules.ai.career_advisor import CareerAdvisor

# =====================================================
# CONFIG
# =====================================================

from config.settings import (

    PAGE_TITLE,

    PAGE_ICON,

)

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(

    page_title=PAGE_TITLE,

    page_icon=PAGE_ICON,

    layout="wide",

    initial_sidebar_state="expanded",

)

# =====================================================
# LOAD CSS
# =====================================================

def load_css():

    css = Path("static/style.css")

    if css.exists():

        with open(css, encoding="utf-8") as f:

            st.markdown(

                f"<style>{f.read()}</style>",

                unsafe_allow_html=True

            )

load_css()

# =====================================================
# LOAD MODULES
# =====================================================

parser = FileParser()

preprocessor = TextPreprocessor()

skill_extractor = SkillExtractor()

ats = ATSScorer()

report_generator = ReportGenerator()

chart_generator = ChartGenerator()

job_loader = JobLoader()

# Lazy loading because SentenceTransformer is large
similarity_model = None

# =====================================================
# AI MODULES
# =====================================================

resume_ai = ResumeReviewer()

roadmap_ai = RoadmapGenerator()

interview_ai = InterviewGenerator()

career_ai = CareerAdvisor()

from PIL import Image

# =====================================================
# HEADER
# =====================================================

import base64


def image_to_base64(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()


logo = image_to_base64("static/images/logo.png")

st.markdown(
    f"""
    <div class="hero">
        <div class="hero-content hero-center">
            <div class="hero-left">
                <img class="hero-logo" src="data:image/png;base64,{logo}" />
                <div>
                    <h1 class="hero-title">AI Resume Analyzer</h1>
                    <p class="hero-subtitle">Analyze. Optimize. Get Hired.</p>
                    <p class="hero-description">
                        AI-powered ATS analysis, resume review,
                        interview preparation and career guidance.
                    </p>
                </div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# INPUT SECTION
# =====================================================
# -----------------------------------------------------
left, right = st.columns([1.2, 1], gap="large")
with left:

    st.subheader("📄 Upload Resume")

    resume_file = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx"]
    )

with right:

    st.subheader("💼 Select Job Role")

    selected_role = st.selectbox(
        "Job Role",
        job_loader.get_roles(),
        index=None,
        placeholder="Select Job Role"
    )

    levels = (
        job_loader.get_levels(selected_role)
        if selected_role
        else []
    )

    selected_level = st.selectbox(
        "Experience Level",
        levels,
        index=None,
        placeholder="Select Experience Level"
    )

    st.subheader("🤖 AI Provider")

    provider = st.selectbox(
        "Choose AI Model",
        [
            "Gemini 2.5 Flash",
            "Ollama (Gemma 3 Local)"
        ],
        index=None,
        placeholder="Select AI Model",
        key="ai_provider"
    )
# =====================================================
# JOB DESCRIPTION PREVIEW
# =====================================================

with st.expander("📋 View Job Description"):

    try:

        jd_preview = job_loader.get_job(

            selected_role,

            selected_level

        )

        st.text_area(

            "Job Description",

            jd_preview,

            height=280,

            disabled=True,

        )

    except Exception as e:

        st.error(e)

# =====================================================
# ANALYZE BUTTON
# =====================================================

st.write("")

analyze = st.button(

    "🚀 Analyze Resume",

    use_container_width=True

)

results = None

# =====================================================
# ANALYSIS
# =====================================================

if analyze:

    if resume_file is None:

        st.error("Please upload your resume.")

        st.stop()

    try:

        # -----------------------------------------
        # Read Resume
        # -----------------------------------------

        with st.spinner("📄 Reading Resume..."):

            resume_text = parser.extract_text(
                resume_file
            )

        # -----------------------------------------
        # Load Job Description
        # -----------------------------------------

        with st.spinner("💼 Loading Job Description..."):

            jd_text = job_loader.get_job(

                selected_role,

                selected_level,

            )

        # -----------------------------------------
        # Preprocessing
        # -----------------------------------------

        with st.spinner("🧹 Cleaning Resume..."):

            resume_clean = preprocessor.clean_text(
                resume_text
            )

            jd_clean = preprocessor.clean_text(
                jd_text
            )

        # -----------------------------------------
        # Skill Extraction
        # -----------------------------------------

        with st.spinner("🔍 Extracting Skills..."):

            skill_result = skill_extractor.analyze(

                resume_clean,

                jd_clean,

            )

        matched_skills = skill_result["matched"]

        missing_skills = skill_result["missing"]

        resume_skills = skill_result["resume_skills"]

        jd_skills = skill_result["jd_skills"]

        skill_match = skill_result[
            "skill_match_percentage"
        ]

        # -----------------------------------------
        # Similarity
        # -----------------------------------------

        with st.spinner("📊 Calculating Similarity..."):

            if similarity_model is None:

                similarity_model = SimilarityCalculator()

            similarity_result = similarity_model.analyze(

                resume_clean,

                jd_clean,

            )

        similarity = similarity_result["similarity"]

        similarity_level = similarity_result["level"]

        # -----------------------------------------
        # ATS Score
        # -----------------------------------------

        with st.spinner("📈 Calculating ATS Score..."):

            ats_result = ats.calculate_score(

                similarity_percent=similarity,

                skill_match_percent=skill_match,

                resume_text=resume_clean,

                jd_text=jd_clean,

            )

        ats_score = ats_result["overall_score"]

        rating = ats.get_rating(
            ats_score
        )

        # =====================================================
        # AI GENERATION
        # =====================================================

        with st.spinner("🤖 Resume Review..."):

            resume_review = resume_ai.review(

                resume_text=resume_text,

                job_description=jd_text,

                ats_score=ats_score,

                similarity=similarity,

                matched_skills=matched_skills,

                missing_skills=missing_skills,

            )

        with st.spinner("📚 Learning Roadmap..."):

            roadmap = roadmap_ai.generate(

                job_role=selected_role,

                experience_level=selected_level,

                missing_skills=missing_skills,

            )

        with st.spinner("🎤 Interview Questions..."):

            interview = interview_ai.generate(

                resume_text=resume_text,

                job_role=selected_role,

                experience_level=selected_level,

                matched_skills=matched_skills,

                missing_skills=missing_skills,

            )

        with st.spinner("💼 Career Advice..."):

            career = career_ai.advise(

                resume_text=resume_text,

                job_role=selected_role,

                experience_level=selected_level,

                ats_score=ats_score,

                similarity=similarity,

                matched_skills=matched_skills,

                missing_skills=missing_skills,

            )

        # -----------------------------------------
        # Generate PDF
        # -----------------------------------------

        report_path = report_generator.generate_report(

            ats_score=ats_score,

            similarity=similarity,

            matched_skills=matched_skills,

            missing_skills=missing_skills,

            ai_review=resume_review,

            roadmap=roadmap,

            interview=interview,

            career=career,

        )

        # -----------------------------------------
        # Store Results
        # -----------------------------------------

        results = {

            "resume_text": resume_text,

            "jd_text": jd_text,

            "resume_skills": resume_skills,

            "jd_skills": jd_skills,

            "matched_skills": matched_skills,

            "missing_skills": missing_skills,

            "skill_match": skill_match,

            "similarity": similarity,

            "similarity_level": similarity_level,

            "ats": ats_result,

            "rating": rating,

            "resume_review": resume_review,

            "roadmap": roadmap,

            "interview": interview,

            "career": career,

            "report": report_path,

        }

        st.success(
            "✅ Analysis Completed Successfully!"
        )

    except Exception as e:

        st.exception(e)

# =====================================================
# DASHBOARD
# =====================================================

if results:

    st.divider()

    # -------------------------------------------------
    # TOP METRICS
    # -------------------------------------------------

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "ATS Score",
            f"{results['ats']['overall_score']}%"
        )

    with c2:
        st.metric(
            "Resume Similarity",
            f"{results['similarity']}%"
        )

    with c3:
        st.metric(
            "Skill Match",
            f"{results['skill_match']}%"
        )

    with c4:
        st.metric(
            "Rating",
            results["rating"]
        )

    st.divider()

    # -------------------------------------------------
    # CHARTS
    # -------------------------------------------------

    left, right = st.columns(2)

    with left:

        st.plotly_chart(

            chart_generator.ats_gauge(

                results["ats"]["overall_score"]

            ),

            use_container_width=True

        )

    with right:

        st.plotly_chart(

            chart_generator.score_breakdown(

                results["ats"]

            ),

            use_container_width=True

        )

    st.divider()

    left, right = st.columns(2)

    with left:

        st.plotly_chart(

            chart_generator.skill_pie(

                results["matched_skills"],

                results["missing_skills"]

            ),

            use_container_width=True

        )

    with right:

        st.plotly_chart(

            chart_generator.skills_bar(

                results["matched_skills"],

                results["missing_skills"]

            ),

            use_container_width=True

        )

    st.divider()

    # =====================================================
    # TABS
    # =====================================================

    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([

        "📄 Resume Review",

        "📚 Learning Roadmap",

        "🎤 Interview Questions",

        "💼 Career Advisor",

        "✅ Skills",

        "📄 Resume Details",

        "📥 Download"

    ])

    # -------------------------------------------------
    # TAB 1
    # -------------------------------------------------

    with tab1:

        st.markdown(

            results["resume_review"]

        )

    # -------------------------------------------------
    # TAB 2
    # -------------------------------------------------

    with tab2:

        st.markdown(

            results["roadmap"]

        )

    # -------------------------------------------------
    # TAB 3
    # -------------------------------------------------

    with tab3:

        st.markdown(

            results["interview"]

        )

    # -------------------------------------------------
    # TAB 4
    # -------------------------------------------------

    with tab4:

        st.markdown(

            results["career"]

        )

    # -------------------------------------------------
    # TAB 5
    # -------------------------------------------------

    with tab5:

        col1, col2 = st.columns(2)

        with col1:

            st.success("Matched Skills")

            st.write(

                results["matched_skills"]

            )

        with col2:

            st.error("Missing Skills")

            st.write(

                results["missing_skills"]

            )

        st.divider()

        st.subheader("Resume Skills")

        st.write(

            results["resume_skills"]

        )

        st.subheader("Job Description Skills")

        st.write(

            results["jd_skills"]

        )

    # -------------------------------------------------
    # TAB 6
    # -------------------------------------------------

    with tab6:

        st.subheader("Resume")

        st.text_area(

            "Resume",

            results["resume_text"],

            height=300

        )

        st.subheader("Job Description")

        st.text_area(

            "Job Description",

            results["jd_text"],

            height=300

        )

    # -------------------------------------------------
    # TAB 7
    # -------------------------------------------------

    with tab7:

        with open(

            results["report"],

            "rb"

        ) as pdf:

            st.download_button(

                "📄 Download PDF Report",

                pdf,

                "ATS_Report.pdf",

                "application/pdf",

                use_container_width=True

            )

else:

    st.info(

        "Upload your Resume, select a Job Role and click **Analyze Resume**."

    )

