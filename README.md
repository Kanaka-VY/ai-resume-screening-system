# 🚀 AI Resume Screening System

An AI-powered application that automates resume screening using NLP and BERT-based semantic similarity to identify the most relevant candidates.

---

## 📌 Problem

Manual resume screening is time-consuming and often limited to keyword matching, which can overlook strong candidates who use different wording.

---

## 💡 Solution

This system uses **BERT-based semantic similarity** to understand the meaning of resumes and job descriptions, enabling more accurate candidate ranking and better hiring decisions.

---

## 🔍 Features

- 📄 Upload multiple PDF resumes  
- 🧠 Semantic matching using BERT (not just keywords)  
- 🏆 Rank candidates based on job relevance  
- 🛠 Automatic skill extraction  
- 📊 Match score visualization  
- 📁 Supports real-time resume analysis  

---

## ⚙️ Tech Stack

- Python  
- Streamlit  
- Sentence Transformers (BERT)  
- Scikit-learn  
- PDFPlumber  

---

## 📸 Screenshots

### 🖥️ Application Interface
![App UI](welcome.png)

### 🏆 Resume Ranking
![Ranking](2nd.png)

### 📊 Detailed Score Visualization
![Scores](3rd.png)

---

## 🚀 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/Kanaka-VY/ai-resume-screening-system.git

# Navigate to project folder
cd ai-resume-screening-system

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
