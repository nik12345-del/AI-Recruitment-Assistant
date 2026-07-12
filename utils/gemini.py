import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def analyze_resume(resume, job):

    prompt = f"""
You are an ATS Resume Analyzer.

Resume:
{resume}

Job Description:
{job}

Analyze the resume and provide:

1. Match Percentage
2. Matching Skills
3. Missing Skills
4. Strengths
5. Weaknesses
6. Final Recommendation

Format the response properly.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content