import pandas as pd
from openai import OpenAI

# Initialize client with your API key
client = OpenAI(api_key="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")

# Load CSV
file_path = input("Enter CSV file path: ")
df = pd.read_csv(file_path)

print("\n--- Dataset Preview ---")
print(df.head())

# Convert dataset to string (for small datasets)
data_str = df.to_string()

print("\nYou can now ask questions about your dataset.")
print("Type 'exit' to stop.\n")

while True:
    question = input("Ask a question: ")

    if question.lower() == "exit":
        break

    prompt = f"""
    You are a data analyst. Answer the question based on this dataset:

    DATA:
    {data_str}

    QUESTION:
    {question}

    Provide a clear and concise answer.
    """

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )

    answer = response.output_text
    print("\nAnswer:", answer)
    print("\n-----------------------------\n")
