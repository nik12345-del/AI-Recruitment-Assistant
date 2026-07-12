import streamlit as st
import plotly.graph_objects as go
from utils.visualization import skill_chart, chunk_chart


def show_dashboard(
    ats_score,
    resume_chunks,
    job_chunks,
    retrieved_chunks,
    matched_skills,
    missing_skills
):

    # ---------------- Dashboard ---------------- #

    st.subheader("📊 Resume Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("ATS Score", f"{ats_score}%")
    col2.metric("Resume Chunks", len(resume_chunks))
    col3.metric("JD Chunks", len(job_chunks))
    col4.metric("Top Matches", len(retrieved_chunks))

    st.divider()

    # ---------------- Resume Rating ---------------- #

    if ats_score >= 85:
        st.success("🌟 Excellent Resume")
    elif ats_score >= 70:
        st.info("👍 Good Resume")
    elif ats_score >= 50:
        st.warning("⚠️ Resume Needs Improvement")
    else:
        st.error("❌ Resume Not Suitable")

    st.divider()

    # ---------------- ATS Gauge ---------------- #

    st.subheader("🎯 ATS Performance Gauge")

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=ats_score,
        number={"suffix": "%"},
        title={"text": "ATS Score"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "#2563EB"},
            "steps": [
                {"range": [0, 40], "color": "#ef4444"},
                {"range": [40, 70], "color": "#facc15"},
                {"range": [70, 100], "color": "#22c55e"}
            ]
        }
    ))

    fig.update_layout(height=350)

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # ---------------- Pie Chart ---------------- #

    st.subheader("📈 Skill Matching")

    skill_chart(
        len(matched_skills),
        len(missing_skills)
    )

    st.divider()

    # ---------------- Bar Chart ---------------- #

    st.subheader("📊 Resume vs Job Description")

    chunk_chart(
        len(resume_chunks),
        len(job_chunks)
    )

    st.divider()

    # ---------------- Skills ---------------- #

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("✅ Matched Skills")

        if matched_skills:
            for skill in sorted(matched_skills):
                st.success(skill)
        else:
            st.info("No matched skills found.")

    with col2:

        st.subheader("❌ Missing Skills")

        if missing_skills:
            for skill in sorted(missing_skills):
                st.error(skill)
        else:
            st.success("No missing skills 🎉")

        st.divider()

    st.subheader("📈 Skill Match Progress")

    total_skills = len(matched_skills) + len(missing_skills)

    if total_skills > 0:

        percentage = int((len(matched_skills) / total_skills) * 100)

        st.progress(percentage / 100)

        st.write(f"### {percentage}% Skills Matched")

    st.divider()

    # ---------------- Recommendation ---------------- #

    st.subheader("💡 AI Recommendation")

    if ats_score >= 85:
        st.success(
            "Your resume is highly compatible with this job description."
        )

    elif ats_score >= 70:
        st.info(
            "Improve a few missing skills to increase your selection chances."
        )

    else:
        st.warning(
            "Add more relevant skills and projects according to the job description."
        )