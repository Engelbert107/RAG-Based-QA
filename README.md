# RAG-Based Question Answering from PDF

This project implements a Retrieval-Augmented Generation (RAG) pipeline for querying PDF documents in natural language. PDF text is extracted and preprocessed, then embedded into a ChromaDB vector store. At query time, relevant chunks are retrieved and combined with a lightweight LLM (TinyLlama) to generate accurate, context-aware answers.

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

