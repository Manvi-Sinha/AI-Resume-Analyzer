import pandas as pd
import re


def extract_skills(processed_text):

    skills_df = pd.read_csv("data/skills.csv")

    skill_list = skills_df["Skill"].dropna().tolist()

    words = set(re.findall(r"\b[\w+.#-]+\b", processed_text.lower()))

    detected_skills = []

    for skill in skill_list:

        skill = skill.lower().strip()

        if " " in skill:
            if skill in processed_text.lower():
                detected_skills.append(skill.title())
        else:
            if skill in words:
                detected_skills.append(skill.title())

    return sorted(list(set(detected_skills)))