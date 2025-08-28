
from retriever import retriever
from generation import generate_text

def rag_query(query: str, max_new_tokens: int = 150) -> str:
    """
    Retrieve context from documents and generate an answer.
    """
    # Retrieve relevant documents
    results = retriever.retrieve(query)
    context = "\n".join([r.node.get_content() for r in results])
    
    # Truncate to prevent exceeding model max length
    max_context_chars = 1500
    context = context[:max_context_chars]

    # Build prompt for LLM
    answer_question_prompt = f""" 
    Use the following pieces of retrieved context to answer the question below.
    Use three to seven sentences maximum and keep the answer concise, while still giving depth.
    Only use information present in the context. If the answer is not found, respond with 'I don't know'.

    Context:
    {context}

    Question:
    {query}

    Answer:"""


    # Generate response
    return generate_text(answer_question_prompt, max_new_tokens=max_new_tokens)

# Test
if __name__ == "__main__":
    print(rag_query("Explain Retrieval-Augmented Generation in simple terms."))
