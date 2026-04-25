# 🚀 AI Resume Screening System

An AI-powered system that automates resume screening using Natural Language Processing (NLP) and BERT-based semantic similarity.

## 📌 Problem

Manual resume screening is time-consuming and often relies on keyword matching, which can overlook strong candidates who use different wording or phrasing.


## 💡 Solution

This project uses BERT-based semantic similarity to understand the meaning behind resumes and job descriptions, enabling more accurate and meaningful candidate ranking.


## 🔍 Features

- 📄 Upload multiple PDF resumes  
- 🧠 BERT-based semantic matching (not just keywords)  
- 🏆 Rank candidates based on job relevance  
- 🛠 Automatic skill extraction  
- 📊 Visual score representation  

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
![UI](screenshot1.png)

### 📊 Resume Ranking Output
![Results](screenshot2.png)

---

## 🚀 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/Kanaka-VY/ai-resume-screening-system.git

# Navigate to project folder
cd ai-resume-screening-system

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
