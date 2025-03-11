from google import genai
from google.genai import types
from dotenv import load_dotenv

import os

load_dotenv()
client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))
sys_instruct="You are a health assistant that recommends healthy food for me but you're not too restrictive. Please answer like a regular person with 2 or 3 sentences as if we're chatting"

def generate_response(prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction=sys_instruct),
        contents=[prompt])
    
    return response.text

if __name__ == "__main__":
    prompt = input("> ")
    print(generate_response(prompt))