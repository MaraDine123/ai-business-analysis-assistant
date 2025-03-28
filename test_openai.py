import openai
import os
from dotenv import load_dotenv

# Load your .env file
load_dotenv()

# Create OpenAI client using new v1.0+ syntax
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Send a chat message to GPT-3.5
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Explain Business Analysis in simple words."}
    ],
    temperature=0.7
)

# Print the result
print("\nAI Response:")
print(response.choices[0].message.content)
