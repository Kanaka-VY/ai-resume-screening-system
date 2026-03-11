import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample resumes
resumes = [
    "Python developer with machine learning experience",
    "Data analyst skilled in SQL and Power BI",
    "AI engineer with deep learning and computer vision"
]

# Job description
job_description = input("enter job_description ")

# Convert text to vectors
vectorizer = TfidfVectorizer()

vectors = vectorizer.fit_transform(resumes + [job_description])

# Calculate similarity
similarity = cosine_similarity(vectors[-1], vectors[:-1])

# Flatten scores
scores = similarity.flatten()

# Print results
print("Resume Screening Results:\n")

for i, score in enumerate(scores):
    print(f"Resume {i+1} Match Score: {score:.2f}")