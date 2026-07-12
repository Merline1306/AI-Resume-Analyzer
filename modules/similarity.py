"""
=========================================================
AI Resume Analyzer
Semantic Similarity Module
=========================================================

Uses Sentence Transformers to calculate semantic
similarity between Resume and Job Description.

Author: Merline Princy
"""

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from config.constants import (
    EXCELLENT_SCORE,
    GOOD_SCORE,
    AVERAGE_SCORE,
    POOR_SCORE,
)


class SimilarityCalculator:
    """Semantic similarity calculator."""

    _model = None

    def __init__(self):

        if SimilarityCalculator._model is None:

            try:
                SimilarityCalculator._model = SentenceTransformer(
                    "all-MiniLM-L6-v2"
    )
            except Exception as e:
                raise RuntimeError(
                    f"Unable to load SentenceTransformer model.\n{e}"
    )

        self.model = SimilarityCalculator._model

    # =====================================================

    def get_embeddings(
        self,
        resume_text: str,
        jd_text: str,
    ):

        if not resume_text.strip():
            raise ValueError("Resume text is empty.")

        if not jd_text.strip():
            raise ValueError("Job Description text is empty.")

        embeddings = self.model.encode(
            [resume_text, jd_text],
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

        return embeddings

    # =====================================================

    def calculate_similarity(
        self,
        resume_text: str,
        jd_text: str,
    ) -> float:

        embeddings = self.get_embeddings(
            resume_text,
            jd_text,
        )

        similarity = cosine_similarity(
            embeddings[0].reshape(1, -1),
            embeddings[1].reshape(1, -1),
        )[0][0]

        similarity = max(0.0, min(1.0, similarity))

        return round(similarity * 100, 2)

    # =====================================================

    @staticmethod
    def similarity_level(score: float) -> str:

        if score >= EXCELLENT_SCORE:
            return "Excellent Match"

        if score >= GOOD_SCORE:
            return "Good Match"

        if score >= AVERAGE_SCORE:
            return "Average Match"

        if score >= POOR_SCORE:
            return "Low Match"

        return "Poor Match"

    # =====================================================

   # =====================================================
# Complete Analysis
# =====================================================

    def analyze(
    self,
    resume_text,
    jd_text,
    ):

        similarity = self.calculate_similarity(
        resume_text,
        jd_text,
        )

        level = self.similarity_level(
        similarity
        )

        return {

        "similarity": similarity,

        "level": level,

        }