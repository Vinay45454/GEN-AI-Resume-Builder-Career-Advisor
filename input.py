import streamlit as st

def get_user_input():
    name = st.text_input("Name")
    email = st.text_input("Email")
    education = st.text_area("Education")
    experience = st.text_area("Work Experience")
    skills = st.text_area("Skills")
    goals = st.text_area("Career Goals")

    return {
        "name": name,
        "email": email,
        "education": education,
        "experience": experience,
        "skills": skills,
        "goals": goals
    }
