import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("AI Resume Screening System")

# Sample resumes
resumes = [
    "Python developer with machine learning experience",
    "Data analyst skilled in SQL and Power BI",
    "AI engineer with deep learning and computer vision"
]

# Job description input
job_description = st.text_area("Enter Job Description")

if st.button("Analyze Resumes"):

    if job_description.strip() == "":
        st.warning("Please enter a job description.")
    else:
        # Convert text into vectors
        vectorizer = TfidfVectorizer()

        vectors = vectorizer.fit_transform(resumes + [job_description])

        # Calculate similarity
        similarity = cosine_similarity(vectors[-1], vectors[:-1])

        scores = similarity.flatten()

        st.subheader("Resume Ranking")

        for i, score in enumerate(scores):
            st.write(f"Resume {i+1} Match Score: {score:.2f}")