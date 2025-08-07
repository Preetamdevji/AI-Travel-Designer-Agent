from openai import OpenAI
from utils.get_flights_prompt import flight_prompt


def get_flights(user_input: str):
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You generate structured mock flight data with json format."},
            {"role": "user", "content": flight_prompt.format(user_input=user_input)}
        ],
        temperature=0.7   #creativity controls -> temperature is take float value
    )

    return response['choices'][0]['message']['content']