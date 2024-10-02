import pandas as pd
from fpdf import FPDF
from lang import get_llm
from langchain_core.prompts import PromptTemplate

def generate_resume(user_profile):
    llm = get_llm()
    
    resume_prompt = PromptTemplate.from_template(
        """
        ### USER PROFILE:
        Name: {name}
        Email: {email}
        Education: {education}
        Work Experience: {experience}
        Skills: {skills}
        Career Goals: {goals}
        
        ### INSTRUCTION:
        Generate a professional resume using the above profile. 
        Format the output to include:
        - Summary
        - Skills
        - Education
        - Work Experience
        """
    )

    # Generate resume content using the language model
    resume_chain = resume_prompt | llm
    resume_response = resume_chain.invoke(input=user_profile)

    # Format the generated resume content for better readability
    formatted_resume_content = format_rcontent(resume_response.content)

    # Save user profile to CSV for record-keeping
    user_profile_df = pd.DataFrame([user_profile])
    user_profile_df.to_csv('user_profile.csv', mode='a', header=False, index=False)
    # Generate PDF from formatted resume content
    pdf_file_path = generate_pdf(formatted_resume_content)

    return formatted_resume_content, pdf_file_path  # Return both formatted content and file path

def format_rcontent(rcont):
    # Format the generated resume content into sections
    formatted_content = []

    # Assume the response contains sections separated by new lines
    sections = rcont.split("\n")

    for section in sections:
        if section.strip():  # Skip empty lines
            formatted_content.append(section.strip())

    # Joining formatted content with double new lines for separation
    return "\n\n".join(formatted_content)

def generate_pdf(resume_content):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Add formatted resume content to PDF
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, resume_content)

    # Save PDF to a file
    pdf_file_path = "generated_resume.pdf"
    pdf.output(pdf_file_path)

    return pdf_file_path  # Return the path to the generated PDF
