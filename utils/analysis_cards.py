import streamlit as st


def analysis_cards(result):

    st.header("🧠 AI Resume Insights")

    sections = result.split("**")

    for section in sections:

        section = section.strip()

        if not section:
            continue

        if "Strength" in section:
            st.success("💪 " + section)

        elif "Weak" in section:
            st.warning("⚠ " + section)

        elif "Missing" in section:
            st.error("❌ " + section)

        elif "Recommendation" in section:
            st.info("🚀 " + section)

        elif "Course" in section:
            st.info("📚 " + section)

        else:
            st.markdown(section)