import requests

# POST requests + sending data (the LLM-shaped one):

# We'll use a free testing API (httpbin.org) that echoes back whatever you send, so you can see the mechanics clearly:

payload = {
    "model": "claude",
    "prompt": "Explain neural networks",
    "temperature": 0.7,
}

response = requests.post("https://httpbin.org/post", json=payload)

# TODO
# Send that POST request with the payload dict as json=payload (this is the key move — requests converts your dict to JSON and ships it)
# Check the status code (200 = success)
# Parse response.json() — httpbin echoes your data back inside a field called "json", so data["json"] will contain exactly what you sent
# Print the echoed model and prompt to prove your data made the round trip

if response.status_code == 200:
    data = response.json()
    echoed = data['json']
    print("Model:",echoed["model"])
    print("Prompt:",echoed["prompt"])
else:
    print(f"request failed with status: {response.status_code}")