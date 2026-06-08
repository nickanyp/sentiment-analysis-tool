import pandas as pd

from preprocess import preprocess_text
from sentiment_analyzer import analyze_sentiment

df = pd.read_csv('sentiment.csv', encoding='iso-8859-1')
df = df.dropna(subset=['text'])

df['clean_text'] = df['text'].apply(preprocess_text)
df['predict_sentiment'] = df['clean_text'].apply(lambda x: analyze_sentiment(x)[0])

df.to_csv(
    "results.csv",
    index=False
)

print(df[['text', 'predict_sentiment']])