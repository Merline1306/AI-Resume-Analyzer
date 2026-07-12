"""
=========================================================
AI Resume Analyzer
Professional PDF Report Generator
=========================================================
"""

import os
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    Image,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

from config.settings import REPORT_DIR


class ReportGenerator:
    """Generate a professional PDF report for the resume analysis."""

    def __init__(self):
        self.styles = getSampleStyleSheet()

        self.title_style = ParagraphStyle(
            "Title",
            parent=self.styles["Heading1"],
            fontSize=24,
            textColor=colors.HexColor("#3F51B5"),
            alignment=TA_CENTER,
            spaceAfter=20,
        )

        self.heading_style = ParagraphStyle(
            "Heading",
            parent=self.styles["Heading2"],
            fontSize=16,
            textColor=colors.HexColor("#3F51B5"),
            spaceBefore=12,
            spaceAfter=8,
        )

        self.subheading_style = ParagraphStyle(
            "SubHeading",
            parent=self.styles["Heading3"],
            fontSize=12,
            textColor=colors.HexColor("#4F46E5"),
            spaceBefore=10,
            spaceAfter=6,
        )

        self.normal_style = ParagraphStyle(
            "Normal",
            parent=self.styles["BodyText"],
            fontSize=10,
            leading=14,
            spaceAfter=6,
        )

    def section(self, title):
        return [
            Spacer(1, 12),
            Paragraph(title, self.heading_style),
            Spacer(1, 6),
        ]

    def _format_text(self, content):
        if content is None:
            return ""

        if isinstance(content, (list, tuple)):
            content = "\n".join(str(item) for item in content)

        text = str(content).replace("\r\n", "\n").replace("\r", "\n")
        return text.replace("\n", "<br/>")

    def _add_section(self, story, title, content):
        if content in (None, "", [], {}):
            return

        story.extend(self.section(title))
        story.append(
            Paragraph(
                self._format_text(content),
                self.normal_style,
            )
        )
        story.append(Spacer(1, 12))

    def _add_logo(self, story):
        logo_path = os.path.join("static", "images", "logo.png")

        if os.path.exists(logo_path):
            logo = Image(
                logo_path,
                width=1.2 * inch,
                height=1.2 * inch,
            )
            logo.hAlign = "CENTER"
            story.append(logo)
            story.append(Spacer(1, 10))

    def generate_report(
        self,
        ats_score,
        similarity,
        matched_skills,
        missing_skills,
        ai_review,
        roadmap=None,
        interview=None,
        career=None,
    ):
        os.makedirs(REPORT_DIR, exist_ok=True)

        filename = os.path.join(REPORT_DIR, "ATS_Report.pdf")
        doc = SimpleDocTemplate(
            filename,
            pagesize=A4,
            rightMargin=36,
            leftMargin=36,
            topMargin=36,
            bottomMargin=36,
        )

        story = []

        story.append(Paragraph("AI Resume Analyzer", self.title_style))
        story.append(
            Paragraph(
                "Professional Resume Analysis Report",
                self.normal_style,
            )
        )
        self._add_logo(story)
        story.append(
            Paragraph(
                f"<b>Generated On:</b> {datetime.now().strftime('%d %B %Y %I:%M %p')}",
                self.normal_style,
            )
        )
        story.append(Spacer(1, 12))
        story.append(PageBreak())

        story.extend(self.section("ATS Summary"))

        data = [
            ["Metric", "Value"],
            ["ATS Score", f"{ats_score}%"],
            ["Similarity", f"{similarity}%"],
            ["Matched Skills", str(len(matched_skills or []))],
            ["Missing Skills", str(len(missing_skills or []))],
        ]

        table = Table(data, colWidths=[220, 220])
        table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#4F46E5")),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                    ("GRID", (0, 0), (-1, -1), 1, colors.grey),
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                    ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
                    ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),
                ]
            )
        )

        story.append(table)
        story.append(Spacer(1, 20))

        story.extend(self.section("Matching Skills"))
        if matched_skills:
            story.append(
                Paragraph(
                    ", ".join(matched_skills),
                    self.normal_style,
                )
            )
        else:
            story.append(Paragraph("No matching skills identified.", self.normal_style))
        story.append(Spacer(1, 12))

        story.extend(self.section("Missing Skills"))
        if missing_skills:
            story.append(
                Paragraph(
                    ", ".join(missing_skills),
                    self.normal_style,
                )
            )
        else:
            story.append(Paragraph("No major missing skills identified.", self.normal_style))
        story.append(Spacer(1, 20))

        self._add_section(story, "AI Resume Review", ai_review)
        self._add_section(story, "Learning Roadmap", roadmap)
        self._add_section(story, "Interview Questions", interview)
        self._add_section(story, "Career Advice", career)

        doc.build(story)
        return filename
