import pdfplumber

skills_list = [
    "python","sql","machine learning","django","html",
    "css","javascript","data analysis","deep learning",
    "nlp","react","pandas","numpy"
]


def extract_resume_text(file):

    text = ""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text.lower()

    return text


def extract_skills(text):

    found = []

    for skill in skills_list:

        if skill in text:
            found.append(skill)

    return found


def match_resume_job(resume_file, job_description):

    resume_text = extract_resume_text(resume_file)

    resume_skills = extract_skills(resume_text)

    job_skills = extract_skills(job_description.lower())

    matched = []

    missing = []

    for skill in job_skills:

        if skill in resume_skills:
            matched.append(skill)

        else:
            missing.append(skill)

    if len(job_skills) == 0:
        score = 0
    else:
        score = int((len(matched) / len(job_skills)) * 100)

    return {
        "score": score,
        "matched": matched,
        "missing": missing
    }