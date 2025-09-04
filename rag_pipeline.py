
from retriever import retriever
from generation import generate_stream



def rag_query(query: str, max_new_tokens: int = 256, stream: bool = False):
    """
    Retrieve context from documents and generate an answer.
    If stream=True, returns a generator that yields tokens.
    """
    # Retrieve relevant documents
    results = retriever.retrieve(query)
    context = "\n".join([r.node.get_content() for r in results]) 

    # Build prompt for LLM
    prompt = f"""
    You are a concise, accurate assistant. Answer questions strictly using the retrieved context.

    Guidelines:
    - Always prioritize factual accuracy over fluency.
    - If the answer is not in the context, respond only with: "I don't know."
    - Keep answers short: 3–5 sentences max.
    - Avoid repetition, vague phrases, or generic explanations.
    - Do not contradict context or introduce false claims.
    - If the user asks about concepts beyond the context, say: "I don't know."
    - Format your answer for readability and ease of understanding.
    
    Context:
    {context}

    User's Question:
    {query}

    Answer:"""

    if stream:
        return generate_stream(prompt, max_new_tokens=max_new_tokens)
    else:
        # Fallback to normal generation
        return "".join(generate_stream(prompt, max_new_tokens=max_new_tokens))



# # Test
# if __name__ == "__main__":
#     question = "Explain Retrieval-Augmented Generation in simple terms."
#     answer = rag_query(question)
#     print(answer)
