"""
=========================================================
AI Resume Analyzer
File Parser Module
=========================================================

Supports:
- PDF
- DOCX
- TXT

Author: Merline Princy
"""

from io import BytesIO
from pathlib import Path

import pdfplumber
from docx import Document


class FileParser:
    """
    Handles text extraction from supported file formats.
    """

    @staticmethod
    def parse_pdf(uploaded_file):
        """Extract text from a PDF file."""

        try:
            uploaded_file.seek(0)

            text = ""

            with pdfplumber.open(BytesIO(uploaded_file.read())) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()

                    if page_text:
                        text += page_text + "\n"

            uploaded_file.seek(0)

            return text.strip()

        except Exception as e:
            raise RuntimeError(f"Unable to read PDF file.\n{e}")

    # --------------------------------------------------

    @staticmethod
    def parse_docx(uploaded_file):
        """Extract text from a DOCX file."""

        try:
            uploaded_file.seek(0)

            document = Document(BytesIO(uploaded_file.read()))

            uploaded_file.seek(0)

            paragraphs = [
                paragraph.text.strip()
                for paragraph in document.paragraphs
                if paragraph.text.strip()
            ]

            return "\n".join(paragraphs)

        except Exception as e:
            raise RuntimeError(f"Unable to read DOCX file.\n{e}")

    # --------------------------------------------------

    @staticmethod
    def parse_txt(uploaded_file):
        """Extract text from a TXT file."""

        try:
            uploaded_file.seek(0)

            try:
                text = uploaded_file.read().decode("utf-8")

            except UnicodeDecodeError:
                uploaded_file.seek(0)
                text = uploaded_file.read().decode("latin-1")

            uploaded_file.seek(0)

            return text

        except Exception as e:
            raise RuntimeError(f"Unable to read TXT file.\n{e}")

    # --------------------------------------------------

    @classmethod
    def extract_text(cls, uploaded_file):
        """
        Automatically detect file type and extract text.
        """

        if uploaded_file is None:
            raise ValueError("No file uploaded.")

        extension = Path(uploaded_file.name).suffix.lower()

        if extension == ".pdf":
            return cls.parse_pdf(uploaded_file)

        elif extension == ".docx":
            return cls.parse_docx(uploaded_file)

        elif extension == ".txt":
            return cls.parse_txt(uploaded_file)

        raise ValueError(
            f"Unsupported file format: {extension}"
        )