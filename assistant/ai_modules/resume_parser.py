import spacy
import pdfplumber

nlp = spacy.load("en_core_web_sm")

skills_list = [
    "python","sql","machine learning","django","html",
    "css","javascript","data analysis","deep learning",
    "nlp","react","pandas","numpy"
]


def extract_text_from_pdf(file):

    text = ""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()

    return text


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills


def calculate_ats_score(found_skills):

    total_skills = len(skills_list)

    matched = len(found_skills)

    score = int((matched / total_skills) * 100)

    missing_skills = []

    for skill in skills_list:
        if skill not in found_skills:
            missing_skills.append(skill)

    return score, missing_skills


def analyze_resume(file):

    text = extract_text_from_pdf(file)

    skills = extract_skills(text)

    score, missing = calculate_ats_score(skills)

    return {
        "skills": skills,
        "ats_score": score,
        "missing_skills": missing
    }