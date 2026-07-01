import os
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr

load_dotenv

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_BASE_URL = os.getenv("GROQ_BASE_URL")
GROQ_MODEL = os.getenv("GROQ_BASE_URL")
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
    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=messages
    )

    if response.choices[0].finish_reason == "tool_calls":
        message = response.choices[0].message
        response = handle_tool_call(message)
        messages.append(message)
        messages.append(response)
        response = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=messages
        )
    
    return response.choices[0].message.content


def handle_tool_call(message):
    tool_call = message.tool_calls[0]
    if tool_call.function.name == "get_ticket_price":
        arguments = json.loads(tool_call.function.arguments)
        city = arguments.get("destination_city")
        price_details = get_ticket_price(city)
        response = {
            "role":"tool",
            "content":price_details,
            "tool_call_id":tool_call.id
        }
    return response

gr.ChatInterface(fn=chat).launch(inbrowser=True)