import streamlit as st

from utils.pdf_extractor import extract_text_from_pdf
from utils.preprocess import preprocess_text
from utils.skills import extract_skills
from utils.ats_score import calculate_ats_score

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# ----------------------------------
# HEADER
# ----------------------------------

st.title("📄 AI Resume Analyzer")
st.caption("Upload your resume and get AI-powered insights.")

st.divider()

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

# ----------------------------------
# PROCESS
# ----------------------------------

if uploaded_file:

    resume_text = extract_text_from_pdf(uploaded_file)

    processed_text = preprocess_text(resume_text)

    detected_skills = extract_skills(processed_text)

    ats_score = calculate_ats_score(
        resume_text,
        detected_skills
    )

    st.success("✅ Resume Uploaded Successfully")

    st.subheader("📊 Resume Analysis")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("ATS Score", f"{ats_score}/100")

    c2.metric(
        "Skills",
        len(detected_skills)
    )

    c3.metric(
        "Words",
        len(processed_text.split())
    )

    c4.metric(
        "Characters",
        len(resume_text)
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

    st.expander("📄 Extracted Resume Text").text(resume_text)

    st.expander("🧹 Processed Resume Text").text(processed_text)