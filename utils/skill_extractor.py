from utils.skills import SKILLS

def extract_skills(text):

    text = text.lower()

    found = []

    for skill in SKILLS:
        if skill in text:
            found.append(skill)

    return list(set(found))


def compare_skills(resume, jd):

    resume_skills = extract_skills(resume)
    jd_skills = extract_skills(jd)

    matched = list(set(resume_skills) & set(jd_skills))
    missing = list(set(jd_skills) - set(resume_skills))

    return matched, missing