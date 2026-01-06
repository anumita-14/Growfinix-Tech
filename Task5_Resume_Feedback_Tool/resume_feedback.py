import fitz  # PyMuPDF
import docx
import os
from datetime import datetime
from groq import Groq

# 1. Extract text from PDF
def extract_text_from_pdf(file_path):
    text = ""
    pdf = fitz.open(file_path)
    for page in pdf:
        text += page.get_text()
    return text


# 2. Extract text from DOCX
def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join(para.text for para in doc.paragraphs)


# 3. Clean text
def clean_text(text):
    return text.replace("\n", " ").strip()


# 4. AI-based feedback using Groq
def ai_feedback(text):
    try:
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))

        prompt = f"""
You are an expert resume reviewer.

Analyze the following resume text and provide:
1. Professional summary
2. Strengths
3. Weaknesses or missing sections
4. Improvement suggestions
5. Score out of 100
6. Improved rewritten resume

Resume Text:
{text}
"""

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error generating feedback: {e}"


# 5. Log feedback
def log_feedback(text):
    os.makedirs("logs", exist_ok=True)
    with open("logs/feedback_log.txt", "a", encoding="utf-8") as f:
        f.write(f"\n\n--- Feedback on {datetime.now()} ---\n")
        f.write(text)


# MAIN PROGRAM
file_path = input("Enter your resume file path (PDF or DOCX): ")

if file_path.lower().endswith(".pdf"):
    extracted = extract_text_from_pdf(file_path)
elif file_path.lower().endswith(".docx"):
    extracted = extract_text_from_docx(file_path)
else:
    raise ValueError("Unsupported file type. Use PDF or DOCX.")

cleaned = clean_text(extracted)

print("\nGenerating AI-powered feedback... Please wait...\n")

ai_result = ai_feedback(cleaned)

print("\n--- AI RESUME FEEDBACK ---\n")
print(ai_result)

log_feedback(ai_result)

print("\nFeedback saved to logs/feedback_log.txt")
