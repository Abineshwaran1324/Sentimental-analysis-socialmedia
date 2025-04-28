import pandas as pd
from textblob import TextBlob
import seaborn as sns
import matplotlib.pyplot as plt

# Sample Tweets
tweets = [
    "I love this!",
    "This is terrible.",
    "Feeling happy today.",
    "I'm not sure how I feel.",
    "Life is hard."
]

df = pd.DataFrame(tweets, columns=["Tweet"])

def get_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment"] = df["Tweet"].apply(get_sentiment)
print(df)

# Visualize
sns.countplot(data=df, x="Sentiment")
plt.title("Sentiment Analysis")
plt.show()
