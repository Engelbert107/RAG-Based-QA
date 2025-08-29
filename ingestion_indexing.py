
import nltk
import glob
import chromadb
import pdfplumber
from nltk.tokenize import sent_tokenize
from llama_index.core import Document, VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore
from helper import clean_text, reconstruct_column


# ----------------------------
# Download punkt tokenizer for sentence splitting
# ----------------------------
nltk.download("punkt")

# ----------------------------
# PDF files folder
# ----------------------------
pdf_files = glob.glob("data/*.pdf")
documents = []

# ----------------------------
# Extract text and split into 3-sentence chunks
# ----------------------------
for pdf_path in pdf_files:
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            # Crop left/right columns
            left_words = page.crop((0, 0, page.width/2, page.height)).extract_words()
            right_words = page.crop((page.width/2, 0, page.width, page.height)).extract_words()
            # Reconstruct text for each column
            left_text = reconstruct_column(left_words)
            right_text = reconstruct_column(right_words)
            # Combine columns in reading order
            combined_text = left_text + "\n" + right_text
            # Clean text
            cleaned_text = clean_text(combined_text, for_embeddings=True)
            # Split into sentences
            sentences = sent_tokenize(cleaned_text)
            # Chunk by 3 sentences
            chunk_size = 3
            for i in range(0, len(sentences), chunk_size):
                chunk_text = " ".join(sentences[i:i+chunk_size])
                chunk_text = clean_text(chunk_text)  # clean references
                if chunk_text:  # skip empty chunks
                    documents.append(Document(text=chunk_text))

print(f"\nCreated {len(documents)} sentence-level chunks from {len(pdf_files)} PDFs.\n")

# ----------------------------
# Embeddings
# ----------------------------
embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

# ----------------------------
# ChromaDB setup
# ----------------------------
chroma_client = chromadb.PersistentClient(path="chroma_db")
chroma_collection = chroma_client.get_or_create_collection("docs")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

# ----------------------------
# Build & persist index
# ----------------------------
index = VectorStoreIndex.from_documents(documents, embed_model=embed_model, vector_store=vector_store)
index.storage_context.persist("storage")

print("\nIndex built & persisted!\n")
