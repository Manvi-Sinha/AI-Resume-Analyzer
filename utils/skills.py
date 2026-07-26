import pandas as pd
import re


def normalize(text):
    text = text.lower()
    text = text.replace(".", " ")
    text = text.replace("-", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_skills(processed_text):

    skills_df = pd.read_csv("data/skills.csv")

    processed_text = normalize(processed_text)

    detected = {}

    for _, row in skills_df.iterrows():

        category = row["Category"].strip()
        skill = row["Skill"].strip()

        skill_normalized = normalize(skill)

        if skill_normalized in processed_text:

            if category not in detected:
                detected[category] = []

            detected[category].append(skill)

    for category in detected:
        detected[category] = sorted(list(set(detected[category])))

    return detected