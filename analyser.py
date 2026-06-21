def analyze_resume(resume_text, job_description):

    # predefined skill list (important for ATS)
    skills = [
        "python", "java", "c++", "sql", "flask",
        "django", "react", "api", "html", "css",
        "javascript", "machine learning"
    ]

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    matched = []
    missing = []

    for skill in skills:
        if skill in job_description:
            if skill in resume_text:
                matched.append(skill)
            else:
                missing.append(skill)

    score = int((len(matched) / len([s for s in skills if s in job_description]) * 100)
                if len([s for s in skills if s in job_description]) > 0 else 0)

    return score, matched, missing