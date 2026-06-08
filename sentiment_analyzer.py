import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from preprocess import preprocess_text

nltk.download("vader_lexicon")

sia = SentimentIntensityAnalyzer()

# polarity_scores -> sentiment scores
# neg -> negative score
# neu -> neutral score
# pos -> positive score
# compound -> overall sentiment score
def analyze_sentiment(text):
    score = sia.polarity_scores(text)
    compound = score['compound']
    if compound > 0.05:
        sentiment = "Positive"
    elif compound <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return sentiment, score

print("Train Success")
