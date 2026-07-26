import streamlit as st
from utils.pdf_extractor import extract_text_from_pdf
from utils.preprocess import preprocess_text

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# -----------------------------------
# Header
# -----------------------------------
st.title("📄 AI Resume Analyzer")
st.caption("Upload your resume and get AI-powered insights.")

st.divider()

# -----------------------------------
# Upload Resume
# -----------------------------------
uploaded_file = st.file_uploader(
    "Choose your Resume (PDF)",
    type=["pdf"]
)

# -----------------------------------
# Process Resume
# -----------------------------------
if uploaded_file:

    resume_text = extract_text_from_pdf(uploaded_file)

    processed_text = preprocess_text(resume_text)

    col1, col2 = st.columns(2)

    with col1:
        st.success("✅ Resume Uploaded Successfully")
        st.write(f"**File Name:** {uploaded_file.name}")

    with col2:
        st.info(f"📄 Characters Extracted: {len(resume_text)}")

    st.divider()

    # Original Resume
    st.subheader("📃 Extracted Resume Text")

    st.text_area(
        label="Original Resume",
        value=resume_text,
        height=300
    )

    # Processed Resume
    st.subheader("🧹 Processed Resume Text")

    st.text_area(
        label="Processed Resume",
        value=processed_text,
        height=300
    )