from openai import OpenAI



# Dectect the intent of the user's input with the help of LLM  -> Smart Approach
def detect_intent_with_llm(user_input: str)-> str:
    client=OpenAI()
    response=client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant that detects the intent of the user's input. You will be given a user's input and you will need to return the intent of the user's input. The intent can be one of the following: destination, booking, explore, or other. The user's unput will be in the language of the user."},
            {"role": "user", "content": user_input}
        ],
        model="gpt-4o-mini"
    )


