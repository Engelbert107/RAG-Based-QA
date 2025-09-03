# RAG-Based Question Answering from PDF

This project makes it easy to ask questions about PDF documents and get clear, reliable answers. The system reads and processes the text from PDFs, stores it in a searchable database, and uses a small AI model (TinyLlama) to provide answers that stay relevant to the document’s content.

## 🔄 How It Works

```mermaid
flowchart TD
    A[📄 PDF Document] --> B[🔍 Text Extraction & Cleaning]
    B --> C[📦 Embedding with HuggingFace]
    C --> D[🗂️ Store in ChromaDB]
    E[❓ User Query] --> F[🔎 Retrieve Relevant Chunks from ChromaDB]
    F --> G[🤖 TinyLlama LLM]
    D --> F
    G --> H[✅ Context-Aware Answer]

