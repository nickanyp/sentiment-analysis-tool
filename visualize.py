import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results.csv")

counts = df["sentiment"].value_counts()

counts.plot(kind="bar")

plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")

plt.show()