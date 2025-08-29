
from retriever import retriever
from generation import generate_text
# from helper import clean_text, truncate_by_tokens

def rag_query(query: str, max_new_tokens: int = 256) -> str:
    """
    Retrieve context from documents and generate an answer.
    """
    # Retrieve relevant documents
    results = retriever.retrieve(query)
    context = "\n".join([r.node.get_content() for r in results])
    
    # # Clean for LLM input (keep original meaning/case)
    # context = clean_text(context, for_embeddings=False)
    
    # # Truncate to prevent exceeding model max length
    # max_context_chars = 2000
    # context = context[:max_context_chars]
    
    # Limit number of sentences 
    sentences = context.split(". ")  # simple sentence split
    max_sentences = 5
    context = ". ".join(sentences[:max_sentences])

    # Truncate by tokens to fit model
    # context_for_llm = truncate_by_tokens(context, max_tokens=2048)

    # Build prompt for LLM
    answer_question_prompt = f"""
    You are a knowledgeable, helpful assistant. Use the following retrieved context to answer the user's question accurately and concisely.

    Guidelines:
    - Always answer based on the context only. If the answer is not found in the context, respond with "I don't know."
    - Limit your answer strictly to 3 to 5 sentences. 
    - Do not write more than 5 sentences under any circumstances.
    - Be respectful, professional, and human-like in tone.
    - Avoid giving speculative or unsafe advice.
    - Do not introduce unrelated topics or make assumptions beyond the provided context.
    - You may ask **one follow-up question at a time** to clarify the user's needs, but only when it helps provide a correct answer.
    - Avoid long explanations or multiple questions at once.
    - Format your answer for readability and ease of understanding.
    
    Context:
    {context}

    User's Question:
    {query}

    Answer:"""

    # Generate response
    return generate_text(answer_question_prompt, max_new_tokens=max_new_tokens)


# Test
if __name__ == "__main__":
    question = "Explain Retrieval-Augmented Generation in simple terms."
    answer = rag_query(question)
    print(answer)
