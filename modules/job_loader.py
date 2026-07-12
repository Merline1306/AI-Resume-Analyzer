import pandas as pd


class JobLoader:

    def __init__(self):

        self.df = pd.read_csv("data/job_dataset.csv")

        # Clean all string columns
        self.df["Title"] = (
            self.df["Title"]
            .fillna("")
            .astype(str)
            .str.strip()
        )

        self.df["ExperienceLevel"] = (
            self.df["ExperienceLevel"]
            .fillna("")
            .astype(str)
            .str.strip()
        )

    # ---------------------------------------------------

    def get_roles(self):

        return sorted(self.df["Title"].unique())

    # ---------------------------------------------------

    def get_levels(self, role):

        role = role.strip()

        levels = self.df.loc[
            self.df["Title"] == role,
            "ExperienceLevel"
        ].unique()

        return sorted(levels)

    # ---------------------------------------------------

    def get_job(self, role, level):

        print("Selected Role:", repr(role))
        print("Selected Level:", repr(level))

        filtered = self.df[
            (self.df["Title"].str.strip() == role.strip()) &
            (self.df["ExperienceLevel"].str.strip() == level.strip())
        ]

        print(filtered)

        if filtered.empty:
            return "Job Description not found."

        row = filtered.iloc[0]

        jd = f"""
    JOB TITLE
    {row['Title']}

    EXPERIENCE LEVEL
    {row['ExperienceLevel']}

    YEARS OF EXPERIENCE
    {row['YearsOfExperience']}

    SKILLS
    {row['Skills']}

    RESPONSIBILITIES
    {row['Responsibilities']}

    KEYWORDS
    {row['Keywords']}
    """

        return jd