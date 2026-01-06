import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Download VADER lexicon (only first time)
nltk.download('vader_lexicon')

# Load dataset
file_path = input("Enter your movie reviews CSV file path: ")
df = pd.read_csv(file_path)

print("\n--- Dataset Loaded ---")
print(df.head())

# Ensure column name
review_col = "review"
if review_col not in df.columns:
    raise ValueError("CSV must contain a column named 'review'")

# Initialize VADER
sia = SentimentIntensityAnalyzer()

# Function to classify sentiment
def get_sentiment(text):
    score = sia.polarity_scores(text)["compound"]
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis
df["sentiment"] = df["review"].astype(str).apply(get_sentiment)

print("\n--- Sentiment Classification Done ---")
print(df.head())

# Count sentiment categories
sentiment_counts = df["sentiment"].value_counts()
print("\nSentiment Counts:")
print(sentiment_counts)

# Plot pie chart
plt.figure(figsize=(6,6))
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct="%1.1f%%")
plt.title("Sentiment Distribution")
plt.show()

# Top 3 positive reviews
print("\n--- Top 3 Positive Reviews ---")
positive_reviews = df[df["sentiment"] == "Positive"].head(3)
print(positive_reviews["review"])

# Top 3 negative reviews
print("\n--- Top 3 Negative Reviews ---")
negative_reviews = df[df["sentiment"] == "Negative"].head(3)
print(negative_reviews["review"])

# Save final CSV
output_path = "sentiment_output.csv"
df.to_csv(output_path, index=False)
print(f"\nFinal CSV saved as {output_path}")
