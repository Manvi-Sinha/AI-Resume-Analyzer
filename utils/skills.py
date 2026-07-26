import pandas as pd


def extract_skills(processed_text):

    skills_df = pd.read_csv("data/skills.csv")

    skills_list = skills_df.iloc[:, 0].tolist()

    found_skills = []

    for skill in skills_list:

        if skill.lower() in processed_text.lower():
            found_skills.append(skill)

    return sorted(list(set(found_skills)))