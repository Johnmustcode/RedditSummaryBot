import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # load .env file in current library

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
)

stream = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-4",
    stream = True,
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")