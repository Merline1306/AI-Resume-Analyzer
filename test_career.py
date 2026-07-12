from modules.ai.career_advisor import CareerAdvisor

advisor = CareerAdvisor()

response = advisor.advise(

    resume_text="""
Python
SQL
Machine Learning
Power BI
TensorFlow
""",

    job_role="AI Analyst",

    experience_level="Fresher",

    ats_score=84,

    similarity=88,

    matched_skills=[
        "Python",
        "SQL",
        "Machine Learning"
    ],

    missing_skills=[
        "Docker",
        "AWS",
        "Spark"
    ]

)

print(response)