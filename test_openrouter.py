import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

response = client.chat.completions.create(
    model="gryphe/mythomax-l2-13b",  # You can also try openchat/openchat-3.5
    messages=[{"role": "user", "content": "What is Business Analysis?"}],
    temperature=0.7
)

print(response.choices[0].message.content)
