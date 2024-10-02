from langchain_groq import ChatGroq


llm = ChatGroq(
    temperature=0,
    groq_api_key='Enter your API keys', 
    model_name="llama-3.1-70b-versatile"
)

def get_llm():
    return llm
