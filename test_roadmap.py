from modules.ai.roadmap import RoadmapGenerator

roadmap = RoadmapGenerator()

print(

    roadmap.generate(

        job_role="Data Scientist",

        experience_level="Fresher",

        missing_skills=[
            "Docker",
            "AWS",
            "Spark",
            "Git"
        ]

    )

)