from google import genai
from google.genai import types
from dotenv import load_dotenv

import os

load_dotenv()
client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))
sys_instruct="Nama kamu adalah JoniBot. Kamu adalah asisten kesehatan yang ingin berada di sebuah aplikasi \
    yang menjaga pola makan dan pola hidup bernama NutriChat. Kamu disini memberikan informasi \
    untuk pengguna agar mereka dapat memilih makanan yang tepat dan sehat. "

categories: list[str] = [
    "Pertanyaan tentang gizi atau kesehatan yang tidak memerlukan informasi pengguna",      #0

    "Pertanyaan tentang gizi atau kesehatan yang memerlukan informasi pengguna",            #1

    "Memberikan informasi apa yang mereka makan",                                           #2

    "Meminta saran makanan untuk dikonsumsi",                                               #3

    "Memberikan informasi pola hidup seperti rutinitas, kondisi medis, \ "                  #4
    "preferensi makanan, alergi, atau lainnya",

    "Hal lainnya"                                                                           #else
]

def get_prompt_type(prompt: str) -> str:
    prompt_instruct = "Terdapat pilihan-pilihan sebagai berikut " \
        + ", ".join(categories) \
        + " Dari semua pilihan tersebut, pilihan mana yang mungkin dimaksud dari prompt pengguna ?\
        Mohon jawab dengan hanya pilihan yang diberikan dengan kata yang persis!"
    
    return generate_response(prompt, prompt_instruct)

def generate_response(prompt: str, instruction: str = "") -> str:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction=sys_instruct + instruction),
        contents=[prompt])
    
    return response.text

def answer(prompt: str) -> str:
    prompt_type = get_prompt_type(prompt)
    
    if (prompt_type == categories[0]):
        return generate_case_0(prompt)
    elif (prompt_type == categories[1]):
        return generate_case_1(prompt)
    elif (prompt_type == categories[2]):
        return generate_case_2(prompt)
    elif (prompt_type == categories[3]):
        return generate_case_3(prompt)
    elif (prompt_type == categories[4]):
        return generate_case_4(prompt)
    else:
        return generate_case_else(prompt)

def generate_case_0 (prompt: str) -> str:
    instruction = "Berikan pengguna jawaban yang berdasarkan fakta dan relevan terkait gizi dan " \
    "kesehatan secara umum"
    return generate_response(prompt, instruction)

def generate_case_1 (prompt: str) -> str:
    instruction = "Berikan pengguna jawaban yang berdasarkan fakta dan relevan terkait gizi dan " \
    "kesehatan secara umum"
    return generate_response(prompt, instruction)

def generate_case_2 (prompt: str) -> str:
    instruction = "Berikan pengguna jawaban yang berdasarkan fakta dan relevan terkait gizi dan " \
    "kesehatan secara umum"
    return generate_response(prompt, instruction)

def generate_case_3 (prompt: str) -> str:
    instruction = "Berikan pengguna jawaban yang berdasarkan fakta dan relevan terkait gizi dan " \
    "kesehatan secara umum"
    return generate_response(prompt, instruction)

def generate_case_4 (prompt: str) -> str:
    instruction = "Berikan pengguna jawaban yang berdasarkan fakta dan relevan terkait gizi dan " \
    "kesehatan secara umum"
    return generate_response(prompt, instruction)

def generate_case_5 (prompt: str) -> str:
    instruction = "Berikan pengguna jawaban yang berdasarkan fakta dan relevan terkait gizi dan " \
    "kesehatan secara umum"
    return generate_response(prompt, instruction)

def generate_case_else (prompt: str) -> str:
    instruction = "Apapun pertanyaannya, jawab dengan penjelasan bahwa kamu hanya dapat membantu " \
    "pada bidang gizi dan kesehatan. Jawaban lain yang tidak berhubungan tidak bisa kamu bantu."
    return generate_response(prompt, instruction)

if __name__ == "__main__":
    prompt = input("> ")
    print(answer(prompt))