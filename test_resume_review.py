from modules.ai.resume_review import ResumeReviewer

reviewer = ResumeReviewer()

response = reviewer.review(

    resume_text="Python SQL Machine Learning",

    job_description="Looking for Python SQL Machine Learning Docker",

    ats_score=82,

    similarity=86,

    matched_skills=["Python", "SQL"],

    missing_skills=["Docker"]

)

print(response)