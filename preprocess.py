import re
from nltk.corpus import stopwords

en_stopwords = stopwords.words('english')

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = ' '.join(word for word in text.split() if word not in en_stopwords)
    return text

# print(preprocess_text("Hello, World! This is a test for exam."))