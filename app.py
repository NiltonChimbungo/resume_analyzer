import streamlit as st
import spacy
from fpdf import FPDF
import io
import PyPDF2
import matplotlib.pyplot as plt

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

SKILL_SET = {
    "html", "css", "javascript", "react", "git", "responsive design", "sql",
    "python", "docker", "aws", "ci/cd", "node.js", "mongodb", "flask", "rest apis"
}

def generate_pdf():
    """Generates a sample PDF file."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="John Doe", ln=1)
    pdf.cell(200, 10, txt="Software Engineer", ln=1)
    pdf.cell(200, 10, txt="Skills: Python, SQL, Git, REST APIs", ln=1)
    pdf_bytes = pdf.output(dest='S').encode('latin1')
    return io.BytesIO(pdf_bytes)

def load_text_from_file(file):
    """Loads text from a file, handling both .txt and .pdf."""
    text = ""
    try:
        if file.type == "text/plain":
            text = file.read().decode("utf-8")
        elif file.type == "application/pdf":
            try:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    text += page.extract_text()
            except Exception as e:
                st.error(f"Error reading PDF: {e}")
                return ""
        else:
            st.error("Unsupported file type")
            return ""
    except Exception as e:
        st.error(f"Error reading file: {e}")
        return ""
    return text

def extract_known_skills(text):
    """Extracts known skills from text using spaCy."""
    doc = nlp(text.lower())
    return {token.text for token in doc if token.text in SKILL_SET}

def calculate_match_score(resume_skills, job_skills):
    """Calculates the match score between resume and job skills."""
    matched_skills = resume_skills.intersection(job_skills)
    if not job_skills:
        return 0
    match_percentage = (len(matched_skills) / len(job_skills)) * 100
    return match_percentage, matched_skills

def display_skills(skills, title):
    """Displays skills with a given title."""
    st.markdown(f"### {title}")
    if skills:
        st.markdown(", ".join(skills))
    else:
        st.markdown("No skills found.")

def create_skill_chart(resume_skills, job_skills, matched_skills):
    """Creates a bar chart comparing total vs matched skills."""
    labels = ['Resume', 'Job Description', 'Matched']
    sizes = [len(resume_skills), len(job_skills), len(matched_skills)]

    fig, ax = plt.subplots()
    ax.bar(labels, sizes, color=['blue', 'green', 'purple'])
    ax.set_ylabel('Number of Skills')
    ax.set_title('Skill Comparison')
    return fig

def main():
    st.title("Resume Analyzer")

    use_demo = st.checkbox("Use demo resume")

    resume_file = None
    if use_demo:
        pdf_io = generate_pdf()
        resume_file = pdf_io

    resume_file = st.file_uploader("Upload Resume (.pdf or .txt)", type=["pdf", "txt"], accept_multiple_files=False, key="resume")
    job_description_file = st.file_uploader("Upload Job Description (.txt)", type=["pdf", "txt"], accept_multiple_files=False, key="job")

    if resume_file is not None and job_description_file is not None:
        resume_text = load_text_from_file(resume_file)
        job_description_text = load_text_from_file(job_description_file)

        if resume_text and job_description_text:
            resume_skills = extract_known_skills(resume_text)
            job_skills = extract_known_skills(job_description_text)

            match_score, matched_skills = calculate_match_score(resume_skills, job_skills)

            st.markdown(f"## Match Score: {match_score:.2f}%")

            display_skills(matched_skills, "Skills Found in Both")

            missing_skills = job_skills - resume_skills
            display_skills(missing_skills, "Skills Missing from Resume")

            # Create and display the skill chart
            fig = create_skill_chart(resume_skills, job_skills, set(matched_skills))
            st.pyplot(fig)
        else:
            st.error("Failed to load text from one or both files.")

if __name__ == "__main__":
    main()
