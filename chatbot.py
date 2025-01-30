import openai
from config import OPENAI_API_KEY
from preprocess import clean_text

openai.api_key = OPENAI_API_KEY

def generate_response(user_input):
    """Generates a chatbot response using OpenAI GPT."""
    user_input = clean_text(user_input)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}],
            max_tokens=100
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return "Error: Unable to generate a response."
