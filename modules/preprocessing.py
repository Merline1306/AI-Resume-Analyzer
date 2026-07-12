"""
=========================================================
AI Resume Analyzer
Text Preprocessing Module
=========================================================

Preprocesses resume and job description text.

Features
--------
- Lowercase conversion
- Remove URLs
- Remove Emails
- Remove Phone Numbers
- Remove Punctuation
- Preserve useful numbers
- Remove Stopwords
- Lemmatization
- Normalize Whitespaces

Author: Merline Princy
"""

import os
import re
import string

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from config.settings import STOPWORDS_FILE


# ==========================================================
# Download Required Resources
# ==========================================================

for resource in (
    "stopwords",
    "wordnet",
    "omw-1.4",
):
    try:
        nltk.data.find(f"corpora/{resource}")
    except LookupError:
        nltk.download(resource, quiet=True)


class TextPreprocessor:
    """Text preprocessing class."""

    def __init__(self):

        self.lemmatizer = WordNetLemmatizer()

        self.stop_words = set(stopwords.words("english"))

        if os.path.exists(STOPWORDS_FILE):

            with open(
                STOPWORDS_FILE,
                "r",
                encoding="utf-8",
            ) as file:

                custom_stopwords = {
                    word.strip().lower()
                    for word in file
                    if word.strip()
                }

            self.stop_words.update(custom_stopwords)

    # ======================================================

    @staticmethod
    def remove_urls(text):

        return re.sub(
            r"https?://\S+|www\.\S+",
            " ",
            text,
        )

    # ======================================================

    @staticmethod
    def remove_emails(text):

        return re.sub(
            r"\b[\w\.-]+@[\w\.-]+\.\w+\b",
            " ",
            text,
        )

    # ======================================================

    @staticmethod
    def remove_phone_numbers(text):

        return re.sub(
            r"\+?\d[\d\s().-]{8,}\d",
            " ",
            text,
        )

    # ======================================================

    @staticmethod
    def remove_punctuation(text):

        punctuation = string.punctuation.replace("+", "")
        punctuation = punctuation.replace("#", "")
        punctuation = punctuation.replace(".", "")

        return text.translate(
            str.maketrans("", "", punctuation)
        )

    # ======================================================

    @staticmethod
    def normalize_spaces(text):

        return re.sub(
            r"\s+",
            " ",
            text,
        ).strip()

    # ======================================================

    def remove_stopwords(self, text):

        words = text.split()

        filtered = [
            word
            for word in words
            if word.lower() not in self.stop_words
        ]

        return " ".join(filtered)

    # ======================================================

    def lemmatize(self, text):

        words = text.split()

        lemmas = [
            self.lemmatizer.lemmatize(word)
            for word in words
        ]

        return " ".join(lemmas)

    # ======================================================

    @staticmethod
    def remove_special_characters(text):

        text = re.sub(
            r"[^\w\s.+#%-]",
            " ",
            text,
        )

        return text

    # ======================================================

    def clean_text(self, text):

        if not text:
            return ""

        text = str(text)

        text = text.lower()

        text = self.remove_urls(text)

        text = self.remove_emails(text)

        text = self.remove_phone_numbers(text)

        text = self.remove_special_characters(text)

        text = self.remove_punctuation(text)

        text = self.normalize_spaces(text)

        text = self.remove_stopwords(text)

        text = self.lemmatize(text)

        text = self.normalize_spaces(text)

        return text