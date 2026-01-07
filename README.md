🌐 Growfinix Data Science Internship

📌 Overview
This repository contains all five tasks completed during the Growfinix Data Science Internship.
Each task demonstrates practical applications of data science, machine learning, and AI integration, culminating in a deployable project.

🗂️ Tasks Completed
Task 1: Titanic Survival Analysis 
Loaded Titanic dataset from Kaggle/Seaborn.

Cleaned missing values (Age, Cabin) and encoded categorical features.

Visualized survival trends by gender, class, age group, family size, and fare.

Applied .groupby() and pivot tables for deeper insights.

Exported cleaned dataset and charts.

Bonus: Interactive plots with Plotly.


Task 2: House Price Prediction 
Downloaded housing dataset with features like area, bedrooms, and price.

Cleaned null values and encoded categorical fields.

Visualized price vs area/rooms using scatter plots.

Trained Linear Regression model with train/test split.

Evaluated using MAE, MSE, and R² score.

Saved trained model with joblib.

Built function for new input predictions.

Bonus: Simple Streamlit UI.


Task 3: ChatGPT for Data Q&A 
Uploaded CSV datasets (student marks, sales, etc.).

Extracted dataset info and converted tables to string for small data.

Queried a GPT-style API for natural language answers (note: OpenAI API requires a paid subscription, so I used [Groq API / alternative] for demonstration).

Parsed responses and displayed in console/web app.

Added predefined question buttons and logging.

Handled large datasets with summarization.

Exported Q&A as PDF report.

Bonus: Streamlit integration for user-uploaded CSVs and custom queries.



Task 4: Movie Review Sentiment Analysis 
Loaded IMDB/custom CSV of reviews.

Cleaned text (stopwords, punctuation, lowercasing).

Applied TextBlob/VADER for sentiment polarity.

Classified reviews as Positive, Negative, Neutral.

Visualized sentiment distribution with pie/bar charts.

Displayed top 3 positive and negative reviews.

Saved final results to CSV.

Bonus: HuggingFace Transformers for advanced sentiment analysis.



Task 5: AI-Powered Resume Feedback Tool 
Allowed users to upload resumes (PDF/DOCX).

Extracted text using PyMuPDF/docx libraries.

Preprocessed and parsed key sections.

Queried GPT for resume feedback (skills, summary, missing sections).

Generated score and improvement tips.

Displayed formatted feedback and logged results.

Bonus: Compared with ideal resume samples, GPT-4 scoring out of 100.

⚙️ Tech Stack
Languages: Python

Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, TextBlob, VADER, HuggingFace, Streamlit

APIs: OpenAI API

Tools: GitHub, VS Code, Jupyter Notebook

🚀 How to Run
bash
# Clone the repository
git clone https://github.com/anumita-14/growfinix-internship.git
cd growfinix-internship

# Install dependencies
pip install -r requirements.txt

# Run Jupyter notebooks
jupyter notebook

# Launch Streamlit apps
streamlit run Task3_app.py
streamlit run Task5_resume_feedback.py

📜 Certificate Requirement
This repository serves as proof of completion for the Growfinix internship.
All tasks are documented with code, outputs, and conclusions.