# 📄 Resume Analyzer (AI-Powered Skill Matcher)

This project is a simple and effective tool that analyzes how well a resume matches a job description using keyword comparison and basic NLP techniques. Built with Streamlit and spaCy, it's designed for job seekers and recruiters alike to measure skill alignment.

## 🚀 Features

- Upload a resume (`.pdf` or `.txt`)
- Upload a job description (`.txt`)
- Extracts and compares relevant technical skills
- Calculates a **match score (%)**
- Displays:
  - ✅ Skills found in both
  - ❌ Skills missing from resume
- Visual skill comparison bar chart using `matplotlib`

## 🧰 Technologies Used

- Python 3
- Streamlit
- spaCy (`en_core_web_sm`)
- PyPDF2 (PDF parsing)
- Matplotlib (charts)

## 📁 File Structure

```
resume_analyzer/
├── app.py
├── README.md
├── resume.txt
├── job_description.txt
├── matched_resume_1.txt ... matched_resume_10.txt
├── job_description_1.txt ... job_description_10.txt
```

## 🧪 How to Run

1. Install dependencies:
```bash
pip install streamlit spacy matplotlib fpdf PyPDF2
python -m spacy download en_core_web_sm
```

2. Run the app:
```bash
streamlit run app.py
```

3. Upload a resume and job description file as prompted.

## 📊 Sample Files

Use the `matched_resume_*.txt` and `job_description_*.txt` files to test different scenarios.

## 🌐 Live Demo (optional)

You can deploy this app online using [Streamlit Cloud](https://share.streamlit.io/).

## 🙋‍♂️ Author

Created by Nilton Chimbungo  
GitHub: [@NiltonChimbungo](https://github.com/NiltonChimbungo)
