import re

# ----------------------------
# Text cleaning function
# ----------------------------
def clean_text(text):
    # Remove numbered references like [1], [23]
    text = re.sub(r'\[\d+\]', '', text)
    # Remove author citations like "J. Smith et al., ..."
    text = re.sub(r'\b[A-Z][a-z]+(?: [A-Z]\.)?(?: et al\.)?,.*', '', text)
    # Remove arXiv references
    text = re.sub(r'arXiv:\d+\.\d+', '', text)
    # Remove common publication markers
    text = re.sub(r'vol\.|abs/|preprint', '', text, flags=re.IGNORECASE)
    # Collapse multiple spaces/newlines
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

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

