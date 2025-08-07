from openai import OpenAI
from utils.get_hotels_prompt import hotel_prompt


def suggest_hotels(user_input: str):
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role":"system", "content": "You generate structured mock for hotels with json format"},
            {"role":"user", "content": hotel_prompt.format(user_input=user_input)}
        ],
        temperature=0.7
    )

    return response['choices'][0]['message']['content']