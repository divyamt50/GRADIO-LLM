import os
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr

load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_BASE_URL = os.getenv("GROQ_BASE_URL")
GROQ_MODEL = os.getenv("GROQ_MODEL")
GRADIO_PASSWORD = os.getenv("GRADIO_PASSWORD")

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url=GROQ_BASE_URL
)

system_message = """
You are a helpful assistant for an Airline called FlightAI.
Give short, courteous answers, no more than 1 sentence.
Always be accurate. If you don't know the answer, say so.
"""

def chat(message, history):
    history = [{"role":h["role"], "content":h["content"]} for h in history]
    messages = [{"role":"system", "content":system_message}] + history + [{"role":"user", "content":message}]

    stream = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=messages,
        stream=True
    )
    
    response = ""
    
    for chunk in stream:
        response += chunk.choices[0].delta.content or ""
        yield response

gr.ChatInterface(fn=chat).launch()