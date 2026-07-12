from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def recommend_projects(resume, job, matched_skills, missing_skills):

    prompt = f"""
You are an expert AI Career Mentor.

Candidate Resume:
{resume}

Job Description:
{job}

Matched Skills:
{", ".join(matched_skills)}

Missing Skills:
{", ".join(missing_skills)}

Suggest ONLY 5 resume-worthy projects.

For each project provide:

Project Name
Difficulty (Beginner/Intermediate/Advanced)
Technologies Required
Estimated Duration
Why it will help in placements

Format your answer using markdown.
"""

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content