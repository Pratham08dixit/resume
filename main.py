import os
import fitz  # PyMuPDF
from docx import Document
import streamlit as st
import json
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM
# from crewai_tools import SerperDevTool  # Temporarily disabled due to installation issues
# from langchain_google_genai import ChatGoogleGenerativeAI

# Load API Keys from .env
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# SERPER_API_KEY = os.getenv("SERPER_API_KEY")  # Temporarily disabled

if not GEMINI_API_KEY:
    st.error("Missing GEMINI_API_KEY in .env file")
    st.stop()

# os.environ["SERPER_API_KEY"] = SERPER_API_KEY  # Temporarily disabled

# Set environment variable for CrewAI
os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY

# Gemini LLM Setup - Using CrewAI's LLM class with correct provider format
llm = LLM(
    model="gemini/gemini-1.5-flash",
    temperature=0.3
)

# Resume Extraction Functions

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    return "\n".join(page.get_text() for page in doc)

def extract_text_from_docx(docx_file):
    document = Document(docx_file)
    return "\n".join(p.text for p in document.paragraphs)

def save_docx(text, output_path):
    doc = Document()
    for line in text.strip().splitlines():
        doc.add_paragraph(line)
    doc.save(output_path)

# Streamlit UI
st.title(" Resume Analyzer & Job Finder ")
#st.caption("Multi-agent AI system using CrewAI + Gemini")

uploaded_file = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])
#location = st.text_input("Preferred Job Location", value="New Delhi")
run_button = st.button("🚀 Analyze")

if run_button and uploaded_file :
    st.info("⏳ Processing your resume...")

    # Extract resume text
    if uploaded_file.name.endswith(".pdf"):
        resume_text = extract_text_from_pdf(uploaded_file)
    else:
        resume_text = extract_text_from_docx(uploaded_file)

    if not resume_text.strip():
        st.error("Could not extract text from resume.")
        st.stop()

    # Agents and Tasks with CrewAI

    # Feedback Agent
    resume_feedback = Agent(
        role="Professional Resume Advisor",
        goal="Give detailed feedback on resumes",
        backstory="Expert in resume analysis and improvement.",
        verbose=False,
        llm=llm
    )
    resume_feedback_task = Task(
        description=(
            "Analyze this resume and return ONLY a valid JSON object with exactly these fields:\n"
            "- sections_detected: array of strings\n"
            "- missing_sections: array of strings\n"
            "- well_written_sections: array of strings\n"
            "- quality_score: number between 0-100\n"
            "- suggestions: array of strings\n\n"
            "Resume:\n{resume}\n\n"
            "Return ONLY the JSON object, no other text or explanation."
        ),
        expected_output="Valid JSON object with the 5 required fields only.",
        agent=resume_feedback
    )

    # Resume Advisor Agent
    resume_advisor = Agent(
        role="Resume Rewriting Expert",
        goal="Improve resumes based on structured feedback",
        backstory="Polishes and optimizes resumes for impact.",
        verbose=False,
        llm=llm
    )
    resume_advisor_task = Task(
        description=(
            "Improve this resume based on feedback in context. Keep the candidate's experience intact "
            "but improve clarity, grammar, and formatting.\nResume:\n{resume}"
        ),
        expected_output="Improved resume as plain text.",
        context=[resume_feedback_task],
        agent=resume_advisor
    )

    # Job Researcher Agent (simplified version without web search)
    job_researcher = Agent(
        role="Job Research Expert",
        goal="Provide job search guidance based on a resume",
        backstory="Experienced in career guidance and job market analysis.",
        verbose=False,
        llm=llm
    )
    job_researcher_task = Task(
        description=(
            "Based on the improved resume, provide job search guidance including: "
            "1) Recommended job titles to search for, "
            "2) Top companies in the candidate's field, "
            "3) Key job boards and websites to use, "
            "4) Networking tips specific to their industry."
        ),
        expected_output="Structured job search guidance with specific recommendations.",
        context=[resume_advisor_task],
        agent=job_researcher
    )

    # Run CrewAI
    crew = Crew(
        agents=[resume_feedback, resume_advisor, job_researcher],
        tasks=[resume_feedback_task, resume_advisor_task, job_researcher_task],
        verbose=True
    )
    result = crew.kickoff(inputs={"resume": resume_text})

    # Display Output

    st.subheader("📊 Resume Feedback")
    try:
        # Try to parse JSON from the raw output
        raw_output = resume_feedback_task.output.raw.strip()

        # Remove any markdown code blocks if present
        if raw_output.startswith('```json'):
            raw_output = raw_output.replace('```json', '').replace('```', '').strip()
        elif raw_output.startswith('```'):
            raw_output = raw_output.replace('```', '').strip()

        feedback_data = json.loads(raw_output)
        st.json(feedback_data)

        # Display key metrics in a more user-friendly way
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Quality Score", f"{feedback_data.get('quality_score', 'N/A')}/100")
        with col2:
            st.metric("Sections Detected", len(feedback_data.get('sections_detected', [])))

    except Exception as e:
        st.warning("⚠️ Could not parse JSON feedback. Showing raw output:")
        st.text_area("Raw Feedback", resume_feedback_task.output.raw, height=200)
        st.error(f"Error details: {str(e)}")

    st.subheader("✅ Improved Resume")
    improved_resume = resume_advisor_task.output.raw.strip()
    st.text_area("Improved Resume", improved_resume, height=300)
    save_docx(improved_resume, "improved_resume.docx")
    with open("improved_resume.docx", "rb") as f:
        st.download_button("⬇️ Download Improved Resume", f, file_name="improved_resume.docx")

    st.subheader("💼 Job Search Guidance")
    st.markdown(job_researcher_task.output.raw.strip())
