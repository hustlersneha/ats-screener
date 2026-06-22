import streamlit as st
import matplotlib.pyplot as plt
from parser import extract_text_from_pdf

st.set_page_config(page_title="ATS Screener", layout="centered")

st.title(" ATS Resume Screener")
st.write("Compare your resume with job description like real ATS systems")


uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
job_description = st.text_area("Paste Job Description")


# Skills list
#add the keywords mannually
SKILLS = [
    "python", "java", "c++", "sql", "flask",
    "django", "react", "html", "css", "javascript",
    "api", "machine learning", "git", "github"
]


# Analyze button

if st.button("Analyze Resume"):

    if uploaded_file and job_description:

        # Extract text
        resume_text = extract_text_from_pdf(uploaded_file).lower()
        job_description = job_description.lower()

        matched = []
        missing = []

        
        # Skill matching logic
        
        for skill in SKILLS:
            if skill in job_description:
                if skill in resume_text:
                    matched.append(skill)
                else:
                    missing.append(skill)

        total = len(matched) + len(missing)

        
        # Score calculation
        
        score = int((len(matched) / total) * 100) if total > 0 else 0

        
        # OUTPUT SECTION
        
        st.subheader(f" ATS Score: {score}/100")
        st.progress(score / 100)

        
        # Matched Skills
        
        st.write(" Matched Skills")
        if matched:
            st.success(matched)
        else:
            st.warning("No matching skills found")

       
        # Missing Skills
        
        st.write(" Missing Skills")
        if missing:
            st.error(missing)
        else:
            st.success("No missing skills ")

       
        # Suggestions
        
        st.write(" Suggestions")

        if score < 40:
            st.error("Low match → Resume needs major improvement")
        elif score < 70:
            st.warning("Medium match → Improve missing skills")
        else:
            st.success("Strong match → Good resume")

        st.write("- Add missing skills in your resume")
        st.write("- Include project descriptions using keywords")
        st.write("- Make resume more job-specific")

       
        #  PIE CHART (NEW FEATURE)
       
        labels = ["Matched Skills", "Missing Skills"]
        values = [len(matched), len(missing)]

        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
        ax.axis("equal")

        st.write("Skill Match Visualization")
        st.pyplot(fig)

       
        # DOWNLOAD REPORT (NEW FEATURE)
        
        report = f"""
                ATS RESUME REPORT
                -----------------------
                Score: {score}/100

                Matched Skills:
                {matched}

                Missing Skills:
                {missing}

                Suggestions:
                - Improve missing skills
                - Add projects with keywords
                - Tailor resume for job description
                """

        st.download_button(
            label=" Download ATS Report",
            data=report,
            file_name="ATS_Report.txt",
            mime="text/plain"
        )

    else:
        st.warning("Please upload resume AND paste job description")