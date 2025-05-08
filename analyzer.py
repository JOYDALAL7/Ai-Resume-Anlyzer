### Project: AI Resume Analyzer (Starter Code)

# analyzer.py
import streamlit as st
from resume_parser import extract_text_from_docx
from utils import analyze_resume

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")
st.title("🤖 AI Resume Analyzer")

st.write("""
Upload your resume and paste a job description to get a match score, missing skills, and improvement tips.
""")

resume_file = st.file_uploader("Upload Resume (.docx)", type=["docx"])
job_desc = st.text_area("Paste Job Description")

if st.button("Analyze") and resume_file and job_desc:
    with st.spinner("Analyzing your resume..."):
        resume_text = extract_text_from_docx(resume_file)
        result = analyze_resume(resume_text, job_desc)
        st.success("Analysis complete!")
        st.markdown("### Results")
        st.write(result)


# resume_parser.py
from docx import Document

def extract_text_from_docx(file):
    doc = Document(file)
    return "\n".join([p.text for p in doc.paragraphs])


# utils.py
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")  # Use environment variable

def analyze_resume(resume_text, job_text):
    prompt = f"""
    Compare this resume:\n{resume_text}\n\nwith this job description:\n{job_text}.
    Return a match percentage, list missing skills, and give 3 resume improvement tips.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']


