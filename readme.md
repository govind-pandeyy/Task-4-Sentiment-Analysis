#  Task 4: Sentiment Analysis using Python

## Project Overview

This project performs Sentiment Analysis on customer reviews using Natural Language Processing (NLP).

The TextBlob library is used to analyze review text and classify sentiments into:

- Positive
- Negative
- Neutral

Visualizations are created to understand the sentiment distribution.

---

## Objectives

- Analyze customer review sentiments
- Classify text into positive, negative, or neutral categories
- Visualize sentiment distribution
- Extract insights from textual data

---

## Technologies Used

- Python
- Pandas
- TextBlob
- Matplotlib
- Seaborn

---

## Dataset

The dataset contains customer reviews stored in:

reviews.csv

Main column used:

- Text

---

## Methodology

### Data Loading
Load customer reviews using Pandas.

### Sentiment Analysis
Use TextBlob polarity scores:

- Polarity > 0 → Positive
- Polarity < 0 → Negative
- Polarity = 0 → Neutral

### Visualization
Generate:

- Sentiment Distribution Bar Chart
- Sentiment Distribution Pie Chart

---

## Output

### Sentiment Results

Each review receives a predicted sentiment label.

Example:

| Review | Predicted Sentiment |
|----------|----------|
| Great product | Positive |
| Bad quality | Negative |
| Average item | Neutral |

---

## Visualizations

### 1. Sentiment Distribution

Displays count of Positive, Negative, and Neutral reviews.

### 2. Sentiment Pie Chart

Shows percentage share of each sentiment category.

---

## How to Run

Install dependencies:

```bash
pip install pandas matplotlib seaborn textblob
```

Run:

```bash
python sentiment.py
```

---

## Project Structure

```text
Task-4-Sentiment-Analysis/
│
├── reviews.csv
├── sentiment.py
├── sentiment_results.csv
├── sentiment_distribution.png
├── sentiment_pie_chart.png
└── README.md
```

---

## Key Insights

- Positive reviews indicate customer satisfaction.
- Negative reviews reveal potential improvement areas.
- Neutral reviews provide balanced feedback.
- Sentiment analysis helps businesses understand customer opinions quickly.

---

## Author

Govind Pandey

BCA Student | Aspiring Data Analyst
