import openai
from app.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_response(prompt):
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=500
    )
    return completion.choices[0].text.strip()

