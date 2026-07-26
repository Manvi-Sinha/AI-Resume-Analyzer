import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Create Lemmatizer
lemmatizer = WordNetLemmatizer()

# English Stop Words
stop_words = set(stopwords.words("english"))


def preprocess_text(text):
    """
    Cleans resume text for NLP processing.
    """

    # Convert to lowercase
    text = text.lower()

    # Remove special characters and numbers
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    # Split into words
    words = text.split()

    cleaned_words = []

    for word in words:

        if word not in stop_words:
            cleaned_words.append(
                lemmatizer.lemmatize(word)
            )

    return " ".join(cleaned_words)