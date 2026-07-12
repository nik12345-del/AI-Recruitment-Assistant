import streamlit as st


def show_roadmap(missing_skills):

    st.subheader("🚀 AI Resume Improvement Roadmap")

    if not missing_skills:
        st.success("🎉 Your resume already matches the job description very well!")
        return

    week = 1

    for skill in missing_skills:

        st.markdown(f"""
### 📅 Week {week}

✅ Learn **{skill}**

- Complete a beginner course
- Build one mini project
- Add it to your resume
- Practice interview questions
""")

        week += 1