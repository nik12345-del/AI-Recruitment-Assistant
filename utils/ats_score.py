import re

def calculate_ats_score(resume_text, job_text):

    resume = resume_text.lower()
    job = job_text.lower()

    words = set(re.findall(r'\w+', job))

    matched = 0

    for word in words:
        if word in resume:
            matched += 1

    if len(words) == 0:
        return 0

    score = int((matched / len(words)) * 100)

    return min(score, 100)