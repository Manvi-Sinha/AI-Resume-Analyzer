import streamlit as st

from utils.pdf_extractor import extract_text_from_pdf
from utils.preprocess import preprocess_text
from utils.skills import extract_skills
from utils.ats_score import calculate_ats_score
from utils.similarity import calculate_similarity

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.caption("Upload your resume and compare it with any Job Description.")

st.divider()

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=220
)

# ----------------------------------------------------
# ANALYZE
# ----------------------------------------------------

if uploaded_file:

    resume_text = extract_text_from_pdf(uploaded_file)

    processed_resume = preprocess_text(resume_text)

    processed_jd = preprocess_text(job_description)

    detected_skills = extract_skills(processed_resume)

    ats_score = calculate_ats_score(
        resume_text,
        detected_skills
    )

    similarity_score = 0

    if job_description.strip():

        similarity_score = calculate_similarity(
            processed_resume,
            processed_jd
        )

    st.success("Resume Uploaded Successfully")

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "ATS Score",
        f"{ats_score}/100"
    )

    c2.metric(
        "Resume Match",
        f"{similarity_score}%"
    )

    c3.metric(
        "Skills",
        len(detected_skills)
    )

    c4.metric(
        "Words",
        len(processed_resume.split())
    )

    st.progress(ats_score / 100)

    if ats_score >= 80:

        st.success("Excellent Resume ⭐")

    elif ats_score >= 60:

        st.info("Good Resume 👍")

    else:

        st.warning("Resume Needs Improvement")

    st.divider()

    st.subheader("🛠 Detected Skills")

    cols = st.columns(4)

    for i, skill in enumerate(detected_skills):

        cols[i % 4].success(skill)

    st.divider()

    with st.expander("📄 Extracted Resume"):

        st.write(resume_text)

    with st.expander("🧹 Processed Resume"):

        st.write(processed_resume)