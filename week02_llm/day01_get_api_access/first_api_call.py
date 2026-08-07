import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()                                    
client = Groq(api_key=os.getenv("GROQ_API_KEY")) 

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": "Explain federated learning in 2 sentences."}
    ],
)

print(response.choices[0].message.content)

print("---")
print("Model used:", response.model)
print("Tokens used:", response.usage.total_tokens)
print("Finish reason:", response.choices[0].finish_reason)