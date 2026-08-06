import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()                                    # reads the .env file
client = Groq(api_key=os.getenv("GROQ_API_KEY")) # your key, pulled safely

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": "Explain what an API is in one sentence."}
    ],
)

print(response.choices[0].message.content)