import os
from openai import OpenAI
from dotenv import load_dotenv
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

system_prompt = "You are a very capable and humorous assistant"

def message_llama(prompt:str):
    messages = [{"role":"system", "content":system_prompt}, {"role":"user", "content":prompt}]

    stream = client.chat.completions.create(
        model= GROQ_MODEL,
        messages= messages,
        stream=True
    )

    reply = ""

    for chunk in stream:
        reply += chunk.choices[0].delta.content or ""
        yield reply

# print(ask("what time is it?"))


def shout(text):
    print(f"shout called with {text}")

    return text.upper()

message_input = gr.Textbox(label="Your message:", info="Enter a message to be shouted", lines=7)
message_output = gr.Textbox(label="Response:", lines=8)

view = gr.Interface(
    fn=message_llama,
    title="LLAMA", 
    inputs=[message_input], 
    outputs=[message_output], 
    examples=["hello", "howdy"], 
    flagging_mode="never"
    )
view.launch(inbrowser="True")