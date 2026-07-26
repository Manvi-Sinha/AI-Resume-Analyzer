def calculate_ats_score(resume_text, detected_skills):

    score = 0

    text = resume_text.lower()

    # -------------------------
    # Resume Length
    # -------------------------
    if len(resume_text) >= 1500:
        score += 15

    # -------------------------
    # Skills
    # -------------------------
    skill_score = min(len(detected_skills), 20)

    score += int((skill_score / 20) * 35)

    # -------------------------
    # Education
    # -------------------------
    education_keywords = [
        "b.tech",
        "btech",
        "computer science",
        "engineering",
        "college",
        "university"
    ]

    if any(word in text for word in education_keywords):
        score += 15

    # -------------------------
    # Projects
    # -------------------------
    if "project" in text:
        score += 15

    # -------------------------
    # GitHub
    # -------------------------
    if "github" in text:
        score += 5

    # -------------------------
    # LinkedIn
    # -------------------------
    if "linkedin" in text:
        score += 5

    # -------------------------
    # Experience / Internship
    # -------------------------
    experience_keywords = [
        "intern",
        "internship",
        "experience"
    ]

    if any(word in text for word in experience_keywords):
        score += 10

    return score