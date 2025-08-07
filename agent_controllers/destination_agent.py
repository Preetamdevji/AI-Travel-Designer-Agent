from openai import OpenAI
from utils.get_destination import destination_prompt
class DestinationAgent:
    
    def find_places(user_input: str):
        client = OpenAI()
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role":"system", "content": "You generate destination suggestions in JSON."},
                {"role":"user", "content": destination_prompt.format(user_input=user_input)}
            ],
            temperature=0.7
        )
        
        return response.choices[0].message.content



