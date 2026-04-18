from skills import *
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def jd_match(resume, jd):

    text = [resume, jd]

    cv = CountVectorizer().fit_transform(text)

    similarity = cosine_similarity(cv)[0][1]

    return int(similarity * 100)

def predict_role(resume_text):

    ds_score = sum(skill in resume_text for skill in DATA_SCIENCE_SKILLS)
    web_score = sum(skill in resume_text for skill in WEB_DEV_SKILLS)
    analyst_score = sum(skill in resume_text for skill in ANALYST_SKILLS)

    scores = {
        "Data Scientist": ds_score,
        "Web Developer": web_score,
        "Data Analyst": analyst_score
    }

    role = max(scores, key=scores.get)
    return role, scores


def skill_gap(resume_text, role):

    if role == "Data Scientist":
        skills = DATA_SCIENCE_SKILLS
    elif role == "Web Developer":
        skills = WEB_DEV_SKILLS
    else:
        skills = ANALYST_SKILLS

    matching = [skill for skill in skills if skill in resume_text]
    missing = [skill for skill in skills if skill not in resume_text]

    score = int((len(matching)/len(skills))*100)

    return matching, missing, score