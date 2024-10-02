
---

# Gen-AI Resume Builder & Career Advisor

The **AI Resume Builder & Career Advisor** is a Python-based application designed to generate professional resumes and provide personalized career advice using state-of-the-art language models. The application collects user input, generates tailored resumes, and offers career advice based on job market trends, skills, and user goals. The final output is provided in text format and exported as a PDF.

## Features
1. **AI-Generated Resume**: 
   - Automatically creates a professional resume using the user's input (name, education, work experience, skills, etc.).
   - Organizes information in a structured format, including summary, skills, education, and work experience.
   
2. **Personalized Career Advice**:
   - Offers career advice based on the provided user profile.
   - Suggests career paths, skills to develop, and emerging job market trends.

3. **PDF Export**:
   - Generates a downloadable PDF containing both the resume and the career advice.

## Tech Stack

- **Language Model**: LLaMA 3.1
- **Inference Engine & API keys**: GroqCloud
- **PDF Generation**: FPDF library for Python
- **User Input**: Streamlit Web interface

## File Structure

```
GenAI_Resume_CareerAdvisor/
├── chains.py          # Contains chain of prompts for resume and career advice generation
├── main.py            # Main script to run the application
├── query.py           # Handles querying of the language model for responses
├── response.py        # Handles formatting and response processing
├── utils.py           # Utility functions like PDF generation and text processing
├── portfolio.py       # Stores generated resumes and career advice for future use
├── requirements.txt   # List of dependencies
└── README.md          # Project documentation
```

### Key Files and Their Roles:

- **`main.py`**: Orchestrates the flow of the program, from collecting user inputs, invoking the language model, generating resumes, and career advice, to saving the results as a PDF.
- **`chains.py`**: Contains the chain logic for handling resume and career advice prompts. Helps build prompt templates for consistency.
- **`query.py`**: Manages interaction with the language model (LLaMA or ChatGroq), sending prompts and retrieving responses.
- **`response.py`**: Processes the responses from the language model, including formatting and refining the output.
- **`utils.py`**: Provides utility functions, including PDF generation, text formatting, and handling other supportive tasks.
- **`portfolio.py`**: Saves and manages previously generated resumes and career advice, allowing future retrieval and analysis.

## How to Use

### Prerequisites

1. Install Python 3.8 or above.
2. Install the necessary libraries by running the following command:
   ```bash
   pip install -r requirements.txt
   ```
   Or manually install the libraries:
   ```bash
   pip install pandas fpdf langchain_groq
   ```

3. Obtain an API key from your preferred LLM provider (e.g., ChatGroq or OpenAI) and replace it in the code.

### Running the Application

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/GenAI_Resume_CareerAdvisor.git
   cd GenAI_Resume_CareerAdvisor
   ```

2. **Run the Application**:
   ```bash
   python main.py
   ```

3. **Input the Required Information**:
   - You will be prompted to enter your name, email, education, work experience, skills, and career goals.
   - Example:
     ```
     Enter your name: John Doe
     Enter your email: john.doe@example.com
     Enter your education: B.Sc. in Computer Science
     Enter your work experience: 2 years as a Software Developer
     Enter your skills: Python, Machine Learning, Data Analysis
     Enter your career goals: To become a Data Scientist
     ```

4. **Output**:
   - The resume and career advice are generated and displayed in the terminal.
   - The generated resume and career advice are saved as a PDF (`generated_resume_and_advice.pdf`).

### Example Output

**Resume**:
```
Name: John Doe
Email: john.doe@example.com
Education: B.Sc. in Computer Science
Work Experience: 2 years as a Software Developer
Skills: Python, Machine Learning, Data Analysis
Career Goals: To become a Data Scientist
```

**Career Advice**:
```
Based on your skills and goals, we suggest pursuing a career path in data science. Developing expertise in deep learning and big data analysis will enhance your marketability. Job market trends show increasing demand for AI and data science professionals.
```

## Future Enhancements

- **Web Interface**: Build a simple web interface using Streamlit or Flask for users to interact with the tool visually.
- **Automated Job Search**: Integrate a job search API to provide real-time job suggestions along with career advice.

---

With this project, you'll have an intelligent assistant for generating personalized resumes and career advice, all in one place.

--- 
