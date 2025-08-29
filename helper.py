import re
import unicodedata
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download("stopwords")
nltk.download("wordnet")

# ----------------------------
# Text cleaning function
# ----------------------------

def clean_text(text: str, for_embeddings: bool = True) -> str:
    """
    Clean text for RAG pipeline.
    - for_embeddings=True: lowercased, stopwords removed, lemmatized
    - for_embeddings=False: cleaned for display/LLM input (keeps natural casing)
    """

    # Normalize unicode
    text = unicodedata.normalize("NFKC", text)

    # Remove references and author info
    text = re.sub(r'\[\d+\]', '', text)
    text = re.sub(r'\b[A-Z][a-z]+(?: [A-Z]\.)?(?: et al\.)?,.*', '', text)
    text = re.sub(r'arXiv:\d+\.\d+', '', text)
    text = re.sub(r'vol\.|abs/|preprint', '', text, flags=re.IGNORECASE)

    # Remove unwanted symbols
    text = re.sub(r'[^\w\s.,;:!?()-]', '', text)

    # Collapse whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    if for_embeddings:
        # Lowercase
        text = text.lower()

        # Remove stopwords
        stop_words = set(stopwords.words("english"))
        words = text.split()
        words = [w for w in words if w not in stop_words]

        # Lemmatize
        lemmatizer = WordNetLemmatizer()
        words = [lemmatizer.lemmatize(w) for w in words]

        text = " ".join(words)

    return text


# ----------------------------
# Reconstruct column text from words
# ----------------------------
def reconstruct_column(words):
    line_text = ""
    last_x1 = None
    for w in words:
        if last_x1 and (w['x0'] - last_x1) > 1:  # add space if gap detected
            line_text += " "
        line_text += w['text']
        last_x1 = w['x1']
    return line_text

