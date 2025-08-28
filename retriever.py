
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# Load persisted index and create retriever
storage_context = StorageContext.from_defaults(persist_dir="storage")
embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
index = load_index_from_storage(storage_context, embed_model=embed_model)
retriever = index.as_retriever(similarity_top_k=3)
