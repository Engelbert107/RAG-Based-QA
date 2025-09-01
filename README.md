# RAG-Based Question Answering from PDF

This project enables users to ask natural-language questions about PDF documents and receive clear, relevant answers. It implements a Retrieval-Augmented Generation (RAG) pipeline where text is extracted and preprocessed from PDFs, embedded into a ChromaDB vector store, and at query time, the most relevant chunks are retrieved and combined with a lightweight LLM (TinyLlama) to produce accurate, context-aware responses.

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

