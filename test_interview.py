from modules.ai.interview import InterviewGenerator

interview = InterviewGenerator()

response = interview.generate(

    resume_text="""
Python
SQL
Machine Learning
TensorFlow
Power BI
""",

    job_role="AI Analyst",

    experience_level="Fresher",

    matched_skills=[
        "Python",
        "SQL",
        "Machine Learning"
    ],

    missing_skills=[
        "Docker",
        "AWS"
    ]

)

print(response)