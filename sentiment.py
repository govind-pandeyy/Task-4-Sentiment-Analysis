from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load dataset
df = pd.read_csv("reviews.csv")
# Sentiment Function
def get_sentiment(text):
    polarity = TextBlob(str(text)).sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"
# Predict Sentiment
df["Predicted_Sentiment"] = df["Text"].apply(get_sentiment)
# Sentiment Counts
sentiment_counts = df["Predicted_Sentiment"].value_counts()
print("\nSentiment Distribution:")
print(sentiment_counts)
# Save Results
df.to_csv("reviews_with_sentiment.csv", index=False)

# Bar Chart
plt.figure(figsize=(8,5))
sns.barplot(
    x=sentiment_counts.index,
    y=sentiment_counts.values
)
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("sentiment_distribution.png")
plt.show()

# Pie Chart
plt.figure(figsize=(6,6))
plt.pie(
    sentiment_counts.values,
    labels=sentiment_counts.index,
    autopct="%1.1f%%"
)
plt.title("Sentiment Analysis Results")
plt.savefig("sentiment_pie_chart.png")
plt.show()
print("\nAnalysis Completed Successfully!")