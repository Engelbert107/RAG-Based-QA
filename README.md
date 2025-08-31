# RAG-Based Question Answering from PDF

This project implements a Retrieval-Augmented Generation (RAG) pipeline that enables users to query PDF documents in natural language. Text is extracted and preprocessed from PDFs, embedded into a ChromaDB vector store, and retrieved chunks are combined with a lightweight LLM (TinyLlama) to generate concise, context-aware answers.

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

