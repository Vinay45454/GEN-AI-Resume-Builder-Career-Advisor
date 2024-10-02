from langchain_core.prompts import PromptTemplate
from gener import get_llm 
def get_career_advice(user_profile):
    llm = get_llm()
    
    advice_prompt = PromptTemplate.from_template(
        """
        ### USER PROFILE:
        {profile}
        
        ### INSTRUCTION:
        Provide career advice based on the user profile above.
        Include:
        - Suggested Career Paths
        - Skills to Develop
        - Job Market Trends
        Format the output clearly with headings and bullet points for readability.
        """
    )

    advice_chain = advice_prompt | llm
    advice_response = advice_chain.invoke(input={"profile": user_profile})

    # Format the career advice for better presentation
    formatted_advice = format_advice_content(advice_response.content)
    
    return formatted_advice  # Return the formatted advice content

def format_advice_content(advice_content):
    # Format the generated advice content into sections
    formatted_content = []

    # Assume the response contains sections separated by new lines
    sections = advice_content.split("\n")

    for section in sections:
        if section.strip():  # Skip empty lines
            formatted_content.append(section.strip())

    # Joining formatted content with double new lines for separation
    return "\n\n".join(formatted_content)
