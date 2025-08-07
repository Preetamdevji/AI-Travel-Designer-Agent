hotel_prompt="""
You are a helpful travel booking assistant.

Based on the user's request, generate 3 mock hotel options in JSON format.

Each hotel should include:
- Hotel name
- Hotel details
- Hotel category (e.g., 3-star, 5-star, boutique)
- Hotel rating and a brief review
- Hotel manager details (name, role)
- Prices in both USD and AED

Output format:
[
  {
    "name": "...",
    "details": "...",
    "category": "...",
    "rating": "4.5",
    "review": "...",
    "manager": {
      "name": "...",
      "role": "Manager"
    },
    "price": {
      "USD": 200,
      "AED": 735
    }
  },
  ...
]

User Request: {user_input}
"""
