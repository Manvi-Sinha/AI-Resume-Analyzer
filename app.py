import streamlit as st

from utils.pdf_extractor import extract_text_from_pdf
from utils.preprocess import preprocess_text
from utils.skills import extract_skills
from utils.ats_score import calculate_ats_score
from utils.similarity import calculate_similarity
from utils.jd_matcher import compare_resume_jd


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="ResumeIQ",
    page_icon="📄",
    layout="wide"
)

st.title("📄 ResumeIQ")
st.caption("AI-Powered Resume Analyzer & Job Match Platform")

st.divider()

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=220
)

# --------------------------------------------------
# START ANALYSIS
# --------------------------------------------------

if uploaded_file:

    # Extract Resume Text
    resume_text = extract_text_from_pdf(uploaded_file)

    # Preprocess Resume
    processed_resume = preprocess_text(resume_text)

    # Detect Skills
    categorized_skills = extract_skills(processed_resume)

    detected_skills = []

    for skills in categorized_skills.values():
        detected_skills.extend(skills)

    # ATS Score
    ats_result = calculate_ats_score(
        resume_text,
        detected_skills
    )

    ats_score = ats_result["total_score"]
    ats_breakdown = ats_result["breakdown"]

    # Default Values
    similarity_score = 0
    skill_match = 0
    matched_skills = []
    missing_skills = []

    # --------------------------------------------------
    # Compare Resume with Job Description
    # --------------------------------------------------

    if job_description.strip():

        processed_jd = preprocess_text(job_description)

        similarity_score = calculate_similarity(
            processed_resume,
            processed_jd
        )

        comparison = compare_resume_jd(
            processed_resume,
            processed_jd
        )

        matched_skills = comparison["matched"]
        missing_skills = comparison["missing"]
        skill_match = comparison["match_percent"]

    st.success("✅ Resume Uploaded Successfully")

    st.divider()

    # --------------------------------------------------
    # DASHBOARD
    # --------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("ATS Score", f"{ats_score}/100")

    with col2:
        st.metric("Skill Match", f"{skill_match}%")

    with col3:
        st.metric("Text Similarity", f"{similarity_score}%")

    with col4:
        st.metric("Skills Found", len(detected_skills))

    st.progress(ats_score / 100)

    if ats_score >= 80:
        st.success("🌟 Excellent Resume")
    elif ats_score >= 60:
        st.info("👍 Good Resume")
    else:
        st.warning("⚠️ Resume Needs Improvement")

    st.divider()

    # --------------------------------------------------
    # ATS BREAKDOWN
    # --------------------------------------------------

    st.subheader("📊 ATS Breakdown")

    max_scores = {
        "Resume Length": 15,
        "Skills": 35,
        "Education": 15,
        "Projects": 15,
        "GitHub": 5,
        "LinkedIn": 5,
        "Experience": 10
    }

    for section, score in ats_breakdown.items():

        maximum = max_scores[section]

        st.write(f"**{section}** : {score}/{maximum}")

        st.progress(score / maximum)

    st.divider()

    # --------------------------------------------------
    # DETECTED SKILLS
    # --------------------------------------------------

    st.subheader("🛠 Detected Skills")

    if categorized_skills:

        for category, skills in categorized_skills.items():

            with st.expander(f"📂 {category}"):

                cols = st.columns(3)

                for index, skill in enumerate(skills):
                    cols[index % 3].success(skill)

    else:

        st.warning("No skills detected.")

        # --------------------------------------------------
    # MATCHED & MISSING SKILLS
    # --------------------------------------------------

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("✅ Matched Skills")

        if matched_skills:

            for skill in matched_skills:
                st.success(skill)

        else:
            st.info("No matched skills found.")

    with col2:

        st.subheader("❌ Missing Skills")

        if missing_skills:

            for skill in missing_skills:
                st.error(skill)

        else:
            st.success("No missing skills found.")

    # --------------------------------------------------
    # RESUME IMPROVEMENT SUGGESTIONS
    # --------------------------------------------------

    st.divider()

    st.subheader("💡 Resume Suggestions")

    suggestions = []

    if ats_breakdown["Resume Length"] < 15:
        suggestions.append("Increase your resume content. Aim for a well-structured one-page resume.")

    if ats_breakdown["Skills"] < 25:
        suggestions.append("Add more relevant technical skills related to your target job.")

    if ats_breakdown["Projects"] == 0:
        suggestions.append("Include at least 2-3 projects with measurable outcomes.")

    if ats_breakdown["Experience"] == 0:
        suggestions.append("Add internship, freelance, or relevant experience if available.")

    if ats_breakdown["GitHub"] == 0:
        suggestions.append("Include your GitHub profile link.")

    if ats_breakdown["LinkedIn"] == 0:
        suggestions.append("Include your LinkedIn profile link.")

    if not suggestions:
        st.success("🎉 Great job! Your resume already covers all major ATS parameters.")

    else:
        for suggestion in suggestions:
            st.info(suggestion)

    # --------------------------------------------------
    # RESUME PREVIEW
    # --------------------------------------------------

    st.divider()

    with st.expander("📄 Extracted Resume Text"):
        st.write(resume_text)

    with st.expander("🧹 Processed Resume Text"):
        st.write(processed_resume)

else:

    st.info("👆 Upload your resume and optionally paste a Job Description to begin analysis.")