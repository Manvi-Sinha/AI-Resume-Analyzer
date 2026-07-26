from utils.skills import extract_skills


def compare_resume_jd(resume_text, job_description):

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_description)

    resume_set = set()
    jd_set = set()

    for skills in resume_skills.values():
        resume_set.update(skills)

    for skills in jd_skills.values():
        jd_set.update(skills)

    matched = sorted(list(resume_set.intersection(jd_set)))
    missing = sorted(list(jd_set.difference(resume_set)))

    if len(jd_set) == 0:
        match_percent = 0
    else:
        match_percent = round(
            (len(matched) / len(jd_set)) * 100,
            2
        )

    return {
        "matched": matched,
        "missing": missing,
        "match_percent": match_percent
    }