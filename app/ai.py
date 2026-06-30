import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("GROQ_API_KEY"),
                base_url="https://api.groq.com/openai/v1")


def get_ai_response(conversation_history):
    try:
        response = client.chat.completions.create(
            model=os.getenv("GROQ_MODEL_NAME"),
            messages=conversation_history

        )
    except Exception :
        return "Sorry, But At This Point Unable To Connect To AI"
    return  response.choices[0].message.content
