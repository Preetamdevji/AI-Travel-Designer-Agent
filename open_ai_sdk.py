from config import OPENAI_API_KEY,OPENAI_BASE_URL
from openai import AsyncOpenAI


external_client = AsyncOpenAI(
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_BASE_URL
)