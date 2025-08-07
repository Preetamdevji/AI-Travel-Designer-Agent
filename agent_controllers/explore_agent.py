from openai import OpenAI
from utils.get_explore_attraction import explore_prompt


class ExploreAgent:
    def find_places(destination: str, interest: str = "food,culture,adventure"):
        client = OpenAI()
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role":"system", "content": "You generate structured mock explore data in JSON format."},
                {"role":"user", "content": explore_prompt.format(destination=destination, interest=interest)}
            ],
            temperature=0.7
        )
        
        return response.choices[0].message.content