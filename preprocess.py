import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

def clean_text(text):
    """Cleans and normalizes user input text."""
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # Remove special characters
    words = text.split()
    words = [word for word in words if word not in stopwords.words("english")]
    return " ".join(words)
