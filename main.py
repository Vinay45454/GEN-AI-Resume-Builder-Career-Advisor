import streamlit as st
from input import get_user_input
from gener import generate_resume
from advisor import get_career_advice

st.title("AI Resume Builder and Career Advisor")

user_profile = get_user_input()

def is_profile_complete(profile):
    return all(value for value in profile.values())

if st.button("Generate Resume"):
    if is_profile_complete(user_profile):
        resume_content, pdf_file_path = generate_resume(user_profile)
        
        st.subheader("Generated Resume")
        st.markdown(resume_content)  

        with open(pdf_file_path, "rb") as f:
            st.download_button("Download Resume (PDF)", f, file_name="generated_resume.pdf")
    else:
        st.error("Please fill in all fields before generating a resume.")

if st.button("Get Career Advice"):
    if is_profile_complete(user_profile):

        advice = get_career_advice(user_profile)
        
        st.subheader("Career Advice")
        st.markdown(advice)  
    else:
        st.error("Please fill in all fields before generating a resume.")
