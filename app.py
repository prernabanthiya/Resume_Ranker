import streamlit as st
import os
from parser import extract_text_from_pdf
from matcher import rank_resumes

# ---------- Page Config ----------
st.set_page_config(
    page_title="AI Resume Ranking Tool",
    page_icon="📁",
    layout="wide"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>

.header {
    background: linear-gradient(90deg, #4A90E2, #357ABD);
    padding: 25px 40px;
    border-radius: 12px;
    color: white;
    margin-bottom: 25px;
}

/* Upload box */
.upload-box {
    padding: 20px;
    border-radius: 12px;
    background: #F7F9FC;
    border: 1px dashed #4A90E2;
}

/* Compact result cards */
.card {
    padding: 12px 16px;
    border-radius: 10px;
    background: #ffffff;
    border: 1px solid #e6e6e6;
    box-shadow: 0 2px 6px rgba(0,0,0,0.06);
    margin-bottom: 12px;
    transition: transform 0.12s ease, box-shadow 0.12s ease;
}

.card:hover {
    transform: translateY(-3px);
    box-shadow: 0 4px 14px rgba(0,0,0,0.12);
}

.card-title {
    background: linear-gradient(90deg, #4A90E2, #357ABD);
    color: white;
    padding: 6px 10px;
    border-radius: 6px;
    margin-bottom: 8px;
    font-size: 15px;
    font-weight: 600;
}

.card-score {
    font-size: 14px;
    color: #333;
    margin-top: 2px;
}

</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown("""
<div class="header">
    <h1 style="margin-bottom:0;">AI Resume Ranking Tool</h1>
    <p style="font-size:18px; opacity:0.9;">Rank Multiple Resumes Against Any Job Description</p>
</div>
""", unsafe_allow_html=True)

# ---------- Sample JD (used internally) ----------
sample_jd = """
We are seeking a highly skilled Python Developer with experience in Machine Learning, 
NLP, and API development. The ideal candidate should have strong knowledge of 
data structures, cloud deployment (AWS/GCP), and modern Python frameworks.
"""

# ---------- Two-Column Layout ----------
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 📌 Job Description")
    job_desc = st.text_area("Paste Job Description", height=200)

with col2:
    st.markdown("### 📄 Upload Resumes (PDF)")
    uploaded_files = st.file_uploader(
        "Upload PDFs",
        type="pdf",
        accept_multiple_files=True
    )

# ---------- Rank Button ----------
st.markdown("### 🚀 Process")
rank_button = st.button("Rank Resumes")

# ---------- Ranking Logic ----------
if rank_button and job_desc and uploaded_files:

    with st.spinner("Analyzing resumes... Please wait ⏳"):
        resume_texts = []
        names = []

        for file in uploaded_files:
            # Save temporary file
            temp_path = f"temp_{file.name}"
            with open(temp_path, "wb") as f:
                f.write(file.getbuffer())

            # Extract text
            text = extract_text_from_pdf(temp_path)
            resume_texts.append(text)
            names.append(file.name)

            # Remove temp temp file
            os.remove(temp_path)

        # Rank resumes
        scores = rank_resumes(job_desc, resume_texts)
        results = sorted(zip(names, scores), key=lambda x: x[1], reverse=True)

    # ---------- Display Ranked Cards ----------
    st.markdown("## 🏆 Ranked Results")

    for name, score in results:
        st.markdown(f"""
        <div class="card">
            <div class="card-title">{name}</div>
            <p class="card-score"><b>Score:</b> {score:.2f}</p>
        </div>
        """, unsafe_allow_html=True)
