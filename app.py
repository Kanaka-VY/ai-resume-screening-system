import streamlit as st
import pdfplumber
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="AI Resume Screener", layout="centered")

st.title("🚀 AI Resume Screening System")
st.write("NEW VERSION RUNNING ✅")

# ------------------ SKILLS LIST ------------------
skills_list = [
    "python", "machine learning", "deep learning",
    "sql", "power bi", "excel", "nlp",
    "computer vision", "data analysis"
]

# ------------------ FUNCTIONS ------------------

# Extract text from PDF
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

# Extract skills
def extract_skills(text):
    found_skills = []
    text = text.lower()
    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)
    return found_skills

# ------------------ INPUT ------------------

job_description = st.text_area("📌 Enter Job Description")

uploaded_files = st.file_uploader(
    "📄 Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

# ------------------ BUTTON ACTION ------------------

if st.button("🔍 Analyze Resumes"):

    if job_description.strip() == "":
        st.warning("⚠️ Please enter a job description.")

    elif not uploaded_files:
        st.warning("⚠️ Please upload at least one resume.")

    else:
        with st.spinner("Analyzing resumes..."):

            resumes = []
            resume_names = []

            # Extract text + names
            for file in uploaded_files:
                resumes.append(extract_text_from_pdf(file))
                resume_names.append(file.name)

            # Load BERT model
            model = SentenceTransformer('all-MiniLM-L6-v2')

            # Convert to embeddings
            resume_embeddings = model.encode(resumes)
            job_embedding = model.encode([job_description])

            # Compute similarity
            similarity = cosine_similarity(job_embedding, resume_embeddings)
            scores = similarity.flatten()

            # Sort results
            ranked_results = sorted(
                [(i, score) for i, score in enumerate(scores)],
                key=lambda x: x[1],
                reverse=True
            )

        st.success("✅ Analysis Complete!")

        st.subheader("🏆 Resume Ranking")

        medals = ["🥇", "🥈", "🥉"]

        for rank, (i, score) in enumerate(ranked_results):
            medal = medals[rank] if rank < 3 else "🔹"
            skills = extract_skills(resumes[i])

            # Show resume name + percentage
            st.write(f"{medal} {resume_names[i]} → **{score*100:.1f}%**")

            # Match explanation
            if score > 0.7:
                st.success("Strong match ✅")
            elif score > 0.4:
                st.info("Moderate match ⚠️")
            else:
                st.error("Low match ❌")

            # Skills
            st.write(f"🛠 Skills: {', '.join(skills) if skills else 'Not found'}")
            st.markdown("---")

        # Detailed scores
        st.subheader("📊 Detailed Scores")
        for i, score in enumerate(scores):
            st.progress(float(score))
            st.write(f"{resume_names[i]}: {score*100:.1f}%")