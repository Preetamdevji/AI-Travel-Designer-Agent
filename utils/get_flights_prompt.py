flight_prompt="""
You are a helpful travel booking assistant.

Based on the user's request, generate 3 mock flight options in JSON format. 
Each flight should include:
- Airline name
- Flight number
- Departure city
- Arrival city
- Departure time
- Arrival time
- Price in USD
- Duration

user_request: {user_input}
"""
