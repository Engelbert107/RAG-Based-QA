# RAG-Based Question Answering from PDF

This project implements a Retrieval-Augmented Generation (RAG) pipeline for querying PDF documents in natural language. PDF text is extracted, cleaned, and embedded into a ChromaDB vector store. At query time, semantically relevant chunks are retrieved and passed to a lightweight LLM (TinyLlama), which generates accurate, context-aware answers grounded in the source documents.

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

