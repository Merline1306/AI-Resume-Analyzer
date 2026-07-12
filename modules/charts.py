"""
=========================================================
AI Resume Analyzer
Charts Module
=========================================================

Creates Plotly charts for ATS analysis.

Author: Merline Princy
"""

import plotly.express as px
import plotly.graph_objects as go

from config.constants import (
    PRIMARY_COLOR,
    SUCCESS_COLOR,
    WARNING_COLOR,
    ERROR_COLOR,
)


class ChartGenerator:
    """Generate interactive charts for the dashboard."""

    # =====================================================
    # ATS Score Gauge
    # =====================================================

    @staticmethod
    def ats_gauge(score: float):

        score = max(0, min(100, score))

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=score,
                title={"text": "ATS Score"},
                number={"suffix": "%"},
                gauge={
                    "axis": {"range": [0, 100]},
                    "bar": {"color": PRIMARY_COLOR},
                    "steps": [
                        {
                            "range": [0, 40],
                            "color": ERROR_COLOR,
                        },
                        {
                            "range": [40, 70],
                            "color": WARNING_COLOR,
                        },
                        {
                            "range": [70, 100],
                            "color": SUCCESS_COLOR,
                        },
                    ],
                },
            )
        )

        fig.update_layout(
            height=350,
            margin=dict(l=20, r=20, t=50, b=20),
        )

        return fig

    # =====================================================
    # Score Breakdown
    # =====================================================

    @staticmethod
    def score_breakdown(scores: dict):

        labels = [
            "Similarity",
            "Skills",
            "Experience",
            "Education",
            "Keywords",
        ]

        values = [
            scores.get("similarity", 0),
            scores.get("skills", 0),
            scores.get("experience", 0),
            scores.get("education", 0),
            scores.get("keyword", 0),
        ]

        fig = px.bar(
            x=labels,
            y=values,
            text=values,
            title="ATS Score Breakdown",
        )

        fig.update_traces(
            marker_color=PRIMARY_COLOR,
            textposition="outside",
        )

        fig.update_layout(
            yaxis_title="Score",
            xaxis_title="Category",
            height=400,
        )

        return fig

    # =====================================================
    # Skill Match Pie
    # =====================================================

    @staticmethod
    def skill_pie(matched_skills, missing_skills):

        matched = len(matched_skills)
        missing = len(missing_skills)

        fig = px.pie(
            names=["Matched", "Missing"],
            values=[matched, missing],
            title="Skill Match Analysis",
        )

        fig.update_traces(
            textinfo="percent+label",
            marker=dict(
                colors=[
                    SUCCESS_COLOR,
                    ERROR_COLOR,
                ]
            ),
        )

        return fig

    # =====================================================
    # Skills Comparison
    # =====================================================

    @staticmethod
    def skills_bar(matched_skills, missing_skills):

        matched = len(matched_skills)
        missing = len(missing_skills)

        fig = px.bar(
            x=["Matched", "Missing"],
            y=[matched, missing],
            text=[matched, missing],
            title="Matching vs Missing Skills",
        )

        fig.update_traces(
            marker_color=[
                SUCCESS_COLOR,
                ERROR_COLOR,
            ],
            textposition="outside",
        )

        fig.update_layout(
            height=350,
            yaxis_title="Skills",
            xaxis_title="",
        )

        return fig

    # =====================================================
    # Resume Statistics
    # =====================================================

    @staticmethod
    def statistics(resume_skills, jd_skills):

        resume_count = len(resume_skills)
        jd_count = len(jd_skills)

        fig = px.bar(
            x=[
                "Resume Skills",
                "Job Description Skills",
            ],
            y=[
                resume_count,
                jd_count,
            ],
            text=[
                resume_count,
                jd_count,
            ],
            title="Resume Statistics",
        )

        fig.update_traces(
            marker_color=PRIMARY_COLOR,
            textposition="outside",
        )

        fig.update_layout(
            height=350,
            yaxis_title="Count",
            xaxis_title="",
        )

        return fig

    # =====================================================
    # Skill Coverage
    # =====================================================

    @staticmethod
    def skill_coverage(skill_match_percent: float):

        skill_match_percent = max(
            0,
            min(100, skill_match_percent),
        )

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=[skill_match_percent],
                y=["Skill Coverage"],
                orientation="h",
                marker_color=SUCCESS_COLOR,
                text=f"{skill_match_percent:.1f}%",
                textposition="inside",
            )
        )

        fig.update_layout(
            title="Skill Coverage",
            xaxis=dict(range=[0, 100]),
            height=220,
            showlegend=False,
        )

        return fig