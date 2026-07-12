"""
=========================================================
AI Resume Analyzer
ATS Scoring Module
=========================================================

Calculates the ATS score using:
- Resume Similarity
- Skill Match
- Experience Match
- Education Match
- Keyword Match

Author: Merline Princy
"""

import re

from config.constants import (
    SIMILARITY_WEIGHT,
    SKILL_MATCH_WEIGHT,
    EXPERIENCE_WEIGHT,
    EDUCATION_WEIGHT,
    KEYWORD_WEIGHT,
    EXPERIENCE_KEYWORDS,
    EDUCATION_KEYWORDS,
    EXCELLENT_SCORE,
    GOOD_SCORE,
    AVERAGE_SCORE,
    POOR_SCORE,
)


class ATSScorer:
    """Calculate ATS score."""

    @staticmethod
    def similarity_score(similarity_percent: float) -> float:
        similarity_percent = max(0, min(100, similarity_percent))
        return round((similarity_percent / 100) * SIMILARITY_WEIGHT, 2)

    @staticmethod
    def skill_score(skill_match_percent: float) -> float:
        skill_match_percent = max(0, min(100, skill_match_percent))
        return round((skill_match_percent / 100) * SKILL_MATCH_WEIGHT, 2)

    @staticmethod
    def experience_score(resume_text: str, jd_text: str) -> float:
        resume = resume_text.lower()
        jd = jd_text.lower()

        jd_keywords = [
            keyword.lower()
            for keyword in EXPERIENCE_KEYWORDS
            if keyword.lower() in jd
        ]

        if not jd_keywords:
            return EXPERIENCE_WEIGHT

        matched = sum(
            keyword in resume
            for keyword in jd_keywords
        )

        return round(
            (matched / len(jd_keywords)) * EXPERIENCE_WEIGHT,
            2,
        )

    @staticmethod
    def education_score(resume_text: str, jd_text: str) -> float:
        resume = resume_text.lower()
        jd = jd_text.lower()

        jd_keywords = [
            keyword.lower()
            for keyword in EDUCATION_KEYWORDS
            if keyword.lower() in jd
        ]

        if not jd_keywords:
            return EDUCATION_WEIGHT

        matched = sum(
            keyword in resume
            for keyword in jd_keywords
        )

        return round(
            (matched / len(jd_keywords)) * EDUCATION_WEIGHT,
            2,
        )

    @staticmethod
    def keyword_score(resume_text: str, jd_text: str) -> float:
        resume_words = set(
            re.findall(r"\b[a-zA-Z][a-zA-Z+#.-]*\b", resume_text.lower())
        )

        jd_words = set(
            re.findall(r"\b[a-zA-Z][a-zA-Z+#.-]*\b", jd_text.lower())
        )

        if not jd_words:
            return 0.0

        matched = len(resume_words.intersection(jd_words))

        return round(
            (matched / len(jd_words)) * KEYWORD_WEIGHT,
            2,
        )

    def calculate_score(
        self,
        similarity_percent: float,
        skill_match_percent: float,
        resume_text: str,
        jd_text: str,
    ) -> dict:

        similarity = self.similarity_score(similarity_percent)

        skills = self.skill_score(skill_match_percent)

        experience = self.experience_score(
            resume_text,
            jd_text,
        )

        education = self.education_score(
            resume_text,
            jd_text,
        )

        keyword = self.keyword_score(
            resume_text,
            jd_text,
        )

        overall_score = round(
            similarity
            + skills
            + experience
            + education
            + keyword,
            2,
        )

        return {
            "similarity": similarity,
            "skills": skills,
            "experience": experience,
            "education": education,
            "keyword": keyword,
            "overall_score": overall_score,
            "rating": self.get_rating(overall_score),
        }

    @staticmethod
    def get_rating(score: float) -> str:

        if score >= EXCELLENT_SCORE:
            return "Excellent"

        if score >= GOOD_SCORE:
            return "Good"

        if score >= AVERAGE_SCORE:
            return "Average"

        if score >= POOR_SCORE:
            return "Needs Improvement"

        return "Poor"