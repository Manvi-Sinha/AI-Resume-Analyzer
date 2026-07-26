import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("📄 AI Resume Analyzer")
st.write("Analyze your resume using AI and get an ATS score.")

st.divider()

# -----------------------------
# Upload Resume
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:
    st.success("✅ Resume uploaded successfully!")
    st.write("Filename:", uploaded_file.name)