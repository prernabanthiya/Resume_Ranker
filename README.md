
# 📁 AI Resume Ranking Tool


**An AI-powered system that analyzes and ranks multiple resumes against a Job Description using NLP and semantic similarity.**

---

## Overview

Screening resumes manually is time-consuming and often inconsistent. This tool uses **AI-driven semantic matching** to automatically analyze multiple resumes and rank them based on their relevance to a given Job Description.

Built with **Python, Streamlit, and NLP models**, it provides a fast, intelligent, and unbiased ranking system for recruiters.

---

## Key Features

### Semantic Resume Matching
The system understands the *meaning* behind resumes and job descriptions, going beyond simple keyword matching.

### Multi-Resume Upload
Upload multiple PDF resumes at once for batch processing.

### Smart Ranking Algorithm
Each resume is scored and ranked based on how well it matches the job description.

### Clean, User-Friendly Interface
The Streamlit interface features:

* Gradient headers
* Responsive cards
* Soft shadows
* Compact and recruiter-friendly design

### Fast and Automated
Processes multiple resumes in seconds.

---

## Tech Stack

| Layer                | Technology                         |
| -------------------- | ---------------------------------- |
| Frontend             | Streamlit, Custom CSS              |
| AI / NLP             | Sentence Transformers / Embeddings |
| Backend              | Python                             |
| PDF Parsing          | PyPDF2 / PDFMiner                  |
| Deployment Ready     | Streamlit Cloud / Docker / EC2     |

---

## How It Works

1. Upload multiple PDF resumes  
2. Paste the job description  
3. Click **Rank Resumes**  
4. The system:
   * Extracts text from PDFs
   * Generates embeddings
   * Compares resumes with the job description
   * Computes similarity scores
   * Ranks the candidates  
5. Results are displayed in simple, compact ranking cards.

---

## Project Structure

```

📦 ai-resume-ranker
│
├── app.py              # Streamlit application
├── parser.py           # PDF text extraction
├── matcher.py          # AI ranking logic
├── requirements.txt    # Dependencies
└── README.md           # Documentation

````

---

## Why This Project Matters

This project highlights the ability to:

* Build an **end-to-end AI product**
* Apply **NLP for practical use cases**
* Integrate **semantic similarity models**
* Design a **professional UI**
* Handle **file processing and pipelines**
* Write **modular, maintainable code**

It’s a real-world tool that demonstrates practical AI skills in a way recruiters can immediately appreciate.

---

## Installation

```bash
git clone https://github.com/yourname/ai-resume-ranker.git
cd ai-resume-ranker
pip install -r requirements.txt
streamlit run app.py
````

---

## Future Enhancements

* Detailed skill-to-JD alignment report
* Match percentage per category (technical skills, soft skills, experience)
* LLM-generated resume improvement suggestions
* Cloud deployment with user authentication
* Export ranked results to CSV

---

## Impact

This project showcases:

* Strong AI and NLP skills
* Ability to build production-ready tools
* End-to-end application development experience
* Solutions for a real recruitment pain point

Recruiters can immediately see that you can build functional, intelligent tools, not just theoretical models.

```

