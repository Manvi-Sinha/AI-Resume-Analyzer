def calculate_ats_score(resume_text, detected_skills):

    text = resume_text.lower()

    breakdown = {}

    total_score = 0

    # -------------------------
    # Resume Length (15)
    # -------------------------

    if len(resume_text) >= 1500:
        breakdown["Resume Length"] = 15
    else:
        breakdown["Resume Length"] = 8

    total_score += breakdown["Resume Length"]

    # -------------------------
    # Skills (35)
    # -------------------------

    skill_score = min(len(detected_skills), 20)

    breakdown["Skills"] = int((skill_score / 20) * 35)

    total_score += breakdown["Skills"]

    # -------------------------
    # Education (15)
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
        breakdown["Education"] = 15
    else:
        breakdown["Education"] = 0

    total_score += breakdown["Education"]

    # -------------------------
    # Projects (15)
    # -------------------------

    if "project" in text:
        breakdown["Projects"] = 15
    else:
        breakdown["Projects"] = 0

    total_score += breakdown["Projects"]

    # -------------------------
    # GitHub (5)
    # -------------------------

    if "github" in text:
        breakdown["GitHub"] = 5
    else:
        breakdown["GitHub"] = 0

    total_score += breakdown["GitHub"]

    # -------------------------
    # LinkedIn (5)
    # -------------------------

    if "linkedin" in text:
        breakdown["LinkedIn"] = 5
    else:
        breakdown["LinkedIn"] = 0

    total_score += breakdown["LinkedIn"]

    # -------------------------
    # Experience (10)
    # -------------------------

    experience_keywords = [
        "intern",
        "internship",
        "experience"
    ]

    if any(word in text for word in experience_keywords):
        breakdown["Experience"] = 10
    else:
        breakdown["Experience"] = 0

    total_score += breakdown["Experience"]

    return {
        "total_score": total_score,
        "breakdown": breakdown
    }