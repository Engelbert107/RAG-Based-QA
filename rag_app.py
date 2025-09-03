import chainlit as cl
from rag_pipeline import rag_query
from generation import pipe  # access Hugging Face pipeline directly

@cl.on_chat_start
async def start():
    await cl.Message(
        content="👋 Hi! I'm your RAG-powered assistant."
    ).send()

@cl.on_message
async def main(message: cl.Message):
    user_query = message.content.strip()

    # Use Chainlit's streaming
    msg = cl.Message(content="")
    await msg.send()

    # Generate tokens step by step
    generator = pipe(
        rag_query(user_query, max_new_tokens=50),
        max_new_tokens=150,
        do_sample=True,
        temperature=0.1,
        top_p=0.95,
        return_full_text=False
    )

    for chunk in generator:
        token = chunk["generated_text"]
        await msg.stream_token(token)

    await msg.update()





# import chainlit as cl
# from rag_pipeline import rag_query  

# @cl.on_chat_start
# async def start():
#     await cl.Message(
#         content="👋 Hi! I'm your RAG-powered assistant. Ask me anything, and I'll answer based on the knowledge base."
#     ).send()

# @cl.on_message
# async def main(message: cl.Message):
#     user_query = message.content.strip()
    
#     # Call your RAG pipeline
#     answer = rag_query(user_query, max_new_tokens=256)

#     # Send response back to user
#     await cl.Message(content=answer).send()
