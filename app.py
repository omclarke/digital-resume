from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Olijoh M. Clarke"
PAGE_ICON = ":wave:"
NAME = "Olijoh M.Clarke"
DESCRIPTION = """
Data Analyst with pharmacy and military experience. Assisting companies by supporting data-driven decision-making and insights.
"""
EMAIL = "olijoh.clarke@email.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/omclarke",
    "GitHub": "https://github.com/omclarke",
    "Replit": "https://replit.com/@omclarke",
    
} #"Web": "www.olijohclarke.me"
PROJECTS = {
    "🏆 Business Analysis - Revenue Growth Models - Lariat Rent-A-Car ": "https://drive.google.com/drive/folders/1v9HcgFNm1ypx5I4lYb4Xtkz5WM6zaNlx?usp=sharing",
    "🏆 Statistical Significance – Annual Fuel Costs – Fuel Economy ": "https://drive.google.com/drive/folders/1qVn46VRbfOqBTtWmztAxdcJI-jhcvsP6?usp=share_link",
    "🏆 Currency Correlations – Foreign Exchange Currency": "https://drive.google.com/drive/folders/1gDE5jUTxbKCotF-v33emtStTephSj6w4?usp=share_link",
} #"🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ Experience extracting actionable insights from data, and dashboarding.
- ✔️ Instructing, Preseting and Public Speaking, 
- ✔️ Supervisory, and Operations Experience
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Pandas, NumPY, Streamlit), SQL, VBA, R Programming 
- 📊 Data Visulization: MS Excel, PowerBI, Tableau, Plotly
- 📚 Modeling: Statistical analysis, A/B testing, t-tests, data visualization, data cleaning, discovery, exploration, and modeling.
- 🗄️ Databases: Postgres, MySQL, SQLite
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Pharmacy Technician | Actalent (Contractor) **")
st.write("02/2023 - Present | Remote")
st.write(
    """
- ► Employing analytical thinking to identify patterns and trends in claim data, aiding in the resolution of each authorization process.
- ► Ensuring compliance with privacy and confidentiality regulations while processing pharmacy benefit prior authorizations.
- ► Collaborating with teams to investigate and resolve challenges impacting member services and medical professionals in claim processing.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Data Analyst (Bootcamp FT) | Thinkful (Certificate)**")
st.write("07/2022 - 11/2022 | Remote")
st.write(
    """
- ► Produced and presented professional projects in areas of business forecasting, price modeling, and statistical analysis.
- ► Acquired skills in data analytics systems such as Pandas, Excel, PostgreSQL, Tableau, and Python.
- ► Adept in dashboarding, performance tracking, data wrangling, and analysis methodologies.
- ►	Graduated 1 month earlier due to efficient time management and beating project deadlines. 
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Military Police  | US Army**")
st.write("10/2020 - 06/2022 | Fort Bragg, NC")
st.write(
    """
- ► Employed analytical thinking to identify insights from collected data, supporting decision-making processes and enhancing mission effectiveness.
- ► Ensured compliance with privacy and confidentiality regulations while handling intelligence data, maintaining the integrity and security of classified information in alignment with organizational policies and procedures.
- ► Managed, analyzed, documented, and reported sensitive military intelligence with secret clearance.
- ► Input and document cases in databases, ensuring comprehensive records of patrols and mission goals for analysis and reporting.
"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**Pharmacy Technician | PAGNY - Correctional Health Services**")
st.write("04/2015 - 01/2018 | Rikers Island, NY")
st.write(
    """
- ► Provided care in a high-stress environment.
- ► Cooperating and collaborating with professionals in various departments and locations.
"""
)

# --- JOB 5
st.write('\n')
st.write("🚧", "**Account Manager | AmerisourceBergen**")
st.write("09/2017 - 08/2018 | Amityville, NY")
st.write(
    """
- ► Exceeded company standards by an additional 10%, by metric-based performance measures.
- ► Managed independent/chain pharmacy accounts with Salesforce CRM.
- ► Excellent written and verbal communication skills with both team, clients and prospects.
"""
)

# --- JOB 6
st.write('\n')
st.write("🚧", "**History Highlights**")
st.write("06/2010 - 08/2018")
st.write(
    """
- ► Supervised a team of 4 pharmacy technicians which led to promotion into position of lead pharmacy technician after 2 years of employment.
- ► Exceeded quarterly targets by 15%, leading to a promotion and 60% pay increase within 7 months of employment.
- ► Utilized data-driven approach to instruction, resulting in a 12% increase in average test scores.
- ► Successfully captured data for metrics and analysis to present to the team.
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# --- EDUCATION ---
st.write('\n')
st.subheader("Education")
st.write(
    """
- BA Computer Science | Thomas Edison State University | Enrolled
"""
)