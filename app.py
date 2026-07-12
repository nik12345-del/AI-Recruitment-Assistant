import streamlit as st
from utils.pdf_parser import extract_text
from utils.text_cleaner import clean_text
from utils.text_chunker import chunk_text
from utils.embeddings import create_embeddings
from utils.vector_store import create_vector_store
from utils.retriever import retrieve_chunks
from utils.gemini import analyze_resume
from utils.ats_score import calculate_ats_score
from utils.visualization import skill_chart, chunk_chart
from utils.dashboard import show_dashboard
from utils.skill_extractor import compare_skills
from utils.chatbot import chatbot_response
from utils.report_generator import generate_report
from utils.analysis_cards import analysis_cards
from utils.roadmap import show_roadmap
from utils.project_recommender import recommend_projects

if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

if "result" not in st.session_state:
    st.session_state.result = ""

if "ats_score" not in st.session_state:
    st.session_state.ats_score = 0

if "matched_skills" not in st.session_state:
    st.session_state.matched_skills = []

if "missing_skills" not in st.session_state:
    st.session_state.missing_skills = []
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- LOAD CSS ---------------- #

def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Recruitment Assistant",
    page_icon="🤖",
    layout="wide"
)

load_css()


# ---------------- TITLE ---------------- #

st.markdown("""
<div class="main-title">
🤖 AI Recruitment Assistant
</div>

<div class="subtitle">
AI Powered ATS Resume Analyzer with RAG + Groq AI
</div>
""", unsafe_allow_html=True)

st.write("Upload your Resume and Job Description to get AI-powered analysis.")

st.divider()


# ---------------- FILE UPLOAD ---------------- #

st.subheader("📄 Upload Resume")

resume = st.file_uploader(
    "Choose Resume",
    type=["pdf"],
    key="resume"
)

st.subheader("💼 Upload Job Description")

job = st.file_uploader(
    "Choose Job Description",
    type=["pdf"],
    key="job"
)


# ---------------- PROCESS ---------------- #

if resume is not None and job is not None:

    # ===========================
    # Resume
    # ===========================

    resume_text = extract_text(resume)

    cleaned_resume = clean_text(resume_text)

    resume_chunks = chunk_text(cleaned_resume)

    resume_embeddings = create_embeddings(resume_chunks)

    resume_index = create_vector_store(resume_embeddings)

    # ===========================
    # Job Description
    # ===========================

    job_text = extract_text(job)

    cleaned_job = clean_text(job_text)

    job_chunks = chunk_text(cleaned_job)

    job_embeddings = create_embeddings(job_chunks)

    job_index = create_vector_store(job_embeddings)

    # ===========================
    # Retrieval
    # ===========================

    retrieved_chunks = retrieve_chunks(
        resume_index,
        job_embeddings[0:1],
        resume_chunks
    )

    # ===========================
    # Resume Section
    # ===========================

    st.success("Resume Uploaded Successfully ✅")

    st.text_area(
        "Clean Resume",
        cleaned_resume,
        height=220,
        key="resume_text"
    )

    st.text_area(
        "First Resume Chunk",
        resume_chunks[0],
        height=180,
        key="resume_chunk"
    )

    st.divider()

    # ===========================
    # Job Section
    # ===========================

    st.success("Job Description Uploaded Successfully ✅")

    st.text_area(
        "Clean Job Description",
        cleaned_job,
        height=220,
        key="job_text"
    )

    st.text_area(
        "First JD Chunk",
        job_chunks[0],
        height=180,
        key="job_chunk"
    )

    st.divider()

    # ===========================
    # Retrieved Chunks
    # ===========================

    st.subheader("🎯 Top Matching Resume Chunks")

    for i, chunk in enumerate(retrieved_chunks, start=1):

        st.text_area(
            f"Match {i}",
            chunk,
            height=160,
            key=f"match{i}"
        )

    st.divider()

    # ===========================
    # Analyze Button
    # ===========================

    st.subheader("🤖 AI Resume Analysis")

    if st.button("Analyze Resume with AI"):

       with st.spinner("Analyzing Resume..."):

        relevant_resume = "\n\n".join(retrieved_chunks)

        result = analyze_resume(
            relevant_resume,
            cleaned_job
        )

        matched_skills, missing_skills = compare_skills(
            cleaned_resume,
            cleaned_job
        )

        ats_score = calculate_ats_score(
            cleaned_resume,
            cleaned_job
        )

    # Save everything AFTER analysis
        st.session_state.result = result
        st.session_state.ats_score = ats_score
        st.session_state.matched_skills = matched_skills
        st.session_state.missing_skills = missing_skills
        st.session_state.analysis_done = True
        
if st.session_state.analysis_done:

    show_dashboard(
        st.session_state.ats_score,
        resume_chunks,
        job_chunks,
        retrieved_chunks,
        st.session_state.matched_skills,
        st.session_state.missing_skills
    )

    generate_report(
        "AI_Recruitment_Report.pdf",
        st.session_state.ats_score,
        st.session_state.matched_skills,
        st.session_state.missing_skills,
        st.session_state.result
    )

    with open("AI_Recruitment_Report.pdf", "rb") as pdf_file:
        st.download_button(
            label="📥 Download AI Report (PDF)",
            data=pdf_file,
            file_name="AI_Recruitment_Report.pdf",
            mime="application/pdf"
        )

    st.success("Analysis Completed ✅")

    analysis_cards(st.session_state.result)
    st.divider()

    show_roadmap(
    st.session_state.missing_skills
    )

    st.divider()

    st.subheader("🚀 AI Recommended Projects")

    projects = recommend_projects(
        cleaned_resume,
        cleaned_job,
        st.session_state.matched_skills,
        st.session_state.missing_skills
    )

    st.markdown(projects)
    st.divider()

    st.subheader("🤖 AI Career Assistant")

    # Show previous chat messages
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    question = st.chat_input(
        "Ask anything about your Resume or Job Description"
    )

    if question:

        # Show user message
        st.session_state.messages.append(
            {"role": "user", "content": question}
        )

        with st.chat_message("user"):
            st.markdown(question)

        # AI response
        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                answer = chatbot_response(
                    cleaned_resume,
                    cleaned_job,
                    question
                )

            st.markdown(answer)

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )