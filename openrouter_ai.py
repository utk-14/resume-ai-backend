# import openai

# # Set OpenRouter API key and base URL
# import os
# from dotenv import load_dotenv
# load_dotenv()
# openai.api_key = os.getenv("OPENROUTER_API_KEY")

# # openai.api_key = "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"
# openai.base_url = "https://openrouter.ai/api/v1"

# client = openai.OpenAI(
#     api_key=openai.api_key,
#     base_url=openai.base_url,
# )

# def generate_questions(skills: list) -> list:
#     prompt = f"Generate 5 technical interview questions for a candidate skilled in: {', '.join(skills)}"

#     try:
#         response = client.chat.completions.create(
#             model="meta-llama/llama-3.3-8b-instruct:free",
#             messages=[
#                 {"role": "system", "content": "You are a helpful AI career assistant."},
#                 {"role": "user", "content": prompt}
#             ]
#         )
#         answer = response.choices[0].message.content
#         return [line.strip() for line in answer.strip().split("\n") if line.strip()]
    
#     except Exception as e:
#         print("❌ OpenRouter API Error:\n", e)
#         return ["Error occurred while generating questions."]
# openrouter_ai.py
# openrouter_ai.py

import os
import httpx
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

def generate_questions(skills: list) -> list:
    """
    Generate 5 technical interview questions for a candidate with given skills.
    """
    prompt = f"Generate 5 technical interview questions for a candidate skilled in: {', '.join(skills)}"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "http://localhost",  # You can change this to your website domain
        "X-Title": "Resume AI"
    }

    json_data = {
        "model": "meta-llama/llama-3.3-8b-instruct:free",
        "messages": [
            {"role": "system", "content": "You are a helpful AI career assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = httpx.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=json_data)
        response.raise_for_status()
        result = response.json()
        answer = result["choices"][0]["message"]["content"]
        return [line.strip() for line in answer.strip().split("\n") if line.strip()]
    
    except Exception as e:
        print("❌ OpenRouter API Error:\n", e)
        return ["Error occurred while generating questions."]
