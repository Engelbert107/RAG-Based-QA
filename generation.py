
import torch
from transformers import pipeline
# from helper import truncate_by_tokens

# Text-generation pipeline using TinyLlama (CPU)
pipe = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    device=-1,                  # -1 = always use CPU
    torch_dtype=torch.float32    # CPU-safe dtype
)


def generate_text(prompt: str, max_new_tokens: int = 256) -> str:
    """
    Generate text from a given prompt using TinyLlama.
    """
    outputs = pipe(
        prompt,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        temperature=0.1,
        top_p=0.95
    )
    return outputs[0]["generated_text"]


# def generate_text(prompt: str, max_new_tokens: int = 150) -> str:
#     """
#     Generate text from a given prompt using TinyLlama, handling long prompts safely.
#     """
#     # Truncate prompt to prevent exceeding model max length
#     safe_prompt = truncate_by_tokens(prompt, max_tokens= 2048)
    
#     outputs = pipe(
#         safe_prompt,
#         max_new_tokens=max_new_tokens,
#         do_sample=True,
#         temperature=0.1,
#         top_p=0.95
#     )
#     return outputs[0]["generated_text"]

