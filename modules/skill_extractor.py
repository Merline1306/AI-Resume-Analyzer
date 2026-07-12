"""
=========================================================
AI Resume Analyzer
Skill Extraction Module
=========================================================

Extracts technical and soft skills from resumes
and job descriptions.

Author: Merline Princy
"""

import json
import re
from pathlib import Path

import pandas as pd

from config.settings import (
    SKILLS_FILE,
    SYNONYMS_FILE,
)

from config.constants import (
    SOFT_SKILLS,
)


class SkillExtractor:
    """Extract and compare resume/JD skills."""

    def __init__(self):

        self.skills = self._load_skills()

        self.synonyms = self._load_synonyms()

        self.soft_skills = {
            skill.lower()
            for skill in SOFT_SKILLS
        }

    # =====================================================
    # Load Skills
    # =====================================================

    @staticmethod
    def _load_skills():

        try:

            if not Path(SKILLS_FILE).exists():
                return []

            df = pd.read_csv(SKILLS_FILE)

            skills = (
                df.iloc[:, 0]
                .dropna()
                .astype(str)
                .str.strip()
                .str.lower()
                .unique()
                .tolist()
            )

            return sorted(skills)

        except Exception:
            return []

    # =====================================================
    # Load Synonyms
    # =====================================================

    @staticmethod
    def _load_synonyms():

        try:

            if not Path(SYNONYMS_FILE).exists():
                return {}

            with open(
                SYNONYMS_FILE,
                "r",
                encoding="utf-8",
            ) as file:

                data = json.load(file)

            normalized = {}

            for canonical, aliases in data.items():

                normalized[
                    canonical.lower().strip()
                ] = [

                    alias.lower().strip()

                    for alias in aliases

                ]

            return normalized

        except Exception:

            return {}

    # =====================================================
    # Normalize Text
    # =====================================================

    @staticmethod
    def normalize_text(text):

        if not text:
            return ""

        text = str(text).lower()

        text = re.sub(
            r"\s+",
            " ",
            text,
        )

        return text.strip()

    # =====================================================
    # Extract Skills
    # =====================================================

    def extract_skills(self, text):

        text = self.normalize_text(text)

        detected = set()

        # -----------------------------------------
        # Direct Skill Matching
        # -----------------------------------------

        for skill in self.skills:

            pattern = rf"\b{re.escape(skill)}\b"

            if re.search(pattern, text):
                detected.add(skill)

        # -----------------------------------------
        # Synonym Matching
        # -----------------------------------------

        for canonical, aliases in self.synonyms.items():

            if canonical in detected:
                continue

            if re.search(
                rf"\b{re.escape(canonical)}\b",
                text,
            ):
                detected.add(canonical)
                continue

            for alias in aliases:

                if re.search(
                    rf"\b{re.escape(alias)}\b",
                    text,
                ):
                    detected.add(canonical)
                    break

        return sorted(detected)

    # =====================================================
    # Technical Skills
    # =====================================================

    def extract_technical_skills(self, text):

        skills = self.extract_skills(text)

        return sorted(

            skill

            for skill in skills

            if skill.lower() not in self.soft_skills

        )

    # =====================================================
    # Soft Skills
    # =====================================================

    def extract_soft_skills(self, text):

        text = self.normalize_text(text)

        detected = set()

        for skill in self.soft_skills:

            if re.search(
                rf"\b{re.escape(skill)}\b",
                text,
            ):
                detected.add(skill.title())

        return sorted(detected)

    # =====================================================
    # Match Skills
    # =====================================================

    @staticmethod
    def match_skills(
        resume_skills,
        jd_skills,
    ):

        resume = {
            skill.lower().strip()
            for skill in resume_skills
        }

        jd = {
            skill.lower().strip()
            for skill in jd_skills
        }

        matched = sorted(resume & jd)

        missing = sorted(jd - resume)

        extra = sorted(resume - jd)

        return {

            "matched": matched,

            "missing": missing,

            "extra": extra,

        }

    # =====================================================
    # Skill Match Percentage
    # =====================================================

    @staticmethod
    def skill_match_percentage(
        resume_skills,
        jd_skills,
    ):

        if not jd_skills:
            return 0.0

        resume = {
            skill.lower().strip()
            for skill in resume_skills
        }

        jd = {
            skill.lower().strip()
            for skill in jd_skills
        }

        matched = len(resume & jd)

        percentage = (
            matched / len(jd)
        ) * 100

        return round(percentage, 2)

    # =====================================================
    # Complete Analysis
    # =====================================================

    def analyze(
        self,
        resume_text,
        jd_text,
    ):

        resume_skills = self.extract_skills(
        resume_text
        )

        jd_skills = self.extract_skills(
        jd_text
        )

        result = self.match_skills(
        resume_skills,
        jd_skills,
        )

        percentage = self.skill_match_percentage(
        resume_skills,
        jd_skills,
        )

        return {

        "resume_skills": resume_skills,

        "jd_skills": jd_skills,

        "matched": result["matched"],

        "missing": result["missing"],

        "extra": result["extra"],

        "skill_match_percentage": percentage,

        }