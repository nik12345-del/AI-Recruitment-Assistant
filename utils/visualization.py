import streamlit as st
import plotly.express as px


# ---------------- Pie Chart ---------------- #

def skill_chart(matched, missing):

    data = {
        "Category": ["Matched Skills", "Missing Skills"],
        "Count": [matched, missing]
    }

    fig = px.pie(
        data,
        names="Category",
        values="Count",
        hole=0.45,
        color="Category",
        color_discrete_map={
            "Matched Skills": "#22C55E",
            "Missing Skills": "#EF4444"
        },
        title="Skill Matching"
    )

    fig.update_layout(height=420)

    st.plotly_chart(fig, use_container_width=True)


# ---------------- Bar Chart ---------------- #

def chunk_chart(resume_chunks, job_chunks):

    data = {
        "Document": ["Resume", "Job Description"],
        "Chunks": [resume_chunks, job_chunks]
    }

    fig = px.bar(
        data,
        x="Document",
        y="Chunks",
        text="Chunks",
        color="Document",
        color_discrete_sequence=["#3B82F6", "#F59E0B"]
    )

    fig.update_layout(
        title="Resume vs Job Description",
        height=420
    )

    st.plotly_chart(fig, use_container_width=True)