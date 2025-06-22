# resume_parser.py
import re

def parse_resume(text: str) -> dict:
    parsed = {}

    # Email
    email_match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    parsed["email"] = email_match.group(0) if email_match else "Not found"

    # Phone
    phone_match = re.search(r'(\+?\d{1,3})?\s?\(?\d{3,5}\)?[\s.-]?\d{3,5}[\s.-]?\d{3,5}', text)
    parsed["phone"] = phone_match.group(0) if phone_match else "Not found"

    # Education (basic)
    education_keywords = ["B.Tech", "Bachelor", "BE", "M.Tech", "Master", "MBA", "PhD"]
    parsed["education"] = [line for line in text.split('\n') if any(k in line for k in education_keywords)]

    # Skills
    skills_keywords = ["Python", "Java", "C++", "SQL", "Machine Learning", "HTML", "CSS", "JavaScript", "React", "Node", "Django"]
    parsed["skills"] = [skill for skill in skills_keywords if skill.lower() in text.lower()]

    # Work Experience (basic section grabbing)
    experience_section = re.search(r'(Experience|Work History|Employment)(.|\n){0,1000}', text, re.IGNORECASE)
    parsed["experience"] = experience_section.group(0).strip() if experience_section else "Not found"

    return parsed
