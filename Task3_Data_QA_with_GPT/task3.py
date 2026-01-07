import pandas as pd
import os
from datetime import datetime
from groq import Groq
from fpdf import FPDF

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# --- Step 1: Load CSV ---
file_path = input("Enter CSV file path: ")
df = pd.read_csv(file_path)

# --- Step 2: Create folders ---
os.makedirs("logs", exist_ok=True)
os.makedirs("reports", exist_ok=True)

# --- Step 2: Basic dataset info ---
print("\n--- Dataset Info ---")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
print(f"Column Names: {list(df.columns)}")
print("\nSample Data:")
print(df.head())

# --- Step 3 & 9: Handle large datasets ---
if df.shape[0] > 50:
    data_context = df.describe().to_string()
    context_note = "Dataset summarized using statistics."
else:
    data_context = df.to_string()
    context_note = "Full dataset used."

print(f"\nℹ️ {context_note}\n")

# --- Step 8: Initialize Q&A log ---
qa_history = []

# Optional predefined questions (Step 7)
predefined_questions = [
    "Which product sold the most?",
    "Top student in Math?",
    "Total sales this month?",
    "Average marks of students?"
]

print("Ask questions about the dataset (type 'exit' to finish)\n")
print("You can also choose a predefined question by number:")
for i, pq in enumerate(predefined_questions, 1):
    print(f"{i}. {pq}")
print("-" * 40)

while True:
    question = input("Question: ")

    if question.lower() == "exit":
        break
    # Handle numeric selection for predefined questions
    if question.isdigit() and 1 <= int(question) <= len(predefined_questions):
        question = predefined_questions[int(question) - 1]

    # --- Step 5: Send prompt to Groq ---
    prompt = f"""
You are a data analyst.

DATA:
{data_context}

QUESTION:
{question}

Answer clearly in natural language.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response.choices[0].message.content

    # --- Step 6: Show answer ---
    print("\nAnswer:", answer)
    print("-" * 40)

    # --- Step 8: Log Q&A ---
    qa_history.append((question, answer))
    with open("logs/qa_log.txt", "a", encoding="utf-8") as f:
        f.write(f"\n[{datetime.now()}]\nQ: {question}\nA: {answer}\n")

# --- Step 10: Export Q&A to PDF ---
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=11)
pdf.cell(0, 10, "Dataset Q&A Report", ln=True)

for q, a in qa_history:
    pdf.multi_cell(0, 8, f"\nQ: {q}\nA: {a}")

pdf.output("reports/qa_report.pdf")

print("\n✅ Q&A saved in logs/qa_log.txt")
print("✅ PDF report generated in reports/qa_report.pdf")
