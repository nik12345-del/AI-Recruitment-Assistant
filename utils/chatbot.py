from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def chatbot_response(resume, job, question):

    prompt = f"""
You are an expert AI Recruitment Assistant.

Candidate Resume:

{resume}

Job Description:

{job}

User Question:

{question}

Answer professionally.
Suggest improvements whenever possible.
Keep the answer concise and helpful.
"""

    response = client.chat.completions.create(
       model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content